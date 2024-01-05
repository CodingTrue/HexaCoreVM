from hcvm.VMValue import VMValue, VMValueType

class Instruction:
    def __init__(self, opcode: int = 0, iden: str = "", target: int = 0, source: int = 0, data_bytes: int = 0):
        self.opcode = opcode
        self.iden = iden
        self.target = target
        self.source = source
        self.target = target
        self.data_bytes = data_bytes

    def serialize(self) -> list[int]:
        return [self.opcode, (self.source << 4) + (self.target & 0xf), self.data_bytes >> 8, self.data_bytes & 0x00ff]

    def __repr__(self):
        return f"{self.iden}[{self.source}, {self.target}](0x{self.data_bytes:04x})"

class NOOP(Instruction):
    def __init__(self):
        super(NOOP, self).__init__(opcode=0x00, iden="NOOP")

class LDR(Instruction):
    def __init__(self):
        super(LDR, self).__init__(opcode=0x01, iden="LDR")

    def set_register_value(self, target: VMValue, source: VMValue):
        if not target.type == VMValueType.REGISTER: raise ValueError(f"The target register must be a type of '{VMValueType.REGISTER}'!")
        self.target = target.get_value()

        if source.type == VMValueType.ADDRESS:
            self.data_bytes = source.value
        elif source.type == VMValueType.REGISTER:
            self.source = source.get_value()

class JUMP(Instruction):
    def __init__(self):
        super(JUMP, self).__init__(opcode=0x02, iden="JUMP")

    def set_target_address(self, source: VMValue):
        if source.type == VMValueType.ADDRESS:
            self.data_bytes = source.value
        elif source.type == VMValueType.REGISTER:
            self.source = source.get_value()

class JUMPZ(JUMP):
    def __init__(self):
        super(JUMP, self).__init__(opcode=0x03, iden="JUMPZ")

class JUMPC(JUMP):
    def __init__(self):
        super(JUMP, self).__init__(opcode=0x04, iden="JUMPC")

class JUMPSR(JUMP):
    def __init__(self):
        super(JUMP, self).__init__(opcode=0x05, iden="JUMPSR")

class RET(Instruction):
    def __init__(self):
        super(RET, self).__init__(opcode=0x06, iden="RET")

class ADD(Instruction):
    def __init__(self):
        super(ADD, self).__init__(opcode=0x07, iden="ADD")

    def set_values(self, target: VMValue, source: VMValue):
        if not target.type == VMValueType.REGISTER: raise ValueError(f"The target register must be a type of '{VMValueType.REGISTER}'!")
        self.target = target.get_value()

        if source.type == VMValueType.ADDRESS:
            self.data_bytes = source.value
        elif source.type == VMValueType.REGISTER:
            self.source = source.get_value()

class SUB(ADD):
    def __init__(self):
        super(ADD, self).__init__(opcode=0x08, iden="SUB")

    def set_values(self, target: VMValue, source: VMValue):
        if not target.type == VMValueType.REGISTER: raise ValueError(f"The target register must be a type of '{VMValueType.REGISTER}'!")
        self.target = target.get_value()

        if source.type == VMValueType.ADDRESS:
            self.data_bytes = source.value
        elif source.type == VMValueType.REGISTER:
            self.source = source.get_value()

class PUSH(Instruction):
    def __init__(self):
        super(PUSH, self).__init__(opcode=0x09, iden="PUSH")

    def set_target_value(self, source: VMValue):
        if source.type == VMValueType.ADDRESS:
            self.data_bytes = source.value
        elif source.type == VMValueType.REGISTER:
            self.source = source.get_value()

class POP(Instruction):
    def __init__(self):
        super(POP, self).__init__(opcode=0x0a, iden="POP")

    def set_target(self, target: VMValue):
        if not target.type == VMValueType.REGISTER: raise ValueError(f"The target register must be a type of '{VMValueType.REGISTER}'!")
        self.target = target.get_value()

class HLT(Instruction):
    def __init__(self):
        super(HLT, self).__init__(opcode=0x0b, iden="HLT")

class IOR(POP):
    def __init__(self):
        super(POP, self).__init__(opcode=0x0c, iden="IOR")

class IOW(JUMP):
    def __init__(self):
        super(JUMP, self).__init__(opcode=0x0d, iden="IOW")

class SWL(Instruction):
    def __init__(self):
        super(SWL, self).__init__(opcode=0x0e, iden="SWL")

    def set_change_targets(self, target: VMValue, source: VMValue):
        if not target.type == VMValueType.REGISTER: raise ValueError(f"The target register must be a type of '{VMValueType.REGISTER}'!")
        if not source.type == VMValueType.REGISTER: raise ValueError(f"The source register must be a type of '{VMValueType.REGISTER}'!")
        self.target = target.get_value()
        self.source = target.get_value()

INSTRUCTION_CLASSES = {
    0: NOOP,
    1: LDR,
    2: JUMP,
    3: JUMPZ,
    4: JUMPC,
    5: JUMPSR,
    6: RET,
    7: ADD,
    8: SUB,
    9: PUSH,
    10: POP,
    11: HLT,
    12: IOR,
    13: IOW,
    14: SWL
}

def build_instruction(instruction_data: list[int] = [0]) -> Instruction:
    if not len(instruction_data) == 4: raise ValueError("'instruction_data' must contain 4 elements")
    opcode, st_register, data_bytes_u, data_bytes_l = instruction_data

    result = INSTRUCTION_CLASSES[opcode]()
    result.source = st_register >> 4
    result.target = st_register & 0xf
    result.data_bytes = (data_bytes_u << 8) | data_bytes_l
    return result