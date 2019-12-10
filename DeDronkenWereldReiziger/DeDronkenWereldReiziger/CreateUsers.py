# drank check

# Sander Moerman, INF1K, 0988465
import functions

# dict for putting the images in
setupData = {}
setupData['defaultColor'] = color(37, 107, 133)

colorsToChoose = [color(255, 0, 0), color(0, 255, 0),color(0, 0, 255),color(255, 255, 0)]
setupData['i'] = 0

gameData = {}
gameData['alcoholicCheck'] = False
gameData['amountOfUsers'] = None
gameData['checkAmountOfUsers'] = 0
gameData['numberAmountOfUsers'] = 0
gameData['users'] = ['', '', '', '']
gameData['youghestPlayer'] = None
gameData['showYounghestPlayer'] = None
gameData['errorMessage'] = None

rects = {}
# setting the dimensions
rects['alcoholicCheck'] = [660, 680, 50, 50]

rects['createUser1'] = [300, 200, 400, 50]
rects['createUser2'] = [300, 350, 400, 50]
rects['createUser3'] = [300, 500, 400, 50]
rects['createUser4'] = [300, 650, 400, 50]

imgWidth=60
imgHeight=50
# setting the values when which blink needs to blink

blinkers = [False, False, False, False]
yPlayers = [False, False, False, False]


screens = {}
screens['secondScreen'] = None
screens['thirdScreen'] = None


shown=True
eventAllowed=False

def setup():
    global setupData, blinkers, eventAllowed
    
    eventAllowed = True

    # setting the background color
    fill(37, 107, 133)
    # size of the project
    size(1000, 800)

    # color and thickness of the lines
    stroke(255, 188, 0)
    strokeWeight(2)

    # the images that are used in this project
    setupData['imageChecked'] = loadImage('images/checked.png')
    setupData['imageNotChecked'] = loadImage('images/notchecked.png')

def draw():
    global setupData, blinkers,yPlayers,imgWidth,imgHeight
    background(51)
    # text size for the title of this project
    textSize(32)
    fill(255)

    text('De dronken wereld reiziger', width/2, 100)
    textAlign(CENTER)

    # text size and color for the rest of this project
    textSize(20)
    fill(255)

    text("Welkom bij ons digitale component \n Met hoeveel spelers wilt u spelen? \n kies uit 2, 3 of 4 spelers", width / 2, 300)

    # a rectangle where the user input is shown
    functions.createRectWithColor(width/2 - 200, 400, 400, 50, setupData['defaultColor'])

    if(gameData['amountOfUsers'] != None):
        fill(255)
        text(str(gameData['amountOfUsers']), width/2, 430)

        if(gameData['amountOfUsers'] == '2' or gameData['amountOfUsers'] == '3' or gameData['amountOfUsers'] == '4'):
            text('Druk op enter om naar het volgende scherm te gaan!', width/2, 500)
    else:
        functions.blink(500, 410, 500, 440)

    fill(255)
    text('Klik het vakje aan om de drank\n variant te spelen', width/2.1, 700)

    imageMode(CENTER)
    image(setupData['imageNotChecked'], width / 1.45, height / 1.13)

    if(gameData['alcoholicCheck'] != False):
        imageMode(CENTER)
        image(setupData['imageChecked'], width / 1.45, height / 1.13)

    if(screens['secondScreen'] != None):
        functions.clearPage()
        text('Kleur', 200, 125)
        text('Naam', width/2, 125)
        text('Jongste speler', 790, 125)

        for i in range(len(yPlayers)):
            functions.createRectWithColor(rects['createUser'+str(i+1)][0], rects['createUser'+str(i+1)][1],rects['createUser'+str(i+1)][2], rects['createUser'+str(i+1)][3], setupData['defaultColor'])
            text(str(gameData['users'][i]), width/2, 230+(i*150))
            functions.createRectWithColor(180, 200+(i*150), 50, 50, colorsToChoose[i])
            if yPlayers[i]:
                functions.showImage(setupData['imageChecked'], 760+(imgWidth/2), 200+(imgHeight/2)+(i*150))
            else:
                functions.showImage(setupData['imageNotChecked'], 761+(imgWidth/2), 200+(imgHeight/2)+(i*150))
    
        if(gameData['errorMessage'] != None):
            text(gameData['errorMessage'], width/2, 170)
        else:
            if(screens['thirdScreen']):
                functions.clearPage()
                text('de spelers zijn', width/2, 50)
                showUsersWithChoosenColor()
                
                shown=False
                eventAllowed=False
        
        for i in range(len(blinkers)):
            if blinkers[i]:
                 functions.blink(500, 210+(i*150), 500, 240+(i*150))
                 
