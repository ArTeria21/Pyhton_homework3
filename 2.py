def mors_tue(n):
    sequence = ["0"]
    while len(sequence) <= n:
        new_els = []
        for el in sequence:
            if el == "0":
                new_els.append("1")
            elif el == "1":
                new_els.append("0")
        sequence += new_els
    return "".join(sequence[0:n])

print(mors_tue(893))