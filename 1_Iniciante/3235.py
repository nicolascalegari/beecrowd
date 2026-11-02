import sys

def main():
    data = sys.stdin.read().split()
    n, L = int(data[0]), int(data[1])
    xs = sorted(round(float(t) * 100) for t in data[2:2 + n])

    if n == 1:
        print("10")
        return
    if n > L or len(set(xs)) < n:
        print("no fika")
        return

    # diferenças distintas (em centímetros)
    diffs = set()
    for i in range(n - 1):
        xi = xs[i]
        for j in range(i + 1, n):
            diffs.add(xs[j] - xi)

    # s = 1/v em [0.1, 10]; para cada diferença d (metros), (d*s) mod L deve estar em [1, L-1]
    # intervalos proibidos (abertos): s em ((kL-1)/d, (kL+1)/d)
    iv = []
    for D in diffs:
        d = D / 100.0
        k = max(0, int((0.1 * d - 1) / L) - 1)
        while True:
            lo = k * L - 1
            if lo >= 10.0 * d:
                break
            hi = k * L + 1
            r = hi / d
            if r > 0.1:
                iv.append((lo / d, r))
            k += 1

    iv.sort()
    eps = 1e-12
    cur = 0.1
    for l, r in iv:
        if l < cur - eps:
            if r > cur:
                cur = r
        else:
            break

    if cur > 10.0 + 1e-9:
        print("no fika")
    else:
        print("%.12g" % (1.0 / cur))

main()