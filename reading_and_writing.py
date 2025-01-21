
file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_ini5.txt'
output_name = 'output.txt'

data = open(file_path + file_name, 'r')
output = open(file_path + output_name, 'w')
lines = data.readlines()

even_lines = [lines[i] for i in range(len(lines)) if (i+1)%2==0]

for line in even_lines:
    output.write(line)


print(lines[0]) 
