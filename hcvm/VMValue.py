from hcvm.HexaCoreBuildInfo import REGISTER, REGISTER2NUM
from enum import Enum

class VMValueType(Enum):
    NOT_ASIGNED = "NOA"
    REGISTER = "REG"
    ADDRESS = "ADDR"

class VMValue:
    def __init__(self, value: any = 0):
        self.value = value
        self.type = VMValueType.NOT_ASIGNED

        self.asign_value_type()

    def asign_value_type(self):
        self.type = VMValueType.REGISTER if self.value in REGISTER else self.type
        self.type = VMValueType.ADDRESS if isinstance(self.value, int) else self.type

    def get_value(self) -> int:
        if self.type == VMValueType.ADDRESS: return self.value
        if self.type == VMValueType.REGISTER: return REGISTER2NUM[self.value]
        return None