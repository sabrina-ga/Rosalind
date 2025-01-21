
file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_dna.txt'

data = open(file_path + file_name, 'r')
seq = data.read()

count_dict = {}

count_dict['A'] = seq.count('A')
count_dict['C'] = seq.count('C')
count_dict['G'] = seq.count('G')
count_dict['T'] = seq.count('T')

print(f"{count_dict['A']} {count_dict['C']} {count_dict['G']} {count_dict['T']}")
