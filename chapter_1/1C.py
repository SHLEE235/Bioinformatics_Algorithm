def ReverseComplement(s):
    rc = ''
    comp_map = {"A":"T", "G":"C", "C":"G", "T":"A"};

    for n in s[::-1]:
        rc += comp_map[n];
            
    return rc;

with open("rosalind_ba1c.txt") as raw:
    s = raw.readline().strip();

print(ReverseComplement(s));