# Lab 03 — Control Logic (Hardwired + PLA simulation)

# Opcodes: 00=LOAD, 01=STORE, 10=ADD, 11=SUB
# Control lines: MRD, MWR, RLD, ALU_ADD, ALU_SUB

def hardwired_control(opcode):
    MRD = int(opcode == 0b00)
    MWR = int(opcode == 0b01)
    RLD = int(opcode in (0b00,0b10,0b11))
    ALU_ADD = int(opcode == 0b10)
    ALU_SUB = int(opcode == 0b11)
    return dict(MRD=MRD, MWR=MWR, RLD=RLD, ALU_ADD=ALU_ADD, ALU_SUB=ALU_SUB)

def pla_control(opcode):
    # AND-plane minterms m0..m3 for inputs [op1 op0]
    m = [0,0,0,0]
    m[opcode] = 1
    # OR-plane to form outputs
    MRD = m[0]
    MWR = m[1]
    RLD = m[0] or m[2] or m[3]
    ALU_ADD = m[2]
    ALU_SUB = m[3]
    return dict(MRD=MRD, MWR=MWR, RLD=RLD, ALU_ADD=ALU_ADD, ALU_SUB=ALU_SUB)

def demo():
    names = ["LOAD","STORE","ADD","SUB"]
    for op in range(4):
        hw = hardwired_control(op)
        pla = pla_control(op)
        print(f"Opcode {op:02b} ({names[op]}) -> Hardwired {hw} | PLA {pla}")

if __name__ == "__main__":
    demo()