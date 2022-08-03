def FindPatternIndex(pattern, genome):
    indices = [];
    l, k = len(genome), len(pattern)
    for i in range(l - k):
        if genome[i: i + k] == pattern:
            indices.append(str(i));

    print(" ".join(indices));

with open("rosalind_ba1d.txt") as raw:
    pattern = raw.readline().strip();
    genome = raw.readline().strip();

FindPatternIndex(pattern, genome);
        