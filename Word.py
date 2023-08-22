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


     

            

    def checkTurn(self,tableLst):
        #iterates through the most recent entry's results and eliminaties letters 
        #that are not in the answer from the possible letter choices for each block
        counter=0
        ALL_CORRECT=True
        REPEAT=False
        for i in range(self.lstStartNum,self.lstStartNum+5):
            let=tableLst[i][12]
            status=tableLst[i][15:]
            if status=='absent':
                ALL_CORRECT=False
                INGREEN=False
                INYELLOW=False
                for item in self.yellowLets:
                    if item.lettr==let.lower():
                        INYELLOW=True
                for item in self.greenLets:
                    if item.lettr==let.lower():
                        INGREEN=True
                if not INGREEN and not INYELLOW:
                    if let.lower() not in self.blackLets:
                        self.blackLets.append(let.lower())
                    
                # for item in self.Lettlst:
                #     if let in item:
                #         item.remove(let)
            
            if status=='present in another position':
                ALL_CORRECT=False
                LettInList=False
                for lett in self.blackLets:
                    if lett==let.lower():
                        self.blackLets.remove(lett)
                for item in self.yellowLets:
                    if item.lettr==let.lower():
                        if counter in item.possibleLocs:
                            item.removeLoc(counter)
                        LettInList=True
                if LettInList==False:
                    x=YellowLett(let.lower(),counter)
                    self.yellowLets.append(x)
                        


                # if let in self.Lettlst[counter]:
                #     self.Lettlst[counter].remove(let)
            if status=='correct':
                LettInList=False
                for item in self.yellowLets:
                    if item.lettr==let.lower():
                        self.yellowLets.remove(item)
                if let.lower() in self.blackLets:
                    self.blackLets.remove(let)
                for item in self.greenLets:
                    if item.lettr==let.lower():
                        LettInList=True
                        if counter not in item.location:
                            item.addLoc(counter)
                if LettInList==False:
                    x=GreenLett(let.lower(),counter)
                    self.greenLets.append(x)

                            
                


                # self.Lettlst[counter]=[let]
            
            counter+=1
        self.lstStartNum+=5
        if ALL_CORRECT:
            self.WORD_FOUND=True
    
    def FilterWordList(self):
        i=0
        WORDDELETED=False
        while i< len(self.WORD_LIST):
            item=self.WORD_LIST[i]
            WORDDELETED=False
            for lett in self.blackLets:
                if lett in item:
                    if item in self.WORD_LIST:
                        self.WORD_LIST.remove(item)
                        WORDDELETED=True
                    break
            if WORDDELETED==False:
                for greenlet in self.greenLets:
                    for loc in greenlet.location:
                        if item[loc]!=greenlet.lettr:
                            if item in self.WORD_LIST:
                                self.WORD_LIST.remove(item)
                                WORDDELETED=True
                            break
            if WORDDELETED==False:
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
                            WORDDELETED=True
                        break
            if WORDDELETED==False:
                i+=1

        print(self.WORD_LIST)
    

    
            
    def FindNextWord(self):
        #Uses the available letters to choose a word from a list of all possible words
        print(len(self.WORD_LIST))
        return random.choice(self.WORD_LIST)
       

        # for item in self.WORD_LIST:

            
        #     for i in range(5):
        #         print(item[i])
        #         if item[i] not in self.Lettlst[i]:
                    
        #             self.WORD_LIST.remove(item)
        #             print(item in self.WORD_LIST)
        #             break
        # return random.choice(self.WORD_LIST)








