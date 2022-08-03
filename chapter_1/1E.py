def FindClump(genome, k, L_window, t_occurrence):
    k, L_window, t_occurrence = int(k), int(L_window), int(t_occurrence);
    clump = [];
    l = len(genome);
    for i in range(l - L_window):
        window = genome[i : i + L_window];
        for j in range(L_window - k):
            kmer = window[j : j + k];
            count = Count(window, kmer);
            if count == t_occurrence:
                if kmer not in clump:
                    clump.append(kmer);
    print(" ".join(clump));


def ClumpFinding(genome, k, L, t):
    FreqPatterns = [];
    clump = {}
    for i in range(4**k):
        clump[i] = 0;
    for i in range(0, len(genome) - L):
        text = genome[i : i + L];
        FreqArray = ComputingFrequencies(text, k);
        
        
            
def ComputingFrequencies(text, k):
    FreqArray = {}
    for i in range(4 ** k):
        FreqArray[i] = 0;
    for i in range(len(text) - k):
        pattern = text[i : i + k];
        j = PatternToNumber(pattern);
        FreqArray[j] += 1;
    return FreqArray;

def PatternToNumber(pattern):
    

        







def Count(text, pattern):
    count = 0;
    k = len(pattern);
    for i in range(len(text)):
        if text[i: i + k] == pattern:
            count += 1;
    return count;

with open("./chapter_1/rosalind_ba1e.txt") as raw:
    genome = raw.readline();
    k, L_window, t_occurrence = raw.readline().split();

    FindClump(genome, k, L_window, t_occurrence);

