from cmu_graphics import *

app.background = gradient('white','white','gainsboro',start='top')
app.drawing_m = False # Sets up state in which the user can draw
app.rect_m = False # Checks if user can or cannot draw: Recatngles
app.circ_m = False # ^ Circles
app.star_m = False # ^ Stars
app.line_m = False # ^ Lines
app.label_m = False # ^ Labels
app.reg_poly_m = False # ^ Polygons Regular 
app.custom_poly_m = False # ^ Polygons Custom (no add point)
app.drawing_sub_ms = [app.rect_m,app.circ_m,app.star_m,app.line_m,app.label_m,app.reg_poly_m,app.custom_poly_m]
app.current_ms = 0 # This keeps track of all modes | ^ list holds all sub
app.current_sub_ms = 0 # This keeps track of all sub-modes        ^ modes
app.sub_m_limit = 1 # This sets limit on how many sub-modes active
draw_switch = Group(Rect(360, 160, 40, 80),Label('DRAW', 380, 200,fill='white',size=14,rotateAngle=270))
rect_switch = Group(Rect(10, 5, 30, 30),Label('RECT', 25, 20,fill='white'))
circ_switch = Group(Rect(10, 65, 30, 30),Label('CIRC', 25, 80,fill='white'))
star_switch = Group(Rect(10, 125, 30, 30),Label('STAR', 25, 140,fill='white'))
line_switch = Group(Rect(10, 185, 30, 30),Label('LINE', 25, 200,fill='white'))
label_switch = Group(Rect(10, 245, 30, 30),Label('LABEL', 25, 260,fill='white',size=7.5,bold=True))
reg_poly_switch = Group(Rect(10, 305, 30, 30),Label('POLY', 25, 320,fill='white',size=7.5,bold=True))
custom_poly_switch = Group(Rect(10, 365, 30, 30),Label('CUSTOM', 25, 380,fill='white',size=6.5,bold=True))
drawing_switches = [rect_switch,circ_switch,star_switch,line_switch,label_switch,reg_poly_switch,custom_poly_switch]
m_names = ['Rectangles Active','Circles Active','Stars Active','Lines Active','Label Active','Polygon Active','CPolygon Active']
activated_switch = [] #^Line 14 - 22 set up all of the switches that can
def toggle(switch): #^be pressed to toggle all the submodes and adds them
    if switch == False: #^to list called drawing switches, also names the
        switch = True   #^differing mode state names for each shape.
    else:               # <- This function called 'toggle' sets the
        switch = False  # <- parameter 'switch' its given to either true
    return switch       # <- if its false, or false if its true.
def draw_rect(x,y): # This function takes the x & y coordinates its given
    Rect(x,y,40,40,fill='red',) # to draw rectangle, preset size & color
def draw_circ(x,y): # This function takes the x & y coordinates its given
    Circle(x,y,20,fill='orange') # to draw circle, preset size & color
def draw_star(x,y): # This function takes the x & y coordinates its given
    Star(x,y,20,5,fill='yellow') # to draw star, preset size & color
def draw_line(x,y): # This function takes the x & y coordinates its given
    Line(x,y,x-15,y-15,fill='green') # to draw line, preset size & color
def draw_label(x,y): #This function takes the x & y coordinates its given
    Label('Text',x,y,fill='blue',size=14) # to draw label, same presets
def draw_reg_poly(x,y): #This function takes the x & y coordinates its g-
    RegularPolygon(x,y,20,6,fill='purple') #iven to draw a regular polyg-
def draw_poly(x,y): #on, preset size & color. the function on this line
    Polygon(x,y) # creates a single point polygon with its given x & y
def draw_shape(mouseX,mouseY):#This draw shapes function takes in the Mou
    if app.drawing_m == True:#se X & Y Parameters to draw shapes below:
        if app.rect_m == True: # Rectangles | Checks if mode is on
            draw_rect(mouseX,mouseY) #Calls functions shown in line 31-44
        if app.circ_m == True: # Circles | Checks if mode is on
            draw_circ(mouseX,mouseY) #Calls functions shown in line 31-44
        if app.star_m == True: # Stars | Checks if mode is on
            draw_star(mouseX,mouseY) #Calls functions shown in line 31-44
        if app.line_m == True: # Lines | Checks if mode is on
            draw_line(mouseX,mouseY) #Calls functions shown in line 31-44
        if app.label_m == True: # Labels | Checks if mode is on
            draw_label(mouseX,mouseY) #Calls functions shown above
        if app.reg_poly_m == True: # Polygons Regular | Checks mode
            draw_reg_poly(mouseX,mouseY) #Calls functions shown above
        if app.custom_poly_m == True: # Polygons Custom | Checks mode
            draw_poly(mouseX,mouseY) #Calls functions shown in line 31-44
        for switch in drawing_switches: #Goes Through all switches in the
            switch.toFront() #drawing_switches list and moves it to front
