# Lab 09 — Direct-Mapped Cache Simulator (tiny)

class DirectMappedCache:
    def __init__(self, lines=4, line_size=4):
        self.lines = lines
        self.line_size = line_size
        self.tags = [-1]*lines
        self.valid = [0]*lines

    def access(self, addr):
        index = (addr // self.line_size) % self.lines
        tag = addr // (self.line_size * self.lines)
        hit = self.valid[index] and (self.tags[index] == tag)
        if not hit:
            self.valid[index] = 1
            self.tags[index] = tag
        return bool(hit)

def simulate(trace):
    cache = DirectMappedCache(lines=4, line_size=4)
    hits = 0
    for a in trace:
        if cache.access(a): hits += 1
    return hits, len(trace), hits/len(trace)

def demo():
    trace = [0,1,2,3,16,17,18,19,0,1,2,3,4,5,6,7,16,17,18,19]
    hits, n, hr = simulate(trace)
    print(f"Trace len={n} hits={hits} hit_rate={hr:.2f}")

if __name__ == "__main__":
    demo()