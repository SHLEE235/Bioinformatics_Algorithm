def SliceString(s, a, b, c, d):
    return s[a:b+1] + ' ' + s[c:d+1];

with open("rosalind_ini3.txt", "r") as raw:
    s = raw.readline();
    a, b, c, d = raw.readline().split();
    a, b, c, d = int(a), int(b), int(c), int(d);
    print(SliceString(s, a, b, c, d));