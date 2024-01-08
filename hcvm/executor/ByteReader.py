from hcvm.Instructions import Instruction, build_instruction
from hcvm.MemoryContainer import MemoryConatiner
from os import getcwd
import struct

def read_program_binary(filename: str = "") -> list[Instruction]:
    result = []
    with open(filename, "rb") as f:
        content = f.read()
        iterations = int(len(content) / 4)

        i = -4
        for _ in range(iterations):
            i += 4
            data = [int.from_bytes(x, "big", signed=False) for x in struct.unpack(">cccc", content[i:i + 4])]
            if data[0] == 0: continue

            result.append(build_instruction(data))
    return result

def create_memory_container_from_binary(filename: str = "") -> MemoryConatiner:
    result = None
    with open(getcwd() + filename, "rb") as f:
        content = f.read()

        result = MemoryConatiner(size=len(content))
        result.memory = content
    return result