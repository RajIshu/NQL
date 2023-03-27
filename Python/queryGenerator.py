
def SQLQueryGenerator(operations, extrakeys, parsedWords):
    query = operations[0]

    # print("Parsed Words: ", parsedWords)

    for each in extrakeys:
        if each == 'all':
            extractWhat = parsedWords[(parsedWords.index(each)) + 1]
            query = query + " * " + extractWhat

        if each == 'from':
            table = parsedWords[(parsedWords.index(each)) + 1]
            # print("Table: ", table)
            query = query + ' from ' + table
    
    return query