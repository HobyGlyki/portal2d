import pygame 
import sys

w=30
h=9
box=75


pygame.init()
sc = pygame.display.set_mode((1080, h*box))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

p="p"#коробка
n1=0
n2=2
opw=0
x=box*2 #x Игрока
y=box*5 #y Игрока


gravi=0 #гравитация
vy=1 #скорость по Y
vx=0 #скорость по X
vr=1 #разгон на права
vl=1 #разгон на лево
imp=0
jump=1 #Кол-Во Прыжков
xm=0 #Координаты Карты по X
ym=0#Координаты Карты по У
dirs=1 #направление движение
dirx=0 #столкновения по X
diry=1 #столкновение по Y
mapw=1 #Карта статическая или нет
Force=0 #сила прыжка
Sprint=4 #спринт
p1y=200
p1x=2000
p2y=200
p2x=200
xc=0
yc=0
dirp=1
time=0
pos=0

hero= pygame.Surface((x, y))
hero=pygame.image.load('icon\manImg.png')
rect = hero.get_rect()
hero=pygame.transform.scale(hero, (box, box))

stenka= pygame.Surface((box, box))
stenka = pygame.image.load('icon\stena1.png').convert()
stenka_rect=stenka.get_rect()
stenka=pygame.transform.scale(stenka, (box, box))

stenkaa= pygame.Surface((box, box))
stenkaa = pygame.image.load('icon\point.png').convert()
stenkaa_rect=stenkaa.get_rect()
stenkaa=pygame.transform.scale(stenkaa, (box, box))

stenka1= pygame.Surface((box, box))

stenka1 = pygame.image.load('icon\stena.png').convert()
stenka1_rect=stenka1.get_rect()
stenka1=pygame.transform.scale(stenka1, (box, box))

boxer= pygame.Surface((box, box))
boxerr= pygame.Surface((box, box))
boxer = pygame.image.load('icon\RadImg.png')
boxerr= pygame.image.load('icon\manImg1.png')
boxer1=boxer.get_rect()
boxer2=boxer.get_rect()
boxer=pygame.transform.scale(boxer, (box, box))
boxerr=pygame.transform.scale(boxerr, (box, box))

pygame.mixer.music.load("icon\main.mp3")
pygame.mixer.music.play(-1)
winmus=pygame.mixer.Sound("icon\win.wav")

start=1

pygame.mouse.set_visible(False)

