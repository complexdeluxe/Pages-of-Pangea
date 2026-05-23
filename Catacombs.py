from cmu_graphics import *

# She cata til i comb
background = Rect(0,0,400,400,fill='skyBlue',opacity=30)
def toggle(value):
    value = not value
    return value

def onMousePress(mouseX,mouseY):
    pass

def onMouseRelease(mouseX,mouseY):
    pass

def onMouseMove(mouseX,mouseY):
    pass

def onMouseDrag(mouseX,mouseY):
    pass

def onKeyPress(key):
    pass

def onKeyRelease(key):
    pass

def onKeyHold(keys, modifiers):
    
    if player.can_move == True:
        
        if ('w' in keys or 'W' in keys) and player.can_move_foward == True: #Foward
            for i in range(player.movement_speed):
                if ('w' in keys or 'W' in keys) and player.can_move_foward == True:
                    player.centerY += -1
                    shift_pod(app.current_pod, 'down', player.movement_speed)
                    
                for item in app.collidable_map_objects:
                    check_collision(item)
            
            if player.moving == False:
                player.moving = True
            
            if player.sprinting == False:
                player.walking = True
                
        if ('s' in keys or 'S' in keys) and player.can_move_backward == True: #Backward
            
            for i in range(player.movement_speed):
                if('s' in keys or 'S' in keys) and player.can_move_backward == True:
                    player.centerY += +1
                    shift_pod(app.current_pod, 'up', player.movement_speed)
                
                for item in app.collidable_map_objects:
                    check_collision(item)
            
            if player.moving == False:
                player.moving = True
            
            if player.sprinting == False:
                player.walking = True
                
        if ('a' in keys or 'A' in keys) and player.can_move_left == True: #Left
            
            for i in range(player.movement_speed):
                if ('a' in keys or 'A' in keys) and player.can_move_left == True:
                    player.centerX += -1
                    shift_pod(app.current_pod, 'right', player.movement_speed)
                    
                for item in app.collidable_map_objects:
                    check_collision(item)
            
            if player.moving == False:
                player.moving = True
            
            if player.sprinting == False:
                player.walking = True
                    
        if ('d' in keys or 'D' in keys) and player.can_move_right == True: #Right
            
            for i in range(player.movement_speed):
                if ('d' in keys or 'D' in keys) and player.can_move_right == True:
                    player.centerX += 1
                    shift_pod(app.current_pod, 'left', player.movement_speed)
                
                for item in app.collidable_map_objects:
                        check_collision(item)
            
            if player.moving == False:
                player.moving = True
            
            if player.sprinting == False:
                player.walking = True
    else:
        if player.moving == True:
            player.moving = False
        
        if player.walking == True:
            player.walking = False
        
        if player.sprinting == True:
            player.sprinting = False
            
    if 'shift' in modifiers and player.sprinting == False and player.walking == True and Stamina.stam_amount > 0 and player.can_sprint == True:
        player.movement_speed = player.movement_speed * player.sprint_multiplier
        player.walking = False
        player.sprinting = True
    
    elif ('shift' in modifiers) == False and player.sprinting == True and player.walking == False:
        player.movement_speed = player.original_movement_speed
        player.walking = True
        player.sprinting = False
        
    elif player.can_sprint == False:
        player.movement_speed = player.original_movement_speed
        player.walking = True
        player.sprinting = False
