intro=input("enter your introduction: ")
print(intro)
characterCount=0
wordCount=1
for character in intro:
    characterCount=characterCount+1
    if(character==' '):
        wordCount=wordCount+1
print("number of characters in intro")
print(characterCount)
print("number of words in intro")
print (wordCount)