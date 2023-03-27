import keywordsFinder
import findMoreKeywords
import queryGenerator

def KeywordsParser(statement):
    words = statement.split(" ")
    return words

def GetMeOperations():
    operationList = []
    for each in parsedWords:
        eachList = keywordsFinder.SynonFinder(each)
        # print(eachList)
        if eachList:
            operationList.append(eachList)

    return operationList[0]


# sent = input("What do you want to perform: ")
sent = 'choose all boys from student'
parsedWords = KeywordsParser(sent)
Operations = GetMeOperations()
print("Operation List: ", Operations)

extraKeys = findMoreKeywords.MoreKeys(parsedWords)
print("Extra Keys: ", extraKeys)

print("SQL Query: ", queryGenerator.SQLQueryGenerator(Operations, extraKeys, parsedWords))