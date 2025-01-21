def compute_cg_content(seq):
    length = len(seq)
    cg_count = seq.count('C') + seq.count('G')
    return cg_count/length * 100


file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_gc.txt'

data = open(file_path + file_name, 'r')
lines = [line.strip() for line in data.readlines()]

dna_strings = {}
header = ''
for line in lines:
    if line.startswith('>'):
        header = line.replace('>','')
        dna_strings[header] = ''
    else:
        dna_strings[header] += line 

max_cg = 0
max_cg_header = ''
for header, seq in dna_strings.items():
    cg = compute_cg_content(dna_strings[header])
    if compute_cg_content(dna_strings[header]) > max_cg:
        max_cg = cg
        max_cg_header = header


print(f"{max_cg_header}\n{max_cg}")