import mysql.connector 

hostName = "localhost"
username = "root"
psd = "hello1521"

def EstablishConn():
    #Create the connection object   
    myconn = mysql.connector.connect(
        host = hostName, 
        user = username, 
        passwd = psd
    )  

    #creating the cursor object  
    cur = myconn.cursor()
    return myconn,cur

def CloseConn(myconn, cur):
    cur.close()
    myconn.close()


def SQLExecutor(word):
    # Establishing the connection with the database
    myconn, cur = EstablishConn()

    # print("Word from dictFInder: ", word)
    try:
        cur.execute("USE DICTIONARY")
        cur.execute("SELECT RESULTANTTABLE.SQLKEY FROM (SELECT SQLKEY,SYNON FROM KEYWORDS NATURAL JOIN KEYMAP WHERE PKEY=FKEY) RESULTANTTABLE WHERE SYNON='" + word + "'")
    except:
        myconn.rollback()

    result = []
    for x in cur: 
        result.append(x[0])

    # Closing the Cursor and Connection
    CloseConn(myconn, cur)
    return result
  

# print("result:\n", SQLExecutor('change'))
