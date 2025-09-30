print("\033c\033[43;30m\nboard\n")


print("\033c\033[43;30m\nboard\n")

def arrays(sizes, value):
    # versão recursiva para criar arrays multidimensionais independentes
    if len(sizes) == 1:
        return [value for _ in range(sizes[0])]
    return [arrays(sizes[1:], value) for _ in range(sizes[0])]


# exemplo de uso
aa = [2,2,2,2]
a = arrays(aa, 0)

a[0][0][0][0] = 1
a[0][0][0][1] = 2

print(a)
