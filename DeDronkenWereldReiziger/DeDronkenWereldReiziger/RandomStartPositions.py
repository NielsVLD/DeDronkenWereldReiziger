#Wessel van leeuwen, 0986664, projectrgroep 3
import random
import time

# Voor navigatie en ontvangen van events als keypressed
shown=True
eventAllowed=False

spelers=["joost","Kees", "henk", "NAME"]
allStartPositions=["Oceanie","Europa","Azie","Noord-Amerika","Zuid-Amerika","Afrika"]
spelerStartPositions=[]
images={}
def setup():
    global images, eventAllowed
    eventAllowed=True
    size(1000,800)
    calculateStartPositions()
    images[allStartPositions[1]]=loadImage("EUrope.png")
    images[allStartPositions[3]]=loadImage("NAmerica.png")
    images[allStartPositions[4]]=loadImage("ZAmerica.png")
    images[allStartPositions[5]]=loadImage("Afrika.png")
    images[allStartPositions[2]]=loadImage("Azie.png")
    images[allStartPositions[0]]=loadImage("Oceanie.png")
    
def draw():
    background(51)
    fill(37, 107, 133)
    stroke(255, 188, 0)
    line((width/2),0,(width/2),800)
    if len(spelers) >= 3: 
        line(0,(height/2),width,((height/2)))
    
    fill(37, 107, 133)
    textAlign(CENTER,CENTER)
    textSize(30)
    if len(spelers) == 2:
        fill(51)
        rect((width/2)-210, 75, 420, 100)
        fill(37, 107, 133)
        text("De Dronken Wereld Reiziger", width/2, 110)
        fill(27, 107, 133)
        rect((width/2)-75,height-125,150,50)
        textSize(25)
        text("Startposities", width/2, 145)
        
    else:
        fill(51)
        rect((width/2)-210, (height/2)-50, 420, 100)
        fill(37, 107, 133)
        text("De Dronken Wereld Reiziger", width/2, (height/2)-25)
        fill(27, 107, 133)
        rect((width/2)-75,height-125,150,50)
        textSize(25)
        text("Startposities", width/2, (height/2)+25)
    textSize(15)
    drawPlayerAndPosition()
    textSize(14)
    fill(255)
    text("Next",width/2,height-100)
    
def drawPlayerAndPosition():
    global images
    textSize(15)
    fill(255)
    for i,speler in enumerate(spelers) :
        textAlign(CENTER,CENTER)
        if len(spelers)==2:
            if i==0:
                text(speler, ((width/4)), (height/2)-140)
            elif i==1:
                 text(speler, (width-(width/4)), (height/2)-140)
        elif len(spelers)>=3:
            if i==0:
                text(speler, ((width/4)), (height/4)- 140)
            elif i==1:
                text(speler, (width-(width/4)), (height/4)- 140)
            elif i==2:
                text(speler, ((width/4)), height-(height/4)- 140)
            elif i==3:
                text(speler, (width-(width/4)), height-(height/4) - 140)
    for i,spelerStartPos in enumerate(spelerStartPositions):
        textAlign(CENTER,CENTER)
        if len(spelers)==2:
            if i==0:
                drawContinents(spelerStartPos,images[spelerStartPos],((width/4)), (height/2))
                text(spelerStartPos, ((width/4)), (height/2))
            elif i==1:       
                 drawContinents(spelerStartPos,images[spelerStartPos], (width-(width/4)), (height/2))
                 text(spelerStartPos, (width-(width/4)), (height/2))
        elif len(spelers)>=3:
            if i==0:                
                drawContinents(spelerStartPos,images[spelerStartPos], ((width/4)), (height/4))
                text(spelerStartPos, ((width/4)), (height/4))
            elif i==1:                
                drawContinents(spelerStartPos,images[spelerStartPos], (width-(width/4)), (height/4))
                text(spelerStartPos, (width-(width/4)), (height/4))
            elif i==2:                
                drawContinents(spelerStartPos,images[spelerStartPos],  ((width/4)), height-(height/4))
                text(spelerStartPos, ((width/4)), height-(height/4))
            elif i==3:            
                drawContinents(spelerStartPos,images[spelerStartPos], (width-(width/4)), height-(height/4))
                text(spelerStartPos, (width-(width/4)), height-(height/4))

def drawContinents(continent,continentImg,x,y):
    imageMode(CENTER)
    if continent == "Europa":
        image(continentImg, x, y, 231, 151)
    elif continent == "Noord-Amerika":
        image(continentImg, x, y, 442, 274) 
    elif continent == "Zuid-Amerika":
        image(continentImg, x, y, 157, 255) 
    elif continent == "Afrika":
        image(continentImg, x, y, 234, 276)
    elif continent == "Azie":
        image(continentImg, x, y, 362, 152)
    elif continent == "Oceanie":
        image(continentImg, x, y, 235, 176)

def calculateStartPositions():
    global spelerStartPositions
    newAllStartPositions=list(allStartPositions)
    for speler in enumerate(spelers) :
        pos=random.choice(newAllStartPositions)
        newAllStartPositions.remove(pos)
        spelerStartPositions.append(pos)

def mousePressed():
    global spelerStartPositions,shown,eventAllowed
    if onRect((width/2)-75,height-125,150,50):
        # next screen
        shown=False
        eventAllowed=False
        pass

def onRect(x, y, w, h):
    return(mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y + h)
