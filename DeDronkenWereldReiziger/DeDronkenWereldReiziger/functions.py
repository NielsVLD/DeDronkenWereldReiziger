import json

blinkTime = None
blinkOn = None

userName = ''

# -----------------------------------------        
# for the json crud
# https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/    
# -----------------------------------------        

gameData = {}
qanda={}
userNames = []
test = None
counter = 0

def getJson():
    with open('gameData.txt') as json_file:
        gameData = json.load(json_file)
        
    return gameData

def createRectWithColor(x, y, widthRect, heightRect, choosenColor):
    fill(choosenColor)
    rect(x , y, widthRect, heightRect)
    fill(255)
    
def blink(x1, y1, x2, y2):
    global blinkOn, blinkTime
    
    y2 = y1 + 30

    if(blinkOn):
        line(x1, y1, x2, y2)
        
    if(millis() - 500 > blinkTime):
        blinkTime = millis()
        blinkOn = not blinkOn


def clearPage():
    background(0)
    background(51)
    
def amountOfUsers():
    amountOfUsers = None
    
    if(key == BACKSPACE):
        amountOfUsers = None
        return amountOfUsers
    
    if(key == '2' or key == '3' or key == '4'):
        amountOfUsers = key
        return amountOfUsers
    else:
        amountOfUsers = 'Dit is geen 2, 3 of 4'
        return amountOfUsers
    
def createUsers():
    global test, gameData, counter

    gameData = getJson()
    
    i = 1

    text('Vul hieronder in uw naam speler ' + str(i), width/2, 20)
    textAlign(CENTER)
    
    rect(width/4, height/ 5, 300, 80)
    fill(37, 107,133)
    
def createUser():
    global userName
    
    if (int(ord(key)) == 8):
        if userName!=None: 
            userName = userName[:-1]
        return userName
    else:
        if userName==None: 
            userName=''
        userName = userName + str(key)          
        return userName
    
def clearUserInput():
    global userName
    userName = None
    return userName

def showImage(imagee, xPosition, yPosition):
    imageMode(CENTER)
    image(imagee, xPosition, yPosition)
    
    
def onRect(x, y, width, height):
    return(mouseX >= x and mouseX <= x + width and mouseY >= y and mouseY <= y + height)


def getQAndAJson():
    with open('qanda.json') as json_file:
        qanda = json.load(json_file)
        
    return qanda
    
