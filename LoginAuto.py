from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def icon_check():
    button_pos = pyautogui.locateOnScreen('icon.png', confidence=0.7)
            
    if button_pos != None:
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def password_write():
    button_pos= pyautogui.locateOnScreen('senha.png', confidence=0.7)

    if button_pos != None:
        click(button_pos.left, button_pos.top)
        pyautogui.write('') #sua senha dentro das aspas
        return True
    
    return False

def write():
    pyautogui.write('') #seu nome de usuário dentro das aspas
    return True

def login():
    button_pos= pyautogui.locateOnScreen('login.png', confidence=0.7)

    if button_pos != None:
        click(button_pos.left, button_pos.top)
        return True
    
    return False

def main():
    
    while True:
        if icon_check():
            sleep(8)
            if write():
                if password_write():
                    if login():
                        break


main()