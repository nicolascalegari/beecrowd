import sys

DIGITS = {
    ("***", "* *", "* *", "* *", "***"): "0",
    ("  *", "  *", "  *", "  *", "  *"): "1",
    ("***", "  *", "***", "*  ", "***"): "2",
    ("***", "  *", "***", "  *", "***"): "3",
    ("* *", "* *", "***", "  *", "  *"): "4",
    ("***", "*  ", "***", "  *", "***"): "5",
    ("***", "*  ", "***", "* *", "***"): "6",
    ("***", "  *", "  *", "  *", "  *"): "7",
    ("***", "* *", "***", "* *", "***"): "8",
    ("***", "* *", "***", "  *", "***"): "9"
}

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    idx = 0
    while idx + 4 < len(lines):
        block = lines[idx:idx+5]

        max_len = max(len(line) for line in block)
        n_digits = (max_len + 1) // 4

        valid = True
        code_str = ""

        for j in range(n_digits):
            digit_rows = []
            for i in range(5):
                start = 4 * j
                end = start + 3
                row_str = block[i][start:end].ljust(3)
                digit_rows.append(row_str)

            digit_tuple = tuple(digit_rows)
            if digit_tuple in DIGITS:
                code_str += DIGITS[digit_tuple]
            else:
                valid = False
                break

        if valid:
            num = int(code_str)
            if num % 6 == 0:
                print("BEER!!")
            else:
                print("BOOM!!")
        else:
            print("BOOM!!")

        idx += 5

if __name__ == '__main__':
    main()
