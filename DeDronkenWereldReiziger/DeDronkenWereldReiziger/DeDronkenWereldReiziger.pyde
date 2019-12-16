import StartScreen,CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen, functions
import traceback
screens=[]
goBack=False
gameData={}
qanda={}
currentQuestion={}
currentAnswer='Geen'
def setup():
    global screens,qanda
    size(1000,800)
    screens=[StartScreen,CreateUsers, RandomStartPositions,QuestionScreen,AnswerScreen,RadScreen]
    qanda = functions.getQAndAJson()
index=0
pageSetup=False
def getRandomQuestion():
    global qanda
    try:
        lengthQanda = len(qanda)
        rdmInt = int(random(0,lengthQanda))
        return qanda[rdmInt]
    except Exception, e:
        print("could not get question",e)
        
def SetupPage3():
    global currentQuestion
    currentQuestion= getRandomQuestion()
    #get the first object from the questionobject
    currentQuestion= currentQuestion[currentQuestion.keys()[0]]
    screens[3].vraag=currentQuestion['question']
    print("Random question sent through to screen\n",currentQuestion)
   
def SetupPage4(): 
    global currentQuestion
    screens[4].vraag=screens[3].vraag
    screens[4].punten_goed_antwoord=1
    screens[4].antwoord=currentAnswer
    try:
        screens[4].goede_antwoord=currentQuestion['answers'][str(currentQuestion['answer'])]   
    except Exception, e:
        print('currentQuestion',currentQuestion)
        print("could not get answers",e)    
    
def draw():
    global index,pageSetup,screens,goBack,gameData,currentAnswer
    
    if screens!=None:
        try:
            if goBack:
                screens[index].shown=True
                index-=1
                screens[index].shown=True
                print("going back")
                goBack=False
            if not screens[index].shown:
                pageSetup=False
                index+=1
                print('goto next screen',index) 
            else:
                if (index != 5) or (index==5 and gameData['alcoholicCheck']):
                    if not pageSetup:
                        print('screen',index)  
                        cursor(ARROW)
                        screens[index].setup()
                        if index==1:
                            if screens[index].gameData!=None:
                                gameData=screens[index].gameData
                            print("test")
                            #get the users from createusers and pass them through to randomstartpos
                        if index ==2:
                            listUsers = gameData['users']
                            res = []
                            for val in listUsers: 
                                if val != None and val!='' : 
                                    res.append(val) 
                            screens[index].spelers=res
                        if index==3:
                            SetupPage3()
                        if index==3:
                            SetupPage4()
                        pageSetup=True
                else:
                    screens[index].shown=False
                    index=4
                    print('Alcohol isnt allowed so dont go to the drink rad')
             
                if index==4:
                    currentAnswer=screens[3].ingevuldAntwoord
                    screens[4].antwoord=currentAnswer
                    # print(currentAnswer)
                screens[index].draw()
                    
        except Exception, e:
            #exception was thrown go back to last page
            if index>5:
                index=4
                screens[index].shown=True
                print('index higher then 5 is out of range so go to next question')
            if(index>0):
                index-=1
                screens[index].shown=True
            else:
                index=0
                screens[index].shown=True
            print(str(e))

def mousePressed():
    global screens
    try:
        screens[index].mousePressed()
    except Exception as e:
        print('mousepressed caused error in: '+str(screens[index])+' --- ignored\n'+str(e))
        traceback.print_exc()
            
def mouseClicked():
    global screens
    try:
        screens[index].mouseClicked()
    except Exception as e:
        print('mouseClicked caused error in: '+str(screens[index])+' --- ignored\n'+str(e))
        traceback.print_exc()

# def mouseClicked():
#     global screens
#     for i in screens:
#         try:
#             if i.eventAllowed:
#                 i.mouseClicked()
#         except Exception, e:
#             print('error by mouseClicked in: '+str(i)+' --- ignored\n'+str(e))

def mouseReleased():
    global screens
    try:
        screens[index].mouseReleased()
    except Exception, e:
        print('mousereleased caused error in: '+str(screens[index])+' --- ignored'+str(e))
        traceback.print_exc()
            
            
def keyPressed():
    global index,screens,goBack,gameData
    if key==TAB and index>0:
        goBack=True
    try:
        screens[index].keyPressed()
            
    except Exception as e:
        print('keyPressed caused error in: '+str(screens[index])+' --- ignored\n'+str(e))    
        traceback.print_exc()
