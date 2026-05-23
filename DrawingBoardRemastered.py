from cmu_graphics import *

app.background = gradient('white','white','gainsboro',start='top')
title = Label('Welcome to the Canvas!',100,20,size=16,italic=True)#Creates title
main_m_text = Label('Mode: None',80,35,size=13,bold=True)#Draws mm text
sub_m_text = Label('Sub-Mode: None',80,50,size=11,bold=True)#sm text
instructions_1 = Label('You can press |DRAW| to enter drawing mode and |SELECT| to eneter selection mode, or Press D / S keys',200,70,size=8,opacity=80,italic=True)
instructions_2 = Label('Press the different Shape Buttons and click on the canvas to draw shapes.',200,300,size=10,opacity=80,italic=True,visible=False)
instructions_3 = Label('Make sure to turn of Shape selections by pressing the button again, DONT PRESS KEYS!!',200,310,size=9.5,opacity=80,italic=True,visible=False)
instructions_4 = Label('Click on shapes to select them, You can Move, Scale, and Rotate selected shapes.',200,280,size=8,opacity=80,italic=True,visible=False)
instructions_5 = Label('Use the keys R, E, and Q respectively, you can click on a shape again to deselect it',200,290,size=8,opacity=80,italic=True,visible=False)
instructions_6 = Label('You can only deselect in scale and rotate mode and not in move, do not press buttons.',200,300,size=8,opacity=80,italic=True,visible=False)
instructions_7 = Label('Click and drag your mouse in each mode to use its effects. TURN OFF MODES BEFORE DRAWING!',200,310,size=8,opacity=80,italic=True,visible=False)
selected_element = []
new_elements = []
drawn_elements = []
# ~~ Drawing Mode ~~
app.drawing_m = False # Sets up state in which the user can draw
app.rect_m = False # Checks if user can or cannot draw: Recatngles
app.oval_m = False # ^ Ovals
app.star_m = False # ^ Stars
app.line_m = False # ^ Lines
app.label_m = False # ^ Labels
app.reg_poly_m = False # ^ Polygons Regular 
app.custom_poly_m = False # ^ Polygons Custom (no add point)
app.drawing_polygon = False # Checks to see if the user is making a custom polygon ^
# ~~ Selection Mode ~~
app.selection_m = False
app.move_m = False
app.scale_m = False
app.rotate_m = False
# ~~ Mode Misc. ~~
app.drawing_sub_ms = [app.rect_m,app.oval_m,app.star_m,app.line_m,app.label_m,app.reg_poly_m,app.custom_poly_m]
app.selection_sub_ms = [app.move_m,app.scale_m,app.rotate_m]
app.current_ms = 0 # This keeps track of all modes | ^ list holds all sub
app.current_sub_ms = 0 # This keeps track of all sub-modes        ^ modes
app.sub_m_limit = 1 # This sets limit on how many sub-modes active
# ~ Misc. ~
app.animation_filp = 1
app.element_selected = False
app.grab_mouse_pos = 'None'
# ~~ UI ~~
# ~ Main Modes ~
draw_switch = Group(Rect(70, 360, 120, 80,rotateAngle=-2,fill=gradient('limeGreen','forestGreen','black',start='top'),border=
gradient('dimGray','silver',start='top')),Label('DRAW', 130, 380,fill='white',size=16))
selection_switch = Group(Rect(210, 360, 120, 80,rotateAngle=2,fill=gradient('mediumBlue','dodgerBlue','skyBlue',start='top'),border=
gradient('dimGray','silver',start='top')),Label('SELECT', 270, 380,fill='white',size=16)) 
main_m_switches = [draw_switch,selection_switch]
# ~ Drawing Sub-Modes ~
rect_switch = Group(Rect(63, 320, 30, 30,border='white'),Label('RECT', 78, 334,fill='white',size=7.5,bold=True))
oval_switch = Group(Rect(105, 320, 30, 30,border='white'),Label('OVAL', 120, 334,fill='white',size=7.5,bold=True))
star_switch = Group(Rect(145, 320, 30, 30,border='white'),Label('STAR', 160, 334,fill='white',size=7.5,bold=True))
line_switch = Group(Rect(185, 320, 30, 30,border='white'),Label('LINE', 200, 334,fill='white',size=7.5,bold=True))
label_switch = Group(Rect(225, 320, 30, 30,border='white'),Label('LABEL', 240, 334,fill='white',size=7.5,bold=True))
reg_poly_switch = Group(Rect(266, 320, 30, 30,border='white'),Label('POLY', 281, 334,fill='white',size=7.5,bold=True))
custom_poly_switch = Group(Rect(305, 320, 30, 30,border='white'),Label('CUSTOM', 320, 334,fill='white',size=6.5,bold=True))
drawing_switches = [rect_switch,oval_switch,star_switch,line_switch,label_switch,reg_poly_switch,custom_poly_switch]
# ~ Selection Sub-Modes ~
move_switch = Group(Rect(145, 320, 30, 30,border='white'),Label('MOVE', 160, 334,fill='white',size=7.5,bold=True))
scale_switch = Group(Rect(185, 320, 30, 30,border='white'),Label('SCALE', 200, 334,fill='white',size=6.5,bold=True))
rotate_switch = Group(Rect(225, 320, 30, 30,border='white'),Label('ROTATE', 240, 334,fill='white',size=6.5,bold=True))
selection_switches = [move_switch,scale_switch,rotate_switch]
app.selection_box = Group()
app.rotateUI = Group()
app.scaleUI = Group()
app.moveUI = Group()
UI = Group(move_switch,scale_switch,rotate_switch,rect_switch,oval_switch,star_switch,
line_switch,label_switch,reg_poly_switch,custom_poly_switch,draw_switch,selection_switch
,title,main_m_text,sub_m_text)
draw_sm_names = ['Rectangles Active','Ovals Active','Stars Active','Lines Active','Label Active','Polygon Active','CPolygon Active']
select_sm_names = ['Move Active','Scale Active','Rotate Active']
activated_switch = []
def toggle(switch): #^be pressed to toggle all the submodes and adds them
    if switch == False: #^to list called drawing switches, also  names the
        switch = True   #^differing mode state names for each shape.
    else:               # <- This function called 'toggle' sets the
        switch = False  # <- parameter 'switch' its given to either true
    return switch       # <- if its false, or false if its true.
