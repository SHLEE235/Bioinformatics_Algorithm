def hypotenuse(a, b):
    return a**2 + b**2;

with open("./rosalind_ini2.txt") as raw:
    data = raw.readline();
    a, b = data.split();
    a = int(a);
    b = int(b);
    print(hypotenuse(a, b));