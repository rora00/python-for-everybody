fname = input("Enter file name: ")
fh = open(fname)
lst = list()
# iterates through each line and stores each word in a list 'word'
for line in fh:
    word = line.split()
    # adds each word to the list
    for i in range(len(word)):
        # rejects words that are already in lst
        if word[i] in lst:
            continue
        lst.append(word[i])
lst.sort()
print(lst)