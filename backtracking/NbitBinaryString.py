def bitstrings(n):
    if n==0:
        return []
    if n==1:
        return ["0","1"]
    else:
        return [digit+bitstring for digit in bitstrings(1) for bitstring in bitstrings(n-1)]


if __name__ == "__main__":
    n = int(input("enter the number of bits for the string: "))
    print(bitstrings(n))