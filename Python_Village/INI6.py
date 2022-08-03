def WordOccurrence(s):
    output = {};
    for word in s.split():
        if word in output.keys():
            output[word] += 1;
        else:
            output[word] = 1;
    with open("INI6.txt", "w") as write:
        for word, occurrence in output.items():
            line = f'{word} {occurrence}\n';
            write.write(line);

with open("rosalind_ini6.txt") as raw:
    s = raw.readline();

WordOccurrence(s);
