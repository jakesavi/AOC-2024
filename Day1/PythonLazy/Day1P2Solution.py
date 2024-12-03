

def GetData():
    with open("InputData.txt") as InputData:
        LeftList = []
        RightList = []
        for Line in InputData:
            LineList = Line.strip().split("   ")
            LeftList.append(int(LineList[0]))
            RightList.append(int(LineList[1]))
        InputData.close()
    return [LeftList, RightList]

def SimilarityScore(DataInput): 
    LeftList = DataInput[0]
    RightList = DataInput[1]
    SimilarityList = []
    while(len(LeftList) > 0):
        FindSimilarity = LeftList.pop(0)
        Count = 0
        for target in RightList:
            if FindSimilarity == target:
                Count = Count + 1
        #Now We Can add Both 
        SimilarityList.append(FindSimilarity*Count) 

    return sum(SimilarityList)


def main():
   print(SimilarityScore(GetData())) 
    

main()
    




