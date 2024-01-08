from hcvm.Instructions import Instruction
from hcvm.MemoryContainer import MemoryConatiner
from hcvm.executor.ByteReader import create_memory_container_from_binary
from hcvm.executor.ControlSignal import *

class ProgramInterpreter:
    def __init__(self, program: list[Instruction]):
        self.program = program
        self.is_running = False

        self.control_signal = 0
        self.memory = MemoryConatiner(0xffff)
        self.register = {
            "pc": MemoryConatiner(4),
            "mar": MemoryConatiner(4),
            "instr_1": MemoryConatiner(2),
            "instr_2": MemoryConatiner(2),
            "instr_3": MemoryConatiner(2),
            "instr_4": MemoryConatiner(2),
            "instr_step_c": MemoryConatiner(1),
            "inst_rom_1": create_memory_container_from_binary(r"\test_bins\out_0.bin"),
            "inst_rom_2": create_memory_container_from_binary(r"\test_bins\out_1.bin"),
            "inst_rom_3": create_memory_container_from_binary(r"\test_bins\out_2.bin"),
            "flag_r": MemoryConatiner(1)
        }
        self.bus = 0x00
        self.alu = 0x00

    def is_cs_set(self, target: int = 0) -> bool:
        return self.control_signal & target == target

    def read_control_signal(self) -> int:
        current_inst_address = (self.register["flag_r"].get_static_value() << 9) | ((self.register["instr_1"].get_static_value() & 0x1f) << 4) | self.register["instr_step_c"].get_static_value()
        return (self.register["inst_rom_3"].get_byte(address=current_inst_address) << 16) | (self.register["inst_rom_2"].get_byte(address=current_inst_address) << 8) | self.register["inst_rom_1"].get_byte(address=current_inst_address)

    def tick(self):
        self.control_signal = self.read_control_signal()

        if self.is_cs_set(CE):
            if not self.is_cs_set(CRI): self.register["pc"].increase_static_value(value=1)
            else: self.register["pc"].decrease_static_value(value=1)
        if self.is_cs_set(CO): self.bus = self.register["pc"].get_static_value()
        if self.is_cs_set(CL): self.register["pc"].set_static_value(value=self.bus)
        if self.is_cs_set(MARI): self.register["mar"].set_static_value(value=self.bus)
        if self.is_cs_set(MWE): pass
        if self.is_cs_set(MRE): pass
        if self.is_cs_set(IRI_1): self.register["instr_1"].set_static_value(value=self.bus)
        if self.is_cs_set(IRI_2): self.register["instr_2"].set_static_value(value=self.bus)
        if self.is_cs_set(IRI_3): self.register["instr_3"].set_static_value(value=self.bus)
        if self.is_cs_set(IRI_4): self.register["instr_4"].set_static_value(value=self.bus)
        if self.is_cs_set(EO): pass
        if self.is_cs_set(EMODE): pass
        if self.is_cs_set(ESE): pass
        if self.is_cs_set(ECIN): pass
        if self.is_cs_set(ESL): pass
        if self.is_cs_set(EE): pass
        if self.is_cs_set(RFWE): pass
        if self.is_cs_set(FOSP): pass
        if self.is_cs_set(SPI): pass
        if self.is_cs_set(UFR): pass
        if self.is_cs_set(IOR): pass
        if self.is_cs_set(IOW): pass
        if self.is_cs_set(HLT): input("CPU HALTED")

    def run(self):
        self.tick()