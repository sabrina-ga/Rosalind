
file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_ini4.txt'

data = open(file_path + file_name, 'r')
numbers = data.read().split()

a = int(numbers[0])
b = int(numbers[1])

sum = 0
for i in range(a,b+1):
    if i%2 != 0:
        sum += i

print(sum)