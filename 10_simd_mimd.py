# Lab 10 — SIMD vs MIMD mini demo

def simd_add(a,b):
    return [x+y for x,y in zip(a,b)]

def mimd_tasks(tasks):
    results = []
    for f,args in tasks:
        results.append(f(*args))
    return results

def demo():
    A = [1,2,3,4]
    B = [10,20,30,40]
    print("SIMD add:", simd_add(A,B))
    tasks = [(pow,(2,10)), (pow,(3,5)), (sum,([1,2,3],))]
    print("MIMD tasks:", mimd_tasks(tasks))

if __name__ == "__main__":
    demo()