def Skew(genome):
    skew_prefix = [0];
    acc = 0;
    result = []
    for i in range(len(genome)):
        if genome[i] == "G":
            acc += 1;
        elif genome[i] == "C":
            acc -= 1;
        skew_prefix.append(acc);

    min_skew = min(skew_prefix);
    for i in range(len(skew_prefix)):
        if skew_prefix[i] == min_skew:
            result.append(i);
            
    return result;

with open("./chapter_1/rosalind_ba1f.txt") as raw:
    genome = raw.readline().strip();

print(Skew(genome));