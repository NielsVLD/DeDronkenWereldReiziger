#Sander Moerman, INF1K, 0988465
import functions

shown=True
eventAllowed=False

# dict for putting the images in
setupData = {}
setupData['defaultColor'] = color(37, 107, 133)
setupData['red'] = color(255, 0, 0) 
setupData['green'] = color(0, 255, 0) 
setupData['blue'] = color(0, 0, 255) 
setupData['yellow'] = color(255,255,0) 
setupData['i'] = 0

gameData = {}
gameData['alcoholicCheck'] = None
gameData['amountOfUsers'] = None
gameData['checkAmountOfUsers'] = 0
gameData['numberAmountOfUsers'] = None
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

# yP means youngest player
rects['yP1Check'] = [760, 200, 60, 50]
rects['yP2Check'] = [760, 350, 60, 50]
rects['yP3Check'] = [760, 500, 60, 50]
rects['yP4Check'] = [760, 650, 60, 50]

# setting the values when which blink needs to blink
rects['blinkUser1'] = None
rects['blinkUser2'] = None
rects['blinkUser3'] = None
rects['blinkUser4'] = None

# setting the checkvalues for the younhest player
rects['checkYoughestPlayer1'] = None
rects['checkYoughestPlayer2'] = None
rects['checkYoughestPlayer3'] = None
rects['checkYoughestPlayer4'] = None

screens = {}
screens['secondScreen'] = None
screens['thirdScreen'] = None

def setup():
    global setupData, eventAllowed
    
    eventAllowed = True
    
    # setting the background color
    fill(37, 107, 133)
    # size of the project
    size(1000, 800)
    
    # color and thickness of the lines
    stroke(255, 188,0)
    strokeWeight(2)
    
    # the images that are used in this project
    setupData['imageChecked'] = loadImage('images/checked.png')
    setupData['imageNotChecked'] = loadImage('images/notchecked.png')
    
def draw():
    global setupData, shown, eventAllowed
    background(51)

    # text size for the title of this project
    textSize(32)
    fill(255)
    
    text('De dronken wereld reiziger', width/2, 100)
    textAlign(CENTER)
    
    # text size and color for the rest of this project
    textSize(20)
    fill(255)
    
    text("Welkom bij ons digitale component \n Met hoeveel spelers wilt u spelen? \n kies uit 2, 3 of 4 spelers", width/ 2, 300)
    
    # a rectangle where the user input is shown
    functions.createRectWithColor(width/2 - 200 , 400, 400, 50, setupData['defaultColor'])
    
    if(gameData['amountOfUsers'] != None):
        fill(255)
        text(gameData['amountOfUsers'], width/2, 430)
        
        if(gameData['amountOfUsers'] == '2' or gameData['amountOfUsers'] == '3' or gameData['amountOfUsers'] == '4'):
            text('Druk op enter om naar het volgende scherm te gaan!', width/2, 500)
    else:
        functions.blink(500, 410, 500, 440)
    
    fill(255)
    text('Klik het vakje aan om de drank\n variant te spelen', width/2.1, 700)
    
    imageMode(CENTER)
    image(setupData['imageNotChecked'], width / 1.45, height / 1.13)
    
    if(gameData['alcoholicCheck'] != None):
        imageMode(CENTER)
        image(setupData['imageChecked'], width / 1.45, height / 1.13)
        
    if(screens['secondScreen'] != None):
        functions.clearPage()
        text('Kleur', 210, 150)
        text('Naam', width/2, 150)
        text('Jongste speler', 790, 150)
        
        # Row one code----------------------------------------------Row one code
        functions.createRectWithColor(180, 200, 60, 50, setupData['red'])
        functions.createRectWithColor(rects['createUser1'][0], rects['createUser1'][1], rects['createUser1'][2], rects['createUser1'][3], setupData['defaultColor'])
        text(str(gameData['users'][0]), width/2, 230)
        
        functions.createRectWithColor(rects['yP1Check'][0], rects['yP1Check'][1], rects['yP1Check'][2], rects['yP1Check'][3], setupData['defaultColor'])
        functions.showImage(setupData['imageNotChecked'], rects['yP1Check'][0] + 30, rects['yP1Check'][1]+ 20)
        
        if(rects['checkYoughestPlayer1'] != None):
            functions.showImage(setupData['imageChecked'], rects['yP1Check'][0] + 30, rects['yP1Check'][1]+ 20)
        else:
            functions.showImage(setupData['imageNotChecked'], rects['yP1Check'][0] + 30, rects['yP1Check'][1]+ 20)
       
        if(rects['blinkUser1'] != None):
            functions.blink(500, 210, 500, 240)

        # Row two code----------------------------------------------Row two code
        functions.createRectWithColor(180, 350, 60, 50, setupData['green']) 
        functions.createRectWithColor(rects['createUser2'][0], rects['createUser2'][1], rects['createUser2'][2], rects['createUser2'][3], setupData['defaultColor'])
        text(str(gameData['users'][1]), width/2, 380)
        
        functions.createRectWithColor(rects['yP2Check'][0], rects['yP2Check'][1], rects['yP2Check'][2], rects['yP2Check'][3], setupData['defaultColor'])
        functions.showImage(setupData['imageNotChecked'], rects['yP2Check'][0] + 30, rects['yP2Check'][1]+ 20)
        
        if(rects['checkYoughestPlayer2'] != None):
            functions.showImage(setupData['imageChecked'], rects['yP2Check'][0] + 30, rects['yP2Check'][1]+ 20)
        else:
            functions.showImage(setupData['imageNotChecked'], rects['yP2Check'][0] + 30, rects['yP2Check'][1]+ 20)
        
        if(rects['blinkUser2'] != None):
            functions.blink(500, 360, 500, 390)
        
        # Row three code----------------------------------------------Row three code
        functions.createRectWithColor(180, 500, 60, 50, setupData['blue'])
        functions.createRectWithColor(rects['createUser3'][0], rects['createUser3'][1], rects['createUser3'][2], rects['createUser3'][3], setupData['defaultColor'])
        text(str(gameData['users'][2]), width/2, 530)
        
        functions.createRectWithColor(rects['yP3Check'][0], rects['yP3Check'][1], rects['yP3Check'][2], rects['yP3Check'][3], setupData['defaultColor'])
        functions.showImage(setupData['imageNotChecked'], rects['yP3Check'][0] + 30, rects['yP3Check'][1]+ 20)
        
        if(rects['checkYoughestPlayer3'] != None):
            functions.showImage(setupData['imageChecked'], rects['yP3Check'][0] + 30, rects['yP3Check'][1]+ 20)
        else:
            functions.showImage(setupData['imageNotChecked'], rects['yP3Check'][0] + 30, rects['yP3Check'][1]+ 20)
        
        if(rects['blinkUser3'] != None):
            functions.blink(500, 510, 500, 540)
        
        # Row four code----------------------------------------------Row four code
        functions.createRectWithColor(180, 650, 60, 50, setupData['yellow'])
        functions.createRectWithColor(rects['createUser4'][0], rects['createUser4'][1], rects['createUser4'][2], rects['createUser4'][3], setupData['defaultColor'])
        text(str(gameData['users'][3]), width/2, 680)
        
        functions.createRectWithColor(rects['yP4Check'][0], rects['yP4Check'][1], rects['yP4Check'][2], rects['yP4Check'][3], setupData['defaultColor'])
        functions.showImage(setupData['imageNotChecked'], rects['yP4Check'][0] + 30, rects['yP4Check'][1]+ 20)
        
        if(rects['checkYoughestPlayer4'] != None):
            functions.showImage(setupData['imageChecked'], rects['yP4Check'][0] + 30, rects['yP4Check'][1]+ 20)
        else:
            functions.showImage(setupData['imageNotChecked'], rects['yP4Check'][0] + 30, rects['yP4Check'][1]+ 20)
          
        if(rects['blinkUser4'] != None):
            functions.blink(500, 660, 500, 690)
            
        if(gameData['errorMessage'] != None):
            text(gameData['errorMessage'], width/2, 170) 
        else:
            if(screens['thirdScreen']):
                functions.clearPage()
                text('de spelers zijn', width/2, 50)
                showUsersWithChoosenColor()
                shown= False
                eventAllowed=False
            
