# Lab 06 — 8085-style tasks in Python

def add_8(a, b):
    s = a + b
    carry = s > 0xFF
    return s & 0xFF, carry

def sub_8(a, b):
    d = a - b
    borrow = d < 0
    return d & 0xFF, borrow

def largest_of_5(arr):
    assert len(arr) == 5
    m = arr[0]
    for x in arr[1:]:
        if x > m: m = x
    return m

def sum_of_arr(arr):
    s = 0
    for x in arr:
        s = (s + x) & 0xFF
    return s

def demo():
    a,b = 0x25, 0x13
    s,c = add_8(a,b)
    print(f"ADD {a:#04x}+{b:#04x}={s:#04x} C={int(c)}")
    d,br = sub_8(0x50,0x30)
    print(f"SUB 0x50-0x30={d:#04x} Borrow={int(br)}")
    arr = [0x11,0x88,0x34,0x22,0x77]
    print("Largest of", arr, "=", hex(largest_of_5(arr)))
    print("Sum of", arr, "=", hex(sum_of_arr(arr)))

if __name__ == "__main__":
    demo()