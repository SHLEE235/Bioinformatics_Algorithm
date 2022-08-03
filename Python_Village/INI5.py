def EvenNumberedLines(input_file, output_file):
    with open(input_file, "r") as read:
        with open(output_file, "w") as write:
            count = 0;
            while line:=read.readline():
                count += 1;
                if count % 2 == 0:
                    write.write(line);
    return None;                

EvenNumberedLines("rosalind_ini5.txt", "INI5.txt");