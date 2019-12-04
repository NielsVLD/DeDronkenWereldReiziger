# Nelus

# Voor navigatie en ontvangen van events als keypressed
shown=True
eventAllowed=False

ingevuldAntwoord =False
def setup():
    size(1000,800)
    loadImage('')

def draw():
    background(255)
    fill(37, 107,133)
    stroke(255,188,0)
    strokeWeight(2)
    rect(0,0,width,height)

    textAlign(CENTER)
    textSize(20)
    fill(255)
    text("Hawaii behoort ook tot Oceanie",width/2,63)
    text("Vraag:",width/2,30)
    line(0,37, width, 37)
    text("Antwoord:",width/2,120)
    line(0,127, width, 127)
    
    textSize(23)
            
    fill(255)
    text("Waar",width/4,210)
    if not ingevuldAntwoord:
        fill(37, 107,133)
        line(160,250,200,250)
    else:
        fill(255)
            
    circle(180, 200, 30)
    fill(255)
    text("Niet waar",width/3.6,260)
    if ingevuldAntwoord:
        fill(37, 107,133)
        line(160,200,200,200)
    else:
        fill(255)   
    circle(180, 250, 30)
    fill(37, 107,133)
    rect((width/2)-75,height-100,150,50)
    fill(255)
    textAlign(CENTER,CENTER)
    text("Controleren",(width/2),height-75,)

def isMouseWithinRect(x,y,w,h):
    return (x < mouseX < x + w and y < mouseY < y + h)
 
def mousePressed():
    global ingevuldAntwoord, touched, shown,eventAllowed
    if isMouseWithinRect(180-15, 200-15,30,30):
        ingevuldAntwoord=True
    elif isMouseWithinRect(180-15, 250-15,30,30):
        ingevuldAntwoord=False
    
    if isMouseWithinRect((width/2)-75,height-100,150,50):
        # nextPage
        shown=False
        eventAllowed=False
        print("to next page ingevuld antwoord: ",ingevuldAntwoord)
