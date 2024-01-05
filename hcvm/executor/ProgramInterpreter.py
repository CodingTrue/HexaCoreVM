from hcvm.Instructions import Instruction
from hcvm.MemoryContainer import MemoryConatiner

class ProgramInterpreter:
    def __init__(self, program: list[Instruction]):
        self.program = program
        self.is_running = False

        self.register = {
            "pc": MemoryConatiner(0xffff),
            "mar": MemoryConatiner(0xffff),
            "instr_1": MemoryConatiner(0xff),
            "instr_2": MemoryConatiner(0xff),
            "instr_3": MemoryConatiner(0xff),
            "instr_4": MemoryConatiner(0xff),
            "instr_step_c": MemoryConatiner(0xf),
            "inst_rom_1": MemoryConatiner(0x800),
            "inst_rom_2": MemoryConatiner(0x800),
            "inst_rom_3": MemoryConatiner(0x800),
            "flag_r": MemoryConatiner(0x02)
        }

    def run(self):
        print(self.program)