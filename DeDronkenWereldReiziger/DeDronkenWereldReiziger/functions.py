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
    amountOfUsers = 0
    
    if(key == BACKSPACE):
        amountOfUsers = 0
        
    if(key == '2' or key == '3' or key == '4'):
        amountOfUsers = key
    else:
        amountOfUsers = 0
        
    return amountOfUsers

def PositionBlink(input, maxLengthInput):
    global positionBlink
    
    if(input == 0):
        positionBlink = 500
    else:
        if(input == '2' or input == '3' or input == '4'):
            positionBlink = 500
            positionBlink = positionBlink + 7
        else:
            positionBlink = positionBlink - 7
    
    return positionBlink
        
def createUser(inputWord):
    global userName
    
    if(key == ENTER):
        inputWord == ''
        return inputWord
    
    if (key != ENTER):
        if (int(ord(key)) == 8):
            inputWord = inputWord[:-1]
            return inputWord
        else:
            inputWord = inputWord + str(key)      
            return inputWord

def loopThroughBlink(InputWord):
    global x
    
    whileInputWord = str(InputWord)
    totalLenghtInputWord = len(whileInputWord)
    
    x = 500
    
    i = 0
    while(totalLenghtInputWord >= i):
        lastLetterOfString = whileInputWord[-1:]
        
        # dit zijn de letters i, j, l
        if(lastLetterOfString == 'i' or lastLetterOfString == 'j' or lastLetterOfString == 'l'):
            x = int(x) + 3
        # dit zijn de letters w & m & e
        elif(lastLetterOfString == 'w' or lastLetterOfString == 'm' or lastLetterOfString == 'e'):
            x = int(x) + 7
        # dit zijn alle overige letters van het alphabet
        else:
            x = x + 5
        
        whileInputWord = whileInputWord[:-1]
        i += 1
    return x
    
def pushBlink(InputWord):
    global x
    
    # alleen kleine letters worden gecheckt
    # als er backspace gedaan wordt dan wordt er wat afgehaald van de positie 
    if(len(InputWord) == 0):
        x = 500
    
    if(key != ENTER):
        
        if(int(ord(key)) == 8):
            
            if(len(InputWord) >= 1):
                lastLetterOfString =  (InputWord[-1:])
                
                # dit zijn de letters i, j, l
                if(int(ord(lastLetterOfString)) == 105 or int(ord(lastLetterOfString)) == 108 or int(ord(lastLetterOfString)) == 106):
                    x = int(x) - 3
                # dit zijn de letters w & m & e
                elif(int(ord(lastLetterOfString)) == 109 or int(ord(lastLetterOfString)) == 119 or int(ord(lastLetterOfString)) == 101):
                    x = int(x) - 7
                # dit zijn alle overige letters van het alphabet
                else:
                    x = int(x) - 5
        else:        
            # dit zijn de letters i, j, l
            if(int(ord(key)) == 105 or int(ord(key)) == 108 or int(ord(key)) == 106):
                x = int(x) + 3
            # dit zijn de letters w & m
            elif(int(ord(key)) == 109 or int(ord(key)) == 119 or int(ord(key)) == 101):
                x = int(x) + 7
            # dit zijn alle overige letters van het alphabet
            else:
                x = x + 5
                
    return x    


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
    
