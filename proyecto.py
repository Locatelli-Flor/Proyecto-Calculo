G = 6.67e-11
M = 5.972e24
RT = 6378000


def f(r):
    return -(G*M)/(r**2)


def f1(r):
    return (G*M)/(2*r**3)


def f2(r):
    return -(G*M)/(6*r**4)


def f3(r):
    return (G*M)/(24*r**5)


def p1(r):
    return f(RT) + f1(r) * (r - RT)


print("--- Parte 1 ---")

print("- 2 -")

h = 8849

print(f"f(RT + h) = {f(RT + h):.4}")
print(f"f(RT) = {f(RT):.4}")
print(f"Diferencia relativa: {(f(RT + h) - f(RT))/f(RT):.2%}")