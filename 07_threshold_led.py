# Lab 07 — Threshold + LED Control (Port simulation)

PORT = {"0x80": 0x00}  # LED port

def write_port(addr_hex, val):
    PORT[addr_hex] = val & 0xFF

def read_port(addr_hex):
    return PORT.get(addr_hex, 0x00)

def threshold_led(sum_val, threshold=0x50):
    if sum_val >= threshold:
        write_port("0x80", 0xFF)  # LED ON
    else:
        write_port("0x80", 0x00)  # LED OFF

def demo():
    for s in (0x30, 0x50, 0x70):
        threshold_led(s, 0x50)
        led = read_port("0x80")
        print(f"Sum={s:#04x} -> LED={'ON' if led==0xFF else 'OFF'}")

if __name__ == "__main__":
    demo()