# ^^^^^^^^^^^^^^^^^^^
'''
IMPORTANT NOTE: Key event handlers can also take an extra argument,
modifiers, which allows them to use a list of modifier keys that could
be held at that moment, this includs: 'ctrl', 'shift', and 'meta'.
While 'alt' and 'option' arent supported this still gives us extra options
EXAMPLE:
    onKeyPress(key, modifiers):
    print(key) -> could be h, H
    print(modifiers) ^ [], ['shift']
EXTRA NOTE: Mouse event handlers can also do somewhat the same as keys,
they use the extra argument button, allowing them to see which mouse button
was actually pressed and in specific 'onMouseDrag' can take buttons
to see all the ones that are held down when draged. this consist of 0, 1, and 2
representing the Left button, Auxiliary buttom i.e. the mouse wheel or middle button
and the Right Button.
'''
def onStep():
    find_current_pod(twisted_garden_upper_yard)
    
    # [-----------------] 
    # Health set up and time stuff
    app.step_count += 1
    if app.step_count % 30 == 0:
        app.second += 1
        app.step_count = 0
        if app.second % 60 == 0:
            app.minute += 1
            app.second = 0
    
    # [------ Health ------]
    
    if (Health.hp_amount*app.ui_scale) <= 0:
        main_h_bar.visible = False
    else:
        main_h_bar.width = Health.hp_amount*app.ui_scale
        
    if app.step_count % 30 == 0 and Health.hp_amount < player.health_value:
        Health.hp_amount += player.health_regen 
        if Health.hp_amount*app.ui_scale >= h_bar_border.left:
            main_h_bar.left = h_bar_border.left  
       
    if main_h_bar.right != h_bar_border.right:
        main_h_bar.right = h_bar_border.right
        
    if main_h_bar.right == h_bar_border.right and main_h_bar.left < h_bar_border.left:
        main_h_bar.left = h_bar_border.left
    
    health_display.value = str(int(Health.hp_amount))+"/"+str(player.health_value)
    
    if main_h_bar.width > h_bar_border.width:
        main_h_bar.width = h_bar_border.width
    

    # [------ Stamina ------]
    if (Stamina.stam_amount*app.ui_scale) <= 0:
        main_s_bar.visible = False
    else:
        main_s_bar.visible = True
        main_s_bar.width = Stamina.stam_amount*app.ui_scale
        
    if app.step_count % 30 == 0 and Stamina.stam_amount < player.stamina_value:
        Stamina.stam_amount += player.stamina_regen*(player.Mobility)
        if Stamina.stam_amount*app.ui_scale >= s_bar_border.left:
            main_s_bar.left = s_bar_border.left  
       
    if main_s_bar.right != s_bar_border.right:
        main_s_bar.right = s_bar_border.right
        
    if main_s_bar.right == s_bar_border.right and main_s_bar.left < s_bar_border.left:
        main_s_bar.left = s_bar_border.left
    
    stamina_display.value = str(int(Stamina.stam_amount))+"/"+str(player.stamina_value)
    
    if main_s_bar.width > s_bar_border.width:
        main_s_bar.width = s_bar_border.width
        
    if Stamina.stam_amount > 0:
        player.can_sprint = True
    
    # [-----------------]
    
    if player.sprinting == True:
        Stamina.stam_amount -= (player.stamina_regen/10)
        if Stamina.stam_amount <= 0:
            player.sprinting = False
            player.can_sprint = False
    
    if player.iframes_activated == True:
        player.Iframes -= 1
        if player.Iframes <= 0:
            player.iframes_activated = False
            player.Iframes += app.og_frames
        
    if Health.hp_amount <= 0: # Death
        app.stop() # will change when death can function correctly
        
    # [-----------------]
    '''
    if player.moving == True:
        if player.position != (player.centerX, player.centerY):
            cell_1.centerX = 400 - player.centerX
            cell_1.centerY = 400 - player.centerY
            player.position = (player.centerX, player.centerY)
    '''
    # [-----------------] 
    if player.hitsShape(kill_brick):
        player_damage(20,['normal','can crit'],7)
        
    if player.hitsShape(heal_brick):
        player_healing(20,['normal','can crit'],7)
     
    if player.hitsShape(stam_brick):
        player_healing(20,['stamina','can crit'],7)
    # [-----------------] 
    animate_floating_value()
    animate_floating_text()
    
def player_damage(damage,types,accuracy):
    if player.iframes_activated == False:
        if 'normal' in types:
            if randrange(1,10) <= accuracy:
                Health.hp_amount -= damage - (damage * player.damage_reduction)
            
                print_floating_value(damage,['damage'])
            
                if 'can crit' in types:
                    if randrange(1,5) == 1:
                        Health.hp_amount -= damage - (damage * player.damage_reduction)
                        print_floating_text('CRITICAL!',['critical'])
                        
                player.iframes_activated = True
            else:
                player.Iframes -= 5
                print_floating_text('miss',['evade'])
                
                player.iframes_activated = True # <- should be not the same level
                # of iframes as a normal attack.
            
