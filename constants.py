import pygame

pygame.init()
 
display_width = 1528
display_height = 780
 
black = (0,0,0)
white = (255,255,255)
grey = (230, 230, 230)
red = (255,26,26)
cement=(204,204,204)

size=(display_width,display_height)


rsts= pygame.image.load('pics/rsts.jpg')
bcsh= pygame.image.load('pics/bcsh.jpg')
bcss= pygame.image.load('pics/bcss.jpg')
bcth= pygame.image.load('pics/bcth.jpg')
bcts= pygame.image.load('pics/bcts.jpg')
bssh= pygame.image.load('pics/bssh.jpg')
bsss= pygame.image.load('pics/bsss.jpg')
bsth= pygame.image.load('pics/bsth.jpg')
bsts= pygame.image.load('pics/bsts.jpg')
rcsh= pygame.image.load('pics/rcsh.jpg')
rcss= pygame.image.load('pics/rcss.jpg')
rsss= pygame.image.load('pics/rsss.jpg')
rcth= pygame.image.load('pics/rcth.jpg')
rcts= pygame.image.load('pics/rcts.jpg')
rssh= pygame.image.load('pics/rssh.jpg')
rsth= pygame.image.load('pics/rsth.jpg')
pic = pygame.image.load('pics/white.jpg')

done=False
list = [grey,cement]
list1 = [bcsh,bcss,bssh,bsss,bcth,bcts,bsth,bsts,rcsh,rcss,rssh,rsss,rcth,rcts,rsth,rsts]
list2 = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
select=[False]

x=list1.copy()
y=list2.copy()
z=select.copy()

temp=["bcsh","bcss","bssh","bsss","bcth","bcts","bsth","bsts","rcsh","rcss","rssh","rsss","rcth","rcts","rsth","rsts"]
win=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
temp1=[False]
won=False

new1=temp.copy()
new2=win.copy()

name1="Player 1"
name2="Computer"
com_select=False
com_place=False

do=1
check_piece=[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16]
check_piece1=check_piece.copy()

frame_count1,frame_count2 = 0,0
frame_rate1,frame_rate2 = 5,5
start_time1,start_time2 = 90,90
minutes1,minutes2= 0,0
seconds1,seconds2 = 0,0

