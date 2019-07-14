import re

#TASK 1
def RetrieveLetter():
    givenletter = input("What is the letter you would like to count: ")
    while not ErrorCheckLetter(givenletter):
        print("Invalid Input")
        givenletter = input("What is the letter you would like to count: ")
    return givenletter

def ErrorCheckLetter(givenletter):
    if len(givenletter) > 1 :
        return False
    if givenletter.isalpha() == False :
        return False
    else : return True

def RetrieveString():
    stringtocheck = input("Please input String: ")
    while not ErrorCheckString(stringtocheck):
        print("Invalid Input")
        stringtocheck = input("Please input String: ")
    return stringtocheck

def ErrorCheckString(stringtosearch):
    if len(stringtosearch) == 0 :
        return False
    else : return True

def CountOccurencesOfLetterInString(givenletter, stringtosearch):
    count = 0
    for letter in stringtosearch.lower():
        if letter == givenletter.lower():
            count = count + 1
    return count


def CountOccurencesOfGivenLetterInString():
    givenletter = RetrieveLetter()
    stringtosearch = RetrieveString()
    return (CountOccurencesOfLetterInString(givenletter,stringtosearch))

#TASK 2


def RemoveNonAlphabet(stringtoremovenonaplhabet):
    regex = re.compile('[^a-zA-Z]')
    stringonlyalphabet = regex.sub('', stringtoremovenonaplhabet)
    return stringonlyalphabet


def CheckifPalindrome(stringtocheck):
    if stringtocheck==stringtocheck[::-1]:
        return True
    else : return False

def CheckIfStringIsPalindrome():
    stringtocheck = RetrieveString()
    stringonlyalphabet = RemoveNonAlphabet(stringtocheck)
    return (CheckifPalindrome(stringonlyalphabet.lower()))


#TASK 3
#part a

def GetCensoredWords():
    censoredwordsstring = input("Please write censored words separated by a , :")
    censoredwordsarray = censoredwordsstring.split(',')
    return censoredwordsarray


def CountOccurencesOfCensoredWordsInString(censoredwordsarray, stringtocheck):
    arrayofarraysofwordsandcounts = []
    totalcount = 0
    for word in censoredwordsarray:
        count = stringtocheck.lower().count(word.lower())
        totalcount = totalcount+count
        arrayofarraysofwordsandcounts.append([word,count])
    arrayofarraysofwordsandcounts.append(['Total',totalcount])
    return arrayofarraysofwordsandcounts



def CountCensoredWordsInString():
    censoredwords = GetCensoredWords()
    stringtocensor = RetrieveString()
    print(CountOccurencesOfCensoredWordsInString(censoredwords,stringtocensor))



#Part b
def CreateCensoredWord(wordtocensor):
    if len(wordtocensor)>2 :
        censoredword = wordtocensor[:1]
        censoredword = censoredword + ("$"*(len(wordtocensor)-2))
        censoredword = censoredword + wordtocensor[-1:]
        return censoredword
    else :
        censoredword = "$"*len(wordtocensor)
        return censoredword

def LowerAllStringsInArray(arrayofstrings):
    arrayoflowerstrings = []
    for word in arrayofstrings:
        arrayoflowerstrings.append(word.lower())
    return arrayoflowerstrings


def CensorWordsinString(censoredwordsarray,stringtocensor):
    stringwithwordscensored = stringtocensor
    stringtocensorarrayofwords = re.findall(r"[\w']+|[.,!?;]", stringtocensor)
    censoredwordsarraylower = LowerAllStringsInArray(censoredwordsarray)
    for word in stringtocensorarrayofwords :
        if word.lower() in censoredwordsarraylower :
            stringwithwordscensored = stringwithwordscensored.replace(word,CreateCensoredWord(word))
    return stringwithwordscensored


def CensorGivenWordsInString():
    censoredwords = GetCensoredWords()
    stringtocensor = RetrieveString()
    print(CensorWordsinString(censoredwords,stringtocensor))


#part c
def CensorPalindromesInString(stringtocensor):
    censoredstring = stringtocensor
    stringtocensorarray = stringtocensor.split(' ')
    for word in stringtocensorarray:
        if CheckifPalindrome(word.lower()):
            censoredstring = censoredstring.replace(word,CreateCensoredWord(word))
    return censoredstring




def CensorPalindromesInGivenString():
    stringtocensor = RetrieveString()
    print(CensorPalindromesInString(stringtocensor))

#part d
#user input. The application can ask the user to manually type each censored word, this can be done by reading the
#user input and separeting by a space or comma.
#read from file. The application could read from a file containing the censored words list. Again each word could be
#separated by a space or comma, or in this case each word could be on a new line.
#read from database. The application could create a censored words list by reading entries from a database table.


def test_CountOccurencesOfLetterInString():
    assert CountOccurencesOfLetterInString('e',"I have some cheese")==5
    assert CountOccurencesOfLetterInString('E',"I have some cheese")==5
    assert CountOccurencesOfLetterInString('',"I have some cheese")==0

def test_CheckIfPalindrome():
    assert CheckifPalindrome("I have some cheese")==False
    assert RemoveNonAlphabet("God saved Eva’s dog")=="GodsavedEvasdog"
    assert CheckifPalindrome("GodsavedEvasdog".lower())==True

def test_CountOccurencesOfCensoredWordsInString():
    assert CountOccurencesOfCensoredWordsInString(["dog", "cat", "large"],"I have a cat named Meow and a dog name Woof. I love the dog a lot. He is larger than a small horse.")==[['dog', 2], ['cat', 1], ['large', 1], ['Total', 4]]


def test_CensorWordsInString():
    assert CensorWordsinString(["meow", "woof"],"I have a cat named Meow and a dog name Woof. I love the dog a lot. He is larger than a small horse.")=="I have a cat named M$$w and a dog name W$$f. I love the dog a lot. He is larger than a small horse."

def test_CensorPalindromesInString():
    assert CensorPalindromesInString("Anna went to vote in the election to fulfil her civic duty")=="A$$a went to vote in the election to fulfil her c$$$c duty"

if __name__ == '__main__':
    test_CountOccurencesOfLetterInString()
    test_CheckIfPalindrome()
    test_CountOccurencesOfCensoredWordsInString()
    test_CensorWordsInString()
    test_CensorPalindromesInString()
