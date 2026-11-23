def resolver():
    try:
        linha = input().strip()
        if not linha:
            return
        n = int(linha)
    except EOFError:
        return

    usuarios_unicos = set()

    for _ in range(n):
        email = input().strip()
        localpart, provider = email.split('@')

        if '+' in localpart:
            localpart = localpart.split('+')[0]

        localpart = localpart.replace('.', '')

        email_normalizado = f"{localpart}@{provider}"
        usuarios_unicos.add(email_normalizado)

    print(len(usuarios_unicos))

if __name__ == '__main__':
    resolver()