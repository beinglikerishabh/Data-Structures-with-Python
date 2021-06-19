def AppendFront(x, L):  # this is without using the List comprehension provided as i did in the C version logic
    return [x+element for element in L]


def bitstring(n):
    if n == 0:
        return []
    if n == 1:
        return ["0", "1"]
    else:
        return (AppendFront("0", bitstring(n-1)) + AppendFront("1", bitstring(n-1)))


if __name__ == "__main__":
    n = int(input("enter the number of bits for the string: "))
    print(bitstring(n))
