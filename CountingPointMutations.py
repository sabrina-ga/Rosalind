file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_hamm.txt'

data = open(file_path + file_name, 'r')
lines = data.readlines()

s = lines[0]
t = lines[1]

hd_count = 0

for i in range(len(s)-1):
    if (s[i] != t[i]):
        hd_count += 1

print(hd_count)