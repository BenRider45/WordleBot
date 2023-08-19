import random
        
class GreenLett:
    def __init__(self,lettr,location):
        self.lettr=lettr
        self.location=[]
        self.location.append(location)

    def addLoc(self, loc):
        self.location.append(loc)

class YellowLett:
    def __init__(self,lettr,loc):
        self.lettr=lettr
        self.possibleLocs=[0,1,2,3,4]
        self.possibleLocs.remove(loc)
    
    def removeLoc(self, loc):
        self.possibleLocs.remove(loc)



class Word:
    def __init__(self):
        #each sublist represents the possible letters in each block.
        self.Lettlst=[['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']]
        self.greenLets=[]
        self.yellowLets=[]
        self.blackLets=[]
        self.MustHaveLettLst=[]
        self.lstStartNum=0
        self.WORD_FOUND=False
        file=open("words.txt","r")
        self.WORD_LIST=file.read()
        self.WORD_LIST=self.WORD_LIST.split('\n')

        
        # self.WORD_LIST=self.WORD_LIST.split('\n')
        #self.WORD_LIST=self.WORD_LIST.split('\t')
        file.close()



    def CheckWordValid(self,word):
        for i in range(5):
            if word[i] not in self.Lettlst[i]:
                return False
        return True

            

    def checkTurn(self,tableLst):
        #iterates through the most recent entry's results and eliminaties letters 
        #that are not in the answer from the possible letter choices for each block
        counter=0
        ALL_CORRECT=True
        REPEAT=False
        print("Got here")
        for i in range(self.lstStartNum,self.lstStartNum+5):
            print(i)
            print(tableLst[i])
            let=tableLst[i][1]
            status=tableLst[i][15:]
            print(f"let: {let},status: {status}")
            if status=='absent':
                print("Absent Status detected")
                ALL_CORRECT=False
                if let not in self.blackLets:
                    self.blackLets.append(let)
                    
                # for item in self.Lettlst:
                #     if let in item:
                #         item.remove(let)
            
            if status=='present in another position':
                ALL_CORRECT=False
                LettInList=False
                for item in self.yellowLets:
                    if item.lettr==let:
                        if counter in item.possibleLocs:
                            item.removeLoc(counter)
                        LettInList=True
                if LettInList==False:
                    x=YellowLett(let,counter)
                    self.yellowLets.append(x)
                        


                # if let in self.Lettlst[counter]:
                #     self.Lettlst[counter].remove(let)
            if status=='correct':
                LettInList=False
                for item in self.greenLets:
                    if item.lettr==let:
                        LettInList=True
                        if counter not in item.location:
                            item.addLoc(counter)
                if LettInList==False:
                    x=GreenLett(let,counter)
                    self.greenLets.append(x)

                            
                


                # self.Lettlst[counter]=[let]
            
            counter+=1
        self.lstStartNum+=5
        if ALL_CORRECT:
            self.WORD_FOUND=True
    
    def FilterWordList(self):
        for item in self.WORD_LIST:
            for lett in self.blackLets:
                if lett in item:
                    if item in self.WORD_LIST:
                        self.WORD_LIST.remove(item)
                    break
            for greenlet in self.greenLets:
                for loc in greenlet.location:
                    if loc!=greenlet.lettr:
                        if item in self.WORD_LIST:
                            self.WORD_LIST.remove(item)
                        break
            for yellowlet in self.yellowLets:
                LETINWORD=False
                for loc in yellowlet.possibleLocs:
                    if LETINWORD:
                        break
                    if item[loc]==yellowlet.lettr:
                        LETINWORD=True
                if LETINWORD==False:
                    if item in self.WORD_LIST:
                        self.WORD_LIST.remove(item)
                    break
    


            
    def FindNextWord(self):
        #Uses the available letters to choose a word from a list of all possible words
        return random.choice(self.WORD_LIST)
       

        # for item in self.WORD_LIST:

            
        #     for i in range(5):
        #         print(item[i])
        #         if item[i] not in self.Lettlst[i]:
                    
        #             self.WORD_LIST.remove(item)
        #             print(item in self.WORD_LIST)
        #             break
        # return random.choice(self.WORD_LIST)








