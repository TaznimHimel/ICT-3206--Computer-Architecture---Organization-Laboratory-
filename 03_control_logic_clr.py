# Lab 03 — Control Logic (Hardwired + PLA simulation with CLR)

# Opcodes (3-bit now):
# 000 = LOAD
# 001 = STORE
# 010 = ADD
# 011 = SUB
# 100 = CLR
# Control lines: MRD, MWR, RLD, ALU_ADD, ALU_SUB

def hardwired_control(opcode):
    MRD = int(opcode == 0b000)
    MWR = int(opcode == 0b001)
    RLD = int(opcode in (0b000, 0b010, 0b011, 0b100))
    ALU_ADD = int(opcode == 0b010)
    ALU_SUB = int(opcode in (0b011, 0b100))  # SUB and CLR use subtraction mode
    return dict(MRD=MRD, MWR=MWR, RLD=RLD, ALU_ADD=ALU_ADD, ALU_SUB=ALU_SUB)

def pla_control(opcode):
    # AND-plane minterms m0..m4 for inputs [op2 op1 op0]
    m = [0, 0, 0, 0, 0]
    if opcode < len(m):
        m[opcode] = 1
    # OR-plane to form outputs
    MRD = m[0]
    MWR = m[1]
    RLD = m[0] or m[2] or m[3] or m[4]
    ALU_ADD = m[2]
    ALU_SUB = m[3] or m[4]
    return dict(MRD=MRD, MWR=MWR, RLD=RLD, ALU_ADD=ALU_ADD, ALU_SUB=ALU_SUB)

def demo():
    names = ["LOAD", "STORE", "ADD", "SUB", "CLR"]
    for op in range(len(names)):
        hw = hardwired_control(op)
        pla = pla_control(op)
        print(f"Opcode {op:03b} ({names[op]}) -> Hardwired {hw} | PLA {pla}")

if __name__ == "__main__":
    demo()