def draw_rect(x,y): # This function takes the x & y coordinates its given
    drawn_elements.append(Rect(x,y,40,40,fill='red',)) # to draw rectangle, preset size & color
def draw_oval(x,y): # This function takes the x & y coordinates its given
    drawn_elements.append(Oval(x,y,20,20,fill='orange')) # to draw Oval, preset size & color
def draw_star(x,y): # This function takes the x & y coordinates its given
    drawn_elements.append(Star(x,y,20,5,fill='yellow')) # to draw star, preset size & color
def draw_line(x,y): # This function takes the x & y coordinates its given
    drawn_elements.append(Line(x,y,x-15,y-15,fill='green')) # to draw line, preset size & color
def draw_label(x,y): #This function takes the x & y coordinates its given
    drawn_elements.append(Label('Text',x,y,fill='blue',size=14)) # to draw label, same presets
def draw_reg_poly(x,y): #This function takes the x & y coordinates its g-
    drawn_elements.append(RegularPolygon(x,y,20,6,fill='purple')) #iven to draw a regular polyg-
def draw_poly(x,y): #on, preset size & color. the function on this line
    drawn_elements.append(Polygon(x,y-5,x-5,y+5,x+5,y+5)) # creates a single point polygon with its given x & y
def draw_shape(x,y):#This draw shapes function takes in the Mou
    if app.drawing_m == True and UI.hits(x,y) != True:#se X & Y Parameters to draw shapes below:
        if app.rect_m == True: # Rectangles | Checks if mode is on
            draw_rect(x,y) #Calls functions shown in line 31-44
        if app.oval_m == True: # Ovals | Checks if mode is on
            draw_oval(x,y) #Calls functions shown in line 31-44
        if app.star_m == True: # Stars | Checks if mode is on
            draw_star(x,y) #Calls functions shown in line 31-44
        if app.line_m == True: # Lines | Checks if mode is on
            draw_line(x,y) #Calls functions shown in line 31-44
        if app.label_m == True: # Labels | Checks if mode is on
            draw_label(x,y) #Calls functions shown above
        if app.reg_poly_m == True: # Polygons Regular | Checks mode
            draw_reg_poly(x,y) #Calls functions shown above
        if app.custom_poly_m == True: # Polygons Custom | Checks mode
            draw_poly(x,y) #Calls functions shown in line 31-44
        for switch in drawing_switches: #Goes Through all switches in the
            switch.toFront() #drawing_switches list and moves it to front
