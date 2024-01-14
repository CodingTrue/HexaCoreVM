from hcvm.MemoryContainer import MemoryConatiner
from hcvm.HexaCoreBuildInfo import NUM2REGISTER

class RegisterFile:
    def __init__(self):
        self.registers = {
            "r0": MemoryConatiner(size=2, max_static_value=0xff),
            "r1": MemoryConatiner(size=2, max_static_value=0xff),
            "r2": MemoryConatiner(size=2, max_static_value=0xff),
            "r3": MemoryConatiner(size=2, max_static_value=0xff),
            "r4": MemoryConatiner(size=2, max_static_value=0xff),
            "r5": MemoryConatiner(size=2, max_static_value=0xff),
            "sp": MemoryConatiner(size=2, max_static_value=0xff)
        }
        self.writeAddr = 0
        self.writeData = 0

    def read(self, readAddr1: int = 0, readAddr2: int = 0) -> tuple[int, int]:
        if readAddr1 > 7 or readAddr1 == 0: raise ValueError("readAddr1 must be 1 to 7")
        if readAddr2 > 7 or readAddr2 == 0: raise ValueError("readAddr2 must be 1 to 7")

        return (self.registers[NUM2REGISTER[readAddr1]], self.registers[NUM2REGISTER[readAddr2]])

    def write(self):
        self.registers[NUM2REGISTER[self.writeAddr]].set_static_value(value=self.writeData)