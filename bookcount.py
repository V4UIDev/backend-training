import sys; print(sys.executable)
import re

print("Enter a number of minimum mentions:")
minimum = int(input())
counts = dict()
filteredList = list()

bookhand = open('harrypotter1.txt', encoding='utf8')
bookfull = bookhand.read().split()

for names in bookfull:
    counts[names] = counts.get(names, 0) + 1

for k,v  in counts.items():
    if counts[k] >= minimum:
        filteredList.append((v,k))
filteredList = sorted(filteredList, reverse=True)

for v, k in filteredList:
    x = re.search('[A-Za-z0-9]+', k)
    try:
        if x.string == k:
            print(v, k)
    except:
        print(" ")


