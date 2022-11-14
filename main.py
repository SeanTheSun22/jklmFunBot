import keyboard
import numpy
import pyautogui
import PIL
import time
import pyperclip
import random
import json

def isturn(Position):
    screen = PIL.ImageGrab.grab(bbox = None)
    pos = x, y = Position["TextBarPosx"], Position["TextBarPosy"]
    pixel = screen.getpixel(pos)
    if pixel == (25, 21, 19):
        return True
    elif pixel == (34, 169, 68):
        pyautogui.click()
        return False
    else:
        return False

def findLetters(Position):
    pyautogui.moveTo(Position["LettersPosx"], Position["LettersPosy"])
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    letters = pyperclip.paste()
    letters = letters.strip()
    letters = letters.lower()
    return letters

def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

def inputword(Words, Letters, n, Position, BonusLifeLetters):

    if BonusLifeLetters == []:
        BonusLifeLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    rand = 0
    found = False
    if random.random() > 0.5:
        found = True
        index = random.randint(0, len(BonusLifeLetters) - 1)
        print(BonusLifeLetters[index])
        i = 0
        while not (Letters in Words[rand] and BonusLifeLetters[index] in Words[rand]):
            rand = random.randint(0,n)
            i += 1
            if i == 1000:
                found = False
                break
    i = 0
    if not found:
        while not Letters in Words[rand]:
            rand = random.randint(0,n)
            i += 1
            if i == n:
                break

    pyautogui.moveTo(Position["TextBarPosx"], Position["TextBarPosy"])
    pyautogui.click()
    for i in range(len(Words[rand])):
        keyboard.write(Words[rand][i])
        time.sleep(random.uniform(0.075, 0.1))

    BonusLifeLetters = diff(BonusLifeLetters, Words[rand])
    print("         Inputted:", Words[rand])
    print("Remaining Letters:", BonusLifeLetters)
    keyboard.press_and_release("enter")
    return BonusLifeLetters
    

def main():
    fp = open("dictionary.txt", "r")
    words = fp.read()
    fp.close()
    words = words.split()
    n = len(words) - 1
    BonusLifeLetters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y"]
    
    print("Hover your cursor over the window to begin")

    with open('position.json', 'r') as openfile:
        Position = json.load(openfile)

    while not keyboard.is_pressed('Esc'):
            MousePos = pyautogui.position()
            if MousePos.x > 0:
                break

    print("Hold escape to exit")

    while not keyboard.is_pressed('Esc'):
        if isturn(Position):
            letters = findLetters(Position)
            print(" Current Sequence:", letters)
            time.sleep(random.uniform(0.5, 1.5))
            BonusLifeLetters = inputword(words, letters, n, Position, BonusLifeLetters)
            time.sleep(random.uniform(0.5, 1.5))


main()
