def Count(text, pattern):
    count = 0;
    k = len(pattern);
    for i in range(len(text)):
        if text[i: i + k] == pattern:
            count += 1;
    return count;

print(Count("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT"));


with open("rosalind_ba1a.txt", 'r') as data:
    text = data.readline().rstrip();
    pattern = data.readline().rstrip();
    print(Count(text, pattern));