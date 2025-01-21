file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_revc.txt'

data = open(file_path + file_name, 'r')
dna = data.read().strip()

dna_compl_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
dna_reversed = dna[::-1]
dna_compl = ''.join(dna_compl_dict[base] for base in dna_reversed)
                                    
print(dna_compl)