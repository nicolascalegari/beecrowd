import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    pos = 1
    teacher = [0] * n
    rank = [[0] * n for _ in range(n)]
    for i in range(n):
        teacher[i] = int(data[pos]); pos += 1
        for r in range(1, n):
            j = int(data[pos]) - 1; pos += 1
            rank[i][j] = r

    # cores permitidas de cada criança (2 opções)
    allowed = [[c for c in range(3) if c != teacher[i]] for i in range(n)]

    def node(i, c):
        # cor c da criança i -> literal (x_i verdadeiro = allowed[i][1])
        return 2 * i if allowed[i][1] == c else 2 * i + 1

    def feasible(T):
        N = 2 * n
        g = [[] for _ in range(N)]
        for i in range(n):
            for j in range(i + 1, n):
                if rank[i][j] > T or rank[j][i] > T:
                    # não podem ficar na mesma turma
                    for c in allowed[i]:
                        if c in allowed[j]:
                            a = node(i, c)
                            b = node(j, c)
                            g[a].append(b ^ 1)
                            g[b].append(a ^ 1)
        # Tarjan
        index = [-1] * N
        low = [0] * N
        onst = [False] * N
        comp = [-1] * N
        st = []
        cnt = [0, 0]

        def dfs(v):
            index[v] = low[v] = cnt[0]; cnt[0] += 1
            st.append(v); onst[v] = True
            for w in g[v]:
                if index[w] == -1:
                    dfs(w)
                    if low[w] < low[v]:
                        low[v] = low[w]
                elif onst[w] and index[w] < low[v]:
                    low[v] = index[w]
            if low[v] == index[v]:
                while True:
                    w = st.pop(); onst[w] = False
                    comp[w] = cnt[1]
                    if w == v:
                        break
                cnt[1] += 1

        for v in range(N):
            if index[v] == -1:
                dfs(v)
        for i in range(n):
            if comp[2 * i] == comp[2 * i + 1]:
                return False
        return True

    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

main()