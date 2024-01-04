from hcvm.MemoryContainer import MemoryConatiner
from hcvm.Instructions import *
from hcvm.VMValue import VMValue

memcont = MemoryConatiner(4096)

tr = VMValue("r0")
sr = VMValue("r1")

target_inst = SWL()
target_inst.set_change_targets(tr, sr)
print(target_inst.iden, target_inst.opcode)

ser = target_inst.serialize()
memcont.set_bytes(0, values=ser)
print(memcont.memory)