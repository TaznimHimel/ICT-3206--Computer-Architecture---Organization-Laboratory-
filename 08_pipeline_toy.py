# Lab 08 — Tiny 2-stage Pipeline (Fetch/Execute) toy

PROGRAM = [
    ("LDI", "R0", 5),
    ("LDI", "R1", 7),
    ("ADD", "R2", "R0", "R1"),
    ("ADD", "R0", "R0", "R2"),
]

class CPU2Stage:
    def __init__(self, prog):
        self.prog = prog
        self.pc = 0
        self.reg = {f"R{i}":0 for i in range(4)}
        self.IF = None
        self.EX = None

    def step(self):
        # Execute stage
        if self.EX:
            op = self.EX
            if op[0] == "LDI":
                _, r, val = op
                self.reg[r] = val
            elif op[0] == "ADD":
                _, rd, ra, rb = op
                self.reg[rd] = self.reg[ra] + self.reg[rb]
            print("[EX]", op, "REG:", self.reg)
        # Fetch stage
        self.EX = self.IF
        if self.pc < len(self.prog):
            self.IF = self.prog[self.pc]
            self.pc += 1
        else:
            self.IF = None

    def run(self):
        while self.EX or self.IF or self.pc < len(self.prog):
            self.step()

def demo():
    cpu = CPU2Stage(PROGRAM)
    cpu.run()

if __name__ == "__main__":
    demo()