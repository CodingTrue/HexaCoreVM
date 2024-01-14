from hcvm.VMValue import VMValue
from hcvm.executor.ByteReader import load_program_memory
from hcvm.executor.ProgramInterpreter import ProgramInterpreter

VM = ProgramInterpreter()
load_program_memory(r"\test_bins\o.bin", VM.memory)

while input("> Step?").lower() == "":
    print(VM.register["pc"].get_static_value(), VM.bus, VM.register["instr_step_c"].get_static_value())
    VM.run()