def check_switch(mouseX,mouseY): # This Function takes parameters Mouse 
    if app.current_sub_ms < app.sub_m_limit: # X & Y and checks if the
        for switch in range(0,len(drawing_switches)): #current sub-modes
            if drawing_switches[switch].hits(mouseX,mouseY): # are less
                app.current_sub_ms += 1 # than the limit. if true then it
                if switch == 0: # goes into a loop in the range of 0 to
                    app.rect_m = toggle(app.rect_m) # length of the swit-
                elif switch == 1: #ches, then it checks index/item in t-
                     app.circ_m = toggle(app.circ_m) #he list by using t-
                elif switch == 2: #he 'switch' interval from the loop. A
                    app.star_m = toggle(app.star_m) #-fter getting the i
                elif switch == 3: #-tem it checks it hits the parameters
                    app.line_m = toggle(app.line_m) #X & Y, if it does 
                elif switch == 4: # the current submodes will increase 
                    app.label_m = toggle(app.label_m) # by 1 and then 
                elif switch == 5: # check which number interval it was
                    app.reg_poly_m = toggle(app.reg_poly_m) # to deter-
                elif switch == 6: #mine which mode to toggle off or on
                    app.custom_poly_m = toggle(app.custom_poly_m) #then
                activated_switch.append(drawing_switches[switch]) #adds
    else: #switch to activated list.if current sub-modes are greater than
        for active_switch in activated_switch: #or equal to the limit th
            if active_switch.hits(mouseX,mouseY):#-en it does slightly d
                app.current_sub_ms -= 1#-ifferent sequence by checking t-
                if active_switch == drawing_switches[0]:#he a ctivated 
                    app.rect_m = toggle(app.rect_m)#switch list, if the
                elif active_switch == drawing_switches[1]:#mouseX&Y para-
                     app.circ_m = toggle(app.circ_m)#ms hit active switch
                elif active_switch == drawing_switches[2]:#then it checks
                    app.star_m = toggle(app.star_m)#which switch it is by
                elif active_switch == drawing_switches[3]:#seeing where i
                    app.line_m = toggle(app.line_m)#-ts equal, then choos
                elif active_switch == drawing_switches[4]:#-es which swi-
                    app.label_m = toggle(app.label_m)#tch to toggle off/
                elif active_switch == drawing_switches[5]:#on. after do-
                    app.reg_poly_m = toggle(app.reg_poly_m)#ing so it re-
                elif active_switch == drawing_switches[6]:#moves the swi-
                    app.custom_poly_m = toggle(app.custom_poly_m)#tch fr-
                activated_switch.remove(active_switch)#om the active list
    check_ms()#After these 2 conditions, it uses the check modes function
def check_drawing(): #this function checks if the user is in drawing mode
    if app.drawing_m == False:# or not, if they are then all of the switc
        for switch in drawing_switches:#-hes assoicated with drawing are
            switch.visible = False #turned visible. but if they are not
    else: # then all of the switches are turned invisible until turned on
        for switch in drawing_switches: # The Function on line 110 is ca-
            switch.visible = True#lled 'check_ms', it stands for check m-
def check_ms():#odes and looks if their are any sub_modes active by look
    if app.current_sub_ms > 0: #-ing at the count and seeing if its over
        for i in range(0,len(app.drawing_sub_ms)):#1, if it is then it 
            if app.drawing_sub_ms[i] == True:#looks for which one is act
                sub_m_text.value = 'Sub-Mode: '+str(m_names[i])#-ive and
    else:#picks which new value to assign to sub mode text value. if its 
        sub_m_text.value = 'Sub-Mode: None'#not it will stay as 'None'
def onMousePress(mouseX,mouseY):# The Mouse press function first checks
    if draw_switch.hits(mouseX,mouseY):# if the draw_switch has been hit
        if app.current_ms < 1:# by mouseX and mouseY, if it has then it
            app.drawing_m = toggle(app.drawing_m)# check if their is mo-
            main_m_text.value = 'Mode: Drawing'#re than 1 mode active,
            app.current_ms += 1#if there is then it will change the main
        else:#text value to Drawing and toggle the drawing mode. if not
            app.drawing_m = toggle(app.drawing_m)# then it will toggle
            main_m_text.value = 'Mode: None'#the drawing mode and change
            app.current_ms -= 1#the main text value to 'None'.
    check_drawing() #Calls 'Check Drawing' function first above all
    draw_shape(mouseX,mouseY)#Calls 'Draw Shape' function second
    check_switch(mouseX,mouseY)#and Finally Calls 'Check switch' function
    app.drawing_sub_ms = [app.rect_m,app.circ_m,app.star_m,app.line_m,app.label_m,app.reg_poly_m,app.custom_poly_m]
check_drawing() #^ Updates the app.drawing_sub_ms list values by reassign
Label('Welcome to the Canvas!',200,20,size=16,italic=True)#Creates title
main_m_text = Label('Mode: None',200,40,size=13,bold=True)#Draws mm text
sub_m_text = Label('Sub-Mode: None',200,55,size=11,bold=True)#sm text
Label('You can press |DRAW| to enter drawing mode, Click buttons on/off to draw on canvas',200,360,size=10,opacity=80,italic=True)

cmu_graphics.run()