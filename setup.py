import keyboard
import pyautogui
import json

def FindPos():
    print("Press \"S\" to set position at current cursor position")
    keyboard.wait("s")
    return pyautogui.position()

print("Place cursor over the center letters")
LettersPos = FindPos()
keyboard.wait("s")
print("Place cursor over the typing bar")
TextBarPos = FindPos()

Positions = {
    "LettersPosx":LettersPos.x,
    "LettersPosy":LettersPos.y,
    "TextBarPosx":TextBarPos.x,
    "TextBarPosy":TextBarPos.y
}

with open("position.json", "w") as outfile:
    json.dump(Positions, outfile)