def player_healing(heal,types,accuracy):
    if 'normal' in types:
        if player.iframes_activated == False:
            if randrange(1,10) <= accuracy:
                if Health.hp_amount < player.health_value:
                    Health.hp_amount += heal
            
                    print_floating_value(heal,['healing'])
                    
                    if 'can crit' in types and Health.hp_amount < player.health_value:
                        if randrange(1,5) == 1:
                            Health.hp_amount += heal
                            print_floating_text('SUPERB!',['critical'])
            
                    player.iframes_activated = True
                    
            else:
                print_floating_text('failed',['evade'])
                
                player.iframes_activated = True # <- should be not the same level
                # of iframes as a normal attack.
         
    if 'stamina' in types:
        if player.iframes_activated == False:
            if randrange(1,10) <= accuracy:
                if Stamina.stam_amount < player.stamina_value:
                    Stamina.stam_amount += heal
            
                    print_floating_value(heal,['stamina boost'])
                    
                    if 'can crit' in types and Stamina.stam_amount < player.stamina_value:
                        if randrange(1,10) == 1:
                            Stamina.stam_amount = player.stamina_value
                            print_floating_text('REPLENISHED!',['critical'])
            
                    player.iframes_activated = True
                    
            else:
                print_floating_text('failed',['evade'])
                
                player.iframes_activated = True # <- should be not the same level
                # of iframes as a normal attack.
        

def player_debuff(debuffs):
    pass

def player_buff(buffs):
    pass

def print_floating_value(number,types):
    has_printed_value = False
    
    if 'damage' in types:
        new_number = Label('-'+str(number),player.centerX,player.centerY,fill='crimson')
        has_printed_value = True

    if 'healing' in types:
        new_number = Label('+'+str(number),player.centerX,player.centerY,fill='springGreen')
        has_printed_value = True
        
    if 'stamina boost' in types:
        new_number = Label('+'+str(number),player.centerX,player.centerY,fill='cornFlowerBlue')
        has_printed_value = True
        
    if has_printed_value == False:
        new_number = Label('N/A',player.centerX,player.centerY)
      
    new_number.og_x = new_number.centerX
    new_number.og_y = new_number.centerY
    
    if randrange(1,3) == 1:
        new_number.random_x = randrange(-20,-6)
    else:
        new_number.random_x = randrange(6,20)
        
    printed_value.add(new_number)


def animate_floating_value():
    for text in printed_value: # 100

        if text.random_x < 0:
            if text.og_x + text.random_x // 2 <= text.centerX:
                text.centerX -= 1
                text.centerY -= 3
            else:
                text.centerX -= 1
                text.centerY += 3
        else:
            if text.og_x + text.random_x // 2 >= text.centerX:
                text.centerX += 1
                text.centerY -= 3
            else:
                text.centerX += 1
                text.centerY += 3
            
        text.opacity -= 5 # last for 20 frames
        
        if text.opacity <= 0:
            printed_value.remove(text)

def print_floating_text(text,types):
    has_printed_text = False
    
    if 'critical' in types:
        new_text = Label(str(text),player.centerX,player.centerY,fill='coral',size=14)
        new_text.rotateAngle = 7
        has_printed_text = True
    
    if 'evade' in types:
        new_text = Label(str(text),player.centerX,player.centerY,fill='midnightBlue',size=14)
        new_text.rotateAngle = 7
        has_printed_text = True
    
    if has_printed_text == False:
        new_text = Label('nothing',player.centerX,player.centerY)
        
    printed_text.add(new_text)
    
