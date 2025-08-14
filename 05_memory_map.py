# Lab 05 — Memory Map & Address Decoding (Simulation)

ROM_RANGE = range(0x0000, 0x1000)   # 0000-0FFF
RAM_RANGE = range(0x4000, 0x5000)   # 4000-4FFF

class Bus:
    def __init__(self):
        self.rom = {addr: 0 for addr in ROM_RANGE}
        self.ram = {addr: 0 for addr in RAM_RANGE}
        # preload a ROM location to show read-only
        self.rom[0x0000] = 0xEA

    def decode(self, addr):
        a15 = (addr >> 15) & 1
        a14 = (addr >> 14) & 1
        # Example: RAM when a15=0 and a14=1
        if addr in RAM_RANGE:
            return "RAM"
        elif addr in ROM_RANGE:
            return "ROM"
        else:
            return "NONE"

    def read(self, addr):
        region = self.decode(addr)
        if region == "ROM":
            return self.rom[addr]
        if region == "RAM":
            return self.ram[addr]
        raise ValueError("Invalid address")

    def write(self, addr, val):
        region = self.decode(addr)
        if region == "ROM":
            raise PermissionError("Cannot write to ROM")
        if region == "RAM":
            self.ram[addr] = val & 0xFF
        else:
            raise ValueError("Invalid address")

def demo():
    bus = Bus()
    print("Decode 0x4000 ->", bus.decode(0x4000))
    print("Write 0x55 to 0x4000 (RAM)")
    bus.write(0x4000, 0x55)
    print("Read 0x4000 =", hex(bus.read(0x4000)))
    print("Read ROM[0x0000] =", hex(bus.read(0x0000)))
    try:
        bus.write(0x0000, 0x99)
    except PermissionError as e:
        print("Expected error:", e)

if __name__ == "__main__":
    demo()