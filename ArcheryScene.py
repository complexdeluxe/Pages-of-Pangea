from cmu_graphics import *
import random
import time
start = time.perf_counter()
print("Starting at ",start)


def arrow_movement(group, xincrement,yincrement,stepcount,sleep_time):
    for i in range(0,stepcount+1):
       print("Count #: "+str(i))
       group.centerX += xincrement
       group.centerY -= yincrement
       if i < 7:
           group.centerX += i*1.5
       if i > 7 and i <= 14:
           group.centerY += yincrement/1.25
           group.centerX -= xincrement-xincrement/(i-7)
           print("Slowing down at a speed of "+str(xincrement-xincrement/(i-7)))
           if i > 11:
               group.centerX += 1.5
               print("Slowing down an addtional speed of 1.5")
       if i > 14:
           group.centerY += yincrement*1.65
           group.centerX += xincrement-xincrement/(i-14)
           print("Speeding up at a speed of "+str(xincrement-xincrement/(i-14)))
           if i > 16:
               group.centerX + 3
               print("Speeding up an addtional speed of 3")
       group.rotateAngle += 3
       if i > 12:
           group.rotateAngle += 1
       time.sleep(sleep_time)
       if i == stepcount:
           print("Movement Complete")
       

           
def move_rect(x,y,xsize,ysize,xincrement,yincrement,stepcount,time):
   for i in range(0,stepcount+1):
       print("Count #: "+str(i))
       rect_group = Group()
       moving_rect = Rect(x+(i*xincrement),y+(i*yincrement),xsize,ysize,fill=rgb(110-(i*2),48,255))
       rect_group.add(moving_rect)
       time.sleep(time)
       
       if i < stepcount:
           rect_group.remove(moving_rect)
       else:
           print("Movement Complete")
"""
THE BACKGROUND
"""
def produce_star(x,y,radius,rotation,opacity):
    Star(x,y,radius,4,fill='white',rotateAngle=rotation,opacity=opacity)
    Star(x,y,radius,4,fill='white',rotateAngle=rotation+45,opacity=opacity)
    
# - Sky
Rect(0,0,400,340,fill=gradient(rgb(255,123,0),rgb(255,217,0),rgb(255,250,186),rgb(74,134,255),rgb(18,62,176),rgb(6,30,89),start='bottom'))

# - Stars
for i in range(40):
    randomX = random.randrange(10,390)
    
    randomY = random.randrange(15,100)
    
    random_radius = random.randrange(3,7)
    
    random_rotate = random.randrange(-50,140)
    
    random_opacity = random.randrange(20,80)
    
    produce_star(randomX,randomY,random_radius,random_rotate,random_opacity)
# - Sun
Star(140,200,75,175,fill=rgb(255,217,0))
Circle(140,200,60,fill=rgb(255,217,0))

# - Large Central Moutain
Polygon(80,313,190,60,280,313)
Polygon(190,60,168.5,110,211,120,fill='white',border='white')
Polygon(169,110,178,125,190,114,198,128,211,120,fill='white',border='white')
# - Mid-sized right Moutain
Polygon(60,313,130,150,200,313,fill=rgb(65,68,74))
# - Small left Mountain
Polygon(180,313,240,180,300,313,fill=rgb(84,86,92))
# - Far Hill
Oval(0,300,500,80,fill=gradient('black','green','green','green','green',rgb(255,217,0),start='bottom-right'))
# - Closer Hill
Oval(400,320,500,80,fill=gradient('black',rgb(71,219,21),rgb(71,219,21),rgb(71,219,21),start='bottom-left'))
# - Tree 1 (Around the center of the screen) (Blown By Wind)

trunk = Group()
trunk.add(Polygon(112,314,116,303,118,298,128,298,130,303,134,314,
fill=gradient(rgb(90,60,10),rgb(106,76,36),rgb(131,109,57),start='bottom'),border='black',borderWidth=1))
trunk.width += 10
trunk.height += 50
trunk.centerX += 40
trunk.centerY -= 20

tree_top = Group()
tree_top.add(Circle(150,271,14,fill='green',border='black',borderWidth=1))
tree_top.add(Circle(165,250,21,fill='green',border='black',borderWidth=1)) 
tree_top.add(Circle(173,269,11,fill='green',border='black',borderWidth=1))
tree_top.add(Rect(146,260,30,13,fill='green'))
tree_top.add(Rect(165,258,10,2,fill='green'))
tree_top.centerY -= 18.5
tree_top.width -= 5
tree_top.height -= 5
tree_top.rotateAngle = -5

