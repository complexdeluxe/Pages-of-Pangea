from cmu_graphics import *

import random
stage_colors_1 = ['royalBlue','lightCoral','paleGreen','darkCyan','slateBLue',
'deepPink','mediumPurple','darkRed','cornSilk','darkGreen']
stage_colors_2 = ['cadetBlue','crimson','khaki','violet','tomato','peru',
'lightSkyBlue','bisque','oldLace','maroon']
app.stage_index = 0
#Main Song Source | https://audio.com/ruan-legal-1/audio/dimrain47-20-every-end
# Audio Compresser || https://www.xconvert.com/audio-compressor
song = Sound('Dimrain47+-+(20)+Every+End....mp3')

# All Sound Effect Sources:
# DW Wipe || https://www.myinstants.com/en/instant/sirxrix-76980/
# GTA5 Bus/Wasted || https://quicksounds.com/sound/90/gta-v-wasted-bus ted 
# JoJo ASR Retired || (shown below)
# https://www.myinstants.com/en/instant/retired-all-star-battle-51059/
# GD Death || (shown below)
# https://audio.com/otis-sampson/audio/geometry-dash-death-sound-effect
# UT Shatter || https://www.myinstants.com/en/instant/undertale-soul-shatter/
# MC Death || https://orangefreesounds.com/minecraft-death-sound
death_sounds = [Sound('Deepwoken Wipe.mp3'),
    Sound('GTA V Wasted Busted - QuickSounds.com.mp3'),
    Sound('retired-sfxasb.mp3'),
    Sound('geometry-dash-death-sound-effect.mp3'),
    Sound('undertale-soul-shatter.mp3'),
    Sound('Minecraft-death-sound.mp3')]
app.map_objects = Group()
world_border = Rect(0,0,400,400) 
player_afterimages = Group()
player = Rect(200,200,20,20,fill='Skyblue',border='dodgerBlue')
world_roof = Rect(-5,-75,410,105,border='dimGray')
world_floor = Rect(-5,370,410,105,border='dimGray')
app.score_label = Label('XXXX',160,15,fill='white', 
size=18,font='orbitron')
time_label = Label('0:00',240,15,fill='white',
size=18,font='orbitron')
stage_label = Label('Stage: ',185,385,fill='white',
size=18,font='orbitron')
stage_count = Label('1',230,385,fill='white',
size=18,font='orbitron',border='black',borderWidth=0)
player.moving_left = False
player.moving_right = False 
player.jump_height = 70
player.jump_des = 0
player.Jumping = False
player.endgame = False 
player.movement_speed = 5
player.alive = True
app.minutes = 0
app.real_seconds = 0
app.seconds = 0 
app.score = 0
cheated_completion = Label('Invicibility was used for this Completion',200,
360,fill='white',font='orbitron',italic=True,opacity=40,visible=False)
app.frames = 0
app.i_frames = 10
app.og_iframes = app.i_frames 
app.i_frames_active = False
app.stage = 1
app.gravity = 4
app.og_grav = app.gravity
app.ob_gap = 100
app.ob_d_gap = 0
app.ob_limit = 6
instructions = Group(
    Label('Press |A| and |D| to move left and right',75,385),
    Label('Press |S| in the air to fall down faster',315,385),
    Label('Press |Space| to jump into the air',65,15),
    Label('Press |W| to dash either left or right',330,15),)
instructions.fill='white'
for script in instructions:
    script.size = 7.5
    script.bold = True
    script.italic = True
UI = Group(instructions,time_label,stage_label,stage_count)
server_message = Label('Dodge Obstacles Until the End...',200,200,
fill='white',size=18,font='orbitron')

def up_stage_label(size_num,border):
    stage_count.border = border
    stage_count.size += size_num
    
def create_server_message(text):
    server_message.value = text
    server_message.opacity = 100
    
def change_color(fill,border):
    player.fill=fill
    player.border=border
    
def move_obstacles():
    for item in app.map_objects:
        if item.right >= world_border.left: 
            item.centerX -= item.speed
        if item.right < world_border.left: 
            app.map_objects.remove(item)
            
def generate_obstacle(): 
    rng_ob = random.randint(1,3) 
    rng_speed = random.randint((app.stage+1),(app.stage+4)) 
    distance = [500,600,700,800] 
    if rng_ob==1:
        obstacle = Rect(distance[app.ob_d_gap],200,45+(2.5*app.stage),
        200+((app.ob_gap*.75)+(1*app.stage)),border='white')
        obstacle.bottom = 400 
    if rng_ob == 2:
        obstacle = Rect(distance[app.ob_d_gap],0,45+(2.5*app.stage),
        200+((app.ob_gap*.75)+(1*app.stage)),border='white')
        obstacle.top = 0 
    if rng_ob == 3:
        obstacle = Group(
            Rect(distance[app.ob_d_gap],200+(app.ob_gap-7*app.stage),
            45+(5*app.stage),200,border='white'),
            Rect(distance[app.ob_d_gap],0-(app.ob_gap-7*app.stage),
            45+(5*app.stage),200,border='white'))
    app.ob_d_gap += 1 
    if app.ob_d_gap > 3:
        app.ob_d_gap = 0 
    obstacle.speed = rng_speed
    app.map_objects.add(obstacle)
    
def death():
    change_color('salmon','fireBrick')
    player.alive = False
    
def dash(length,item):
    item.centerX += length
    for i in range(6):
        image = Rect(item.left-((length/6)*i),
        item.top,item.width/1.5,item.height/1.5,opacity=90-(10*i))
        image.centerY = item.centerY
        if player.endgame == True:
            image.fill = gradient('aquamarine','cyan')
            image.rotateAngle = random.randint(0,360)
        player_afterimages.add(image)
    app.i_frames_active = True
    
