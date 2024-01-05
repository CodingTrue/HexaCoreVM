from hcvm.Instructions import Instruction
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

            result.append(data)
    return result