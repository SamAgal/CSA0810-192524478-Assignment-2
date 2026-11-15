"""Task 6: Recursion and Its Limits (Counting Ways to Climb Temple Steps)."""

from functools import lru_cache
import sys

sys.setrecursionlimit(5000)

calls_naive = 0
def ways_naive(n):
    global calls_naive
    calls_naive += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)

calls_memo = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls_memo
    calls_memo += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)

if __name__ == "__main__":
    n_test = 25
    
    calls_naive = 0
    res_naive = ways_naive(n_test)
    print(f"Naive n={n_test} -> Ways: {res_naive:10d} | Function Calls: {calls_naive}")
    
    calls_memo = 0
    res_memo = ways_memo(n_test)
    print(f"Memo  n={n_test} -> Ways: {res_memo:10d} | Function Calls: {calls_memo}")

    print("\nTesting memoized recursion up to n = 1000:")
    try:
        ways_memo.cache_clear()
        calls_memo = 0
        res_1000 = ways_memo(1000)
        print(f"Ways to climb 1000 steps calculated successfully! Calls: {calls_memo}")
    except Exception as e:
        print(f"Error at n=1000: {e}")