def animate_floating_text():
    for text in printed_text:
        text.opacity -= 2.5 # last for 40 frames
        text.rotateAngle -= .1875
        text.centerY -= 1 
        if text.size > 6:
            text.size -= .1
        if text.opacity <= 0:
            printed_text.remove(text)

    '''
    if player.moving == True:
        if player.position != (player.centerX, player.centerY):
            cell_1.centerX = 400 - player.centerX
            cell_1.centerY = 400 - player.centerY
            player.position = (player.centerX, player.centerY)
    '''
    '''
    GAME PLAN: The pods should be shifting relative to the direction
    the player is currently moving, before shifting it should check 
    where the pod is currently at on the map by looking at its centerX and Y
    the function itself should check which pod is shifting and what
    direction it should be going in + how much it should be moving in that direction
    how to fix collisions? make it so the map only shifts in certain directions when the
    player can actually move in that direction, so can move left means map can move left
    how to make borders work? borders will be 4 rectangles that are 10 pixels
    thick and 2 1200 pixels wide and 2 1180 pixels wide with the shorter ones being
    left and right. 
    '''
    
def shift_pod(pod, direction, shift):
    if direction == 'down':
        if (pod.centerY + shift) <= 600:
            for i in range(shift):
                for item in app.collidable_map_objects:
                    check_collision(item)
                    
                if player.can_move_foward == True:
                    pod.centerY += 1
                
            
    if direction == 'up':
        if (pod.centerY - shift) >= -200:
            for i in range(shift):
                for item in app.collidable_map_objects:
                    check_collision(item)
                    
                if player.can_move_backward == True:
                    pod.centerY -= 1
            
    if direction == 'right':
        if (pod.centerX + shift) <= 600:
            for i in range(shift):
                for item in app.collidable_map_objects:
                    check_collision(item)
                    
                if player.can_move_left == True:
                    pod.centerX += 1
            
    if direction == 'left':
        if (pod.centerX - shift) >= -200:
            for i in range(shift):
                for item in app.collidable_map_objects:
                    check_collision(item)
                    
                if player.can_move_right == True:
                    pod.centerX -= 1

def find_current_pod(chosen_map):
    for pod in chosen_map:
        if pod.containsShape(player):
            app.current_pod = pod
    
def check_collision(item):
    '''
    if player.hitsShape(item):
        print('YOU HIT THE PLAYER')
    else:
        print('YOU AINT HITTIN THE PLAYER')
    '''
    # -- Foward Collision --
    if player.hitsShape(item) and player.top == item.bottom:
        if item.can_collide == True:
            player.can_move_foward = False
            if (item in app.objects_in_contact) == False:
                app.objects_in_contact.append(item)
    
    # -- Backward Collision --
    if player.hitsShape(item) and player.bottom == item.top:
        if item.can_collide == True:
            player.can_move_backward = False
            if (item in app.objects_in_contact) == False:
                app.objects_in_contact.append(item)

    # -- Right Collision --
    if player.hitsShape(item) and player.right == item.left:
        if item.can_collide == True:
            player.can_move_right = False
            if (item in app.objects_in_contact) == False:
                app.objects_in_contact.append(item)
        
    # -- Left Collision --
    if player.hitsShape(item) and player.left == item.right:
        if item.can_collide == True:
            player.can_move_left = False
            if (item in app.objects_in_contact) == False:
                app.objects_in_contact.append(item)
    
    if item in app.objects_in_contact and player.hitsShape(item) == False:
        if player.can_move_foward == False:
            player.can_move_foward = True
            
        if player.can_move_backward == False:
            player.can_move_backward = True
        
        if player.can_move_right == False:
            player.can_move_right = True
            
        if player.can_move_left == False:
            player.can_move_left = True
            
        app.objects_in_contact.remove(item)

    '''
    print('ALL THE OBJECTS IN CONTACT')
    print(app.objects_in_contact)
    '''
# - Player Set Up -

player = Group()
player.add(Rect(180,180,16,16,fill='purple'))

player.centerX = 200
player.centerY = 200
player.position = (player.centerX, player.centerY)

player.can_move = True
player.moving = False
player.walking = False
player.sprinting = False

player.can_move_foward = True
player.can_move_backward = True
player.can_move_left = True
player.can_move_right = True

player.can_sprint = True
player.iframes_activated = False


# -- Buliding Set-Up & Structures --
app.current_pod = 'None'
app.collidable_map_objects = []
app.objects_in_contact = []

