# recursive int to binary function
def base2(n: int) -> list[int]:
    if n == 0:
        return []
    
    return base2(n // 2) + [n % 2]

# recursive binary to int function
def base10(a):
    if type(a) == int:
        return base10(str(a))
    if not a:
        return 0
    return int(a[-1]) + 2 * base10(a[:-1])

# Test Cases
print(base2(6)) # [1, 1, 0]
print(base10([1, 1, 0])) # 6
print(base10(1111)) # 15