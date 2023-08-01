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
btn=driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[3]/button[2]")
blocker=driver.find_element(By.CLASS_NAME,"purr-blocker-card__button")
if blocker is not None:
    blocker.click()
# py.keyDown('return')
# time.sleep(5)
btn.click()
time.sleep(2)


py.keyDown('esc')
time.sleep(2)
py.write("penis")
py.keyDown("return")
time.sleep(2)
print(len(Word.WORD_LIST))
boxNamelst=gatherData()
Word.checkTurn(boxNamelst)
print("BlackLetts:")
print(Word.blackLets)
for item in Word.yellowLets:
    print("Got here")
    print(f"YellowLett: {item.lettr},{item.possibleLocs}")
for item in Word.greenLets:
    print(f"GreenLett: {item.lettr},{item.location}")



time.sleep(10)
driver.quit()

# keyboard= Controller()

# webbrowser.open("https://www.nytimes.com/games/wordle/index.html")
# time.sleep(1)
# py.keyDown("tab")


# py.keyDown("return")

# py.write("www.nytimes.com/games/wordle/index.html")
# py.keyDown('return')
# time.sleep(2)
# for i in range(25):
#     py.keyDown('tab')
#     time.sleep(.01)
# py.keyDown('return')
# for char in WEB_LINK:
#     keyboard.press(char)
#     print("got here")
#     keyboard.release(char)
#     time.sleep(.0005)
# keyboard.press(Key.enter)


# main()