twisted_garden_upper_yard = []
uy_pod_1 = Group()
uy_pod_1_top_border = Rect(-400,-400,1200,10,fill=None,border='black',borderWidth=1)
app.collidable_map_objects.append(uy_pod_1_top_border)
uy_pod_1_bottom_border = Rect(-400,790,1200,10,fill=None,border='black',borderWidth=1)
app.collidable_map_objects.append(uy_pod_1_bottom_border)
uy_pod_1_left_border = Rect(-400,-400,10,1200,fill=None,border='black',borderWidth=1)
app.collidable_map_objects.append(uy_pod_1_left_border)
uy_pod_1_right_border = Rect(790,-400,10,1200,fill=None,border='black',borderWidth=1)
app.collidable_map_objects.append(uy_pod_1_right_border)
uy_pod_1_ground = Rect(-400,-400,1200,1200,fill=gradient('black','slateGray',start='center'),opacity=30)

uy_pod_1.add(uy_pod_1_top_border)
uy_pod_1.add(uy_pod_1_bottom_border)
uy_pod_1.add(uy_pod_1_left_border)
uy_pod_1.add(uy_pod_1_right_border)
uy_pod_1.add(uy_pod_1_ground)

uy_pod_1_cell_1 = Group()

wall1 = Rect(330,20,30,360,fill='grey')
app.collidable_map_objects.append(wall1)

wall2 = Rect(40,20,30,360)
app.collidable_map_objects.append(wall2)

wall3 = Rect(180,240,30,80,fill='lightSlateGray')
app.collidable_map_objects.append(wall3)

wall4 = Rect(120,360,160,20,fill='gainsboro')
app.collidable_map_objects.append(wall4)

kill_brick = Rect(120,120,30,80,fill='fireBrick',border='black',borderWidth=1)
app.collidable_map_objects.append(kill_brick)

heal_brick = Rect(250,120,30,80,fill='seaGreen',border='black',borderWidth=1)
app.collidable_map_objects.append(heal_brick)

stam_brick = Rect(120,70,160,30,fill='deepSkyBlue',border='black',borderWidth=1)
app.collidable_map_objects.append(stam_brick)

for item in app.collidable_map_objects:
    item.can_collide = True

uy_pod_1_cell_1.add(wall1)
uy_pod_1_cell_1.add(wall2)
uy_pod_1_cell_1.add(wall3)
uy_pod_1_cell_1.add(wall4)
uy_pod_1_cell_1.add(kill_brick)
uy_pod_1_cell_1.add(heal_brick)
uy_pod_1_cell_1.add(stam_brick)

uy_pod_1.add(uy_pod_1_cell_1)
twisted_garden_upper_yard.append(uy_pod_1)

# -- Player Statistics

player.Iframes = 15

player.Accuracy = 1 # Increases your chance to land attacks

player.armor_penetration = 1 # Greater chance to pierece through armor

player.Defense = 1 # Boost damage reduction

player.Durability = 5 # Impacts raw health

player.Endurance = 3 # Impacts raw stamina and slight damage reduction

player.Mobility = 2 # Slight increases stamina regen, boost movement & sprint

player.Strength = 1 # Boost Physical Attacks

player.Spirit = 0 # Grants access to the spiritual arts, boosting their 
# affectiveness and power whilst also keeping your spirit more full.
# and be more resistant to spirital attacks.

# Health

health_stats = [70,100,130,180,300,9999]
health_regen_stats = [1,2,3,5,12,999]

player.health_value = health_stats[player.Durability-1]
player.health_regen = health_regen_stats[player.Durability-1]

# Stamina
player.stamina_value = (95*player.Endurance) + (5*player.Mobility)
player.stamina_regen = 1 + (.25*player.Mobility)

# Movement Speed & Sprint
player.movement_speed = 1 # <- this is how many pixels you move in one step
player.original_movement_speed = player.movement_speed
player.sprint_multiplier = 2

# Damage Reduction
damage_reduction_stats = [0,0,.05,.1,.2,0]
player.damage_reduction = damage_reduction_stats[player.Durability-1]

# Former Statsaves
app.og_dura = player.Durability
app.og_frames = player.Iframes

# -- UI -- 
app.ui_scale = 2

