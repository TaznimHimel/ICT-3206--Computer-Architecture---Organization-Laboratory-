# Lab 02 — 4-bit ALU with Status Flags + 1-bit shifter

def full_add_4(a, b, sub=False):
    # a,b are 4-bit ints. If sub=True, compute a + (~b + 1)
    if sub:
        b = ((~b) & 0b1111) + 1
    s = a + b
    carry = 1 if s > 0b1111 else 0
    out = s & 0b1111
    return out, carry

def alu_4(a, b, ctrl):
    # ctrl: 0=ADD, 1=SUB, 2=AND, 3=OR
    if ctrl == 0:
        out, c = full_add_4(a, b, sub=False)
    elif ctrl == 1:
        out, c = full_add_4(a, b, sub=True)
    elif ctrl == 2:
        out, c = (a & b), 0
    else:
        out, c = (a | b), 0
    z = 1 if out == 0 else 0
    return out, c, z

def shift_left_1(x):
    return (x << 1) & 0b1111

def demo():
    A, B = 0b1010, 0b0101
    labels = ["ADD","SUB","AND","OR"]
    for ctrl in range(4):
        out, c, z = alu_4(A,B,ctrl)
        print(f"{labels[ctrl]}: A={A:04b} B={B:04b} -> OUT={out:04b} C={c} Z={z} SHIFTED={shift_left_1(out):04b}")

if __name__ == "__main__":
    demo()



