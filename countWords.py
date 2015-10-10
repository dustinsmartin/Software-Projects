##############################
#### AUTHOR: Dustin Martin ###
##############################

#Open the file you are counting words from
file = open(input("Enter file name: "), "r+")

#Create a Dictionary
wordCount = {}

#Read in each word, if the word is original create an entry for it
#otherwise increase the counter it is associated with.
for word in file.read().split():
    word = word.lower()
    if word.isalpha():
        if word not in wordCount:
             wordCount[word] = 1
        else:
            wordCount[word] += 1

#Create an array to copy the entries of the dictionary to.
copy = []

#For the entries in the dictionary append to the copy
for k,v in wordCount.items():
    copy.append((v, k))

#sort the the copy's entries in reverse order
copy = sorted(copy, reverse = True)

#print the result.
for k in copy:
    print( k[1] + ": " + str(k[0]) )


