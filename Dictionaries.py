file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_ini6.txt'

data = open(file_path + file_name, 'r')
words = data.read().split()

word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


for word, count in word_dict.items():
    print(f"{word} {count}")