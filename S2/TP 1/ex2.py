from ex1 import power # import power function from ex1.py

# 1: assign power function to f1 variable
f1 = power 

f1(7, 3)

# 2: define scale function and assign it to f2 variable
def scale(x, factor=1.2):
    return x * factor
f2 = scale

# 3: define the main apply_all function
def apply_all(funcs, value):
    ans = []
    f1 = funcs[0]
    ans.append(f1(value))
    f2 = funcs[1]
    ans.append(f2(value))
    return ans
    
# 4: Test apply_all function
print(apply_all([f1, f2], 10))