def mouseClicked():
    global rects, gameData
    
    alcoholicVariant = functions.onRect(rects['alcoholicCheck'][0], rects['alcoholicCheck'][1], rects['alcoholicCheck'][2], rects['alcoholicCheck'][3])
    
    if(alcoholicVariant and gameData['alcoholicCheck'] == None):
        gameData['alcoholicCheck'] = True
    else:
        gameData['alcoholicCheck'] = None
        
    createUser1 = functions.onRect(rects['createUser1'][0], rects['createUser1'][1], rects['createUser1'][2], rects['createUser1'][3])
    if(createUser1):
        functions.clearUserInput()
        rects['blinkUser1'] = True
    else:
        rects['blinkUser1'] = None
        
    createUser2 = functions.onRect(rects['createUser2'][0], rects['createUser2'][1], rects['createUser2'][2], rects['createUser2'][3])
    if(createUser2):
        functions.clearUserInput()
        rects['blinkUser2'] = True
    else:
        rects['blinkUser2'] = None
        
    createUser3 = functions.onRect(rects['createUser3'][0], rects['createUser3'][1], rects['createUser3'][2], rects['createUser3'][3])
    if(createUser3):
        functions.clearUserInput()
        rects['blinkUser3'] = True
    else:
        rects['blinkUser3'] = None
        
    createUser4 = functions.onRect(rects['createUser4'][0], rects['createUser4'][1], rects['createUser4'][2], rects['createUser4'][3])
    if(createUser4):
        functions.clearUserInput()
        rects['blinkUser4'] = True
    else:
        rects['blinkUser4'] = None
        
    yP1Check = functions.onRect(rects['yP1Check'][0], rects['yP1Check'][1], rects['yP1Check'][2], rects['yP1Check'][3])
  
    if(yP1Check):
        rects['checkYoughestPlayer1'] = True
        gameData['youghestPlayer'] = 1
        gameData['showYounghestPlayer'] = gameData['youghestPlayer'] - 1
    else:
        rects['checkYoughestPlayer1'] = None
        
    yP2Check = functions.onRect(rects['yP2Check'][0], rects['yP2Check'][1], rects['yP2Check'][2], rects['yP2Check'][3])
  
    if(yP2Check):
            rects['checkYoughestPlayer2'] = True
            gameData['youghestPlayer'] = 2
            gameData['showYounghestPlayer'] = gameData['youghestPlayer'] - 1
    else:
        rects['checkYoughestPlayer2'] = None
            
    yP3Check = functions.onRect(rects['yP3Check'][0], rects['yP3Check'][1], rects['yP3Check'][2], rects['yP3Check'][3])
  
    if(yP3Check):
        rects['checkYoughestPlayer3'] = True
        gameData['youghestPlayer'] = 3
        gameData['showYounghestPlayer'] = gameData['youghestPlayer'] - 1
    else:
        rects['checkYoughestPlayer3'] = None
            
    yP4Check = functions.onRect(rects['yP4Check'][0], rects['yP4Check'][1], rects['yP4Check'][2], rects['yP4Check'][3])
  
    if(yP4Check):
        rects['checkYoughestPlayer4'] = True
        gameData['youghestPlayer'] = 4
        gameData['showYounghestPlayer'] = gameData['youghestPlayer'] - 1
    else:
        rects['checkYoughestPlayer4'] = None
     
    if(yP4Check or yP3Check or yP2Check or yP1Check):
        if(gameData['users'][gameData['showYounghestPlayer']] == ''):
            gameData['errorMessage'] = 'u moet een ingevuld veld kiezen als jongste speler'        
        else:
            gameData['errorMessage'] = None
        
