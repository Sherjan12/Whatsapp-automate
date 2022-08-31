import datetime
import pyautogui
import os
import pyperclip

current_time = datetime.datetime.now()
time_delta = datetime.timedelta(seconds=4)
t = (current_time + time_delta)
print(current_time)
print(t)


def send_message():
    while True:
        s = datetime.datetime.now()

        if t <= s:

            os.startfile("C:/Users/Jan\'s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/WhatsApp/WhatsApp")
            pyautogui.sleep(5)

            c = pyautogui.locateOnScreen("Sir.png")
            print(c)

            pyautogui.moveTo(c, duration=.5)

            pyautogui.click()

            pyautogui.sleep(2)
            l = pyautogui.locateOnScreen('Typer.png')
            pyautogui.moveTo(l)
            pyautogui.sleep(2)
            # pyautogui.typewrite("Should I shutdown the laptop\n")
            # pyautogui.sleep(2)
            b = pyautogui.locateOnScreen("ClickHere.png")
            pyautogui.moveTo(b)
            pyautogui.click()

            break


def wait():
    while True:

        w = pyautogui.locateOnScreen("Sir.png")
        print(w)

        pyautogui.moveRel(-20, 3)
        pyautogui.moveTo(w)
        m = pyautogui.displayMousePosition()
        print(m)

        pyautogui.click()

        s = pyautogui.locateOnScreen("Smiley.png")
        pyautogui.moveTo(s)

        # pyautogui.moveTo(x=599, y=608, duration=.5)
        pyautogui.moveRel(80,-60)
        pyautogui.rightClick()
        pyautogui.sleep(2)
        pyautogui.doubleClick()
        pyautogui.sleep(4)
        pyautogui.rightClick()
        pyautogui.sleep(2)
        pyautogui.moveRel(15, 15)
        pyautogui.sleep(1)
        pyautogui.leftClick()
        global message
        message = pyperclip.paste()
        # if message is None:
        #     print('lol')
        pyautogui.sleep(10)

        if not message:
            print("there is no msg")
        else:
            print(message)
            break


def response():
    # f = message.lower(message)

    if message == 'yes':
        os.system('shutdown /s')
    elif message == 'video call' or 'videocall':
        os.startfile("C:/Users/Jan\'s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/WhatsApp/WhatsApp")
        pyautogui.sleep(5)
        s = pyautogui.locateOnScreen('Sir.png')
        pyautogui.moveTo(s)
        pyautogui.click(interval = .3)
        v = pyautogui.locateOnScreen('video call.png')
        pyautogui.moveTo(v)
        pyautogui.click(interval=.3)
    else:
        print('ERROR')


send_message()
wait()
response()
