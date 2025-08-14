# Lab 04 — Interrupt-Driven I/O (Simulation)
# Simulate a CPU doing work; a keyboard 'event' interrupts processing.

import threading, time

class CPU:
    def __init__(self):
        self.counter = 0
        self.interrupt_flag = False

    def isr(self):
        print("[ISR] Interrupt serviced: toggling LED and logging event.")
        # simulated LED state change
        print("[ISR] LED -> ON")
        time.sleep(0.1)
        print("[ISR] LED -> OFF")

    def main_loop(self, duration=3.0):
        start = time.time()
        while time.time() - start < duration:
            # simulate work
            self.counter += 1
            if self.interrupt_flag:
                self.interrupt_flag = False
                self.isr()
            time.sleep(0.05)
        print("[CPU] main loop done. counter =", self.counter)

def trigger_interrupt(cpu, after=0.5):
    time.sleep(after)
    cpu.interrupt_flag = True

def demo():
    cpu = CPU()
    t = threading.Thread(target=trigger_interrupt, args=(cpu,1.0))
    t.start()
    cpu.main_loop(2.5)
    t.join()

if __name__ == "__main__":
    demo()