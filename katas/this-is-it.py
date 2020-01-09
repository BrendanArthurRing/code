def ais(a):
    g = []
    for i, j in zip(a, a[1:]):
        if i > j:
            g.append('>')
        elif i < j:
            g.append('<')
        elif i == j:
            g.append('=')
    print(g)
    print(len(a))
    print(len(g))


s = [40, 50, 60, 10, 20, 30]
ais(s)
