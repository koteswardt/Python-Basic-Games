import time
gameScore = 0
wrongquestions = 0
print("<---Welcome to the Quiz Games--->")
GameEntry = input("Would you like to play the Quiz Y/N?  ")
if (GameEntry == "y" or GameEntry == "Y" or GameEntry == "yes" or GameEntry == "YES"):
    playerName = input("Please enter the Name before playing the Quiz: ")
    print("{} the quiz will begin in 3 seconds".format(playerName))
    time.sleep(3);
    userInput1 = int(input("In which year the 1st iphone launched? "))
    ans1 = 2007
    if userInput1 == ans1:
        gameScore+=1
    else:
        wrongquestions+=1
    userInput2 = input("What is the hero name in bahubhalli? ")
    ans2 = "prabhas"
    if userInput2.lower() == ans2:
        gameScore+=1
    else:
        wrongquestions+=1
    userInput3 = int(input("In which year the covid occurred? "))
    ans3 = 2019
    if userInput3 == ans3:
        gameScore+=1
    else:
        wrongquestions+=1
    userInput4 = input("In which country do we have niagara falls? ")
    ans4 = "canada"
    if userInput4.lower() == ans4:
            gameScore+=1
    else:
        wrongquestions+=1
    userInput5 = input("Who's mr.bean? ")
    ans5 = "comedian"
    if userInput5.lower() == ans5:
        gameScore+=1
    else:
        wrongquestions+=1
    userInput6 = int(input("Price of new macbook2? "))
    ans6 = 100000
    if userInput6 == ans6:
        gameScore+=1
    else:
        wrongquestions+=1
    

    print("{} your total correct answers user answers is:", gameScore,format(playerName))
    print("{} total wrong answers user answers is:", wrongquestions,format(playerName))
else:
    print("Don't forget to play next time")
