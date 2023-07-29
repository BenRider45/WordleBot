
#currently unuesed class
class WordLetter:
    def __init__(self):
        self.availableLetters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.LETTERCORRECT=False

    def checkAvailableLetters(self):
        print(self.availableLetters)

    def CheckLetter(self,str):
        if self.LETTERCORRECT:
            return
        let=str[0]
        status=str[2:]
        if status=='absent':
            return 'absent'
        if status=='present':
            self.availableLetters.remove(let)
            return 'present'
        if status=='correct':
            self.availableLetters=[let]
            self.LETTERCORRECT=True
            return 'correct'
    
        
