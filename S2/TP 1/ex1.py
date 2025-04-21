# 1 power Function
def power(base, exponent=2):
    if exponent < 0:
        return float(base ** exponent)
    return base ** exponent

# 2 Test Cases
if __name__ == "__main__":
    print(power(5))
    print(power(base=3, exponent=4))
    print(power(2, exponent=5))