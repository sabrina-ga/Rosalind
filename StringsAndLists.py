
file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_ini3.txt'

data = open(file_path + file_name, 'r')
lines = data.readlines()

text = lines[0]
a = int(lines[1].split()[0])
b = int(lines[1].split()[1])
c = int(lines[1].split()[2])
d = int(lines[1].split()[3])

string_1 = text[a:b+1]
string_2 = text[c:d+1]

print(string_1 + " " + string_2)