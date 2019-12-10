# Voor navigatie en ontvangen van events als keypressed
shown=True

lvraagnummer = 1
antwoord = "Waar"
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
    text("Hawaii behoort ook tot Oceanie",width/2,63)
    text("Vraag:",width/2,30)
    line(0,37, width, 37)
    text("Uw antwoord is",width/2,120)
    line(0,127, width, 127)
    text(antwoord,width/2,160)
    text("Het goede antwoord is",width/2,400)
    text(goede_antwoord,width/2,440)
    if punten_goed_antwoord == 1:
        text("+"+str(punten_goed_antwoord)+" punt",width/2,480)
    else:
        if punten_goed_antwoord == 0:
            fill(200,0,0)
        else:
            fill(0,200,0)
        text("+"+str(punten_goed_antwoord)+" punten",width/2,480)
        
def keyPressed():
    global shown
    if key==ENTER:
        shown=False