def mouseClicked():
    global rects, gameData,imgWidth,imgHeight

    alcoholicVariant = functions.onRect(
        rects['alcoholicCheck'][0], rects['alcoholicCheck'][1], rects['alcoholicCheck'][2], rects['alcoholicCheck'][3])

    if(alcoholicVariant):
        gameData['alcoholicCheck'] = not gameData['alcoholicCheck']
        
    for i in range(len(blinkers)):
        if functions.onRect(rects['createUser'+str(i + 1)][0], rects['createUser'+str(i + 1)][1], rects['createUser'+str(i + 1)][2], rects['createUser'+str(i + 1)][3]) and screens['secondScreen']:
            print(i)
            blinkers[i]=True
            functions.clearUserInput()
        else:
            blinkers[i]=False            
    
    for i in range(len(yPlayers)):
        if functions.onRect(760,  200+(i*150), imgWidth,imgHeight) and screens['secondScreen']:
            
            gameData['youghestPlayer'] = i+1
            gameData['showYounghestPlayer'] = gameData['youghestPlayer'] - 1
            if(gameData['users'][gameData['showYounghestPlayer']] == ''):
                gameData['errorMessage'] = 'Naam mag niet leeg zijn'
                yPlayers[i]= False
            else:
                gameData['errorMessage'] = None
                yPlayers[i]= True
        else:
            yPlayers[i]= False
    for i in range(len(gameData['users'])):
        if(len(gameData['users'][i]) == 0):
            functions.setBlinkToX()


def keyPressed():
    global gameData
    if(key != ENTER):
        gameData['amountOfUsers'] = functions.amountOfUsers()

    if(key == ENTER and gameData['amountOfUsers'] != 'Dit is geen 2, 3 of 4' and not screens['secondScreen']):
        gameData['numberAmountOfUsers'] = gameData['amountOfUsers'] if gameData['amountOfUsers']!=None else 0 
        if(gameData['amountOfUsers'] != None):
            screens['secondScreen'] = True
            functions.clearPage()
            
    for i in range(len(blinkers)):
        if blinkers[i]:
            gameData['users'][i] = functions.createUser()
            functions.pushBlink()
            
    if(not any(yPlayers)):
        gameData['errorMessage'] = 'kies een jongste speler'

    else:
        gameData['errorMessage'] = None
        
    if(gameData['showYounghestPlayer'] != None):
            if(key == ENTER and gameData['youghestPlayer'] != None and screens['secondScreen']):
                gameData['checkAmountOfUsers']=0
                for i in range(len(gameData['users'])):
                    if gameData['users'][i]!= None and gameData['users'][i]!='':
                         gameData['checkAmountOfUsers']+=1

                if(int(gameData['numberAmountOfUsers']) > int(gameData['checkAmountOfUsers'])):
                    gameData['errorMessage'] = 'U moet meer spelers aanmaken'
                else:
                    gameData['createMoreUsers'] = None

                if(int(gameData['numberAmountOfUsers']) < int(gameData['checkAmountOfUsers'])):
                    gameData['errorMessage'] = 'U moet minder spelers aanmaken'
                else:
                    gameData['createLessUsers'] = None

                if(int(gameData['numberAmountOfUsers']) == int(gameData['checkAmountOfUsers'])):
                    screens['thirdScreen'] = True

def showUsersWithChoosenColor():
    global colorsToChoose
    for i in range(len(gameData['users'])):
        if(gameData['users'][i] != ''):
            fill(colorsToChoose[i])
            text(str(gameData['users'][i]), width/2, 200+(i*100))

    fill(255)
    text('de jongste speler is :' +
         str(gameData['users'][gameData['showYounghestPlayer']]), width/2, 600)