def onKeyPress(key):
    if player.alive == True:
        if key == 'space':
            player.centerY -= 10
            player.Jumping = True
            player.jump_des = player.centerY-player.jump_height
        if key == 'w' or key == 'W':
            if player.moving_right == True: 
                dash(85,player)
            if player.moving_left == True:
                dash(-85,player)
                
def onKeyHold(keys):
    if player.alive == True:
        if ('A' in keys or 'a' in keys):
            for i in range(player.movement_speed):
                player.centerX -= 1
            player.moving_left = True
            player.moving_right = False
        if ('D' in keys or 'd' in keys):
            for i in range(player.movement_speed):
                player.centerX += 1
            player.moving_right = True
            player.moving_left = False
        if ('D' in keys or 'd' in keys) and ('A' in keys or 'a' in keys):
            player.moving_right = False
            player.moving_left = False
        if ('S' in keys or 's' in keys):
            app.gravity = app.og_grav*2
            player.Jumping = False
            change_color('dimGray','gainsboro')
        else:
            app.gravity = app.og_grav
            change_color('skyBlue','dodgerBlue')
        if app.real_seconds < 5 and ('|' in keys) and ('~' in keys):
            try:
                cheat_code = app.getTextInput('%*(@!&%)(!*&!@)(*&SH{{}~F~HA')
                if cheat_code == 'The Author of the Continental Page':
                    app.i_frames = 869251968158709
                    app.i_frames_active = True
                    cheated_completion.visible = True
                else:
                    create_server_message('The End You Seek... ')
                    death()
            except:
                create_server_message('The End You Seek... ')
                death()
            
def onStep():
    app.frames += 1 
    
    if(app.frames % 2) == 0:
        if server_message.opacity > 0:
            server_message.opacity -= 1
        if world_border.opacity > 0 and app.minutes < 1:
            world_border.opacity -= 1
        elif app.minutes == 7 and app.seconds > 19 and world_border.opacity < 100:
            world_border.opacity += 1
            app.score_label.value = 'Victory is Yours'
            app.score_label.size = 7.5
    if player.alive == True:
        if (app.frames % 5) == 0:
            app.score += 1 
            if app.score_label.value != 'Victory is Yours':
                app.score_label.value = app.score
        if (app.frames % 30) == 0:
            app.seconds += 1
            app.real_seconds += 1
            if app.seconds < 10:
                time_label.value = str(app.minutes)+':0'+str(app.seconds)
            else:
                time_label.value = str(app.minutes)+':'+str(app.seconds)
            if app.real_seconds % 40 == 0 and app.stage < 5:
                app.stage += 1 
                app.stage_index += 1
                up_stage_label(0,'darkGoldenrod')
                create_server_message('Obstacle Size and Speed Increased!')
                stage_count.borderWidth = 1
            if app.real_seconds % 40 == 0 and app.stage > 3 and app.stage <= 5:
                up_stage_label(0,'gainsboro')
            if app.real_seconds % 50 == 0 and app.stage < 10 and app.stage >= 5:
                app.stage += 1
                app.stage_index += 1
            if app.stage == 6 and stage_count.border != 'gold':
                up_stage_label(1,'gold') 
            if app.stage == 8 and stage_count.border != 'lightCyan':
                if player.endgame == False:
                    create_server_message('The End draws near...')
                    player.endgame = True 
                    app.og_iframes += 5
                up_stage_label(1,'lightCyan')
            if app.stage == 10 and stage_count.border != 'limeGreen':
                stage_count.fill = 'black' 
                up_stage_label(1,'limeGreen')
            stage_count.value = str(app.stage)
            if (app.real_seconds % 60) == 0:
                app.minutes += 1
                app.seconds = 0
        if player.top < world_roof.bottom:
            player.top = world_roof.bottom
            player.Jumping = False
        if player.bottom < world_floor.top:
            for i in range(app.gravity):
                player.centerY += 1
        if player.Jumping == True:
            change_color('limeGreen','chartreuse')
            if player.centerY  >= player.jump_des:
                player.centerY -= player.jump_height/6
            else:
                player.Jumping = False
                change_color('skyBlue','dodgerBlue')
        for image in player_afterimages:
            if image.opacity > 0:
                image.opacity -= 10
            else:
                player_afterimages.remove(image)
        if app.i_frames_active == True:
            player.border = 'azure'
            app.i_frames -= 1
            if app.i_frames == 0:
                app.i_frames = app.og_iframes
                app.i_frames_active = False
                player.border = 'dodgerBlue'
        if app.score_label.value != 'Victory is Yours':
            player.movement_speed = app.stage+5
            move_obstacles()
            if len(app.map_objects) < app.ob_limit and app.real_seconds > 5:
                generate_obstacle() 
        else:
            app.map_objects.clear()
            if world_border.opacity == 100:
                death()
        app.background = gradient('black',stage_colors_1[app.stage_index],
        stage_colors_2[app.stage_index],'black',start='top')        
        if player.hitsShape(app.map_objects) or world_border.hitsShape(player) != True:
            if app.i_frames_active == False:
                death()
    
    else:
        if song.isPlaying == True:
            song.pause()
            death_sound = random.choice(death_sounds)
            if app.score_label.value != 'Victory is Yours':    
                death_sound.play()
            song.isPlaying = False
        if (app.frames % 2) == 0:
            if player.opacity > 0:    
                player.opacity -= 1
            else:
                app.stop()
            if UI.opacity > 0:
                UI.opacity -= 2
            world_roof.centerY -= .35
            world_floor.centerY += .35
            app.score_label.centerX = 200
            app.score_label.centerY = 200
            app.score_label.size = 28
song.isPlaying = True
song.play()
cmu_graphics.run()