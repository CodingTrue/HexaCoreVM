from hcvm.MemoryContainer import MemoryConatiner
from hcvm.Instructions import *
from hcvm.VMValue import VMValue
from hcvm.executor.ByteReader import read_program_binary
from hcvm.executor.ProgramInterpreter import ProgramInterpreter

import struct


a = MemoryConatiner()
a.increase_static_value(100)
a.decrease_static_value(27)

print(a.get_static_value())
exit()

program = read_program_binary("test_bins/o.bin")
VM = ProgramInterpreter(program=program)

VM.run()