mass=[[2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 22,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
 	  [2, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
 	  [2, 0, 0, 0, 0, p, p,p, p, p, p, p, p, p,p, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
	  [2, 0, 0, 0, p, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
	  [2, 0, 0, p, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
	  [2, 0, p, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
	  [2, p, 0, 0, 0, 0, 0,0, 0, 2, 0, 0, 0, 0,0, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
	  [2, 0, p, 0, 0, 0, 0,0, 0, 2, 0, 0, 0, 0,0, 2, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 2],
	  [2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2, 2, 2, 2, 2, 2, 2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]


port=[[0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 	  [0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
 	  [0, 0, 0, 0, 0, p, p,p, p, p, p, p, p, p,p, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
	  [0, 0, 0, 0, p, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
	  [0, 0, 0, p, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
	  [0, 0, p, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
	  [0, p, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
	  [2, 0, p, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 1, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0, 0],
	  [0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	  [0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]




leveldr=[mass]


dr=-100
level=0
f = pygame.font.SysFont('arial', 24)
sc_text = f.render("hui", 1, "white")
pos = sc_text.get_rect(center=(w*box//2, h*box//2))


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:               
			pygame.quit()
			sys.exit()


		elif event.type ==pygame.KEYUP:
				if event.key== pygame.K_w and jump>0 and Force>=1:
					y-=0.1
					diry=1
					gravi=Force
					Force=0
					jump-=1
				elif event.key== pygame.K_w and jump==0:Force=0 
#прыжок
	pressed = pygame.mouse.get_pressed()
	pos = pygame.mouse.get_pos()
	bt = pygame.key.get_pressed() 
	#Управление скорости по X v
	if bt[pygame.K_a] and dirx!=-1:##л_скорость
		dirs="l"
		vx=-vl-Force/1
	if bt[pygame.K_d] and dirx!=1:##п_скорость	
		dirs="r"
		vx=vr+Force/4
	else: ##ничего
		vx*=0.70
	if vx<=0.01 and vx>=-0.01: vx=0


	if bt[pygame.K_w] and Force<=3: #максимальная сила прыжка при зажатии вверх
			Force+=1 ##на сколько увеличивается
	if bt[pygame.K_f]:print(p2x-x+xm+box) ##дебаг
	if bt[pygame.K_LSHIFT]:Sprint=10
	else:Sprint=2

	if bt[pygame.K_a] and vl<=Sprint:##л_скорость
		vl+=1
	elif vl>=1.01:
		vl-=0.1
	else:vl=1

	if bt[pygame.K_d] and vr<=Sprint:	##п_скорость
		vr+=1
	elif vr>=1.01:
		vr-=0.1
	else:vr=1
	#управление скорости ^
#Гравитация
	if diry!=1:
		jump=1
		gravi=0
	elif(gravi!=10):gravi-=0.1
#поотлок
	if y>=3:
		y-=gravi*vy
	else:y+=abs(gravi)
#игрок 
	boxer2=(x, y)
#управление камерой и игроком по X
	if(dirs=="l" and x<=box and mapw==1 and dirx!=-1 or dirs=="r" and x>=10*box and mapw==1 and dirx!=1):xm-=vx*vy
	elif(dirs =="l" and x>=4 and dirx!=-1 or dirs=="r" and x<=13.5*box and dirx!=1):x+=vx*vy
	if(x<60) and mapw==1:
		x+=time
		xm+=time
		time+=5
	elif(x>771):
		x-=time
		xm-=time
		time+=5
	else:time=0

#карта конец и начало
	if(xm>=-67*box-2 and dirs=="r" or xm<=0-2 and dirs=="l"):mapw=1
	else:mapw=0

	if x>=11*box and x<=13.5*box:mapw=0
	else:mapw=1

#скорость по Y 
	if abs(vx)>=0.1 and vy<=2 or abs(gravi)>=0.1 and vy<=3:
		vy+=0.05
	elif abs(gravi)<=0.1 and vy>1.5:
		vy-=0.5
	elif abs(vx)<=0.1 and vy<1.5:
		vy=1

	
##стены
	sc.fill("black")
	for m in range(len(mass)):
		for i in range(len(mass[m])):

			if port[m][i] ==1:
				p1y=m*box
				p1x=i*box
			if port[m][i] ==2:
				p2y=m*box
				p2x=i*box
			if port[m][i] ==3:
				p2y=m*box
				p2x=i*box
				p1y=m*box
				p1x=i*box

			stenka_rect = ((i) * box+xm, (m) * box+ym)
			sc.blit(stenka, stenka_rect)
			if mass[m][i] == 2:
				stenka1_rect = ((i) * box+xm, (m) * box+ym)
				sc.blit(stenka1, stenka1_rect)
				##пол
				if x+box-15>=(i) * box+xm and x+20<=(i) * box+xm+box and y+box>=(m) * box+ym-10 and y+box<=(m) * box+ym+20 and gravi<=0 and port[m][i]==0:
					y=(m)*box+ym-box
					diry=0

					
					##cтена справа
				if x+box-10>=(i) * box+xm and x<=(i) * box+xm+box/5 and y+box>=(m) * box+ym+1 and y<=(m) * box+ym+box/2:
						if port[m+1][i]==1 and n1==0 or n1==0 and port[m][i]==1 or port[m][i]==2 and n2==0 or port[m+1][i]==2 and n2==0 or port[m][i]==3:dirx=0 
						elif n1==n2==0 and port[m][i]!=0: dirx=0
						else:
							x=(i) *box+xm-box+10
							dirx=1.5
				##cтена слева
				if x+box/5>=(i) * box+xm and x<=(i) * box+xm+box-10 and y+box>=(m) * box+ym+1 and y<=(m) * box+ym+box/2:
					if port[m][i]==2 and n2==2 or port[m+1][i]==2 and n2==2 or n1==2 and port[m][i]==1 or n1==2 and port[m+1][i]==1  or port[m][i]==3:dirx=0
					elif n1==n2==2 and port[m][i]!=0: dirx=0
					else:
						x=(i) * box+xm+box-10
						dirx=-1.5
				##потолок
				
				if x+box-15>=(i) * box+xm and x+20<=(i) * box+xm+box and y<=(m) * box+ym+box+10	 and y>=(m) * box+ym and port[m+1][i]==0:
					gravi-=1

					
				if pygame.mouse.get_focused():
					if pressed[0] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and port[m][i]<=1 and pos[0]-x+box/2>0:n1=0
					if pressed[0] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and port[m][i]<=1 and pos[0]-x-10<0:n1=2
					if pressed[0] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and port[m][i]!=2 and port[m][i]!=3 and port[m+1][i]<2 and port[m-1][i]<2:
						port[round(p1y/box)][round(p1x/box)]-=1
						port[(pos[1]//box)][round((pos[0]-xm)//box)]=1
					elif pressed[0] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and port[m][i]==2 and n1!=n2:
						port[round(p1y/box)][round(p1x/box)]=0
						port[(pos[1]//box)][round((pos[0]-xm)//box)]=3

					if pressed[2] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and ((port[m][i])+n1+1)%2!=0 and pos[0]-x+box/2>0:n2=0
					if pressed[2] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and (port[m][i])*n1==0 and pos[0]-x-10<0:n2=2

					if pressed[2] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and port[m][i]%2==0 and  (port[m+1][i])%2==0 and (port[m-1][i])%2==0:
						port[round(p2y/box)][round(p2x/box)]-=2
						port[(pos[1]//box)][round((pos[0]-xm)//box)]=2
					elif pressed[2] and m==pos[1]//box and i==(pos[0]-xm)//box and mass[m-1][i]==2 and port[m][i]==1 and n1!=n2:
						port[round(p2y/box)][round(p2x/box)]=0
						port[(pos[1]//box)][round((pos[0]-xm)//box)]=3



			if mass[m][i] == p:
				boxer1 = ((i) * box+xm, (m) * box+ym)
				sc.blit(boxer, boxer1)
				if not bt[pygame.K_s] and x+box-15>=(i) * box+xm and x+20<=(i) * box+xm+box and y+box>=(m) * box+ym-10 and y+box<=(m) * box+ym+20 and gravi<=0:
					y=(m)*box+ym-box
					diry=0


	sc.blit(boxerr, boxer2)
		# y7 x78 y7 x15

		
	if bt[pygame.K_c]:
		port[7][15]=0
		port[7][78]=1

	if n1!=n2:
		if x<p1x+xm+box/2 and x>=p1x-box/2+xm and  y<p1y+8 and y+box*2>=p1y+2:
			x=xc
			y=yc
			#1:/2 2:+2
		elif x<p1x+xm+box/(2-n1+0.999999) and x+box*(abs(n1-2)/2)>p1x+xm and y<p1y+8 and y+box*2>=p1y+3:
			xc=p2x-(-x+p1x+box*(n1-1))
			yc=y-(p1y-p2y)
			dirp=1
		elif x<p2x+xm+box/2 and x>=p2x-box/2+xm  and y<p2y+8 and y+box*2>=p2y+3:
			x=xc
			y=yc
		elif x<p2x+xm+box*(n2/2) and x+box/(n2+0.999999)>p2x+xm and y<p2y+8 and y+box*2>=p2y+3:
			xc=p1x-(-x+p2x+box*(n2-1))
			yc=y-(p2y-p1y)
			dirp=1
		else:dirp=0
		if dirp>0:sc.blit(boxerr, (xc, yc, box, box))
	else:
		if x<p1x+xm+box/3 and x>=p1x-box/2+xm and  y<p1y+8 and y+box*2>=p1y+2:
			x=xc
			y=yc
			imp=4
			#1:/2 2:+2
		elif x<p1x+xm+box/(2-n1+0.999999) and x+box*(abs(n1-2)/2)>p1x+xm and y<p1y+8 and y+box*2>=p1y+3:
			xc=p2x+xm+((p1x+xm)-x+(box*(n2-1)))
			yc=y-(p1y-p2y)
			dirp=1
		elif x<p2x+xm+box/2 and x>=p2x-box/2+xm  and y<p2y+8 and y+box*2>=p2y+3:
			x=xc
			y=yc
			imp=4
		elif x<p2x+xm+box*(n2/2) and x+box/(n2+0.999999)>p2x+xm and y<p2y+8 and y+box*2>=p2y+3:
			xc=p1x+xm+((p2x+xm)-x+(box*(n2-1)))
			yc=y-(p2y-p1y)
			dirp=1
		else:dirp=0
		if dirp>0:sc.blit(boxerr, (xc, yc, box, box))
		if imp>0:
			x+=imp*5*(n1-1)+vy*(n1-1)
			imp-=0.5


	if diry<1:diry+=0.5
	if diry>1:diry=1

	if dirx<0:dirx+=0.5
	elif dirx>0:dirx-=0.5
	if dirx>-0.1 and dirx<0.1:dirx=0


	for m in range(len(mass)):
		for i in range(len(mass[m])):
			if mass[m][i] == 2:
				stenka1_rect = ((i) * box+xm, (m) * box+ym)
				sc.blit(stenka1, stenka1_rect)

	pygame.draw.rect(sc, (0, 0, 255),   (p1x+xm+box/3*n1, p1y-box, box/3, box*2))
	pygame.draw.rect(sc, (255, 0, 255), (p2x+xm+box/3*n2, p2y-box, box/3, box*2))

	if pygame.mouse.get_focused():
		pygame.draw.rect(sc, (24, 23, 24), (pos[0], pos[1], 12, 12))

	pygame.display.update()
	clock.tick(120)