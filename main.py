import time
import keyboard
import psutil
import pyautogui
from colorama import Fore, Style
from pystyle import Colors, Colorate
import pywinauto.mouse
import pywinauto.keyboard

pyautogui.PAUSE=2.5
pyautogui.FAILSAFE=False

playbutton_png = "assets/Play.png"
deathmatch_png = "assets/Deathmatch.png"
start_png = "assets/Start.png"
MatchResults_png = "assets/MatchResults.png"
Bullets_png = "assets/Bullets.png"
PROCNAME = "VALORANT-Win64-Shipping.exe"
ingame_png = "assets/ingame.png"
judge_png = "assets/judge.png"
judgebullets_png = "assets/judgebullets.png"

print(Colorate.Horizontal(Colors.rainbow, """
      
      ya afk dolbaeb  || razverni igru                                                                                                                                                          
      """))


def valorantrunning():
    found = False
    print(Fore.YELLOW, "[-] CHECKING IF VALORANT IS RUNNING")
    print(Style.RESET_ALL)
    time.sleep(2)

    for proc in psutil.process_iter():
        if proc.name() == "VALORANT-Win64-Shipping.exe":
            found = True
            break

    if not found:
        print(Fore.RED, "[!] VALORANT IS NOT RUNNING")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN, "[√] VALORANT IS RUNNING")
        time.sleep(4)
valorantrunning()

azerty = "z"
qwerty = "w"

print("F2 - Запуск")
print("Hold F3 - Стоп")

time.sleep(0.3)

#Click on play in main menu of valorant
def clickplay():
    playbutton = pyautogui.locateOnScreen(playbutton_png, confidence = 0.6)
    if playbutton:
        print("Нажимаю кнопку Play")
        time.sleep(0.3)
        pyautogui.moveTo(playbutton, duration = 0.2)
        time.sleep(0.3)
        pyautogui.doubleClick(playbutton)

#Click on deathmatch
def clickdeathmatch():
    deathmatchclick = pyautogui.locateOnScreen(deathmatch_png, confidence = 0.6)
    if deathmatchclick:
        print("Нажимаю кнопку DeathMatch")
        time.sleep(0.3)
        pyautogui.moveTo(deathmatchclick, duration = 0.2)
        time.sleep(0.3)
        pyautogui.doubleClick(deathmatchclick)
        time.sleep(0.3)

#Click on start
def clickstart():
    startclick = pyautogui.locateOnScreen(start_png, confidence = 0.6)
    if startclick:
        print("Запускаю игру")
        time.sleep(0.3)
        pyautogui.moveTo(startclick, duration = 0.2)
        time.sleep(0.3)
        pyautogui.doubleClick(startclick)
        time.sleep(10)

def afk():
    pywinauto.mouse.press(button='left')
    time.sleep(0.3)
    pywinauto.mouse.release(button='left')
    keyboard.press('w')
    time.sleep(1)
    keyboard.release('w')
    keyboard.press('a')
    pywinauto.mouse.press(button='left')
    time.sleep(0.3)
    pywinauto.mouse.release(button='left')
    time.sleep(1)
    keyboard.release('a')
    pywinauto.mouse.press(button='left')
    time.sleep(0.3)
    pywinauto.mouse.release(button='left')
    keyboard.press("s")
    pywinauto.mouse.press(button='left')
    time.sleep(0.3)
    pywinauto.mouse.release(button='left')
    time.sleep(1)
    keyboard.release("s")
    pywinauto.mouse.press(button='left')
    time.sleep(0.3)
    pywinauto.mouse.release(button='left')
    time.sleep(0.1)
    pywinauto.mouse.press(button='left')
    time.sleep(0.3)
    pywinauto.mouse.release(button='left')


def ingame():
    IngameS = pyautogui.locateOnScreen(ingame_png, confidence = 0.6, grayscale = True)
    JudgeBullets = pyautogui.locateOnScreen(judgebullets_png, confidence=0.6, grayscale=True)
    if JudgeBullets:
        print("В матче, активирую автобег")
        afk()
    if IngameS:
        print("Покупаю оружие")
        keyboard.press("b")
        time.sleep(0.2)
        keyboard.release("b")
        judgelocation = pyautogui.locateOnScreen(judge_png, confidence=0.6, grayscale=True)
        pyautogui.doubleClick(judgelocation)
        time.sleep(0.4)
        keyboard.press("b")
        time.sleep(0.1)
        keyboard.release("b")
        afk()

def Matchfinished():
    MatchFinish = pyautogui.locateOnScreen(MatchResults_png, confidence=0.6)
    if MatchFinish:
        print("Матч закончен")
        print("Начинаю новый")
        clickplay()
        clickdeathmatch()
        clickstart()
        ingame()

def Loopa():
    loop = True
    while loop:
        if keyboard.is_pressed("F3"):
            print("Скрипт завершает работу...")
            time.sleep(1)
            loop = False
        else:
            clickplay()
            clickdeathmatch()
            clickstart()
            ingame()
            Matchfinished()

start = True
while start:
    if keyboard.is_pressed("F2"):
        print("Скрипт запускается...")
        start = False
        Loopa()


