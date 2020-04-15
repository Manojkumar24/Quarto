import pygame,ctypes,time,random,sys
import sqlite3
import Quarto


pygame.init()
display_width = 1528
display_height = 780
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)
rbg=(255,235,205)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Quarto')
clock = pygame.time.Clock()
a=pygame.image.load('pics/white.jpg')
c=pygame.image.load('pics/music2.jpg')
d=pygame.image.load('pics/music1.jpg')
x = 0
y = 0

gamesounds = {'click':pygame.mixer.Sound('click.wav')}
#gamesounds['click'] = pygame.mixer.Sound('click.wav')


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects1(text, font):
    textSurface1 = font.render(text, True, black)
    return textSurface1, textSurface1.get_rect()

def game_loop():
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.flip()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",50)
        TextSurf, TextRect = text_objects("Main game", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
        button1("BACK",display_width-175,display_height-125,125,75,white,bright_red,game_intro)
        pygame.display.update()
        clock.tick(60)

def options():
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("Options", largeText)
        TextRect.center = ((display_width/2),(display_height/7))   
        gameDisplay.fill(white)
        gameDisplay.blit(TextSurf, TextRect)
        #gameDisplay.blit(b, (display_width-100,display_height-100))
        button("HIGH SCORE",display_width/2.45,display_height/3,300,90,white,bright_green,highscore)
        button("HELP",display_width/2.3,display_height/2,215,90,white,bright_green,help1)
        button1("BACK",25,25,125,75,white,bright_red,game_intro)
        mouse1 = pygame.mouse.get_pos()
        click1 = pygame.mouse.get_pressed()
        if display_width > mouse1[0] > (display_width-100) and display_height > mouse1[1] > (display_height-100):
            
            if click1[0] == 1 and settings != None:
                
                if (a1%2==0):
                    pygame.mixer.Sound.play(gamesounds['click'])
                settings()
                
        pygame.display.update()
        clock.tick(60)
        
def highscore():
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        pygame.display.flip()
        largeText = pygame.font.SysFont("comicsansms",45)
        TextSurf, TextRect = text_objects("Highscores", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        ltext = pygame.font.SysFont("comicsansms",25)
        TextSurf, TextRect = text_objects("NAME         WINS         TOTAL_NO_OF_GAMES_PLAYED ", ltext)
        TextRect.center = ((display_width/2),(display_height/4))
        gameDisplay.fill(block_color)
        gameDisplay.blit(TextSurf, TextRect)
        button1("BACK",25,25,125,75,block_color,bright_red,game_intro)
        pygame.display.update()
        clock.tick(60)
            
def help1():
    while not False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
        largeText = pygame.font.SysFont("comicsansms",45)
        TextSurf, TextRect = text_objects("Help", largeText)
        TextRect.center = ((display_width/2),(display_height/6))   
        gameDisplay.fill(block_color)
        gameDisplay.blit(TextSurf, TextRect)
        button1("BACK",25,25,125,75,block_color,bright_red,options)
        pygame.display.update()
        clock.tick(60)



def music2():
    pygame.display.flip()
    mouse1 = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    gameDisplay.blit(d, (display_width-75,display_height-150))
    if (display_width-25) > mouse1[0] > (display_width-75) and (display_height-100) > mouse1[1] > (display_height-150):
            if click1[0] == 1 :
                if (a1%2==0):
                    pygame.mixer.Sound.play(gamesounds['click'])
                pygame.time.delay(500)
                music()   
                
    #pygame.display.update()
def music():
    #pygame.display.flip()
    gameDisplay.blit(d,(display_width-75,display_height-150))
    #pygame.display.update()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.ellipse(gameDisplay, black,(x,y,w+5,h+5),5)
        pygame.draw.ellipse(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if (a1%2==0):
                pygame.mixer.Sound.play(gamesounds['click'])
            pygame.time.delay(500)
            while True:
                action()
            
    else:
        pygame.draw.ellipse(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def button1(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.ellipse(gameDisplay, black,(x,y,w+5,h+5),5)
        pygame.draw.ellipse(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if(a1%2==0):
                pygame.mixer.Sound.play(gamesounds['click'])
            pygame.time.delay(500)
            action()
            
    else:
        pygame.draw.ellipse(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def img(a,x,y):
    gameDisplay.blit(a, (x,y))
    #pygame.display.flip()

def quitgame():
    conn = sqlite3.connect('scores.db')
    print ("Opened database successfully")

    conn.execute('''CREATE TABLE SCORES (NAME , WINS , TOTAL_NO_OF_GAMES_PLAYED );''')
    print ("Table created successfully")
    conn.execute("INSERT INTO SCORES  VALUES ('Paul', 32, 200 )");

    conn.execute("INSERT INTO SCORES  VALUES ('Allen', 25, 150)");

    conn.execute("INSERT INTO SCORES  VALUES ('Teddy', 23,  23 )");

    conn.execute("INSERT INTO SCORES  VALUES ('Mark', 25, 65 )");

    conn.execute("UPDATE SCORES SET WINS  = 32 WHERE NAME = 'Paul'");

    conn.commit()
    cursor = conn.execute("SELECT NAME, WINS, TOTAL_NO_OF_GAMES_PLAYED  FROM SCORES")
    print ("NAME \t\t\tWINS  \t\t\tTOTAL_NO_OF_GAMES_PLAYED  ")
    for row in cursor:
       
       print (row[0],'\t\t\t',row[1],'\t\t\t',row[2],'\n')
       #print ("= ", row[2],"\n")
   
    print ("Records created successfully")
    conn.close()

    pygame.quit()
    sys.exit()


def set2(action=None):
    if action != None:
        action()

def img1():
    return img(d,display_width-75,display_height-150)
a1=0
def game_intro():
    global a1,x1
    #a1=0
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        
        gameDisplay.blit(a,(0,0))
        largeText = pygame.font.SysFont("comicsansms",150)
        TextSurf, TextRect = text_objects("Quarto", largeText)
        TextRect.center = ((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf, TextRect)
        
        # gameDisplay.blit(e, (display_width-100,display_height-200))
        button("TAP TO PLAY",display_width/2.575,display_height/3,350,100,green,bright_green,Quarto.playerselect)
        button("OPTIONS",display_width/2.45,display_height/2,300,90,green,bright_green,options)
        button1("QUIT",display_width/2.15,display_height/1.5,125,75,red,bright_red,quitgame)
        mouse1 = pygame.mouse.get_pos()
        click1 = pygame.mouse.get_pressed()
        if a1%2==0:
            x1=c
                
        else:            
            x1=d

        
    
        def set1(action=None):
            if action != None:
                action()
        gameDisplay.blit(x1, (display_width-100,display_height-100))
        if display_width > mouse1[0] > (display_width-100) and display_height > mouse1[1] > (display_height-100):
            smallText = pygame.font.SysFont("comicsansms",20)
            textSurf, textRect = text_objects("Touch sounds", smallText)
            textRect.center = ( 1350, 725 )
            gameDisplay.blit(textSurf, textRect)
            if click1[0] == 1:
                gam=True
                a1=a1+1
                if (a1%2==0):
                    pygame.mixer.Sound.play(gamesounds['click'])
                pygame.time.delay(500)
                while gam:
                    set1(game_intro)
        pygame.display.update()
        clock.tick(15)

game_intro()
game_loop()

pygame.quit()
quit()