def check_switch(x,y): # This Function takes parameters Mouse 
    if app.current_sub_ms < app.sub_m_limit: # X & Y and checks if the
        for switch in range(0,len(drawing_switches)): #current sub-modes
            if drawing_switches[switch].hits(x,y): # are less
                app.current_sub_ms += 1 # than the limit. if true then it
                if switch == 0: # goes into a loop in the range of 0 to
                    app.rect_m = toggle(app.rect_m) # length of the swit-
                elif switch == 1: #ches, then it checks index/item in t-
                     app.oval_m = toggle(app.oval_m) #he list by using t-
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
            if active_switch.hits(x,y):#-en it does slightly d
                app.current_sub_ms -= 1#-ifferent sequence by checking t-
                if active_switch == drawing_switches[0]:#he a ctivated 
                    app.rect_m = toggle(app.rect_m)#switch list, if the
                elif active_switch == drawing_switches[1]:#x&Y para-
                     app.oval_m = toggle(app.oval_m)#ms hit active switch
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
    check_sub_ms()#After these 2 conditions, it uses the check modes function
def check_drawing(): #this function checks if the user is in drawing mode
    if app.drawing_m == False:# or not, if they are then all of the switc
        for switch in drawing_switches:#-hes assoicated with drawing are
            switch.visible = False #turned visible. but if they are not
    else: # then all of the switches are turned invisible until turned on
        for switch in drawing_switches: # The Function on line 110 is ca-
            switch.visible = True#lled 'check_ms', it stands for check m-
def check_selection():
    if app.selection_m == False:
        for switch in selection_switches:
            switch.visible = False
    else:
        for switch in selection_switches:
            switch.visible = True
def check_sub_ms():#odes and looks if their are any sub_modes active by look
    if app.current_sub_ms > 0:#-ing at the count and seeing if its over
        if app.drawing_m == True:
            for i in range(0,len(app.drawing_sub_ms)):#1, if it is then it 
                if app.drawing_sub_ms[i] == True:#looks for which one is act
                    sub_m_text.value = 'Sub-Mode: '+str(draw_sm_names[i])#-ive and
                    
        elif app.selection_m == True:
            for i in range(0,len(app.selection_sub_ms)):
                if app.selection_sub_ms[i] == True:
                    sub_m_text.value = 'Sub-Mode: '+str(select_sm_names[i])
    else:#picks which new value to assign to sub mode text value. if its 
        sub_m_text.value = 'Sub-Mode: None'#not it will stay as 'None'
def create_selection_box(item):
    app.selection_box.clear()
    app.selection_box.add(Rect(item.top, item.left, item.width, item.height,
    fill=None,border='lightSkyBlue',opacity=100,borderWidth=2.25,
    dashes=True))
    app.selection_box.centerX = item.centerX
    app.selection_box.centerY = item.centerY 
    app.selection_box.toFront()
