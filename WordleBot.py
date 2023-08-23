import webbrowser
import pyautogui as py
from pynput.keyboard import  Key, Controller
from selenium import webdriver
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
btn=driver.find_element(By.CLASS_NAME,"Welcome-module_button__ZG0Zh")
blocker=driver.find_element(By.CLASS_NAME,"purr-blocker-card__button")
if blocker is not None:
    blocker.click()

btn.click()
time.sleep(2)


py.keyDown('esc')
time.sleep(2)
py.write("lemur")
py.keyDown("return")
for i in range(5):
    if Word.WORD_FOUND:
        break
    time.sleep(2)
    print(len(Word.WORD_LIST))
    boxNamelst=gatherData()
    Word.checkTurn(boxNamelst)
    print("BlackLetts:")
    print(Word.blackLets)
    for item in Word.yellowLets:
        print(f"YellowLett: {item.lettr},{item.possibleLocs}")
    for item in Word.greenLets:
        print(f"GreenLett: {item.lettr},{item.location}")
    print(f"WORD_LIST len: {len(Word.WORD_LIST)}")
    Word.FilterWordList()
    print(f"WORD_LIST len: {len(Word.WORD_LIST)}")
    time.sleep(1)
    py.write(Word.FindNextWord())
    py.keyDown("return")
    time.sleep(2)
time.sleep(10)
driver.quit()
