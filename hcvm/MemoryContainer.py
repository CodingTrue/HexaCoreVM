class MemoryConatiner:
    def __init__(self, size: int = 4096, max_static_value: int = 0):
        self.size = size
        self.memory = bytearray(size)
        self.max_static_value = 2**(size*4) if max_static_value == 0 else max_static_value

    def get_byte_range(self, start_address: int = 0, address_range: int = 1) -> list[int]:
        return [self.memory[(start_address + x) % self.size] for x in range(address_range)]

    def get_byte(self, address: int = 0) -> int:
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

    def get_static_value(self) -> int:
        return int.from_bytes(self.memory, byteorder="big", signed=False) % self.max_static_value

    def set_static_value(self, value: int = 0):
        self.memory = int.to_bytes(value, byteorder="big", signed=False, length=value)

    def increase_static_value(self, value: int = 0):
        target_value = (self.get_static_value() + value) % self.max_static_value
        self.memory = int.to_bytes(target_value, byteorder="big", signed=False, length=target_value)

    def decrease_static_value(self, value: int = 0):
        self.increase_static_value(value=-value)