def create_rotate_ui(item):
    app.rotateUI.clear()
    degrees_text = Label(str(item.rotateAngle)+' Degrees',item.centerX, item.centerY - item.top*.3,size=10,italic=True,bold=True,border='white',borderWidth=.5)
    upper_right_arrow_base1 = Arc(item.centerX,item.centerY-15,30,30,0,90,fill='black')
    upper_right_arrow_base2 = Polygon(item.centerX,item.centerY-16,item.centerX+15,item.centerY-16,
    item.centerX+15,item.centerY,item.centerX,item.centerY-10)
    upper_right_arrow_pointer = Polygon(item.centerX+3,item.centerY-15,item.centerX-15,item.centerY-15,
    item.centerX-15, item.centerY-5, item.centerX-30, item.centerY-22.5, item.centerX-15,item.centerY-40,
    item.centerX-15,item.centerY-30,item.centerX+3,item.centerY-30,
    fill='black')
    upper_arrow = Group(upper_right_arrow_base1,upper_right_arrow_base2,upper_right_arrow_pointer)
    lower_left_arrow_base1 = Arc(item.centerX,item.centerY+15,30,30,0,90,fill='black',rotateAngle=180)
    lower_left_arrow_base2 = Polygon(item.centerX,item.centerY+16,item.centerX-15,item.centerY+16,
    item.centerX-15,item.centerY,item.centerX,item.centerY+10)
    lower_left_arrow_pointer = Polygon(item.centerX-3,item.centerY+15,item.centerX+15,item.centerY+15,
    item.centerX+15, item.centerY+5, item.centerX+30, item.centerY+22.5, item.centerX+15,item.centerY+40,
    item.centerX+15,item.centerY+30,item.centerX-3,item.centerY+30,
    fill='black')
    lower_arrow = Group(lower_left_arrow_base1,lower_left_arrow_base2,lower_left_arrow_pointer)
    upper_arrow.width = item.width/4
    upper_arrow.height = item.height/4
    upper_arrow.centerX = item.right
    upper_arrow.centerY = item.top - item.top/10
    lower_arrow.width = item.width/4
    lower_arrow.height = item.height/4
    lower_arrow.centerX = item.left
    lower_arrow.centerY = item.bottom + item.top/10
    app.rotateUI.add(degrees_text
    ,upper_right_arrow_base1,upper_right_arrow_base2
    ,upper_right_arrow_pointer,lower_left_arrow_base1,
    lower_left_arrow_base2,lower_left_arrow_pointer)
    for element in app.rotateUI:
        if item.containsShape(element):
            element.fill = 'white'
            element.border = 'black'
        elif element.centerY == (item.centerY - item.top/3):
            element.fill = 'black'
            element.border = 'white'
    app.rotateUI.toFront()
def create_scale_ui(item):
    app.scaleUI.clear()
    top_handle = Circle(item.centerX,item.top-item.top/3,15,fill='limeGreen',opacity=40)
    bottom_handle = Circle(item.centerX,item.bottom+item.top/3,15,fill='limeGreen',opacity=40)
    left_handle = Circle(item.left-item.left/3,item.centerY,15,fill='fireBrick',opacity=40)
    right_handle = Circle(item.right+item.left/3,item.centerY,15,fill='fireBrick',opacity=40)
    app.scaleUI.add(top_handle,bottom_handle,left_handle,right_handle)
def create_move_ui(item):
    app.moveUI.clear()
    top_arrow = Polygon(item.centerX,item.top-40,item.centerX+20,item.top-10,
    item.centerX,item.top-17.5,item.centerX-20,item.top-10,opacity=40)
    bottom_arrow = Polygon(item.centerX,item.bottom+40,item.centerX+20,item.bottom+10,
    item.centerX,item.bottom+17.5,item.centerX-20,item.bottom+10,opacity=40)
    left_arrow = Polygon(item.centerX,item.top-40,item.centerX+20,item.top-10,
    item.centerX,item.top-17.5,item.centerX-20,item.top-10,opacity=40,rotateAngle=270)
    right_arrow = Polygon(item.centerX,item.top-40,item.centerX+20,item.top-10,
    item.centerX,item.top-17.5,item.centerX-20,item.top-10,opacity=40,rotateAngle=90)
    left_arrow.centerY = item.centerY
    right_arrow.centerY = item.centerY
    left_arrow.centerX = item.left-25
    right_arrow.centerX = item.right+25
    app.moveUI.add(top_arrow,bottom_arrow,left_arrow,right_arrow)
def delete_selection_ui():
    app.selection_box.clear()
    app.rotateUI.clear()
    app.scaleUI.clear()
    app.moveUI.clear()
