G = 6.67e-11
M = 5.972e24
RT = 6378000


def f(r):
    return -(G * M) / (r ** 2)


def f1(r):
    return (2 * G * M) / (r ** 3)


def f2(r):
    return -(6 * G * M) / (r ** 4)


def f3(r):
    return (24 * G * M) / (r ** 5)


def p1(r, a):
    return f(a) + f1(r) * (r - a)


def p2(r, a):
    return p1(r, a) + f2(a) / 2 * (r - a) ** 2


def p3(r, a):
    return p2(r, a) + f3(a) / 6 * (r - a) ** 3


print("--- Parte 1 ---")

print("- 2 -")

h = 8849

print(f"f(RT + h) = {f(RT + h):.4}")
print(f"f(RT) = {f(RT):.4}")
print(f"Diferencia relativa: {(f(RT + h) - f(RT)) / f(RT):.2%}")

print("- 6 -")

print(f"f(0.01) = {f(0.01):.4}")
print(f"f(0.02) = {f(0.02):.4}")
print(f"Diferencia relativa: {(f(0.02) - f(0.01)) / f(0.01):.2%}")

print(f"p2(0.02) = {p2(0.02, 0.01):.4}")
print(f"Diferencia relativa entre p2(0.02) y f(0.02): {(p2(0.02, 0.01) - f(0.02)) / f(0.02):.2%}")
print(f"p3(0.02) = {p3(0.02, 0.01):.4}")
print(f"Diferencia relativa entre p3(0.02) y f(0.02): {(p3(0.02, 0.01) - f(0.02)) / f(0.02):.2%}")
