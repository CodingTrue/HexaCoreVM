from hcvm.VMValue import VMValue
from hcvm.executor.ByteReader import load_program_memory
from hcvm.executor.ProgramInterpreter import ProgramInterpreter

VM = ProgramInterpreter()
load_program_memory(r"\test_bins\o.bin", VM.memory)

VM.register["flag_r"].set_static_value(0)
VM.register["instr_1"].set_static_value(0x1f)
VM.register["instr_step_c"].set_static_value(0xf)

VM.run()

print(VM.register["pc"].get_static_value())