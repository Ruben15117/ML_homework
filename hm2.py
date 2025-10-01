import numpy as np

# 1
a = np.zeros(5, dtype=int)
b = np.ones(5, dtype=int)
c = np.full(5, 9, dtype=int)
print("1)", a, b, c)

# 2
x = np.arange(100).reshape(10, 10)
sh = [(i, 100 // i) for i in range(1, 101) if 100 % i == 0]
print("\n2) orig:", x.shape)
for s in sh:
    print("shape", s, "\n", x.reshape(s))

# 3
m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[7, 8, 9], [10, 11, 12]])
e = m1 * m2
mm = m1 @ m2.T
print("\n3)e\n", e)
print(" Matrix \n", mm)

# 4
r1 = np.random.randint(0, 21, (10, 10))
r2 = np.random.randint(0, 21, (10, 10))
d = r1 / r2.astype(float)
f = d[np.isfinite(d)]
inf = np.argwhere(np.isinf(d))
nan = np.argwhere(np.isnan(d))
print("\n4) r1:\n", r1)
print("r2:\n", r2)
print("div:\n", d)
print("fin:", f)
print("inf idx:", inf)
print("nan idx:", nan)

# 5
m = np.arange(11, 20, dtype=float).reshape(3, 3)
print("\n5)", m)
