def f(h, r, rho):
    return h**3 - 3 * r * h**2 + 4 * r**3 * rho

def df(h, r):
    return 3 * h**2 - 6 * r * h

def newton_method(f, h, df, r, rho, tol=0.001):
    count = 0
    while True:
        h_next = h - f(h, r, rho) / df(h, r)
        if abs(h_next - h) < tol:
            break
        h = h_next
        count +=1
        print(f"iteration {count}: {h}")
    return h

def secant_method(f, h0, h1, r, rho, tol=0.001):
    count = 0
    while True:
        h_next = h1 - f(h1, r, rho) * (h1 - h0) / (f(h1, r, rho) - f(h0, r, rho))
        if abs(h_next - h1) < tol:
            break
        h0, h1 = h1, h_next
        count +=1
        print(f"iteration {count}: {h_next}")
    return h_next

radius = 10
density = 0.62
h0, h1 = input("Enter initial values: ").split()

h0 = int(h0)
h1 = int(h1)

result_newton = newton_method(f, h0, df, radius, density)
print("Depth of sphere submersion (Newton Method:", result_newton)

result_secant = secant_method(f, h0, h1, radius, density)
print("Depth of sphere submersion (Secant Method):", result_secant)
