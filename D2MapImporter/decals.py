import bpy
import mathutils
import json
import os

from . import destiny_importer as globals
from . import helper_functions as Helpers
from .materials import *

def add_decal_planes(self):
    Helpers.log("Creating Decal planes...")
    if not os.path.exists(globals.FilePath + f"/Rendering/Decals.json"): # Rendering is written next to the cfgs, same as Lights.json
        Helpers.log(f"Could not find Decals.Json in '{globals.FilePath}/Rendering', skipping...")
        return
    
    if bpy.data.collections.get("Decal Planes"):
        Helpers.log("Decals collection already exists, skipping...")
        return

    bpy.data.collections.new("Decal Planes")
    bpy.context.scene.collection.children.link(bpy.data.collections["Decal Planes"])
    bpy.context.view_layer.active_layer_collection = bpy.context.view_layer.layer_collection.children["Decal Planes"]
   
    with open(globals.FilePath + f"/Rendering/Decals.json", 'r') as f:
        Cfg = json.load(f)

    collection = bpy.context.collection
    for name, data in Cfg.items():
        if bpy.data.materials.get(name) is None:
            create_material(name)

        # one plane mesh per decal shared by all its instances, same as a size 1 primitive plane
        mesh = create_plane_mesh(name)
        material = bpy.data.materials.get(name)
        if material:
            mesh.materials.append(material)

        for instance in data["Instances"]:
            location = [instance["Translation"][0], instance["Translation"][1], instance["Translation"][2]]
            quat = mathutils.Quaternion([instance["Rotation"][3], instance["Rotation"][0], instance["Rotation"][1], instance["Rotation"][2]]) #WXYZ
            scale = [instance["Scale"][0], instance["Scale"][1], instance["Scale"][2]]

            plane = bpy.data.objects.new(name, mesh)
            collection.objects.link(plane)
            plane.location = location
            plane.rotation_mode = 'QUATERNION'
            plane.rotation_quaternion = quat
            plane.scale = scale

    Helpers.log("Imported Decal Planes.")

def create_plane_mesh(name):
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata([(-0.5, -0.5, 0), (0.5, -0.5, 0), (0.5, 0.5, 0), (-0.5, 0.5, 0)], [], [(0, 1, 2, 3)])
    uv_layer = mesh.uv_layers.new(name="UVMap")
    uv_layer.data.foreach_set("uv", [0, 0, 1, 0, 1, 1, 0, 1])
    mesh.update()
    return mesh