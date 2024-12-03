
def main():
    with open("InputData.txt") as file:
        leftColumn = []

        rightColumn = []

        DistanceToSum = []
        for i in file:
            lineList = i.strip().split("   ")
            leftColumn.append(int(lineList[0]))
            rightColumn.append(int(lineList[1]))
            
        #Actual procedure below
        while(len(leftColumn) > 0 and len(rightColumn) > 0  ):

            smallestL = min(leftColumn)
            smallestR = min(rightColumn)
            DistanceToSum.append(abs(smallestL-smallestR)) 
            leftColumn.pop(leftColumn.index(smallestL))
            rightColumn.pop(rightColumn.index(smallestR))

        print(sum(DistanceToSum))
main()
