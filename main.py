from hcvm.VMValue import VMValue
from hcvm.executor.ByteReader import read_program_binary
from hcvm.executor.ProgramInterpreter import ProgramInterpreter

program = read_program_binary("test_bins/o.bin")
VM = ProgramInterpreter(program=program)
VM.register["flag_r"].set_static_value(0)
VM.register["instr_1"].set_static_value(0x1f)
VM.register["instr_step_c"].set_static_value(0xf)

print(VM.register["inst_rom_1"].memory)

VM.run()

print(VM.register["pc"].get_static_value())