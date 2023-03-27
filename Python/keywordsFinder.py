from nltk.corpus import wordnet
import duplicacyRemover
import dictFinder

def SynonFinder(word):
	# print("Word: ", word)
	keywords=['delete', 'update', 'insert', 'alter', 'drop', 'select']
	synonyms = []
	for syn in wordnet.synsets(word):
			for l in syn.lemmas():
				synonyms.append(l.name())
		
	result = []

	for each in duplicacyRemover.Remove(synonyms):
		for eachKey in keywords:
			if(each == eachKey):
				result.append(eachKey)
	# print("Result from KF: ", result)

	if not result:
		resultIf = dictFinder.SQLExecutor(word)
		# print("Result from KF inside if: ", resultIf)
		result = resultIf
		# if len(resultIf) >= len(result):
		# 	result = resultIf
	
	return result
					
    
# gotResult = []
# gotResult = SynonFinder('give')
# print("Got Result: ", gotResult)