def keyPressed():
    global gameData
    
    if(key != ENTER):
        gameData['amountOfUsers'] = functions.amountOfUsers()
        
    if(key == ENTER and gameData['amountOfUsers'] != 'Dit is geen 2, 3 of 4'):
        gameData['numberAmountOfUsers'] = gameData['amountOfUsers']
        if(gameData['amountOfUsers'] != None):
            screens['secondScreen'] = True
            functions.clearPage()
            
    if(rects['blinkUser1']):
        gameData['users'][0] = functions.createUser()
        
    if(rects['blinkUser2']):
        gameData['users'][1] = functions.createUser()

    if(rects['blinkUser3']):
        gameData['users'][2] = functions.createUser()
        
    if(rects['blinkUser4']):
        gameData['users'][3] = functions.createUser()
    
    if(gameData['showYounghestPlayer'] != None):
        print(gameData['showYounghestPlayer'])
        
        if(rects['checkYoughestPlayer4'] == None and rects['checkYoughestPlayer3'] == None and rects['checkYoughestPlayer2'] == None and rects['checkYoughestPlayer1'] == None):
            gameData['errorMessage'] = 'kies een jongste speler'
            
        else:
            gameData['errorMessage'] = None
            
        if(gameData['users'][gameData['showYounghestPlayer']] == ''):
                gameData['errorMessage'] = 'u moet een ingevuld veld kiezen als jongste speler'        
        else:
            gameData['errorMessage'] = None
    
            if(key == ENTER and gameData['youghestPlayer'] != None):
                if(screens['thirdScreen'] != True):
                    if(gameData['users'][0] != ''):
                        gameData['checkAmountOfUsers'] += 1
                    if(gameData['users'][1] != ''):
                        gameData['checkAmountOfUsers'] += 1
                    if(gameData['users'][2] != ''):
                        gameData['checkAmountOfUsers'] += 1
                    if(gameData['users'][3] != ''):
                        gameData['checkAmountOfUsers'] += 1
                
                if(int(gameData['numberAmountOfUsers']) > int(gameData['checkAmountOfUsers'])):
                    gameData['errorMessage'] = 'U moet meer spelers aanmaken'
                    gameData['checkAmountOfUsers'] = 0
                else:
                    gameData['createMoreUsers'] = None
            
                if(int(gameData['numberAmountOfUsers']) < int(gameData['checkAmountOfUsers'])):
                    gameData['errorMessage'] = 'U moet minder spelers aanmaken'
                    gameData['checkAmountOfUsers'] = 0
                else:
                    gameData['createLessUsers'] = None
                                        
                if(int(gameData['numberAmountOfUsers']) == int(gameData['checkAmountOfUsers'])):
                    screens['thirdScreen'] = True
            
def showUsersWithChoosenColor():
    if(gameData['users'][0] != ''):    
        fill(setupData['red'])
        text(str(gameData['users'][0]), width/2, 200)
        
    if(gameData['users'][1] != ''):            
        fill(setupData['green'])
        text(str(gameData['users'][1]), width/2, 300)
    
    if(gameData['users'][2] != ''):      
        fill(setupData['blue'])
        text(str(gameData['users'][2]), width/2, 400)
                
    if(gameData['users'][3] != ''):       
        fill(setupData['yellow'])    
        text(str(gameData['users'][3]), width/2, 500)
        
    fill(255)
    text('de jongste speler is :' + str(gameData['users'][gameData['showYounghestPlayer']]), width/2 , 600)
