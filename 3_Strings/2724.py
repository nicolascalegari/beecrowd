import sys

linhas = sys.stdin.read().splitlines()

if linhas:
    idx = 0
    n = int(linhas[idx].strip())
    idx += 1

    for caso in range(n):
        if caso > 0:
            print()

        t = int(linhas[idx].strip())
        idx += 1
        perigosos = []
        for _ in range(t):
            perigosos.append(linhas[idx].strip())
            idx += 1

        u = int(linhas[idx].strip())
        idx += 1
        for _ in range(u):
            exp = linhas[idx].strip()
            idx += 1
            abortar = False

            for p in perigosos:
                pos = exp.find(p)
                while pos != -1:
                    fim = pos + len(p)
                    if fim == len(exp) or exp[fim].isupper():
                        abortar = True
                        break
                    pos = exp.find(p, pos + 1)

                if abortar:
                    break

            print("Abortar" if abortar else "Prossiga")