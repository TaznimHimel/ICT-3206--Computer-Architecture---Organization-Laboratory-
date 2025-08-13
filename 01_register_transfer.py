# Lab 01 — Register Transfer Operations (4-bit)
# Run: python 01_register_transfer.py

class Register4:
    def __init__(self, value=0):
        self.value = value & 0b1111  # keep 4 bits

    def load(self, value):
        self.value = value & 0b1111

    def inc(self):
        self.value = (self.value + 1) & 0b1111

    def and_with(self, other):
        return Register4(self.value & other.value)

    def shift_left(self):
        self.value = ((self.value << 1) & 0b1111)

    def bits(self):
        return format(self.value, "04b")

class ControlUnit:
    def __init__(self):
        self.A = Register4()
        self.B = Register4()
        self.C = Register4()

    def transfer_A_to_B(self):
        self.B.load(self.A.value)

    def increment_A(self):
        self.A.inc()

    def and_A_B_to_C(self):
        self.C = self.A.and_with(self.B)

    def shift_A_left(self):
        self.A.shift_left()

    def state(self):
        return dict(A=self.A.bits(), B=self.B.bits(), C=self.C.bits())

def demo():
    cu = ControlUnit()
    cu.A.load(0b1010)
    print("Initial:", cu.state())
    cu.transfer_A_to_B()
    print("After transfer A→B:", cu.state())
    cu.increment_A()
    print("After INC A:", cu.state())
    cu.and_A_B_to_C()
    print("After AND A&B → C:", cu.state())
    cu.shift_A_left()
    print("After SHIFT LEFT A:", cu.state())

if __name__ == "__main__":
    demo()







# Modified initial value of a to 0b0101
# def demo():
#     cu = ControlUnit()
#     # The initial value of A is changed to 0b0101
#     cu.A.load(0b0101)
#     print("Initial:", cu.state())
#     cu.transfer_A_to_B()
#     print("After transfer A→B:", cu.state())
#     cu.increment_A()
#     print("After INC A:", cu.state())
#     cu.and_A_B_to_C()
#     print("After AND A&B → C:", cu.state())
#     cu.shift_A_left()
#     print("After SHIFT LEFT A:", cu.state())





#  Explain (2‒3 lines) the effect of logical left shift on the carry-out (if any) for 4-bit truncation.
# In a logical left shift with 4-bit truncation, the **most significant bit (MSB)** is shifted out of its position. ⚙️ This shifted-out bit, which represents the potential carry-out, is immediately **discarded** by the truncation mask (`& 0b1111`). Consequently, the carry-out is effectively lost and not stored or propagated.