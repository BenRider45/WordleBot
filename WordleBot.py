import pyautogui as py
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import time
import Word as W

Word=W.Word()
def gatherData():
    boxLst= driver.find_elements(By.CLASS_NAME ,"Tile-module_tile__UWEHN")
    boxNamelst=[]
    for thing in boxLst:
        boxName= thing.get_attribute("aria-label")
        boxNamelst.append(boxName)
    return boxNamelst

driver= webdriver.Chrome()
driver.get("https://www.nytimes.com/games/wordle/index.html")
try:
    termsAndCondButton = driver.find_element(By.XPATH,"/html/body/div[3]/div/div/button")
    if termsAndCondButton is not None:
        termsAndCondButton.click()
    btn=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/button[3]") 

except exceptions.NoSuchElementException:
    print("No Element Found!")
except:
    print("Extra Broken")

#btn=driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div > div > div > div > div.Welcome-module_buttonContainer__K4GEw > button:nth-child(3)") 
try:
    blocker=driver.find_element(By.CLASS_NAME,"Modal-module_closeIcon__TcEKb")
    if blocker is not None:
        blocker.click()
except exceptions.NoSuchElementException:
    doNothing=True
except:
    print("Different oopsie occured")




btn.click()
time.sleep(2)

#Entering the first word entry
py.keyDown('esc')
time.sleep(2)
py.write("lemur")
py.keyDown("return")

#Enters a word or collects datwa either 5 more times or until the word is found
for i in range(5):
    if Word.WORD_FOUND:
        break
    time.sleep(2)
    #print(len(Word.WORD_LIST))
    boxNamelst=gatherData()
    Word.checkTurn(boxNamelst)
    #print("BlackLetts:")
    #print(Word.blackLets)
    #for item in Word.yellowLets:
        #print(f"YellowLett: {item.lettr},{item.possibleLocs}")
    #for item in Word.greenLets:
        #print(f"GreenLett: {item.lettr},{item.location}")
    #print(f"WORD_LIST len: {len(Word.WORD_LIST)}")
    Word.FilterWordList()
    #print(f"WORD_LIST len: {len(Word.WORD_LIST)}")
    time.sleep(1)
    py.write(Word.FindNextWord())
    py.keyDown("return")
    time.sleep(2)

if Word.WORD_FOUND:
    print("Word Found!")
time.sleep(3)
driver.quit()
