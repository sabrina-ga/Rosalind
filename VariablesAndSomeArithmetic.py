
file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'test.txt'

data = open(file_path + file_name, 'r')
numbers = data.read().split()

a = int(numbers[0])
b = int(numbers[1])

result = a*a + b*b

print(result)
