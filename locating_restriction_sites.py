def read_fasta(fasta_file): 
    lines = [line.strip() for line in fasta_file.readlines()]
    seq_dic = {}
    header = ''
    for line in lines:
        if line.startswith('>'):
            header = line.replace('>','')
            seq_dic[header] = ''
        else:
            seq_dic[header] += line 
    return seq_dic

def dna_reverse_complement(dna):
    dna_compl_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    dna_reversed = dna[::-1]
    dna_compl = ''.join(dna_compl_dict[base] for base in dna_reversed)
    return dna_compl

def find_reverse_palindromes(fasta_dic):
    for header, seq in fasta_dic.items():
        compl = dna_reverse_complement(seq)
        for start in range(len(seq)-1):
            for length in range(4, 13):
                end = start + length
                if end > len(seq):
                    continue

                part_seq = seq[start:end]
                part_compl = compl[len(seq)-end : len(seq)-start]

                if part_seq == part_compl:
                    print(f"{start+1} {length}")

file_path = 'C:/Users/sabri/OneDrive/Dokumente/MyGitHub/Rosalind/Data/'
file_name = 'rosalind_revp.txt'
data = open(file_path + file_name, 'r')
fasta_dic = read_fasta(data)

find_reverse_palindromes(fasta_dic)







