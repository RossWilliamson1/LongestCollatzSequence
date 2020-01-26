def collatz(n):
    seq = [n]
    while n!=1:
        if n%2==0:
            n/=2
            seq.append(n)
        else:
            n*=3
            n+=1
            seq.append(n)
    return len(seq)

def biggest_seq(end):
    biggest = 1
    for x in range(1, end):
        if collatz(x) > collatz(biggest):
            biggest = x
    return biggest

longest = biggest_seq(100000)
print longest
print collatz(longest)