# - Tree 2 (Larger Behind Target) (Blown By Wind)
Polygon(368,314,375,290,380,250,390,200,400,200,400,313,
fill=gradient(rgb(126,86,36),rgb(166,106,46),rgb(191,129,67),start='bottom'),border='black',borderWidth=1)
Circle(400,140,20,fill='green',border='black',borderWidth=1)
Circle(380,175,33,fill='green',border='black',borderWidth=1)
Circle(400,150,20,fill='green')
Circle(390,200,20,fill='green',border='black',borderWidth=1)
Circle(390,190,20,fill='green')
Rect(363,160,40,42,fill='green')

# - Bush 1 (Behind archer a bit off screen)

# - Bush 2 (Larger than bush 1 and around the middle of the screen) (Blown By Wind)

# - Bush 3 (Smallest bush and just at the bottom of the target) 

"""
THE SUBJECTS of IMPORTANCE
"""


# - Target
Rect(315,225,80,80,opacity=20)
Target = Group()
Target.add(Rect(310,220,80,80,fill='white',border='black',borderWidth=1))
Target.add(Circle(349,261,35,fill=None, border='black',borderWidth=1)) # Black Ring
Target.add(Circle(349,261,30,fill='black')) # Black Ring
Target.add(Circle(349,261,25,fill=None,border="white",borderWidth=1)) # White Line
Target.add(Circle(349,261,17.5,fill='blue')) # Blue Ring
Target.add(Circle(349,261,14.5,fill=None,border="black",borderWidth=1)) # Outer Black Line (blue)
Target.add(Circle(349,261,10,fill='red')) # Red Ring
Target.add(Circle(349,261,7.5,fill=None,border="black",borderWidth=1)) # Outer Black Line (blue)
Target.add(Circle(349,261,5,fill='yellow')) # Yellow Ring
Target.add(Circle(349,261,3.5,fill=None,border="black",borderWidth=1)) # Outer Black Line (blue)
Rect(318,303,10,10,opacity=20)
Rect(315,303,10,10)
Rect(378,303,10,10,opacity=20)
Rect(375,303,10,10)
Target.width += 5.5
Target.height += 5.5



# - The Archer (Blown By Wind)
head = Group()
head.add(Circle(30,240,12,fill=None,border='black',borderWidth=4)) # Adding the head
head.centerX -= 13
# --
# --
body = Group()
body.add(Line(30,248,30,290,lineWidth = 5)) # Adding the body
body.rotateAngle = -15
body.centerX -= 6
body.centerY += 1
# --
# --
right_arm = Group()

close_right_arm = Group()
close_right_arm.add(Line(30,255,40,270,lineWidth = 4))

latter_right_arm = Group()
latter_right_arm.add(Line(40,270,45,280,lineWidth = 4))

right_arm.add(close_right_arm) # Adding the right arm parts
right_arm.add(latter_right_arm) # ^^^

right_arm.centerX -= 1
right_arm.rotateAngle = -30
#--
#--
left_arm = Group()

close_left_arm = Group()
close_left_arm.add(Line(30,255,20,270,lineWidth = 4))

latter_left_arm = Group()
latter_left_arm.add(Line(20,270,15,280,lineWidth = 4))

left_arm.add(close_left_arm) # Adding left arm parts
left_arm.add(latter_left_arm)

left_arm.centerX -= 10.5
left_arm.centerY += 4
close_left_arm.rotateAngle = -20
close_left_arm.centerX += 3
latter_left_arm.rotateAngle = -100
latter_left_arm.centerX += 11
latter_left_arm.centerY -= 1

#--
#--
right_leg = Group()

close_right_leg = Group()
close_right_leg.add(Line(30,290,40,305,lineWidth = 4))

latter_right_leg = Group()
latter_right_leg.add(Line(40,305,45,320,lineWidth = 4))

right_foot = Group()
right_foot.add(Line(45,320,50,320,lineWidth = 4))

right_leg.add(close_right_leg) # Adding right leg parts
right_leg.add(latter_right_leg)
right_leg.add(right_foot)
#--
#--
left_leg = Group()

close_left_leg = Group()
close_left_leg.add(Line(30,290,20,305,lineWidth = 4))

latter_left_leg = Group()
latter_left_leg.add(Line(20,305,15,320,lineWidth = 4))

left_foot = Group()
left_foot.add(Line(15,320,20,320,lineWidth = 4))

left_leg.add(close_left_leg) # Adding left leg parts
left_leg.add(latter_left_leg)
left_leg.add(left_foot)

