from hcvm.MemoryContainer import MemoryConatiner
from hcvm.Instructions import *
from hcvm.VMValue import VMValue
from hcvm.executor.ByteReader import read_program_binary
from hcvm.executor.ProgramInterpreter import ProgramInterpreter

import struct

program = read_program_binary("test_bins/o.bin")
VM = ProgramInterpreter(program=program)

VM.run()