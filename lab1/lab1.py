import numpy as np

def f_float(x):
    return np.float32(x + 1/3 - (x - 1 / 3))

def f_double(x):
    return np.float64(x + 1/3 - (x - 1 / 3))

def g_float(x):
    if (x == 0):
        return np.nan
    else:
        return np.float32(((3 + x**2 / 3) - (3 - x**2 / 3)) / x**2)
    
def g_double(x):
    if (x == 0):
        return np.nan
    else:
        return np.float64(((3 + x**2 / 3) - (3 - x**2 / 3)) / x**2)
    
def main():
    x1_values = [10**3, 10**6, 10**9, 10**10, 10**11]
    print("f(x):")
    for x in x1_values:
        f_exact = 2 / 3
        f_float_result = f_float(x)
        f_double_result = f_double(x)
        f_float_error = abs(f_exact - f_float_result)
        f_double_error = abs(f_exact - f_double_result)

        print(f"f_float = {f_float_result}, Error = {f_float_error}")
        print(f"f_double = {f_double_result}, Error = {f_double_error}")

    print("\ng(x):")
    x2_values = [10**i for i in range(-6, 1)]
    for x in x2_values:
        g_exact = 2 / 3 if x != 0 else np.nan
        g_float_result = f_float(x)
        g_double_result = f_double(x)
        g_float_error = abs(g_exact - g_float_result)
        g_double_error = abs(g_exact - g_double_result)

        print(f"g_float = {g_float_result}, Error = {g_float_error}")
        print(f"g_double = {g_double_result}, Error = {g_double_error}")

if (__name__ == "__main__"):
    main()