import time, pyautogui

def waiter(a):
    count=a
    for i in range(0,count):
        print('wait', count,'second(s)')
        count=count-1
        time.sleep(1)
    print('starting')

def wait(a):
    time.sleep(a)
    
def press(a):
    pyautogui.press(a)

def click(a,b):
    pyautogui.click(a,b)

def powerUp(a):
    for i in range(0,a):
        click(1646, 229)
        wait(0.1)

def cursor(a):
    for i in range(0,a):
        click(1740,350)
        wait(0.1)

def grandma(a):
    for i in range(0,a):
        click(1813, 400)
        wait(0.1)

def farm(a):
    for i in range(0,a):
        click(1743,471)
        wait(0.1)

def mine(a):
    for i in range(0,a):
        click(1748, 528)
        wait(0.1)

def factory(a):
    for i in range(0,a):
        click(1761, 605)
        wait(0.1)

def bank(a):
    for i in range(0,a):
        click(1769, 652)
        wait(0.1)

def temple(a):
    for i in range(0,a):
        click(1761, 740)
        wait(0.1)

def wizard(a):
    for i in range(0,a):
        click(1752, 785)
        wait(0.1)

def shipment(a):
    for i in range(0,a):
        click(1752, 862)
        wait(0.1)

def alchemy(a):
    for i in range(0,a):
        click(1712, 905)
        wait(0.1)

def valami1(a):
    for i in range(0,a):
        click(1762, 996)
        wait(0.1)

def valami2(a):
    for i in range(0,a):
        click(1739,1021)
        wait(0.1)

def downCycle():
    cursor(1)
    grandma(1)
    farm(1)
    mine(1)
    factory(1)
    bank(1)
    temple(1)
    wizard(1)
    shipment(1)
    alchemy(1)
    valami1(1)
    valami2(1)
    powerUp(1)

def topCycle():
    powerUp(1)
    valami2(1)
    valami1(1)
    alchemy(1)
    shipment(1)
    wizard(1)
    temple(1)
    bank(1)
    factory(1)
    mine(1)
    farm(1)
    grandma(1)
    cursor(1)

def cookieClick():
        click(284,500)
        wait(0.1)

count=0

cycles=int(input('Amount of cycles: '))
cycleBreak=int(input('Time between cycles: '))
autoClick=input('Auto click between upgrades y/n? ')
clicksBetweenCycles=int(input('Amount clicks between cycles: '))
waiter(5)
for i in range(0,cycles):
    topCycle()
    count=count+1
    if autoClick=='y':
        for i in range(0,clicksBetweenCycles):
            cookieClick()
    print(round((count/cycles)*100, 2),'% done')
    wait(cycleBreak)
