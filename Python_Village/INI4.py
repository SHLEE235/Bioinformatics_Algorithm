def SumOddInRange(a, b):
    a, b = int(a), int(b);
    sumodd = 0;
    for n in range(a, b+1):
        if n % 2 == 1:
            sumodd += n;
    return sumodd;

with open("rosalind_ini4.txt") as raw:
    a, b = raw.readline().split();
    print(SumOddInRange(a, b));