def onKeyPress(key):
    if ('d' or 'D') == key: # <- Drawing Key Filp
        drawing_filp()
        for m in app.drawing_sub_ms: # Turns off all drawing sub modes
            m = False
        for m in app.selection_sub_ms: # Turns off all selection sub modes
            m = False
    if ('s' or 'S') == key:
        selection_filp()
        for m in app.drawing_sub_ms: # Turns off all drawing sub modes
            m = False
        for m in app.selection_sub_ms: # Turns off all selection sub modes
            m = False
    if ('q' or 'Q') == key:
        app.move_m = toggle(app.move_m)
        if app.move_m == True:
            app.current_sub_ms += 1
            activated_switch.append(selection_switches[0])
        else:
            app.current_sub_ms -= 1
            activated_switch.remove(selection_switches[0])
        if (app.scale_m or app.rotate_m) == True:
            app.current_sub_ms -= 1
            for switch in selection_switches:
                if switch in activated_switch and switch != selection_switches[0]:
                    activated_switch.remove(switch)
        app.scale_m = False
        app.rotate_m = False
    if ('e' or 'E') == key:
        app.scale_m = toggle(app.scale_m)
        if app.scale_m == True:
            app.current_sub_ms += 1
            activated_switch.append(selection_switches[1])
        else:
            app.current_sub_ms -= 1
            activated_switch.remove(selection_switches[1])
        if (app.move_m or app.rotate_m) == True:
            app.current_sub_ms -= 1
            for switch in selection_switches:
                if switch in activated_switch and switch != selection_switches[1]:
                    activated_switch.remove(switch)
        app.rotate_m = False
        app.move_m = False
    if ('r' or 'R') == key:
        app.rotate_m = toggle(app.rotate_m)
        if app.rotate_m == True:
            app.current_sub_ms += 1
            activated_switch.append(selection_switches[2])
        else:
            app.current_sub_ms -= 1
            activated_switch.remove(selection_switches[2])
        if (app.move_m or app.scale_m) == True:
            app.current_sub_ms -= 1
            for switch in selection_switches:
                if switch in activated_switch and switch != selection_switches[2]:
                    activated_switch.remove(switch)
        app.move_m = False
        app.scale_m = False
    check_selection()
    check_drawing()
    check_sub_ms()
def drawing_filp():
    if app.current_ms < 1:# by x and y, if it has then it
        app.drawing_m = toggle(app.drawing_m)# check if their is mo-
        main_m_text.value = 'Mode: Drawing'#re than 1 mode active,
        app.current_ms += 1#if there is then it will change the main
    elif app.drawing_m == True:#text value to Drawing and toggle the drawing mode. if not
        app.drawing_m = toggle(app.drawing_m)# then it will toggle
        main_m_text.value = 'Mode: None'#the drawing mode and change
        app.current_ms -= 1#the main text value to 'None'.
def selection_filp():
    if app.current_ms < 1:
        app.selection_m = toggle(app.selection_m)
        main_m_text.value = 'Mode: Selection'
        app.current_ms += 1
    elif app.selection_m == True:
        app.selection_m = toggle(app.selection_m)
        main_m_text.value = 'Mode: None'
        app.current_ms -= 1
def onMousePress(x,y):
    for switch in main_m_switches:
        if switch == draw_switch:
            if switch.hits(x,y):
                drawing_filp()
        elif switch == selection_switch:
            if switch.hits(x,y):
               selection_filp()
    if app.drawing_m == True:    
        check_drawing() #Calls 'Check Drawing' function first above all
        check_selection()
        draw_shape(x,y)#Calls 'Draw Shape' function second
        check_switch(x,y)#and Finally Calls 'Check switch' function
        app.drawing_sub_ms = [app.rect_m,app.oval_m,app.star_m,app.line_m,app.label_m,app.reg_poly_m,app.custom_poly_m]
    if app.selection_m == True:
        check_drawing()
        check_selection()
        app.selection_sub_ms = [app.move_m,app.scale_m,app.rotate_m]
        for element in drawn_elements:
            if element.hits(x,y):
                if element.selected == False and app.element_selected == False and app.move_m == False:
                    element.selected = True
                    app.element_selected = True
                    selected_element.append(element)
                    create_selection_box(element)
                elif element.selected == True and app.element_selected == True and app.move_m == False:
                    element.selected = False
                    app.element_selected = False
                    selected_element.remove(element)
                    delete_selection_ui()
        if app.element_selected == True:
            if selected_element[0].hits(x,y):
                app.grab_mouse_pos = (x,y)
    check_drawing()
    check_selection()
    check_sub_ms()
