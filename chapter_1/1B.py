def FrequentWords(text, k):
    kmer_freq = {};
    mc_kmers = [];
    count = []

    for i in range(len(text) - k):
        kmer = text[i: i + k];
        count.append(Count(text, kmer));
        if kmer not in kmer_freq.keys():
            kmer_freq[kmer] = count[i];

    mc_count = max(kmer_freq.values());

    for i in range(len(text) - k):
        if count[i] == mc_count:
            kmer = text[i: i + k];
            if kmer not in mc_kmers:
                mc_kmers.append(kmer);
    return ' '.join(mc_kmers);


def Count(text, pattern):
    count = 0;
    k = len(pattern);
    for i in range(len(text)):
        if text[i: i + k] == pattern:
            count += 1;
    return count;

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT";
k = 4;

with open("rosalind_ba1b.txt") as raw:
    text = raw.readline().strip();
    k = int(raw.readline());

print(FrequentWords(text, k));
