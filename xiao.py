import keyboard
import time
a = 3
while True:
    if keyboard.is_pressed('0') == True:
        print('хватит')
        time.sleep(1)
    if keyboard.is_pressed('1') == True:
        print('перестань')
        time.sleep(1)
    if keyboard.is_pressed('2') == True:
        print('зачем ты продолжаешь?')
        time.sleep(1)
    if keyboard.is_pressed(str(a)) == True:
        print('вы угадали число')
        time.sleep(1)
    if keyboard.is_pressed('4') == True:
        print('повторю хватит!')
        time.sleep(1)
    if keyboard.is_pressed('5') == True:
        print('ладно')
        time.sleep(1)
    if keyboard.is_pressed('6') == True:
        print('...')
        time.sleep(1)
    if keyboard.is_pressed('7') == True:
        print('ты зассоряешь базу данных!')
        time.sleep(1)
    if keyboard.is_pressed('8') == True:
        print('ЭЙ!!')
        time.sleep(1)
    if keyboard.is_pressed('9') == True:
        print('ладноб проходи')
        time.sleep(1)
