class MemoryConatiner:
    def __init__(self, size: int = 4096):
        self.size = size
        self.memory = bytearray(size)

    def get_byte_range(self, start_address: int = 0, address_range: int = 1) -> list[int]:
        return [self.memory[(start_address + x) % self.size] for x in range(address_range)]

    def get_single_byte(self, address: int = 0) -> int:
        return self.get_byte_range(start_address=address, address_range=1)[0]

    def get_two_bytes(self, start_address: int = 0) -> list[int]:
        return self.get_byte_range(start_address=start_address, address_range=2)

    def fetch_instruction(self, start_address: int = 0) -> list[int]:
        return self.get_byte_range(start_address=start_address, address_range=4)

    def set_byte(self, address: int = 0, value: int = 0):
        self.memory[address] = value

    def set_bytes(self, start_address: int = 0, values: list[int] = [0]):
        for i in range(len(values)):
            self.memory[(start_address + i) % self.size] = values[i]