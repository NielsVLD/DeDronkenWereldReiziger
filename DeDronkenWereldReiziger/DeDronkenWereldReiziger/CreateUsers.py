# Sander Moerman, INF1K, 0988465
import functions
import json

rectXDrankCheck = 660
rectYDrankCheck = 680
rectWidth = 50
rectHeight = 50

y1Blink = 210
y2Blink = y1Blink + 30

# this data is only be used on this screen
mainScreenData = {}
mainScreenData['showContinueText'] = None
mainScreenData['errorMessage'] = ''
mainScreenData['secondScreen'] = None
mainScreenData['thirdScreen'] = None
mainScreenData['userName'] = ''
mainScreenData['i'] = 1
mainScreenData['checkImage'] = None



# this data will be used through the whole game
gameData = {}
gameData['drank'] = None
gameData['amountOfPlayers'] = 0
gameData['users'] = []
gameData['colors'] = []

checked = None
notChecked = None

blinkTime = None
blinkOn = None



def setup():
    global checked, notChecked, blinkTime, blinkOn
    fill(37, 107, 133)
    size(1000, 800)
    
    stroke(255, 188, 0)
    strokeWeight(2)
    
    checked = loadImage('images/checked.png')
    notChecked = loadImage('images/notchecked.png')
    
    blinkTime = millis()
    blinkOn = True
    
    
    p1C = color(255, 0, 0)
    p2C = color(0, 255, 0)
    p3C = color(0, 0, 255)
    p4C = color(255, 0, 255)
    
    gameData['colors'].append(p1C)
    gameData['colors'].append(p2C)
    gameData['colors'].append(p3C)
    gameData['colors'].append(p4C)
    
    
            
def draw():
    
    # set background color
    background(51)
    
    global blinkTime, blinkOn
    
    # create textsize for the title
    textSize(32)
    fill(255)
    text('De dronken wereld reiziger', width /2, 100)
    textAlign(CENTER)
    
    # create a normal text size
    textSize(20)
    fill(255)
    text("Welkom bij ons digitale component \n Met hoeveel spelers wilt u spelen? \n kies uit 2, 3 of 4 spelers", width/ 2, 300)

    # a rectangle where the user input is shown
    fill(37, 107,133)
    rect(width/2 - 200 , 400, 400, 50)
    fill(255)
    
    # creating checkbox for the drank element
    fill(0)
    rect(rectXDrankCheck, rectYDrankCheck, rectWidth, rectHeight)
    fill(255)
    text('Klik het vakje aan om de drank\n variant te spelen', width/2.1, 700)
    
    imageMode(CENTER)
    image(notChecked, width / 1.45, height / 1.13)
    
    if(gameData['drank'] != None):
        imageMode(CENTER)
        image(mainScreenData['checkImage'], width / 1.45, height / 1.13)
    
    if(mainScreenData['showContinueText'] == None):
        
        if(blinkOn):
            line(500, 410, 500, 440)
        
        if( millis() - 500 > blinkTime):
            blinkTime = millis()
            blinkOn = not blinkOn
    
    # when the user has filled in a correct value the user can proceed to the next window of the game
    if(mainScreenData['showContinueText'] == True):
        text(key, width/2, 430)
        text('Druk op enter om naar het volgende scherm te gaan!', width/2, 500)
        fill(0)    
    else:
        # otherwise a error message will be shown
        text(mainScreenData['errorMessage'], width/2, 430)
        
    if(mainScreenData['secondScreen']):
        functions.clearPage()
        text('Wat is de naam van speler ' + str(mainScreenData['i']), width/2, 50)
        
        fill(37, 107,133)
        rect(width/2 - 200 , 200, 400, 50)
        
        if(blinkOn):
            line(500, y1Blink, 500, y2Blink)
        
        if( millis() - 500 > blinkTime):
            blinkTime = millis()
            blinkOn = not blinkOn
            
        fill(255)
        text(mainScreenData['userName'], width/2, 230)
        
    if(mainScreenData['thirdScreen']):   
        functions.clearPage() 

        fill(gameData['colors'][0])
        text(str(gameData['users'][0]), 200, 100)
        fill(gameData['colors'][1])
        text(str(gameData['users'][1]), 200, 150)
                
def keyPressed():
    global gameData
    
    createUsers()
    amountOfUsers()    

    if(key == ENTER):
        
        if(len(mainScreenData['userName']) != 0):
           
            if(mainScreenData['userName'] != '2' or mainScreenData['userName'] != '3' or mainScreenData['userName'] != '4'):
                mainScreenData['secondScreen'] = True
                
                if(len(mainScreenData['userName']) > 1):
                    gameData['users'].append(mainScreenData['userName'])
                    mainScreenData['i'] = mainScreenData['i'] + 1
                
                # clear the input from the user
                mainScreenData['userName'] = ''
                
            # need to add 1 to the gamedata value because there is one player less to make
            if(int(mainScreenData['i']) == int(gameData['amountOfPlayers']) + 1):
                mainScreenData['thirdScreen'] = True
        
def mouseClicked():
    global mainScreenData, gameData
    
    mouseCheck = functions.onRect(rectXDrankCheck, rectYDrankCheck, rectWidth, rectHeight)
    
    if(mouseCheck and gameData['drank'] == True):
        gameData['drank'] = False
        mainScreenData['checkImage'] = notChecked
    else:
        gameData['drank'] = True
        mainScreenData['checkImage'] = checked
    
def amountOfUsers():
    
    if(key == BACKSPACE):
        mainScreenData['showContinueText'] = None
    else:
        if(key == '2' or key == '3' or key == '4'):
            gameData['amountOfPlayers'] = key
            mainScreenData['showContinueText'] = True
            
                # write the json data to a txt file
            with open('gameData.txt', 'w') as outfile:
                json.dump(gameData, outfile)
        else:
            mainScreenData['errorMessage'] = str('Dit is geen 2, 3 of 4')
            mainScreenData['showContinueText'] = False
        
    return gameData

def createUsers():
    if(key != SHIFT or key == ENTER):
        if ((int(ord(key)) >= 65 and int(ord((key))) <= 90) or (int(ord(key)) >= 97 and int(ord(key)) <= 122 or key == ENTER)):  
        
            mainScreenData['userName'] = mainScreenData['userName'] + str(key)
        
        if ((int(ord(key))) == 8):
            mainScreenData['userName'] = mainScreenData['userName'][:-1]
        
        return mainScreenData['userName']
