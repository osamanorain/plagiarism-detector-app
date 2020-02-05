import re


# Takes a string and splits its words and puts them in a list, and returns the list
def createlist(string):
    rgx = re.compile(r"(\w[\w']*\w|\w)")
    list = rgx.findall(string)

    # make all words lower case for the future comparisons
    for i in range(0, len(list)):
        list[i] = list[i].lower()

    return list


# Creates and returns a hashmap(dictionary) from a list
def createHashmap(list):
    hashmap = {}

    for word in list:
        if hashmap.get(word) != None:
            value = hashmap.get(word)
            hashmap.update({word: value + 1})
        else:
            hashmap.update({word: 1})

    return hashmap


# Takes in a dictionary  and compares unique words from both lists and outputs the jaccardvalue
def compareMaps(map1, map2):
    # divide total words in both maps by the total words in either map
    sharedwords = 0

    for word in map1:
        if word in map2:
            sharedwords += 1

    jaccardval = (sharedwords / (len(map1) + len(map2) - sharedwords)) * 100
    return jaccardval


# Takes String and outputs the jaccardvalue *(The function kivy uses to calculate similarity)*
# Abstracts away many included functions
def testTexts(text_1, text_2):
    text1list = createlist(text_1)
    text2list = createlist(text_2)

    text1dict = createHashmap(text1list)
    text2dict = createHashmap(text2list)

    jaccardval = compareMaps(text1dict, text2dict)
    return jaccardval


# Gets the word length of string/text
def getWordLength(text):
    return len(createlist(text))


# Inputs are lists and the longest common sequence of words value of the two lists
# lcs(longest common sequence). This algorithm is similar to Dynamic Programming's Longest common substring
def lcs(text1, text2, lcs):
    # matrix with len(text1)+1 columns and len(text2)+1 rows
    matrix = [[0 for m in range(len(text1)+1)] for n in range(len(text2)+1)]
    commonlist = []
    lcscount = 0

    # text1 is in the x axis and text2 in the y axis. We compare every text1 word to the text2 word of that row.
    # Then, move on to the next text2 word and repeat.
    for i in range(0, len(text2)):
        for u in range(0, len(text1)):
            if text2[i] == text1[u]:
                matrix[i+1][u+1] = 1 + matrix[i][u]
                if matrix[i+1][u+1] > lcscount:
                    lcscount = matrix[i+1][u+1]
                    # once we find the last item in the common substring by checking the substring count with the already retrived count
                    # we back track the common substring size so we can append the common elements
                    # only need to worry about one list because they items will be the same anyway
                    if lcscount == lcs:
                        startu = u - lcscount + 1
                        # append the common elements
                        for p in range(0, lcscount):
                            commonlist.append(text1[startu + p])

    return commonlist


# The inputs are two lists, and the output is the longest common sequence of words and value
# lcs(longest common sequence). This algorithm is similar to Dynamic Programming's Longest common substring
def getlcs(text1, text2):
    # matrix with len(text1)+1 columns and len(text2)+1 rows
    matrix = [[0 for m in range(len(text1)+1)] for n in range(len(text2)+1)]
    lcscount = 0

    # text1 is in the x axis and text2 in the y axis. We compare every text1 word to the text2 word of that row.
    # Then, move on to the next text2 word and repeat.
    for i in range(0, len(text2)):
        for u in range(0, len(text1)):
            if text2[i] == text1[u]:
                matrix[i+1][u+1] = 1 + matrix[i][u]
                if matrix[i+1][u+1] > lcscount:
                    lcscount = matrix[i+1][u+1]

    # Get the lcs elements and return it with lcs value
    commonlist = lcs(text1, text2, lcscount)
    return commonlist, lcscount


# The inputs are strings and output is the longes common sequence of words between strings
def getCommonString(text1, text2):
    commonstring = ""
    text1 = createlist(text1)
    text2 = createlist(text2)
    # Get the lcs as a list
    commonlist, value = getlcs(text1, text2)
    # Append list items to form a string
    for word in commonlist:
        commonstring += word + " "

    return commonstring
