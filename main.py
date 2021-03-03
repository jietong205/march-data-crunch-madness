from random import random
def printIntro():
    print("MDCM GAME SIMPLIZED SIMULATION BY TYPING INPUT")
    print("We need both team's score (such as seed number, coach rank)（type 0 - 1 in the terminal）")
def getInputs():
    a = eval(input("Please put in team 1's ability value (0-1): "))
    b = eval(input("Please put in team 2's ability value (0-1): "))
    n = eval(input("The number of games will be played: "))
    return a, b, n
def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(1,n+1):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def gameOver(a,b):
    if a>=97.5 and b>=97.5:
        if abs(a-b)==5:
            return True
    if a<100 or b<100:
        if a==100 or b==100:
            return True
    else:
        return False
def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 2.5
            else:
                scoreB +=2.5
                serving="B"
        else:
            if random() < probB:
                scoreB += 2.5
            else:
                scoreA += 2.5
                serving="A"
        return scoreA, scoreB
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("The analysis ends，total in {} simulation games".format(n))
    print("team 1 winned {} games，percentage is {:0.1%}".format(winsA, winsA/n))
    print("team 2 winned {} games，percentage is {:0.1%}".format(winsB, winsB/n))
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()
