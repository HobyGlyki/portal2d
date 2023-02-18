import pygame
pygame.init()

numbox=8
box=48
print(numbox*box)
grind_widht=numbox*box
grind_hidht=numbox*box+20
sc = pygame.display.set_mode((grind_widht, grind_hidht))
pygame.display.set_caption("порталы")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
YAL = (255, 255, 0)
BLOU=(0, 0, 255)
GREEN = (0, 255, 10)
GREEN2=((0, 255, 200))


x=1
y=1
dir=0


gravi=10
jump=1
pygame.display.update()
rad=1
pizd=0
pos=[0, box*6]

p1x=box*4
p1y=box*5
p2x=box*1
p2y=box*2
grow=0

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	pygame.draw.rect(sc, (0, 0, 0), (0, 0, grind_widht, grind_hidht))
	bt = pygame.key.get_pressed()
	

	if bt[pygame.K_a]:	
		pos[0]-=1
	if bt[pygame.K_f]:	
		pos[0]+=0.5
	if bt[pygame.K_d]:	
		pos[0]+=1
	pygame.draw.rect(sc, GREEN2, (pos[0], pos[1], box, box))
	
	if bt[pygame.K_RIGHT]:	
		p1x+=1
	elif bt[pygame.K_LEFT] and p1x>pos[0] or bt[pygame.K_LEFT] and pos[1]!=p1y+box:
		p1x-=1
	elif bt[pygame.K_UP] and pos[0]<p1x:	
		p1y=p2y
	elif bt[pygame.K_DOWN] and pos[0]<p1x:	
		p1y=box*5

	if pos[0]+box>p1x and pos[1]==p1y+box:
		x=p2x-(-pos[0]+p1x-box)
		y=pos[1]-(p1y-p2y)
		pygame.draw.rect(sc, GREEN2, (x, y, box, box))
	if pos[0]>p1x-box/2 and pos[1]==p1y+box:
		pos[0]=x
		pos[1]=y

	if pos[0]-box<p2x and pos[1]==p2y+box:
		x=p1x-(-pos[0]+p2x+box)
		y=pos[1]-(p2y-p1y)
		pygame.draw.rect(sc, GREEN2, (x, y, box, box))
	if pos[0]<p2x+box/2 and pos[1]==p2y+box:
		pos[0]=x
		pos[1]=y



	pygame.draw.rect(sc, BLOU, (p1x, p1y, box, box*2))
	pygame.draw.rect(sc, YAL, (p2x, p2y, box, box*2))


	clock.tick(60)
	pygame.display.update()