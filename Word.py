import WordLetter
        



class Word:
    def __init__(self):
        self.Lettlst=[['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]
        self.lstStartNum=0
        self.WORD_FOUND=False

    def checkTurn(self,tableLst):
        counter=0
        ALL_CORRECT=True
        for i in range(self.lstStartNum,self.lstStartNum+5):
            let=tableLst[i][0]
            status=tableLst[i][2:]
            if status=='absent':
                ALL_CORRECT=False
                for item in self.Lettlst:
                    if let in item:
                        item.remove(let)
            
            if status=='present':
                ALL_CORRECT=False
                if let in self.Lettlst[counter]:
                    self.Lettlst[counter].remove(let)
            if status=='correct':
                self.Lettlst[counter]=[let]
            
            counter+=1
        self.lstStartNum+=5
        if ALL_CORRECT:
            self.WORD_FOUND=True
    
    def FindNextWord(self):
        pass

        
    




