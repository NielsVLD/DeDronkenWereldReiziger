import random
spelers=["joost","Kees","Test", "Peoples"]
allStartPositions=["Oceanie","Europa","Azie","Noord-Amerika","Zuid-Amerika","Afrika"]
spelerStartPositions=[]
def setup():
    size(1000,800)
    calculateStartPositions()
def draw():
    background(51)
    fill(37, 107, 133)
    textAlign(CENTER,CENTER)
    textSize(30)
    text("De Dronken Wereld Reiziger", width/2, (height/2)-175)
    textSize(25)
    text("Startposities", width/2, (height/2)-125)

    stroke(255, 188, 0)
    line((width/2),(height/2)-20,(width/2),(height/2)+43.75*len(spelers))
    line((width/2)-250,(height/2)-20,(width/2)+250,((height/2)-20))
    textSize(15)
    text("Speler",(width/2)-150, (height/2)-50)
    text("Continent",(width/2)+150, (height/2)-50)
    drawPlayerAndPosition()
    rect((width/2)-75,height-125,150,50)
    textSize(14)
    fill(255)
    text("Next",width/2,height-100)
    
def drawPlayerAndPosition():
    textSize(15)
    for i,speler in enumerate(spelers) :
        textAlign(CENTER,CENTER)
        text(speler,(width/2)-150, (height/2)+i*50)
    for i,spelerStartPos in enumerate(spelerStartPositions):
        textAlign(CENTER,CENTER)
        text(spelerStartPos,(width/2)+150, (height/2)+i*50)

def calculateStartPositions():
    global spelerStartPositions
    # create a new list from the old list of all start positions so the default wont be changed
    newAllStartPositions=list(allStartPositions)
    # loop through the spelers
    for speler in enumerate(spelers) :
        # pick a random position from the new list
        pos=random.choice(newAllStartPositions)
        # remove the position from the new list
        newAllStartPositions.remove(pos)
        # add the position to the spelerStartPositions
        spelerStartPositions.append(pos)

def mousePressed():
    global spelerStartPositions
    if onRect((width/2)-75,height-125,150,50):
        # next screen
        pass

def onRect(x, y, w, h):
    return(mouseX >= x and mouseX <= x + w and mouseY >= y and mouseY <= y + h)
