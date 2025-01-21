import re

def find_matches(s, t):
    positions = []
    start = 0
    while (match := re.search(t, s[start:])) is not None:
        positions.append(start + match.start()) 
        start += match.start() + 1  
    return positions

file_path = 'C:/Users/sabri/OneDrive/Dokumente/Rosalind/Data/'
file_name = 'rosalind_subs.txt'

data = open(file_path + file_name, 'r')
lines = [line.strip() for line in data.readlines()]

s = lines[0]
t = lines[1]

matches = find_matches(s, t)
print(" ".join(str(pos + 1) for pos in matches))
