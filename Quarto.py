import pygame,sys,random
import inputtext
import constants as c

gameDisplay = pygame.display.set_mode(c.size)
win=[]
for i in range(16):
    win.append(False)

pygame.display.set_caption('Quarto')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, c.black)
    return textSurface, textSurface.get_rect()
 
def button(msg,x,y,w,h,ic,ac,action=None,attribute=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if(attribute==None):
                action()
            else:
                action(attribute)
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    sys.exit()

def singleplay():
    textinput = inputtext.TextInput()
    a=True
    while a:
        gameDisplay.blit(c.pic,[-150,-200])
        pygame.display.set_caption('Player1')
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                a=False
                playerselect()

        gameDisplay.blit(textinput.get_surface(), (10, 10))     
        pygame.display.update()
        
        if textinput.update(events):
            c.name1=textinput.get_text()
            if(len(c.name1)==0):
                continue
            name2="Computer"
            a=False
            gameplay()
            
        clock.tick(30)    

def multiplay():
    textinput = inputtext.TextInput()
    a=True
    while a:
        gameDisplay.blit(c.pic,[-150,-200])
        pygame.display.set_caption('Player1')
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                a=False
                playerselect()

        gameDisplay.blit(textinput.get_surface(), (10, 10))
        pygame.display.update()
        clock.tick(60)

        if textinput.update(events):
            c.name1=textinput.get_text()
            if(len(c.name2)==0):
                continue
            a=False
    
    textinput = inputtext.TextInput()
    a=True
    while a:
        gameDisplay.blit(c.pic,[-150,-200])
        pygame.display.set_caption('Player2')
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                a=False
                multiplay()

        gameDisplay.blit(textinput.get_surface(), (10, 10))
        pygame.display.update()
        clock.tick(60)

        if textinput.update(events):
            c.name2=textinput.get_text()
            if(len(c.name2)==0):
                continue
            a=False
            gameplay()

def buttongame(x,y,w,h,ic,ac,action=None,img=False,ind=None):
    global win
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and ind != None and c.select[0]!= False and c.list2[ind]==False:
            c.list2[ind]=c.select[0]
            c.select[0]=False
            win[ind]=c.temp1[0]
            if(c.do==1):
                c.do=0
            elif(c.do==0):
                c.do=1
            if(check_win(ind)):
                c.won=True
            
        if click[0] == 1 and action != None and c.list1[action]!= False and c.select[0]==False:
            c.select[0]=c.list1[action]
            c.temp1[0]=c.temp[action]
            c.list1[action]=False
            
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    if(img!=False):
        gameDisplay.blit(img,(x,y))

def computerplace():
    global win
    cou=0
    for i in range(16):
        if(win[i]==False):
            win[i]=c.temp1[0]
            if(check_win(i)):
                c.won=True
                c.temp1[0]=False
                c.list2[i]=c.select[0]
                c.select[0]=False
                cou=1
                break
            else:
                win[i]=False
    if(cou==0):
        i=random.randint(0,15)
        while(win[i]):
            i=random.randint(0,15)
        win[i]=c.temp1[0]
        c.list2[i]=c.select[0]
        c.select[0]=False
            
    c.do=0            

def computerselect():
    global win
    
    for i in range(16):
        if(c.temp[i]):
            for j in range(16):
                if(win[j]==False):
                    win[j]=c.temp[i]
                    if(check_win(j)):
                        c.check_piece[i]-=1
                    win[j]=False    

    k=max(c.check_piece)
    i=random.randint(0,15)
    while(c.check_piece[i]!=k):
        i=random.randint(0,15)
        
    c.select[0]=c.list1[i]
    c.list1[i]=False
    c.temp1[0]=c.temp[i]
    c.temp[i]=False
    c.check_piece[i]=0

def check_win(ind):
    global win
    if(ind<4):
        c=check(0,ind%4)
        if(c==True):
            return True
    elif(ind<8):
        c=check(4,ind%4)
        if(c==True):
            return True
    elif(ind<12):
        c=check(8,ind%4)
        if(c==True):
            return True
    elif(ind<16):
        c=check(12,ind%4)
        if(c==True):
            return True

    if(ind%5==0):
        if(win[0] and win[5] and win[10] and win[15]):
            for j in range(4):
                count=0
                for i in range(0,11,5):
                    if(win[i][j]==win[i+5][j]):
                        count+=1
                if(count==3):
                    return True
    elif(ind%3==0):
        if(win[3] and win[6] and win[9] and win[12]):
            for j in range(4):
                count=0
                for i in range(3,10,3):
                    if(win[i][j]==win[i+3][j]):
                        count+=1
                if(count==3):
                    return True

def check(row,col):
    global win
    if(win[row] and win[row+1] and win[row+2] and win[row+3]):
        for j in range(4):
            count=0
            for i in range(3):
                if(win[row+i][j]==win[row+i+1][j]):
                    count+=1
            if(count==3):
                return True
    if(win[col] and win[col+4] and win[col+8] and win[col+12]):
        for j in range(4):
            count=0
            for i in range(col,col+9,4):
                if(win[i][j]==win[i+4][j]):
                    count+=1
            if(count==3):
                return True

def playagain():
    button("Play Again..!!",670,400,200,55,c.grey,c.cement,restart)
    
def PlayerPiece():
    if(c.won==True and c.do==1):
        largeText = pygame.font.SysFont("comicsansms",20)
        TextSurf2, TextRect2 = text_objects("You won", largeText)
        TextRect2.center = (325,400)
        gameDisplay.blit(TextSurf2, TextRect2)
        largeText = pygame.font.SysFont("comicsansms",20)
        TextSurf2, TextRect2 = text_objects("You lose", largeText)
        TextRect2.center = (1200,400)
        gameDisplay.blit(TextSurf2, TextRect2)
        c.list1=c.y.copy()
        playagain()

    elif(c.won==True and c.do==0):
        largeText = pygame.font.SysFont("comicsansms",20)
        TextSurf2, TextRect2 = text_objects("You won", largeText)
        TextRect2.center = (1200,400)
        gameDisplay.blit(TextSurf2, TextRect2)
        largeText = pygame.font.SysFont("comicsansms",20)
        TextSurf2, TextRect2 = text_objects("You lose", largeText)
        TextRect2.center = (325,400)
        gameDisplay.blit(TextSurf2, TextRect2)
        c.list1=c.y.copy()
        playagain()
        
    elif(c.do==1):
        buttongame(270,190,75,75,c.list[0],c.list[0])
        buttongame(1180,190,75,75,c.list[0],c.list[0],img=c.select[0])

        if(c.select[0]==False):
            largeText = pygame.font.SysFont("comicsansms",20)
            TextSurf2, TextRect2 = text_objects("Select a piece!", largeText)
            TextRect2.center = (310,300)
            gameDisplay.blit(TextSurf2, TextRect2)

        else:
            largeText = pygame.font.SysFont("comicsansms",20)
            TextSurf2, TextRect2 = text_objects("Place your piece", largeText)
            TextRect2.center = (1200,300)
            gameDisplay.blit(TextSurf2, TextRect2)
            if(c.name2=="Computer"):
                computerplace()

    else:
        buttongame(270,190,75,75,c.list[0],c.list[0],img=c.select[0])
        buttongame(1180,190,75,75,c.list[0],c.list[0])

        if(c.select[0]==False):
            largeText = pygame.font.SysFont("comicsansms",20)
            TextSurf2, TextRect2 = text_objects("Select a piece!", largeText)
            TextRect2.center = (1200,300)
            gameDisplay.blit(TextSurf2, TextRect2)
            if(c.name2=="Computer"):
                computerselect()

        else:
            largeText = pygame.font.SysFont("comicsansms",20)
            TextSurf2, TextRect2 = text_objects("Place your piece", largeText)
            TextRect2.center = (310,300)
            gameDisplay.blit(TextSurf2, TextRect2)



def restart():
    global win
    c.list1=c.x.copy()
    c.list2=c.y.copy()
    c.select[0]=False
    c.won=False
    c.temp1[0]=False
    c.temp=c.new1.copy()
    win=c.new2.copy()
    c.check_piece=c.check_piece1.copy()
    c.do=1
    gameplay()

def confirm(attribute):
    done = True
    screen = pygame.display.set_mode(c.size)
    if attribute=="resume":
        gameplay()
        done=False
        
    while done:
        screen.blit(c.pic,[-150,-200])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
        var="Do you want to " + attribute + "....??"
        
        largeText = pygame.font.SysFont("comicsansms",35)
        TextSurf2, TextRect2 = text_objects(var, largeText)
        TextRect2.center = (780,300)
        screen.blit(TextSurf2, TextRect2)
        
        if(attribute=="restart"):
            button("YUP",470,400,160,60,c.white,c.grey,restart)
            button("NOPE",900,400,160,60,c.white,c.grey,pause)
        elif(attribute=="exit"):
            button("YUP :-(",470,400,160,60,c.white,c.red,playerselect)
            button("NOPE :-)",900,400,160,60,c.white,c.grey,pause)
        
        
        
        pygame.display.update()
        clock.tick(60)

def pause():
    done = True
    while done:
        gameDisplay.blit(c.pic,[-150,-200])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        button("Resume",670,300,200,60,c.white,c.grey,confirm,"resume")
        button("Restart",670,400,200,60,c.white,c.grey,confirm,"restart")
        button("Back to Menu",670,500,200,60,c.white,c.grey,confirm,"exit")
        pygame.display.update()
        clock.tick(60)
         
def gameplay():
    pygame.display.set_caption("LET'S PLAY")
   
    done = False
    clock = pygame.time.Clock()
    
    
    while not done:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause()

        gameDisplay.blit(c.pic,[-150,-200])

        largeText = pygame.font.SysFont("comicsansms",30)
        TextSurf1, TextRect1 = text_objects("QUARTO", largeText)
        TextRect1.center = (760,30)
        gameDisplay.blit(TextSurf1, TextRect1)

        TextSurf, TextRect = text_objects(c.name1, largeText)
        TextRect.center = (310,150)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf2, TextRect2 = text_objects(c.name2, largeText)
        TextRect2.center = (1210,150)
        gameDisplay.blit(TextSurf2, TextRect2)

        button("Pause",1350,700,140,60,c.grey,c.cement,pause)

        line,i=0,0
        for y in range(80,380,75):
            for x in range(610,910,75):
                buttongame(x,y,75,75,c.list[(i+line)%2],c.list[(i+line)%2],img=c.list2[i],ind=i)
                i+=1
            line+=1

        i=0
        for x in range(460,1060,75):
            buttongame(x,500,75,75,c.list[(i)%2],c.list[(i)%2],img=c.list1[i],action=i)
            buttongame(x,600,75,75,c.list[(i+1)%2],c.list[(i+1)%2],img=c.list1[i+8],action=i+8)
            i+=1

        PlayerPiece()        
        pygame.display.flip()

        
def playerselect():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro=False
        
        gameDisplay.blit(c.pic,[-150,-200])
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("Quarto", largeText)
        TextRect.center = ((c.display_width/2),150)
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Single Player",670,300,200,60,c.white,c.grey,singleplay)
        button("Multi Player",670,380,200,60,c.white,c.grey,multiplay)
        button("Quit",730,555,90,50,c.white,c.red,quitgame)
        pygame.display.update()
        clock.tick(60)
if __name__=="__main__":
    playerselect()
    pygame.quit()
