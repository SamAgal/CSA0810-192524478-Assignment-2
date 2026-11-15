"""Task 4: Building Long Text: + or join()?."""

import time

def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text

def build_join(parts):
    return ";".join(parts) + ";"

if __name__ == "__main__":
    for n in [1000, 10000, 50000]:
        items = [f"Item{i}:Rs{i % 50}" for i in range(n)]
        
        start = time.perf_counter()
        a = build_plus(items)
        t_plus = time.perf_counter() - start
        
        start = time.perf_counter()
        b = build_join(items)
        t_join = time.perf_counter() - start
        
        print(f"N = {n:6d} | += time: {t_plus:.6f} s | join() time: {t_join:.6f} s | Match: {a == b}")
