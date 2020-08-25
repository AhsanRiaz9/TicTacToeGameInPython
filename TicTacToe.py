def displayBoard(array):
    for i in range(3):
        for j in range(3):
            print(array[i][j],end="\t")
        print()

def isValidPosition(array,index):
    if(index<1 or index>9):
        return -1
    x = int((index - 1) / 3)
    y = (index - 1) % 3
    value = array[x][y]
    if(type(value)==str):
        return 0
    else:
        return 1

def markBoard(array,index,symbol):
    x = int((index - 1) / 3)
    y = (index - 1) % 3
    array[x][y]=symbol

def isSameRow(array):
    for i in range(3):
        if(array[i][0]==array[i][1] and array[i][1]==array[i][2]):
            return 1
    return 0

def isSameCol(array):
    for i in range(3):
        if(array[0][i]==array[1][i] and array[1][i]==array[2][i]):
            return 1
    return 0

def isSameDigonal(array):
    if(array[0][0]==array[1][1] and array[1][1]==array[2][2]):
        return 1
    elif (array[0][2]==array[1][1] and array[1][1]==array[2][0]):
        return 1
    else:
        return 0

def isWin(array):
    if(isSameRow(array) or isSameCol(array) or isSameDigonal(array)):
        return 1
    else:
        return 0
def startGame():
    array=[[1,2,3],[4,5,6],[7,8,9]]
    symbol1 = input(str("Enter Player 1 Symbol:\t"))
    symbol2 = input(str("Enter Player 1 Symbol:\t"))
    displayBoard(array)
    gameStatus=0
    count=0
    index=1
    flag=0
    currentPlayerSymnol=symbol1
    while(gameStatus!=1):
        flag=0
        print()
        if(count%2==0):
            currentPlayerSymnol=symbol1
            while(flag!=1):
                index = int(input("Player 1 Turn: Enter Cell #:\t"))
                flag=isValidPosition(array,index)
                if(flag==-1):
                    print("Invalid Position")
                elif(flag==0):
                    print("Position is Already Marked")
            markBoard(array,index,currentPlayerSymnol)
            displayBoard(array)
        else:
            currentPlayerSymnol = symbol2
            while (flag != 1):
                index = int(input("Player 2 Turn: Enter Cell #:\t"))
                flag = isValidPosition(array, index)
                if (flag == -1):
                    print("Invalid Position")
                elif (flag == 0):
                    print("Position is Already Marked")
            markBoard(array, index, currentPlayerSymnol)
            displayBoard(array)
        gameStatus=isWin(array)
        if(gameStatus==1):
            print("Game Won by Player:",end="\t")
            if(currentPlayerSymnol==symbol1):
                print(1)
            else:
                print(2)
        count = count + 1

#main
startGame()
