import sys; print(sys.executable)

print("Enter a search term: ")

bookhand = open('harrypotter1.txt', encoding='utf8')
bookfull = bookhand.read()
searchTerm = input()
searchCount = bookfull.count(searchTerm)
searchCountAnswer = str(searchCount)


print("The word " + searchTerm + " appeared " + searchCountAnswer + " times.")



