# Voor navigatie
shown=True

vraag = "Hawaii behoort ook tot Oceanie"
antwoord = ""
goede_antwoord = "Waar"
punten_goed_antwoord=0


def setup():
    size(1000, 800)
    
def draw():
    background(255)
    fill(37, 107,133)
    stroke(255,188,0)
    strokeWeight(2)
    rect(0,0,width, height)

    textAlign(CENTER)
    textSize(20)
    fill(255)
    text(vraag,width/2,63)
    text("Vraag:",width/2,30)
    line(0,37, width, 37)
    text("Uw antwoord is",width/2,120)
    line(0,127, width, 127)
    text(antwoord,width/2,160)
    text("Het goede antwoord is",width/2,400)
    text(goede_antwoord,width/2,440)
    punten=0
    if antwoord==goede_antwoord:
        punten=punten_goed_antwoord
    if punten == 1:
        fill(0,200,0)
        text("+"+str(punten)+" punt",width/2,480)
    else:
        if punten == 0:
            fill(200,0,0)
            text("Helaas geen punten",width/2,480)
        else:
            fill(0,200,0)
            text("+"+str(punten)+" punten",width/2,480)
    fill(37, 107,133)
    rect((width/2)-75,height-100,150,50)
    fill(255)
    textAlign(CENTER,CENTER)
    text("Volgende",(width/2),height-75,)
    if isMouseWithinRect((width/2)-75,height-100,150,50):
        cursor(HAND)
    else:
        cursor(ARROW)
def keyPressed():
    global shown
    if key==ENTER:
        shown=False
        
def mousePressed():    
    global shown    
    if isMouseWithinRect((width/2)-75,height-100,150,50):
    
        # nextPage
        shown=False
        
def isMouseWithinRect(x,y,w,h):
    return (x < mouseX < x + w and y < mouseY < y + h)
 