# ~ Health ~
Health = Group()
Health.hp_amount = player.health_value

health_x = 100
health_y = 10

health_width = 200
health_height = 15

h_bar_gap = 40
h_bar_tilt = 1.5

under_h_bar = Rect(health_x,health_y,health_width,health_height,fill=gradient('crimson','crimson','white',start='top'))
Health.add(under_h_bar)

main_h_bar = Rect(health_x,health_y,health_width,health_height,fill=gradient('forestGreen','forestGreen','black',start='top'))
Health.add(main_h_bar)

h_bar_border = Rect(health_x,health_y,health_width,health_height,fill=None,border='dimGray',borderWidth=1+(.5*app.ui_scale))
Health.add(h_bar_border)

h_bar_separators = Group()

for i in range(0,4):
    # print(i)
    if i == 0 or i == 1:
        h_mini_bar = Line((health_x+(h_bar_gap-h_bar_tilt))+(h_bar_gap*i),Health.bottom,(health_x+(h_bar_gap+h_bar_tilt))+(h_bar_gap*i),Health.top,lineWidth=2,fill='dimGray')
        h_bar_separators.add(h_mini_bar)
        
    if i == 2 or i == 3:
        h_mini_bar = Line((health_x+(h_bar_gap+h_bar_tilt))+(h_bar_gap*i),Health.bottom,(health_x+(h_bar_gap-h_bar_tilt))+(h_bar_gap*i),Health.top,lineWidth=2,fill='dimGray')
        h_bar_separators.add(h_mini_bar)
        
health_display = Label(str(Health.hp_amount)+"/"+str(player.health_value),Health.centerX,Health.centerY,fill='white',size=5*app.ui_scale,font='montserrat',italic=True,bold=True)    

Health.add(h_bar_separators)
Health.add(h_bar_border)
Health.add(health_display)

# ~ Stamina ~
Stamina = Group()
Stamina.stam_amount = player.stamina_value

stamina_x = 100
stamina_y = 30

stamina_width = 200
stamina_height = 15

s_bar_gap = 40
s_bar_tilt = 1.5

under_s_bar = Rect(stamina_x,stamina_y,stamina_width,stamina_height,fill=gradient('slateGray','slateGray','black',start='top'))
Stamina.add(under_s_bar)

main_s_bar = Rect(stamina_x,stamina_y,stamina_width,stamina_height,fill=gradient('dodgerBlue','dodgerBlue','skyBlue',start='top'))
Stamina.add(main_s_bar)

s_bar_border = Rect(stamina_x,stamina_y,stamina_width,stamina_height,fill=None,border='dimGray',borderWidth=1+(.5*app.ui_scale))
Stamina.add(s_bar_border)

s_bar_separators = Group()

for i in range(0,4):
    # print(i)
    if i == 0 or i == 1:
        s_mini_bar = Line((stamina_x+(s_bar_gap-s_bar_tilt))+(s_bar_gap*i),Stamina.bottom,(stamina_x+(s_bar_gap+s_bar_tilt))+(s_bar_gap*i),Stamina.top,fill='dimGray',lineWidth=2)
        s_bar_separators.add(s_mini_bar)
        
    if i == 2 or i == 3:
        s_mini_bar = Line((stamina_x+(s_bar_gap+s_bar_tilt))+(s_bar_gap*i),Stamina.bottom,(stamina_x+(s_bar_gap-s_bar_tilt))+(s_bar_gap*i),Stamina.top,fill='dimGray',lineWidth=2)
        s_bar_separators.add(s_mini_bar)
        
stamina_display = Label(str(Stamina.stam_amount)+"/"+str(Stamina.stam_amount),Stamina.centerX,Stamina.centerY,fill='white',size=5*app.ui_scale,font='montserrat',italic=True,bold=True)    

Stamina.add(s_bar_separators)
Stamina.add(s_bar_border)
Stamina.add(stamina_display)


# [-----------]

printed_value = Group()
printed_text = Group()

app.step_count = 0
app.second = 0
app.minute = 0
app.score = 0

app.stepsPerSecond = 30

cmu_graphics.run()