def onMouseDrag(x,y):
    if app.move_m == True:
        if app.element_selected:
            selected_element[0].centerX = x
            selected_element[0].centerY = y
    if app.rotate_m == True:
        if app.element_selected:
            selected_element[0].rotateAngle = (x - app.grab_mouse_pos[0])
    if app.scale_m == True:
        if app.element_selected:
            if x - app.grab_mouse_pos[0] > 0:
                if x - app.grab_mouse_pos[0] != 0:
                    selected_element[0].width = (x - app.grab_mouse_pos[0])
            if y - app.grab_mouse_pos[1] > 0:
                if y - app.grab_mouse_pos[1] != 0:
                    selected_element[0].height = (y - app.grab_mouse_pos[1])
def onStep():
    if app.drawing_m == True:
        instructions_2.visible = True
        instructions_3.visible = True
        instructions_4.visible = False
        instructions_5.visible = False
        instructions_6.visible = False
        instructions_7.visible = False
        for element in drawn_elements:
            try:
                if element.selected == False:
                    pass
                if element.selected == True:
                    pass
            except AttributeError:
                element.selected = False
        delete_selection_ui()
        if len(selected_element) > 0:
            selected_element[0].selected = False
            selected_element.remove(selected_element[0])
            app.element_selected = False
        for switch in drawing_switches:
            if (switch in activated_switch) == False:
                for part in switch:
                    if part.fill != 'black' and part.fill != 'white':
                        part.fill = 'black'
        for switch in activated_switch:
            for part in switch:
                if part.fill == 'black':
                    part.fill = gradient('seaGreen','darkGreen',start='top')
    if app.selection_m == True:
        instructions_2.visible = False
        instructions_3.visible = False
        instructions_4.visible = True
        instructions_5.visible = True
        instructions_6.visible = True
        instructions_7.visible = True
        for element in drawn_elements:
            try:
                if element.selected == False:
                    pass
                if element.selected == True:
                    pass
            except AttributeError:
                element.selected = False
        if app.element_selected == True:
            # Updating UI around selected object
            app.selection_box.top = selected_element[-1].top
            app.selection_box.left = selected_element[-1].left
            app.selection_box.width = selected_element[-1].width
            app.selection_box.height = selected_element[-1].height
            if app.rotate_m == True:
                create_rotate_ui(selected_element[-1])
                for ui in app.rotateUI:
                    ui.value = str(selected_element[-1].rotateAngle)+' Degrees'
                    ui.visible = True
            else:
                for ui in app.rotateUI:
                    ui.visible = False
            if app.scale_m == True:
                create_scale_ui(selected_element[-1])
                for ui in app.scaleUI:
                    ui.visible = True
            else:
                for ui in app.scaleUI:
                    ui.visible = False
            if app.move_m == True:
                create_move_ui(selected_element[-1])
                for ui in app.moveUI:
                    ui.visible = True
            else:
                for ui in app.moveUI:
                    ui.visible = False
            if app.animation_filp == 1:
                if app.selection_box.opacity > 100:
                    app.selection_box.opacity += -4*(app.animation_filp)
                elif app.selection_box.opacity > 50:
                    app.selection_box.opacity += -2*(app.animation_filp)
                elif app.selection_box.opacity > 0:
                    app.selection_box.opacity += -1*(app.animation_filp)
                elif app.selection_box.opacity == 0:
                    app.animation_filp = -1    
            elif app.animation_filp == -1:
                if app.selection_box.opacity < 100:
                    app.selection_box.opacity += -4*(app.animation_filp)
                elif app.selection_box.opacity < 50:
                    app.selection_box.opacity += -2*(app.animation_filp)
                elif app.selection_box.opacity < 0:
                    app.selection_box.opacity += -1*(app.animation_filp)
                elif app.selection_box.opacity == 100:
                    app.animation_filp = 1
        for switch in selection_switches:
            if (switch in activated_switch) == False:
                for part in switch:
                    if part.fill != 'black' and part.fill != 'white':
                        part.fill = 'black'
        for switch in activated_switch:
            for part in switch:
                if part.fill == 'black':
                    part.fill = gradient('seaGreen','darkGreen',start='top')
    else:
        for ui in app.rotateUI:
            ui.visible = False
check_drawing()
check_selection()
# like bro i was under 360 but i had to add in the QOL stuff so that brought it up this high ;-;

cmu_graphics.run()