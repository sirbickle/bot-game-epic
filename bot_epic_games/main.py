import pyautogui
import time
import Biblioteca
import os

pyautogui.press("win")
time.sleep(2)
pyautogui.write("epic")
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)
confirm = Biblioteca.ExistsOnScreen('FullScreen.png')
if confirm == True:
    pyautogui.click('FullScreen.png')
    pyautogui.moveTo(1000,500)
    pyautogui.scroll(-1700)
    time.sleep(5)
    try:
        pyautogui.click('gratis.png')
        time.sleep(2)
        confirm = Biblioteca.ExistsOnScreen('NaBiblioteca.png')
        time.sleep(2)
        if confirm == True:
            pyautogui.hotkey('alt', 'f4')
            Biblioteca.SendMailPossui()
            ###os.system("shutdown /s /t 10")
        else:
            pyautogui.click('obter.png')
            time.sleep(5)
            pyautogui.click('fazer_pedido.png')
            time.sleep(5)
            pyautogui.click('ver_na_biblioteca.png')
            time.sleep(5)
            pyautogui.press('alt', 'f4')
            Biblioteca.SendMailPossui()
            ###os.system("shutdown /s /t 10")
    except pyautogui.ImageNotFoundException:
        pyautogui.press('alt', 'f4')
        Biblioteca.SendMailErro()
        ###os.system("shutdown /s /t 10")
else:
    pyautogui.moveTo(1000,500)
    pyautogui.scroll(-1700)
    time.sleep(5)
    try:
        pyautogui.click('gratis.png')
        time.sleep(5)
        confirm = Biblioteca.ExistsOnScreen('NaBiblioteca.png')
        time.sleep(2)
        if confirm == True:
            pyautogui.hotkey('alt', 'f4')
            Biblioteca.SendMailPossui()
            ###os.system("shutdown /s /t 10")
        else:
            pyautogui.click('obter.png')
            time.sleep(5)
            pyautogui.click('fazer_pedido.png')
            time.sleep(5)
            pyautogui.click('ver_na_biblioteca.png')
            time.sleep(5)
            pyautogui.hotkey('alt', 'f4')
            Biblioteca.SendMailPossui()
            ###os.system("shutdown /s /t 10")
    except pyautogui.ImageNotFoundException:
        pyautogui.hotkey('alt', 'f4')
        Biblioteca.SendMailErro()
        ###os.system("shutdown /s /t 10")

