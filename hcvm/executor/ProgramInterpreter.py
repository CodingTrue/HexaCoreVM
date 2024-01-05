from hcvm.Instructions import Instruction
from hcvm.MemoryContainer import MemoryConatiner

class ProgramInterpreter:
    def __init__(self, program: list[Instruction]):
        self.program = program
        self.is_running = False

        self.register = {
            "pc": MemoryConatiner(4),
            "mar": MemoryConatiner(4),
            "instr_1": MemoryConatiner(2),
            "instr_2": MemoryConatiner(2),
            "instr_3": MemoryConatiner(2),
            "instr_4": MemoryConatiner(2),
            "instr_step_c": MemoryConatiner(1),
            "inst_rom_1": MemoryConatiner(2),
            "inst_rom_2": MemoryConatiner(2),
            "inst_rom_3": MemoryConatiner(2),
            "flag_r": MemoryConatiner(1)
        }
        self.bus = 0x00

    def tick(self):
        self.register[0]

    def run(self):
        self.tick()