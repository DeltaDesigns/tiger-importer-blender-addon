import bpy
import os

from . import destiny_importer as globals
from . import helper_functions as Helpers

BYTECODE_BLEND = os.path.join(os.path.dirname(__file__), "blends", "BytecodeOps.blend")

GLOBAL_CHANNEL_DEFAULTS = [
    [0.25, 0, 0, 0], [0, 0, 0, 0], [0.05, 0, 0, 0], [0.05, 0, 0, 0], [6, 0, 0, 0], [-3, -3, -3, -3], [3, 3, 3, 3], [0, 0, 0, 0],
    [10, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [50, 1, 1, 1], [0.025, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [5, 0, 0, 0],
    [0, 0, 0, 0], [30000, 0, 0, 0], [0, 0, 0, 0], [1.85, 0, 0, 0], [1, 1, 1, 0], [0.05, 0, 0, 0], [1, 0, 0, 0], [100, 0, 0, 0],
    [10, 0, 0, 0], [40, 0, 0, 0], [0.5, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [100000, 0, 0, 1], [50, 0, 0, 0], [0, 0, 0, 0],
    [1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [49500, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [90, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 0],
    [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0.35, 0, 0, 0], [0.7, 0, 0, 0], [1, 1, 1, 1], [0.1, 0, 0, 0], [0.5, 0, 0, 0],
    [1, 1, 1, 1], [0.15, 0, 0, 0], [0.5, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [1, 0, 0, 0], [0.1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [-1, 0, 0, 0], [1, 0, 0, 0],
    [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
    [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
    [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0],
    [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
    [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1],
]

IGNORED_OPS = {"PushSampler", "SetShaderSampler", "SetShaderTexture", "PushExternInputTextureView", "PushExternInputUav", "SetShaderUav"}

BINARY_OPS = {
    "Add": "Add4", "Add2": "Add4", "Subtract": "Subtract4", "Multiply": "Multiply4", "Multiply2": "Multiply4",
    "Divide": "Divide4", "Min": "Min4", "Max": "Max4", "LessThan": "LessThan4", "Dot": "Dot4", "Cubic": "Cubic",
    "Unk34_EoF": "CompareLessThan4", "Unk35_EoF": "CompareLessEqual4", "Unk36_EoF": "CompareGreaterThan4",
    "Unk37_EoF": "CompareGreaterEqual4", "Unk38_EoF": "CompareEqual4", "Unk39_EoF": "CompareNotEqual4",
}

UNARY_OPS = {
    "IsZero": "IsZero4", "Abs": "Abs4", "Sign": "Sign4", "Floor": "Floor4", "Ceil": "Ceil4", "Round": "Round4",
    "Frac": "Frac4", "Negate": "Negate", "VecRotSin": "VecRotSin", "VecRotCos": "VecRotCos", "VecRotSinCos": "VecRotSinCos",
    "PermuteAllX": "PermuteAllX", "Saturate": "Saturate4", "Triangle": "Triangle", "Jitter": "Jitter", "Wander": "Wander",
    "Rand": "Rand", "RandSmooth": "RandSmooth",
    "Unk1b": "Normalize4", "Unk1c": "Normalize3", "Unk26": "Length4", "Unk24": "Exp2 4", "Unk25": "Log2 4",
    "Unk3A_EoF": "NotZero4",
}

MERGE_OPS = {"Merge_1_3": "Merge_1_3", "Merge_2_2": "Merge_2_2", "Merge_3_1": "Merge_3_1"}

ORDERED_OPS = {
    "Lerp": ("Lerp4", (2, 0, 1)),
    "LerpSaturated": ("Lerp4Saturated", (2, 0, 1)),
    "MultiplyAdd": ("MultiplyAdd4", (0, 1, 2)),
    "Clamp": ("Clamp4", (1, 2, 0)),
    "TransformVec4": ("TransformVec4", (0, 1, 2, 3, 4)),
    "Unk14": ("SmoothStep4", (2, 1, 0)), # smoothstep(edge0, edge1, x), x on top
}

CONSTANT_OPS = {
    "LerpConstant": ("Lerp4", 2, (0,)),
    "LerpConstantSaturated": ("Lerp4Saturated", 2, (0,)),
    "Spline4Const": ("Spline4Const", 5, (0,)), 
    "Spline8Const": ("Spline8Const", 10, (0,)), 
    "Spline8ConstChain": ("Spline8ConstChain", 10, (1, 0)),
    "Gradient4Const": ("Gradient4Const", 6, (0,)), 
    "Gradient8Const": ("Gradient8Const", 11, (0,)),
}

PUSH_VALUE_OPS = {"Unk42": [1, 1, 1, 1], "Unk4c": [1, 1, 1, 1], "Unk50": [0, 0, 0, 0]}
DISCARD_OPS = {"Unk2c": 1, "Unk49": 1, "Unk51": 1, "Unk2d": 4}

# (extern, byte offset) -> (default value, label)
EXTERN_FLOATS = {
    ("Frame", 0x10): ([0.5] * 4, "Frame Extern: Time of Day"),
    ("Frame", 0x14): ([0.05] * 4, "Frame Extern: Frame Delta"),
    ("Frame", 0x18): ([0.016] * 4, "Frame Extern: Exposure Time"),
    ("Frame", 0x1C): ([1] * 4, "Frame Extern: Exposure Scale"),
    ("Frame", 0x28): ([1] * 4, "Frame Extern: ExposureIllumRelative"),
    ("Atmosphere", 0x70): ([0.5] * 4, "Atmosphere Extern: Time of Day"),
    ("Atmosphere", 0x170): ([0.0001] * 4, "Atmosphere Extern: Element 0x170"),
    ("Atmosphere", 0x198): ([0.0001] * 4, "Atmosphere Extern: Element 0x198"),
    ("Atmosphere", 0x1B4): ([0] * 4, "Atmosphere Extern: Rotation"),
    ("Atmosphere", 0x1B8): ([1] * 4, "Atmosphere Extern: Intensity"),
    ("Atmosphere", 0x1BC): ([0.5] * 4, "Atmosphere Extern: Element 0x1bc"),
    ("Atmosphere", 0x1E4): ([0.05923] * 4, "Atmosphere Extern: Sun Intensity"),
    ("Atmosphere", 0x1E8): ([0] * 4, "Atmosphere Extern: Element 0x1e8"),
}
EXTERN_VEC4S = {
    ("Frame", 0x1A0): ([0, 0, 0, 0], None),
    ("Frame", 0x1C0): ([1, 1, 0, 1], None),
    ("Deferred", 0x0): ([0, 100, 0, 0], None),
    ("Atmosphere", 0xD0): ([512.0, 512.0, 1.0 / 512.0, 1.0 / 512.0], None),
    ("Atmosphere", 0x90): ([480.0, 270.0, 0.00208, 0.0037], "AtmosRTDimensions"),
    ("Atmosphere", 0x110): ([-0.30372, -0.59835, 0.74144, 0.0], "AtmosSunDir"),
    ("Atmosphere", 0x140): ([1.0, 0.95, 0.85, 1.0], "AtmosSunColor"),
    ("Atmosphere", 0x1D0): ([0, 0, 0, 0], None),
    ("Decal", 0x10): ([0, 100, 0, 0], None),
    ("Decal", 0x20): ([0.03, 0, 0, 0], None),
    ("DecalSetTransform", 0x0): ([0, 0, 0, 1], None),
    ("DecalSetTransform", 0x10): ([0, 0, 0, 1], None),
}

FLOAT_CHANNELS = {"rounds_loaded_maximum", "rounds_loaded"}

raw_bytecode_materials = set()
time_cb0_groups = set()
failed_bytecode_materials = set()

def used_node_groups():
    groups = {"Combine4", "Seperate4", "CurTime", "Passthrough", "Time"}
    groups.update(BINARY_OPS.values(), UNARY_OPS.values(), MERGE_OPS.values())
    groups.update(group for group, _ in ORDERED_OPS.values())
    groups.update(group for group, _, _ in CONSTANT_OPS.values())
    return groups

def ensure_op_groups():
    missing = [name for name in used_node_groups() if bpy.data.node_groups.get(name) is None]
    if missing:
        if not os.path.isfile(BYTECODE_BLEND):
            Helpers.log(f"Could not find {BYTECODE_BLEND}, skipping material cbuffers")
            return False
        with bpy.data.libraries.load(BYTECODE_BLEND) as (data_from, data_to):
            data_to.node_groups = [name for name in missing if name in data_from.node_groups]
        for group in data_to.node_groups:
            group.use_fake_user = True
    return True

def add_time_modifiers():
    time_group = bpy.data.node_groups.get("Time")
    if not time_cb0_groups or time_group is None:
        return 0

    uses_time = {} 
    def material_uses_time(material):
        if material not in uses_time:
            uses_time[material] = material.node_tree is not None and any(
                node.bl_idname == 'ShaderNodeGroup' and node.node_tree is not None and node.node_tree.name in time_cb0_groups
                for node in material.node_tree.nodes)
        return uses_time[material]

    count = 0
    for obj in bpy.data.objects:
        if obj.type != 'MESH' or not obj.users_collection or any(m.type == 'NODES' and m.node_group == time_group for m in obj.modifiers):
            continue
        if any(slot.material is not None and material_uses_time(slot.material) for slot in obj.material_slots):
            modifier = obj.modifiers.new("Time", 'NODES')
            modifier.node_group = time_group
            count += 1
    return count

class TfxOp:
    def __init__(self, text):
        name, _, rest = text.partition(":")
        self.name = name.strip()
        self.args = [int(a) if a.strip().lstrip("-").isdigit() else a.strip() for a in rest.split(",")] if rest.strip() else []

    def __repr__(self):
        return f"{self.name}: {self.args}" if self.args else self.name

def parse_ops(bytecode):
    ops = [TfxOp(text) for text in bytecode]
    ops = [op for op in ops if op.name not in IGNORED_OPS]

    result = []
    current = []
    temps = {}
    for op in ops:
        if op.name == "PushTemp":
            current.extend(temps.get(op.args[0], []))
        elif op.name == "PopTemp":
            temps[op.args[0]] = current
            current = []
        else:
            current.append(op)

        if op.name in ("PopOutput", "PopOutputMat4"):
            result.extend(current)
            current = []
    return result

def vec4(value):
    def number(v):
        try:
            return float(v)
        except (TypeError, ValueError):
            return 0.0
    if value is None:
        return [0.0] * 4
    return [number(value.get(k)) for k in ("X", "Y", "Z", "W")]

def swizzle(fields):
    return [(fields >> 6) & 0b11, (fields >> 4) & 0b11, (fields >> 2) & 0b11, fields & 0b11]

def add_cbuffer_node(material, data):
    pixel = data.get("Material", {}).get("Pixel")
    if not pixel or material.node_tree.nodes.get("cb0") is not None:
        return
    if not ensure_op_groups():
        return

    builder = CBufferBuilder(data, pixel)
    try:
        group = builder.build()
    except Exception as error:
        Helpers.log(f"Material {data.get('Hash')} cbuffers: {error}")
        builder.discard()
        return

    node = material.node_tree.nodes.new(type='ShaderNodeGroup')
    node.node_tree = group
    node.name = "cb0"
    node.label = "cb0"
    node.location = (-800.0, 200.0)

class CBufferBuilder:
    NODE_SPACING = (220, -260)

    def __init__(self, data, pixel):
        self.data = data
        self.pixel = pixel
        self.constants = pixel.get("Constants") or []
        self.static = [vec4(v) for v in pixel.get("CBuffers") or []]
        self.group = None

    def discard(self):
        if self.group is not None:
            bpy.data.node_groups.remove(self.group)
            self.group = None

    def build(self):
        bytecode = self.pixel.get("Bytecode") or []
        ops = []
        if bytecode and not isinstance(bytecode[0], str):
            raw_bytecode_materials.add(self.data['Hash'])
        elif bytecode:
            ops = parse_ops(bytecode)

        slot_count = len(self.static)
        for op in ops:
            if op.name in ("PopOutput", "PopOutputMat4") and op.args:
                slot_count = max(slot_count, op.args[0] + (4 if op.name == "PopOutputMat4" else 1))

        self.group = bpy.data.node_groups.new(f"{self.data['Hash']} cb0", 'ShaderNodeTree')
        self.group_input = self.group.nodes.new(type='NodeGroupInput')
        self.group_output = self.group.nodes.new(type='NodeGroupOutput')
        for slot in range(slot_count):
            self.group.interface.new_socket(name=f"{slot}.XYZ", in_out='OUTPUT', socket_type='NodeSocketVector')
            self.group.interface.new_socket(name=f"{slot}.W", in_out='OUTPUT', socket_type='NodeSocketFloat')

        self.slot_values = {} 
        self.static_nodes = {}
        self.created = []
        self.created_inputs = []
        self.row = 0
        self.column = 0
        self.run(ops)

        for slot in range(slot_count):
            node = self.slot_values.get(slot) or self.static_node(slot)
            self.link_output(node, slot)

        self.group_input.location = (-self.NODE_SPACING[0] * 2, 0)
        self.group_output.location = (self.NODE_SPACING[0] * (self.max_column + 2), 0)
        if any(node.bl_idname == 'ShaderNodeGroup' and node.node_tree is not None and node.node_tree.name == "CurTime" for node in self.group.nodes):
            time_cb0_groups.add(self.group.name)
        return self.group

    max_column = 0

    def new_node(self, group_name, label=None):
        node = self.group.nodes.new(type='ShaderNodeGroup')
        self.created.append(node)
        node.node_tree = bpy.data.node_groups.get(group_name)
        if node.node_tree is None:
            raise ValueError(f"node group {group_name} is missing")
        if label:
            node.label = label
        node.location = (self.column * self.NODE_SPACING[0], self.row * self.NODE_SPACING[1])
        self.column += 1
        self.max_column = max(self.max_column, self.column)
        return node

    def value_node(self, value, label=None):
        node = self.new_node("Combine4", label)
        for k in range(4):
            node.inputs[k].default_value = value[k]
        return node

    def static_node(self, slot):
        node = self.static_nodes.get(slot)
        if node is None:
            column, row = self.column, self.row
            self.column, self.row = -1, slot * 0.4 # static values in their own column left of the bytecode
            value = self.static[slot] if slot < len(self.static) else [0.0] * 4
            node = self.static_nodes[slot] = self.value_node(value, f"cb0[{slot}]")
            node.hide = True
            self.column, self.row = column, row
        return node

    def link(self, source, node, first_input):
        self.group.links.new(source.outputs[0], node.inputs[first_input])
        self.group.links.new(source.outputs[1] if len(source.outputs) > 1 else source.outputs[0], node.inputs[first_input + 1])

    def link_output(self, node, slot):
        self.group.links.new(node.outputs[0], self.group_output.inputs[f"{slot}.XYZ"])
        self.group.links.new(node.outputs[1] if len(node.outputs) > 1 else node.outputs[0], self.group_output.inputs[f"{slot}.W"])

    def set_constant(self, node, first_input, value):
        node.inputs[first_input].default_value = value[:3]
        node.inputs[first_input + 1].default_value = value[3]

    def constant(self, index):
        return vec4(self.constants[index]) if 0 <= index < len(self.constants) else [0.0] * 4

    def group_input_socket(self, name, socket_type, default):
        if name not in self.group_input.outputs:
            socket = self.group.interface.new_socket(name=name, in_out='INPUT', socket_type=socket_type)
            socket.default_value = default
            self.created_inputs.append(socket)
        return self.group_input.outputs[name]

    def channel_node(self, name, as_float, vector_default, w_default):
        cached = self.channel_nodes.get(name)
        if cached is not None:
            return cached
        node = self.new_node("Combine4", name)
        sep = self.new_node("Seperate4")
        if as_float:
            self.group.links.new(self.group_input_socket(name, 'NodeSocketFloat', w_default), sep.inputs[0])
        else:
            self.group.links.new(self.group_input_socket(f"{name} XYZ", 'NodeSocketVector', vector_default), sep.inputs[0])
            self.group.links.new(self.group_input_socket(f"{name} W", 'NodeSocketFloat', w_default), sep.inputs[1])
        for k in range(4):
            self.group.links.new(sep.outputs[k], node.inputs[k])
        self.channel_nodes[name] = node
        return node

    def run(self, ops):
        self.channel_nodes = {}
        start = 0
        for end, op in enumerate(ops):
            if op.name not in ("PopOutput", "PopOutputMat4"):
                continue
            expression = ops[start:end + 1]
            start = end + 1

            nodes_before, inputs_before = len(self.created), len(self.created_inputs)
            try:
                self.run_expression(expression)
            except Exception as error:
                self.remove_since(nodes_before, inputs_before)
                first = op.args[0]
                zero = self.value_node([0.0] * 4, "failed, 0")
                for slot in range(first, first + (4 if op.name == "PopOutputMat4" else 1)):
                    self.slot_values[slot] = zero
                failed_bytecode_materials.add(self.data['Hash'])
                Helpers.log_debug(f"Material {self.data['Hash']}: bytecode for cb0[{first}] failed, it's 0 instead: {error}")
            self.next_row()

    def remove_since(self, nodes_before, inputs_before):
        removed = self.created[nodes_before:]
        del self.created[nodes_before:]
        self.static_nodes = {slot: node for slot, node in self.static_nodes.items() if node not in removed}
        for node in removed:
            self.group.nodes.remove(node)
        for socket in self.created_inputs[inputs_before:]:
            self.group.interface.remove(socket)
        del self.created_inputs[inputs_before:]

    def run_expression(self, ops):
        stack = []

        def pop(count=1):
            if len(stack) < count:
                raise ValueError(f"stack underflow, {op} needs {count} values but only {len(stack)} are on the stack")
            values = stack[-count:]
            del stack[-count:]
            return values

        for index, op in enumerate(ops):
            name = op.name
            if name in BINARY_OPS:
                a, b = pop(2)
                node = self.new_node(BINARY_OPS[name])
                self.link(a, node, 0)
                self.link(b, node, 2)
                stack.append(node)

            elif name in UNARY_OPS:
                a, = pop(1)
                node = self.new_node(UNARY_OPS[name])
                self.link(a, node, 0)
                stack.append(node)

            elif name in MERGE_OPS:
                a, b = pop(2)
                node = self.new_node(MERGE_OPS[name])
                self.group.links.new(a.outputs[0], node.inputs[0])
                self.group.links.new(b.outputs[0], node.inputs[1])
                stack.append(node)

            elif name in ORDERED_OPS:
                group_name, order = ORDERED_OPS[name]
                values = pop(len(order))
                node = self.new_node(group_name)
                for pair, value_index in enumerate(order):
                    self.link(values[value_index], node, pair * 2)
                stack.append(node)

            elif name in CONSTANT_OPS:
                group_name, count, order = CONSTANT_OPS[name]
                values = pop(len(order))
                node = self.new_node(group_name, f"{name} {op.args[0]}")
                for pair, value_index in enumerate(order):
                    self.link(values[value_index], node, pair * 2)
                for k in range(count):
                    self.set_constant(node, (len(order) + k) * 2, self.constant(op.args[0] + k))
                stack.append(node)

            elif name in PUSH_VALUE_OPS:
                stack.append(self.value_node(PUSH_VALUE_OPS[name], name))

            elif name in DISCARD_OPS:
                pop(DISCARD_OPS[name])

            elif name == "Permute":
                a, = pop(1)
                sep = self.new_node("Seperate4")
                node = self.new_node("Combine4")
                self.link(a, sep, 0)
                for k, field in enumerate(swizzle(op.args[0])):
                    self.group.links.new(sep.outputs[field], node.inputs[k])
                stack.append(node)

            elif name == "PushConstantVec4":
                stack.append(self.value_node(self.constant(op.args[0]), f"Constant {op.args[0]}"))

            elif name == "PushExternInputFloat":
                extern, element = op.args
                if extern == "Frame" and element in (0, 1): # time
                    stack.append(self.new_node("CurTime"))
                else:
                    value, label = EXTERN_FLOATS.get((extern, element * 4), ([1] * 4, None))
                    stack.append(self.value_node(value, label or f"{extern} Extern: Element {hex(element * 4)}"))

            elif name == "PushExternInputVec4":
                extern, element = op.args
                value, label = EXTERN_VEC4S.get((extern, element * 16), ([1] * 4, None))
                stack.append(self.value_node(value, label or f"{extern} Extern: Element {hex(element * 16)}"))

            elif name == "PushExternInputMat4":
                for k in range(4):
                    stack.append(self.value_node([1 if i == k else 0 for i in range(4)], f"{op.args[0]} Extern Mat4 row {k}"))

            elif name == "PushGlobalChannelVector":
                channel = op.args[0]
                default = GLOBAL_CHANNEL_DEFAULTS[channel] if channel < len(GLOBAL_CHANNEL_DEFAULTS) else [0] * 4
                stack.append(self.channel_node(f"Global Channel {channel}", False, default[:3], default[3]))

            elif name == "PushObjectChannelVector":
                channel = self.data.get("UsedChannelNames", {}).get(str(op.args[0])) or f"Channel {op.args[0]}"
                next_op = ops[index + 1] if index + 1 < len(ops) else None
                as_float = channel in FLOAT_CHANNELS or (next_op is not None and (next_op.name == "PermuteAllX" or (next_op.name == "Permute" and next_op.args[0] == 0)))
                stack.append(self.channel_node(channel, as_float, (1, 1, 1), 1))

            elif name in ("PushTexDimensions", "PushTexTileParams", "PushTexTileCount"):
                index_, fields = op.args
                tex = self.pixel.get("TileTextureDetails", {}).get(str(index_), {})
                if name == "PushTexDimensions":
                    values = [tex.get("Width", 1), tex.get("Height", 1), tex.get("ArraySize", 1), tex.get("Depth", 1)]
                elif name == "PushTexTileParams":
                    values = vec4(tex.get("TilingScaleOffset"))
                else:
                    values = [tex.get("TileCount", 1), tex.get("ArraySize", 1), 0.0, 0.0]
                stack.append(self.value_node([values[k] for k in swizzle(fields)], name))

            elif name == "PushFromOutput":
                slot = op.args[0]
                stack.append(self.slot_values.get(slot) or self.static_node(slot))

            elif name == "PopOutput":
                final, = pop(1)
                self.slot_values[op.args[0]] = final

            elif name == "PopOutputMat4":
                rows = pop(4)
                for k, row in enumerate(rows):
                    self.slot_values[op.args[0] + k] = row

            else:
                raise ValueError(f"unimplemented op {op}")

    def next_row(self):
        self.channel_nodes = {}
        self.row += 1
        self.column = 0