full_body = Group()
full_body.add(head)
full_body.add(body)
full_body.add(right_arm)
full_body.add(left_arm)
full_body.add(right_leg)
full_body.add(left_leg)

full_body.centerX += 33
full_body.centerY -= 7
#--
# - The Arrow (Blown By Wind)
Arrow = Group(Rect(25,175,50,5)
,Polygon(75,165,95,177.5,75,190,fill = gradient("black","green",start = "left"))
,Polygon(0,170,20,170,30,177,5,177.5,fill = gradient("yellow","yellow","red",start = "top"))
,Polygon(5,178,30,177.5,20,185,0,185,fill = "red"))
Arrow.rotateAngle = -27
Arrow.centerX = 78
Arrow.centerY = 268
Arrow.width += -36.5
Arrow.height += -36.5
Circle(349,261,2.5,fill='yellow') # Where the arrow gets stuck

# - The Bow
bow = Group()


first_string = Group()
first_string.add(Line(62,100,338,100,fill='gainsboro',lineWidth=3))
bow.add(first_string)
second_string = Group()
second_string.add(Line(62,100,200,85,fill='gainsboro',lineWidth=3))
second_string.add(Line(200,85,338,100,fill='gainsboro',lineWidth=3))
bow.add(second_string)
second_string.opacity = 0
third_string = Group()
third_string.add(Line(62,100,200,70,fill='gainsboro',lineWidth=3))
third_string.add(Line(200,70,338,100,fill='gainsboro',lineWidth=3))
bow.add(third_string)
third_string.opacity = 0
lower_limb = Polygon(50,120,95,150,120,160,150,173,170,178,185,180,192,190,197,195,197,225,193,215,190,210,160,200,80,160,
40,120,50,90,70,82,78,89,80,95,82,98,67.5,105,62,100,64,95,70,92.5,72,94.5,73,96.5,66,100,76,98,74,92,70,88,55,93,50,120,
fill=gradient('sienna', 'peru',start='left'),border='black',borderWidth=1)

upper_limb = Polygon(360,120,320,160,240,200,210,210,207,215,203,225,203,195,208,190,215,180,230,178,250,173,280,160,305,150,350,120,
350,120,345,93,330,88,326,92,324,98,334,100,327,96.5,328,94.5,330,92.5,336,95,338,100,332.5,105,318,98,320,95,322,89,330,82,350,90,360,120,
fill=gradient('sienna', 'peru',start='right'),border='black',borderWidth=1)

bow.add(lower_limb)
bow.add(upper_limb)

bow.rotateAngle = 257
bow.width -= 125
bow.height -= 260
bow.centerX = 31.5
bow.centerY = 277.5


bow.centerX += 33
bow.centerY -= 7
"""
THE FOREGROUND
"""
# - Ground
Rect(0,313,400,25, fill = gradient(rgb(23,183,17),rgb(23,120,17),start = "top"))
Rect(0,335,400,10, fill = gradient(rgb(23,120,17),rgb(125,62,0),start = "top"))
Rect(0,345,400,60, fill = gradient(rgb(125,62,0),rgb(125,62,0),rgb(100,40,0),start = "top"))


# - Grass (Blown By Wind)
grass_blades = Group()
for i in range(50):
    grass_blades.add(Polygon(0+(i*8),313,2+(i*8),310,4+(i*8),305,6+(i*8),310,8+(i*8),313,fill = rgb(23,183,17)))
grass_blades.height += 2

# - Filter
Rect(0,0,400,400,fill=gradient('white','orange',rgb(255,217,0),'black'),opacity=18)
# - Animations (THIS TOOK WAY TO LONG ADD MULTIPROCESSING T-T)
time.sleep(.5)
first_string.opacity = 0
second_string.opacity = 100
latter_left_arm.rotateAngle = 65
latter_left_arm.centerX -= 3
close_left_arm.rotateAngle = 5
close_left_arm.height += 7
Arrow.centerX -= 2
time.sleep(.5)
second_string.opacity = 0
third_string.opacity = 100
latter_left_arm.rotateAngle = 65
latter_left_arm.centerX -= 1
close_left_arm.rotateAngle += 3
close_left_arm.height += 2
Arrow.centerX -= 4
time.sleep(1)
third_string.opacity = 0
second_string.opacity = 100
Arrow.centerX += 4
second_string.opacity = 0
first_string.opacity = 100
Arrow.centerX += 2
arrow_movement(Arrow, 11.05, 4.5, 20,0)

finish = time.perf_counter()
cmu_graphics.run()