from cmu_graphics import *

# Take Flight! | Alpha | Version 2.1
# Version 2.2 -> Gun Heat, Extra Obstaciles, Damage, Title Screen
# ^ Potential 2.2 Addons, Day/Night Cycle? Real Plane Model?
import random
import time
flight_mode = True
def generate_tree():
    
    if app.tree_gen_count >= 3:
        app.tree_gen_count = 0
        
    if app.tree_count < 2:
        
        app.tree_limit = False
        
        chosen_tree = tree_list[app.tree_gen_count]
        chosen_tree.distance = randrange(5, 10)
        chosen_tree.height = 110+randrange(-5,28) 
        chosen_tree.width = 40+randrange(-3,6)
        if randrange(1,4) == 1:
            chosen_tree.distance += 5
        chosen_tree.visible = True
        chosen_tree.centerX = randrange(500,550)
        chosen_tree.centerY = randrange(350,360)
        
        
        app.map_items.add(chosen_tree)
        app.tree_gen_count += 1
        app.tree_count += 1
        #print("A Tree has been Generated")
    else:
        app.tree_limit = True
        
def generate_cloud():
    if app.cloud_gen_count >= 4:
        app.cloud_gen_count = 0
        
    if app.cloud_count < 2:
        
        app.cloud_limit = False
      
        chosen_cloud = cloud_list[app.cloud_gen_count]
        chosen_cloud.distance = randrange(6, 18)
        if chosen_cloud.distance < 10:
            chosen_cloud.height = chosen_cloud.distance*3
            chosen_cloud.width = chosen_cloud.distance*10
            if randrange(1,4) == 1:
                chosen_cloud.distance += 5
        chosen_cloud.visible = True
        chosen_cloud.centerX += randrange(500,700)
        chosen_cloud.centerY = randrange(20,250)
        if chosen_cloud.centerY < 0:
            chosen_cloud.centerY += 20
        if chosen_cloud.centerY > 400:
            chosen_cloud.centerY -= 20
        app.map_items.add(chosen_cloud)
        app.cloud_count += 1
        app.cloud_gen_count += 1
        
        #print("A Cloud has been Generated")
    else:
        app.cloud_limit = True
        
def generate_bullet():
    bullet = Rect(Plane.centerX,Plane.centerY-5,10,5,fill = 'gold',rotateAngle = randrange(app.bloom-(app.bloom*2), app.bloom))
    Bullets.add(bullet)
    print(Bullets.children)
    return bullet
    
def clean_bullets():
    for bullet in Bullets.children:
        if bullet.centerX > 405:
            app.bullets_fired = True
            Bullets.clear()
            app.bullet_count -= 1
            print(Bullets.children)
            #print("Bullet Cleared, Count: "+str(app.bullet_count))
    app.bullets_fired = False
            
def onMousePress(mouseX,mouseY):
    if app.bullet_count >= app.bullet_limit :
        app.firing_cooldown = True
        print("[Gun Fire on Cooldown]")
        
    if app.firing_cooldown == False and app.stat_window_open == False:
        generate_bullet()
        
        app.bullet_count += 1
        
        #print("Current Bullet Count: "+str(app.bullet_count))
    
    if stat_opener_button.hits(mouseX, mouseY):
        if app.stat_window_open == False:
            flip_down_arrow.visible = True
            flip_up_arrow.visible = False
            stat_window.visible = True
            app.stat_window_open = True
        elif app.stat_window_open == True:
            flip_down_arrow.visible = False
            flip_up_arrow.visible = True
            stat_window.visible = False
            app.stat_window_open = False
    
    if stat_up_dura.hits(mouseX,mouseY):
        if app.skill_points > 0 and Plane.Durability <= 4:
            app.skill_points -= 1
            Plane.Durability += 1
    if stat_up_powr.hits(mouseX,mouseY):
        if app.skill_points > 0 and Plane.Power <= 4:
            app.skill_points -= 1
            Plane.Power += 1
    if stat_up_mobl.hits(mouseX,mouseY):
        if app.skill_points > 0 and Plane.Mobility <= 4:
            app.skill_points -= 1
            Plane.Mobility += 1
    if stat_up_prec.hits(mouseX,mouseY):
        if app.skill_points > 0 and Plane.Precision <= 4:
            app.skill_points -= 1
            Plane.Precision += 1

    if stat_down_dura.hits(mouseX,mouseY):
        if Plane.Durability >= 2:
            app.skill_points += 1
            Plane.Durability -= 1
    if stat_down_powr.hits(mouseX,mouseY):
        if Plane.Power >= 2:
            app.skill_points += 1
            Plane.Power -= 1
    if stat_down_mobl.hits(mouseX,mouseY):
        if Plane.Mobility >= 2:
            app.skill_points += 1
            Plane.Mobility -= 1
    if stat_down_prec.hits(mouseX,mouseY):
        if Plane.Precision >= 2:
            app.skill_points += 1
            Plane.Precision -= 1

def onKeyHold(keys):
    if flight_mode == True and app.stat_window_open == False:  
        # | Combo Keys |
        if "w" in keys and "s" in keys:
            Plane.centerY += randrange(-1,2)
            Plane.rotateAngle += randrange(-3,3)
            app.direction_change_cooldown = True
            Plane.changing_direction = False
        
        # | D Keys |    
        if "d" in keys and Plane.centerX <= 60: # Fly Foward
            Plane.centerX += Plane.flight_speed 
            app.d_key_pressed = True
        elif "d" in keys and Plane.centerX <= 120:
            Plane.centerX += Plane.flight_speed - Plane.drag/3
            app.d_key_pressed = True
        elif "d" in keys and Plane.centerX <= 160:
            Plane.centerX += Plane.flight_speed - Plane.drag/2
            app.d_key_pressed = True
            
        # | A Keys |    
        if "a" in keys and Plane.centerX >= 40: # Fly Backward
            Plane.centerX -= Plane.flight_speed + Plane.drag/2
            app.a_key_pressed = True
        elif "a" in keys and Plane.centerX >= 25:
            Plane.centerX -= Plane.flight_speed
            app.a_key_pressed = True
        elif "a" in keys and Plane.centerX < 25:
            Plane.centerX -= Plane.flight_speed/8
            app.a_key_pressed = True
            
        # | W Keys |    
        if "w" in keys and app.s_key_pressed == False: # Fly Upward
            if app.direction_change_cooldown == True:
                Plane.centerY -= Plane.ascent_speed/5
                
            if app.direction_change_cooldown == False:    
                app.w_key_pressed = True
            
                Plane.centerY -= Plane.ascent_speed**(Plane.acceleration)
                
                if Plane.acceleration <= 20:
                    Plane.acceleration += 1
                  
                # Plane Tilt Up
                Plane.changing_direction = True
                
                if Plane.rotateAngle <= 0 and Plane.rotateAngle >= -26:
                    Plane.rotateAngle -= 2
                if Plane.rotateAngle < -26:
                    Plane.rotateAngle -= 1
                Plane.momentum = Plane.ascent_speed**(Plane.acceleration)
        
        # | S Keys |
        if "s" in keys and app.w_key_pressed == False: # Fly Downward
            if app.direction_change_cooldown == True:
                Plane.centerY += Plane.decent_speed/5
                
            if app.direction_change_cooldown == False:
                app.s_key_pressed = True
                
                Plane.centerY += Plane.decent_speed**(Plane.acceleration)
                if Plane.acceleration <= 20:
                    Plane.acceleration += 1
                
                # Plane Tilt Down
                Plane.changing_direction = True
                
                if Plane.rotateAngle >= 0 and Plane.rotateAngle <= 26:
                    Plane.rotateAngle += 2
                if Plane.rotateAngle > 26:
                    Plane.rotateAngle += 1
                Plane.momentum = Plane.decent_speed**(Plane.acceleration)
                
        if 'S' in keys and '(' in keys and ')' in keys:
            score_promt = app.getTextInput("?")
            if score_promt == 'complexscore':
                app.score = int(app.getTextInput("Whats the New Score?"))
        if 'D' in keys and '+' in keys and 'T'in keys:
            score_promt = app.getTextInput("?")
            if score_promt == 'complexdura':
                Plane.Durability = int(app.getTextInput("Un-Cap Dura?"))
def onKeyRelease(key):
    print("You Released the ("+str(key)+") Key")
    if key == "w":
        app.w_key_pressed = False
        Plane.acceleration = 1
        Plane.changing_direction = False
    if key == "s":
        app.s_key_pressed = False
        Plane.acceleration = 1
        Plane.changing_direction = False
    if key == "a":
        app.a_key_pressed = False
    if key == "d":
        app.d_key_pressed = False

def onStep():
    # Allows time to function | Updates Score
    if app.stat_window_open == False:
        app.step_count += 1
        if app.step_count % 30 == 0:
            app.second += 1
            app.step_count = 0
            if app.second % 60 == 0:
                app.minute += 1
                app.second = 0
                
        if app.step_count % 5 == 0:
            app.score += 1 * Plane.acceleration
        
        if app.stat_point_requirement < app.score:
            app.skill_points += 1
            if app.stat_point_requirement == 200 and app.first_req == False:
                app.stat_point_requirement = 400
                app.first_req = True
            elif app.stat_point_requirement == 400 and app.second_req == False:
                app.stat_point_requirement = 750
                app.second_req = True
            elif app.stat_point_requirement == 750 and app.third_req == False:
                app.stat_point_requirement = 1000
                app.third_req = True
            elif app.stat_point_requirement == 1000 and app.fourth_req == False:
                app.stat_point_requirement = 2000
                app.fourth_req = True # <- Becomes Always True ON PURPOSE
                
        clock_shadow.value = str(app.minute)+":"+str(app.second)  
        clock.value = str(app.minute)+":"+str(app.second)
        score_counter_shadow.value = "Score | "+str(app.score)
        score_counter.value = "Score | "+str(app.score)
        # [---------------------------]
        # Checks if death, applies damage&regen to health bar, and lowered iframe count
        
        main_bar.left = 400 - Health.hp_amount*2
        if main_bar.left < 200:
            main_bar.left = 200
        health_display.value = str(int(Health.hp_amount))+"/"+str(Plane.health_value)
        
        if app.step_count % 30 == 0 and Health.hp_amount < Plane.health_value:
            Health.hp_amount += Plane.health_regen 
            if main_bar.left < 200:
                main_bar.left = 200
        if app.iframes_activated == True:
            Plane.Iframes -= 1
            if Plane.Iframes <= 0:
                app.iframes_activated = False
                Plane.Iframes += app.og_frames
            
        if Health.hp_amount <= 0: # Death
            app.stop() # will change when death can function correctly
        # [---------------------------]
        for item in app.map_items.children:
            item.centerX -= (app.map_speed*item.distance)
            if app.d_key_pressed == True:
                item.centerX -= Plane.flight_speed/2
                
            elif app.a_key_pressed == True:
                item.centerX += Plane.flight_speed/2
            
            if (world_border.containsShape(item) == False) and (item.right < world_border.left):
                app.map_items.remove(item)
                #print("Item as been cleared off the map")
                if app.cloud_limit == True and app.cloud_count > 0 and item.is_cloud == True:
                    app.cloud_count -= 1
                    #print("Cloud Count after Item Removal "+str(app.cloud_count))
                    if len(app.map_items) == 2 and app.cloud_count == 1: # Fixes one cloud spawn bug
                        app.cloud_count -= 1
                if app.tree_limit == True and item.is_tree == True:
                    app.tree_count -= 1
                    if len(app.map_items) == 2 and app.tree_count == 1: # Fixes one tree spawn bug
                        app.tree_count -= 1
                    #print("Tree Count after Item Removal "+str(app.tree_count))
        
        # [---------------------------]
        # Fixes plane tilt to look straight and applying momentum
        if Plane.changing_direction == False:
            app.direction_change_cooldown = True
            
            if Plane.rotateAngle < 0: # Looking Up
                if Plane.rotateAngle <= -20:
                    Plane.rotateAngle += 2 + Plane.turning_speed
                elif Plane.rotateAngle <= -5:
                    Plane.rotateAngle += 1 + Plane.turning_speed
                else:
                    Plane.rotateAngle += 1
                Plane.centerY -= Plane.momentum
                if Plane.momentum > 0:
                   Plane.momentum -= 2
                
            elif Plane.rotateAngle > 0: # Looking Down
                if Plane.rotateAngle >= 20:
                    Plane.rotateAngle -= 2 + Plane.turning_speed
                elif Plane.rotateAngle >= 5:
                    Plane.rotateAngle -= 1 + Plane.turning_speed
                else:
                    Plane.rotateAngle -= 1
                Plane.centerY += Plane.momentum
                if Plane.momentum > 0:
                   Plane.momentum -= 2
                
            if Plane.rotateAngle == 0:
                app.direction_change_cooldown = False
                Plane.momentum = 0
            
        # [---------------------------]    
        # Moves bullet when fired(generated) and applies its bloom        
        for bullet in Bullets.children:
            if bullet.centerX < 160:
                bullet.centerY += int(bullet.rotateAngle) / 8 # Applies Least Bloom
            if bullet.centerX < 275:
                bullet.centerX += app.bullet_speed * 4
                bullet.centerY += int(bullet.rotateAngle) / 4 # Applies Less Bloom
            elif bullet.centerX < 355:
                bullet.centerX += app.bullet_speed * 2 
                bullet.centerY += int(bullet.rotateAngle) / 2 # Applies Less Bloom
            elif bullet.centerX < 370:
                bullet.centerX += app.bullet_speed + 1
                bullet.centerY += int(bullet.rotateAngle) / 1.5 # Applies Even Less Bloom
            elif bullet.centerX < 395:
                bullet.centerX += app.bullet_speed + 1
                bullet.centerY += int(bullet.rotateAngle)  # Applies Normal  Bloom
            else:
                bullet.centerX += app.bullet_speed
        
        # [---------------------------]
        cloud1.fill = rgb(252,240,240)
        
        if Plane.hitsShape(cloud1) and item.opacity > 0:
            if app.iframes_activated == False:
                
                Health.hp_amount -= 20 - (20 * Plane.damage_reduction)
                print("Damage has been taken (Cloud) ["+str(Health.hp_amount)+"]")
                
                if randrange(1,10) == 1:
                    Health.hp_amount -= 20 - (20 * Plane.damage_reduction)
                    print("It's a Critcal Hit! (Cloud) ["+str(Health.hp_amount)+"]")
                    
                app.iframes_activated = True    
        cloud2.fill = rgb(240,252,240)
        
        if Plane.hitsShape(cloud2) and item.opacity > 0:
            if app.iframes_activated == False:
                if Health.hp_amount < Plane.health_value:
                    Health.hp_amount += 10 
                    print("Healing has been giving (Cloud) ["+str(Health.hp_amount)+"]")
                    
                    if randrange(1,10) == 1:
                        if Health.hp_amount < Plane.health_value:
                            Health.hp_amount += 50 
                            print("Superb Heal! (Cloud) ["+str(Health.hp_amount)+"]")
                    
                    app.iframes_activated = True
        cloud3.fill = rgb(240,240,252)
        
        if Plane.hitsShape(cloud3) and item.opacity > 0:
            if app.iframes_activated == False:
                Health.hp_amount -= 15 - (15 * Plane.damage_reduction)
                print("Damage has been taken (Cloud) ["+str(Health.hp_amount)+"]")
                
                if randrange(1,10) == 1:
                    Health.hp_amount -= 15 - (15 * Plane.damage_reduction)
                    print("Its a Critcal Hit! (Cloud) ["+str(Health.hp_amount)+"]")
                    
                if randrange(1,4) == 1:
                    if Plane.Mobility < 5:
                        Plane.Mobility += 1
                        print("Speed has been increased (Cloud) ["+str(Plane.Mobility)+"]")
                else:
                    if Plane.Mobility > 1:
                        Plane.Mobility -= 1
                        print("Speed has been decreased (Cloud) ["+str(Plane.Mobility)+"]")
                app.iframes_activated = True
                
            
        cloud4.fill = rgb(252,195,195)
        
        if Plane.hitsShape(cloud4) and item.opacity > 0:
            if app.iframes_activated == False:
                Health.hp_amount -= 50 - (50 * Plane.damage_reduction)
                print("Heavy Damage has been taken (Cloud) ["+str(Health.hp_amount)+"]")
                if randrange(1,2) == 1:
                    if Plane.Durability > 1:
                        Plane.Durability -= 1
                        print("Due to Damage, Durability has been decreased (Cloud) ["+str(Plane.Durability)+"]")
                
                if randrange(1,10) == 1:
                    Health.hp_amount -= 50 - (50 * Plane.damage_reduction)
                    print("Its a Critcal Hit! (Cloud) ["+str(Health.hp_amount)+"]")
                app.iframes_activated = True
                
                
        tree_top1.fill = rgb(120,250,87)
        if Plane.hitsShape(tree1) and item.opacity > 0:
            if app.iframes_activated == False:
                Health.hp_amount -= 30 - (30 * Plane.damage_reduction)
                print("Damage has been taken (Tree1) ["+str(Health.hp_amount)+"]")
                
                if randrange(1,4) == 1:
                    if Plane.Power > 1:
                        Plane.Power -= 1
                        print("Tree Branches have got into your gun, Power has been decreased (Tree1) ["+str(Plane.Power)+"]")
                
                if randrange(1,10) == 1:
                    Health.hp_amount -= 30 - (30 * Plane.damage_reduction)
                    print("Its a Critcal Hit! (Tree1) ["+str(Health.hp_amount)+"]")
                
                app.iframes_activated = True
                
        tree_top2.fill = rgb(87,250,115)
        if Plane.hitsShape(tree2) and item.opacity > 0:
            if app.iframes_activated == False:
                Health.hp_amount -= 10 - (10 * Plane.damage_reduction)
                
                if randrange(1,2) == 1:
                    Health.hp_amount -= 10 - (10 * Plane.damage_reduction)
                    print("Its a Critcal Hit! (Tree2) ["+str(Health.hp_amount)+"]")
                    
                print("Damage has been taken (Tree2) ["+str(Health.hp_amount)+"]")
                
                if randrange(1,2) == 1:
                    if app.score > 0:
                        app.score -= 100
                        print("A Goblin in the tree stole your score! (Tree2) ["+str(app.score)+"]")
                
                app.iframes_activated = True
                
        tree_top3.fill = rgb(54,255,101)
        if Plane.hitsShape(tree3) and item.opacity > 0:
            if app.iframes_activated == False:
                Health.hp_amount -= 45 - (45 * Plane.damage_reduction)
                
                if randrange(1,10) == 1:
                    Health.hp_amount -= 45 - (45 * Plane.damage_reduction)
                    print("Its a Critcal Hit! (Tree3) ["+str(Health.hp_amount)+"]")
                if randrange(1,4) == 1:
                    if Plane.Precision > 1:
                        Plane.Precision -= 1
                        print("Leaves Block your vision, Precision has been decreased (Tree)3 ["+str(Plane.Precision)+"]")    
                app.iframes_activated = True
                
                print("Damage has been taken (Tree3) ["+str(Health.hp_amount)+"]")
                
                
        if world_border.contains(Plane.right,Plane.centerY) == False:
            if app.iframes_activated == False:
                Health.hp_amount -= 40 - (40 * Plane.damage_reduction)
                app.iframes_activated = True
                print("Damage has been taken (Out of Bounds) ["+str(Health.hp_amount)+"]")
        
        
        for item in app.map_items:
            if Bullets.hitsShape(item):
                if item.opacity - ((item.distance*2) * (app.bullet_damage/2)) > 0:
                    item.opacity -= ((item.distance*2) * (app.bullet_damage/2))
                    print("Item has taken damage "+str(item.opacity))
                
                elif item.opacity - ((item.distance*2) * (app.bullet_damage/2)) < 0:
                    item.opacity = 0
                    print("Item has no more hitpoints"+str(item.opacity))
                
                if Plane.Power > 2:
                    item.centerX += app.bullet_knockback * item.distance
                    
            for bullet in Bullets:
                if bullet.hitsShape(item):
                    
                    Bullets.remove(bullet) 
                    app.bullet_count -= 1
                    
            if item.opacity <= 0:
                item.opacity = 100
                app.map_items.remove(item)
                
                if app.cloud_limit == True and app.cloud_count > 0 and item.is_cloud == True:
                    app.cloud_count -= 1
                    print("Cloud Count after Item Removal "+str(app.cloud_count))
                    if len(app.map_items) == 2 and app.cloud_count == 1: # Fixes one cloud spawn bug
                        app.cloud_count -= 1
                if app.tree_limit == True and item.is_tree == True:
                    app.tree_count -= 1
                    if len(app.map_items) == 2 and app.tree_count == 1: # Fixes one tree spawn bug
                        app.tree_count -= 1
                    print("Tree Count after Item Removal "+str(app.tree_count))
                    
        # [---------------------------]
        # Cleans up bullets and checks firing cooldown
        clean_bullets()
        if app.bullets_fired == False: 
            app.firing_cooldown = False   
        
        # [---------------------------]
        # Generates items
        generate_cloud()
        generate_tree()
        
        # [---------------------------]
        # Drags Plane Backward
        Plane.centerX -= Plane.drag/10 # Dragging the Plane Backward
        if Plane.centerX < 30:
            Plane.centerX -= Plane.drag/2
            
        if Plane.centerY < 70: # Dragging out of the map [TOP]
            Plane.centerY -= Plane.drag/5
            if Plane.centerY < 40:
                Plane.centerY -= Plane.drag/4
                if Plane.centerY < 10:
                    Plane.centerY -= Plane.drag/2
                    
        if Plane.centerY > 330: # Dragging out of the map [BOTTOM]
            Plane.centerY += Plane.drag/5
            if Plane.centerY > 370:
                Plane.centerY += Plane.drag/4
                if Plane.centerY > 390:
                    Plane.centerY += Plane.drag/2
                    
        if Plane.centerX > 130:
            Plane.centerX -= Plane.drag/2
        
    
    current_skill_point_counter.value = "Current Skill Points: "+str(app.skill_points)
    next_skill_point_counter.value = "Next Score until SP gain: "+str(app.stat_point_requirement)    
   
    skill_point_counter_dura.value = Plane.Durability
    skill_point_counter_powr.value = Plane.Power
    skill_point_counter_mobl.value = Plane.Mobility
    skill_point_counter_prec.value = Plane.Precision
    # D
    if skill_point_counter_dura.value == 5:
        skill_point_counter_dura.fill = 'gold'
        skill_point_counter_dura.size = 40
        
    if skill_point_counter_dura.value == 6:
            skill_point_counter_dura.fill = 'cyan'
            skill_point_counter_dura.size = 50
    # P    
    if skill_point_counter_powr.value == 5:
        skill_point_counter_powr.fill = 'gold'
        skill_point_counter_powr.size = 40
    # M
    if skill_point_counter_mobl.value == 5:
        skill_point_counter_mobl.fill = 'gold'
        skill_point_counter_mobl.size = 40
    # P
    if skill_point_counter_prec.value == 5:
        skill_point_counter_prec.fill = 'gold'
        skill_point_counter_prec.size = 40
        
    # Durability 
    if Plane.Durability != app.og_dura:
        Plane.health_value = health_stats[Plane.Durability-1]
        Plane.health_regen = health_regen_stats[Plane.Durability-1]
        Plane.damage_reduction = damage_reduction_stats[Plane.Durability-1]
    else:
        Plane.health_value = health_stats[app.og_dura-1]
        Plane.health_regen = health_regen_stats[app.og_dura-1]
        Plane.damage_reduction = damage_reduction_stats[app.og_dura-1]
    # Mobility
    if Plane.Mobility != app.og_mobl:
        Plane.flight_speed = flight_speed_stats[Plane.Mobility-1]
        Plane.turning_speed = turning_stats[Plane.Mobility-1]
        Plane.ascent_speed = ascent_speed_stats[Plane.Mobility-1]
        Plane.decent_speed = decent_speed_stats[Plane.Mobility-1]
    else:
        Plane.flight_speed = flight_speed_stats[app.og_mobl-1]
        Plane.turning_speed = turning_stats[app.og_mobl-1]
        Plane.ascent_speed = ascent_speed_stats[app.og_mobl-1]
        Plane.decent_speed = decent_speed_stats[app.og_mobl-1]
    
    # Power
    if Plane.Power != app.og_powa:
        app.bullet_damage = bullet_damage_stats[Plane.Power-1]
        app.bullet_knockback = bullet_knockback_stats[Plane.Power-1]
    else:
        app.bullet_damage = bullet_damage_stats[app.og_powa-1]
        app.bullet_knockback = bullet_knockback_stats[app.og_powa-1]
    # Precision
    if Plane.Precision != app.og_prec:
        app.bloom = bloom_stats[Plane.Precision-1]
        app.bullet_speed = bullet_speed_stats[Plane.Precision-1]
    else:
        app.bloom = bloom_stats[app.og_prec-1]
        app.bullet_speed = bullet_speed_stats[app.og_prec-1]
    
        
## Time & Score ##
app.step_count = 0
app.second = 0
app.minute = 0
app.score = 0

## Assets ##
Sky = Rect(0,0,400,400,fill=gradient('white','skyBlue','orange',start='top'))
Sun = Circle(200,280,40,fill='yellow')
def background_holder():
    grass_back_layer_one = Polygon(0,246
    ,64,259,133,266
    ,233,263,310,258
    ,372,256,400,251
    ,400,400,0,400,fill='forestGreen')
    
    grass_back_layer_one_tint = Polygon(0,246
    ,64,259,133,266
    ,233,263,310,258
    ,372,256,400,251
    ,400,400,0,400,fill='black',
    opacity=20)
    
    grass_back_layer_one.centerY += 20
    grass_back_layer_one_tint.centerY += 20
    
    back_mountain = Polygon(46,398
    ,81,290,92,296
    ,106,242,113,247
    ,126,208,140,251
    ,146,250,150,278
    ,160,263,170,282
    ,181,300,184,321
    ,193,356,201,396
    ,58,398,fill='silver')
    
    back_mountain_snow = Polygon(126,208,112,246
    ,114,251,121,243
    ,125,254,128,256
    ,130,249,134,252
    ,138,245,126,208,fill='white')
    
    front_mountain_small = Polygon(137,348
    ,140,338
    ,143,329,146,336
    ,148,334,151,327
    ,153,324,154,315
    ,155,310,158,304
    ,161,310,163,318
    ,168,328,168,335
    ,170,340,172,344,
    fill='gainsboro')
    
    
    front_mountain = Polygon(0,399
    ,21,323,26,328,37,295
    ,39,301,46,286
    ,60,257,76,295
    ,85,318,93,306
    ,100,324,113,350
    ,120,399,1,398,fill='lightGray')
    
    grass_fore_layer_five = Polygon(398,399
    ,396,380,391,370
    ,382,361,377,361
    ,372,362,361,363
    ,350,360,344,354
    ,337,348,329,345
    ,317,343,301,344
    ,290,335,281,330
    ,261,328,238,328
    ,222,329,205,330
    ,188,331,173,336
    ,162,339,150,344
    ,137,351,132,355
    ,124,353,114,347
    ,106,338,101,334
    ,90,330,73,327
    ,62,326,50,327
    ,40,335,33,334
    ,20,331,14,332
    ,6,338,1,347
    ,0,354,4,378
    ,6,385,6,386
    ,5,390,3,395,3,397,fill='darkGreen')
    
    grass_fore_layer_four = Polygon(0,355,
    2,354,10,352,18,350
    ,30,348,40,350
    ,49,351,59,353
    ,70,354,79,354
    ,86,354,94,353
    ,100,351,111,347
    ,118,343,130,340
    ,162,341,177,343
    ,200,346,216,346
    ,229,342,248,340
    ,268,344,290,345
    ,311,342,332,338
    ,349,338,369,339
    ,379,344,384,351
    ,390,359,396,367
    ,398,377,399,386
    ,398,394,0,397,fill='darkOliveGreen')
    
    grass_fore_layer_three = Polygon(0,383,
    0,360,8,356,
    32,353,59,351,
    78,354,95,358,
    116,360,123,357,
    137,353,162,355,
    177,359,186,367,
    198,375,204,380,
    213,400,0,400,
    fill='oliveDrab')
    
    grass_fore_layer_two =Polygon(100,380,
    109,371,133,363,
    156,360,178,365,
    202,365,226,362,
    245,362,289,359,
    306,359,324,363,
    338,367,354,369,
    372,368,389,371,
    393,376,396,378,
    400,383,400,400,
    105,400,fill='seaGreen')
    
    grass_fore_layer_one = Polygon(0,379,
    183,377,246,380,
    317,378,374,380,
    400,379,400,400,
    0,400,fill='limeGreen')
    
    pond = Polygon(318,284
    ,316,286,308,289
    ,305,290,299,291
    ,292,290,284,291
    ,281,291,274,290
    ,271,288,267,286
    ,257,282,251,282
    ,241,284,229,284
    ,223,284,217,287
    ,207,292,206,294
    ,206,302,208,307
    ,219,312,229,316
    ,239,317,247,318
    ,257,320,267,322
    ,276,322,284,322
    ,294,322,298,322
    ,309,322,318,324
    ,327,327,336,330
    ,345,331,350,332
    ,362,334,372,335
    ,377,332,384,327
    ,387,323,390,315
    ,391,308,392,304
    ,392,299,391,292
    ,389,288,384,284
    ,378,282,372,280
    ,365,278,358,278
    ,350,278,343,279
    ,336,280,329,282
    ,324,282,fill='blue')
    
    pond_grass = Polygon(209,313
    ,211,313,218,314
    ,221,316,225,318
    ,229,319,231,319
    ,240,319,244,320
    ,251,321,257,322
    ,270,323,277,323
    ,284,323,292,323
    ,300,324,312,326
    ,325,326,332,326
    ,341,327,354,328
    ,365,329,368,330
    ,379,330,381,327
    ,383,327,383,326
    ,383,323,383,320
    ,378,316,374,313
    ,374,318,375,321
    ,371,323,358,324
    ,355,324,346,322
    ,345,319,346,317
    ,346,315,340,315
    ,336,318,330,320
    ,326,322,324,316
    ,319,313,316,311
    ,313,319,308,320
    ,304,315,302,311
    ,297,315,292,317
    ,286,312,286,311
    ,282,317,276,317
    ,271,312,274,310
    ,269,308,263,309
    ,261,314,259,316
    ,252,315,248,308
    ,245,305,244,315
    ,244,315,236,306
    ,234,308,232,312
    ,223,312,225,306
    ,227,305,fill='forestGreen')
    
    pond_grass_tint = Polygon(209,313
    ,211,313,218,314
    ,221,316,225,318
    ,229,319,231,319
    ,240,319,244,320
    ,251,321,257,322
    ,270,323,277,323
    ,284,323,292,323
    ,300,324,312,326
    ,325,326,332,326
    ,341,327,354,328
    ,365,329,368,330
    ,379,330,381,327
    ,383,327,383,326
    ,383,323,383,320
    ,378,316,374,313
    ,374,318,375,321
    ,371,323,358,324
    ,355,324,346,322
    ,345,319,346,317
    ,346,315,340,315
    ,336,318,330,320
    ,326,322,324,316
    ,319,313,316,311
    ,313,319,308,320
    ,304,315,302,311
    ,297,315,292,317
    ,286,312,286,311
    ,282,317,276,317
    ,271,312,274,310
    ,269,308,263,309
    ,261,314,259,316
    ,252,315,248,308
    ,245,305,244,315
    ,244,315,236,306
    ,234,308,232,312
    ,223,312,225,306
    ,227,305,fill='black',
    opacity=20)
    
    pond_missing_grass = Polygon(351,325,355,322
    ,358,316,360,322
    ,361,325,363,327,fill='forestGreen')
    pond_missing_grass_tint = Polygon(351,325,355,322
    ,358,316,360,322
    ,361,325,363,327,fill='black',
    opacity=20)
    
    pond.height -= 20
    pond.width -= 10
background_holder()
Bullets = Group()
Plane = Polygon(40,185,50,200,40,215,90,200)
clock_shadow = Label("0:0",79,21,size=15,fill='dimGray',opacity=60)
clock = Label("0:0",80,20,size=15,fill='white')
score_counter_shadow = Label("Score | 0",79,41,size=18,fill='dimGray',font='orbitron',opacity=60)
score_counter = Label("Score | 0",80,40,size=18,fill='white',font='orbitron')
cloud_holder = True
tree_holder = True
if cloud_holder == True:
    cloud_list = []
    
    
    # Cloud 1
    cloud1 = Group()
    cloud1.add(Arc(220,120,40,80,0,180, rotateAngle = -90,fill='white'))
    cloud1.add(Arc(260,120,30,60,0,180, rotateAngle = -90,fill='white'))
    cloud1.add(Arc(250,120,40,50,0,180, rotateAngle = -90,fill='white'))
    cloud1.visible = False
    cloud_list.append(cloud1)
    
    
    # Cloud 2
    cloud2 = Group()
    cloud2.add(Arc(210,200,30,50,0,180, rotateAngle = -90,fill='white'))
    cloud2.add(Arc(230,200,40,60,0,180, rotateAngle = -90,fill='white'))
    cloud2.add(Arc(260,200,25,60,0,180, rotateAngle = -90,fill='white'))
    cloud2.visible = False
    cloud_list.append(cloud2)
    
    
    # Cloud 3
    cloud3 = Group()
    cloud3.add(Arc(210,240,30,50,0,180, rotateAngle = -90,fill='white'))
    cloud3.add(Arc(260,240,40,60,0,180, rotateAngle = -90,fill='white'))
    cloud3.add(Arc(230,240,35,50,0,180, rotateAngle = -90,fill='white'))
    cloud3.visible = False
    cloud_list.append(cloud3)
    
    
    # Cloud 4
    cloud4 = Group()
    cloud4.add(Arc(210,280,30,50,0,180, rotateAngle = -90,fill='white'))
    cloud4.add(Arc(260,280,30,60,0,180, rotateAngle = -90,fill='white'))
    cloud4.add(Arc(230,280,25,50,0,180, rotateAngle = -90,fill='white'))
    cloud4.add(Arc(215,280,35,40,0,180, rotateAngle = -90,fill='white'))
    cloud4.visible = False
    cloud_list.append(cloud4)
    
    cloud1.is_cloud = True
    cloud2.is_cloud = True
    cloud3.is_cloud = True
    cloud4.is_cloud = True
    
    cloud1.is_tree = False
    cloud2.is_tree = False
    cloud3.is_tree = False
    cloud4.is_tree = False
tree_holder = True        
if tree_holder == True:  
    tree_list = []
    
    
    tree1 = Group()
    trunk1 = Polygon(190,200,210,200,210,220,215,230,180,230,188,220,fill='sienna')
    
    tree_top1 = Polygon(170,205
    ,190,180,170,185
    ,190,160,170,165
    ,200,130,230,165
    ,210,160,230,185
    ,210,180,230,205,
    200,200,fill='green')
    tree1.add(trunk1)
    tree1.add(tree_top1)
    tree1.centerY += 10
    tree1.centerX += 60
    
    tree2 = Group()
    trunk2 = Polygon(194,143,206,143,208,220,212,240,188,240,192,220,fill='sienna')
    tree_top2 = Polygon(180,160,200,150
    ,220,160,210,145
    ,220,145,205,135
    ,200,125,195,135
    ,180,145,190,145,fill='green')
    
    tree2.add(trunk2)
    tree2.add(tree_top2)
    tree2.height += 40
    tree2.centerY -= 10
    
    tree3 = Group()
    trunk3 = Polygon(116,240,126,220,131,181,155,180,158,224,162,230,171,240,fill='sienna')
    tree_top3 = Polygon(142,150
    ,117,186,131,185
    ,117,200,128,200
    ,119,215,142,210,168,215
    ,155,200,169,200
    ,156,185,167,186,fill='green')
    tree3.add(trunk3)
    tree3.add(tree_top3)    
    tree1.visible = False
    tree2.visible = False
    tree3.visible = False
    
    tree1.is_tree = True
    tree2.is_tree = True
    tree3.is_tree = True
    
    tree1.is_cloud = False
    tree2.is_cloud = False
    tree3.is_cloud = False
    
    tree_list.append(tree1)
    tree_list.append(tree2)
    tree_list.append(tree3)

##  Map States ##
app.map_speed = 1
app.map_items = Group()
#print(app.map_items)
#print(app.map_items.children)

app.cloud_count = 0
app.cloud_limit = False
app.cloud_gen_count = 0

app.tree_count = 0
app.tree_limit = False
app.tree_gen_count = 0
## Plane & Bullet States ##
# Plane Stats
app.skill_points = 0
app.stat_point_requirement = 200
app.first_req = False
app.second_req = False
app.third_req = False
app.fourth_req = False

health_stats = [70,100,130,180,300,9999]
health_regen_stats = [1,2,3,5,12,999]
damage_reduction_stats = [0,0,.05,.1,.2,0]

bullet_damage_stats = [1,2,3,5,8]
bullet_knockback_stats = [0,0,1,2,4]
pierce_stats = [0,0,1,1,2] 

flight_speed_stats =[1,2,2.5,3.5,5]
turning_stats = [1,2,3,4,10]
acceleration_stats = [1, 1 ,1.1,1.5,1.8]
ascent_speed_stats = [1.1, 1.1, 1.11, 1.12, 1.13]
decent_speed_stats = [1.1, 1.11, 1.11, 1.12, 1.13]

bloom_stats = [20,10,5,3,1]
bullet_speed_stats = [3,5,8,15,30]

Plane.Durability = 2
app.og_dura = Plane.Durability
Plane.Power = 2
app.og_powa = Plane.Power
Plane.Mobility = 2
app.og_mobl = Plane.Mobility
Plane.Precision = 2
app.og_prec = Plane.Precision
Plane.Iframes = 15
app.og_frames = 15

#  - Plane - 
Plane.changing_direction = False
Plane.drag = 2
Plane.momentum = 0
app.iframes_activated = False

# Durability 
Plane.health_value = health_stats[Plane.Durability-1]
Plane.health_regen = health_regen_stats[Plane.Durability-1]
Plane.damage_reduction = damage_reduction_stats[Plane.Durability-1]

# Mobility
Plane.flight_speed = flight_speed_stats[Plane.Mobility-1]
Plane.turning_speed = turning_stats[Plane.Mobility-1]
Plane.acceleration = acceleration_stats[Plane.Mobility-1]
Plane.ascent_speed = ascent_speed_stats[Plane.Mobility-1]
Plane.decent_speed = decent_speed_stats[Plane.Mobility-1]

# - Bullet -
app.bullets_fired = False
app.bullet_count = 0
app.bullet_limit = 600

# Power
app.bullet_damage = bullet_damage_stats[Plane.Power-1]
app.bullet_knockback = bullet_knockback_stats[Plane.Power-1]

# Precision
app.bloom = bloom_stats[Plane.Precision-1]
app.bullet_speed = bullet_speed_stats[Plane.Precision-1]

## Key States ##
app.w_key_pressed = False
app.a_key_pressed = False
app.s_key_pressed = False
app.d_key_pressed = False

## Cooldowns
app.firing_cooldown = False
app.direction_change_cooldown = False

## UI ##
world_border = Rect(0,0,400,400,fill=None,border='white',borderWidth=4,opacity=10,dashes=True)
Health = Group()
Health.hp_amount = Plane.health_value

under_bar = Rect((Plane.health_value*2),0,200,40,fill='crimson')
Health.add(under_bar)

main_bar = Rect((Plane.health_value*2),0,200,40,fill='forestGreen')
Health.add(main_bar)


bar_border = Rect(200,0,200,40,fill=None,border='black',borderWidth=2)
bar_separators = Group()
for i in range(0,4):
    bar = Line(239+(40*i),40,241+(40*i),0,lineWidth=1)
    bar_separators.add(bar)
Health.add(bar_border)
health_display = Label(str(Health.hp_amount)+"/"+str(Plane.health_value),300,20,fill='white',size=20,font='montserrat',italic=True)

stat_opener_button = Group()

stat_opener_button.add(Polygon(120,370,280,
370,290,420,110,420,fill='white'))

flip_up_arrow = Polygon(145,395,150,385,200,375,250,385,255,395,200,385,fill='black')
flip_down_arrow = Polygon(145,395,150,385,200,375,250,385,255,395,200,385,fill='black',rotateAngle = 180)

stat_opener_button.add(flip_up_arrow)
stat_opener_button.add(flip_down_arrow)
flip_down_arrow.visible = False

stat_window = Group()
app.stat_window_open = False

stat_window_frame = Rect(50,60,300,280,fill='white',border='black')
durability_title = Label("Durability",95,90,size=20,font='grenze',italic=True)
power_title = Label("Power",165,90,size=20,font='grenze',italic=True)
mobility_title = Label("Mobility",235,90,size=20,font='grenze',italic=True)
precision_title = Label("Precision",305,90,size=20,font='grenze',italic=True)

stat_window.add(stat_window_frame)
stat_window.add(durability_title)
stat_window.add(power_title)
stat_window.add(mobility_title)
stat_window.add(precision_title)

skill_point_counter_dura = Label("0",95,130,size=35,font='grenze',italic=True)
skill_point_counter_powr = Label("0",165,130,size=35,font='grenze',italic=True)
skill_point_counter_mobl = Label("0",235,130,size=35,font='grenze',italic=True)
skill_point_counter_prec = Label("0",305,130,size=35,font='grenze',italic=True)

stat_window.add(skill_point_counter_dura)
stat_window.add(skill_point_counter_powr)
stat_window.add(skill_point_counter_mobl)
stat_window.add(skill_point_counter_prec)

durability_icon = Circle(95,180,20,fill='springGreen',border='black')
power_icon = Circle(165,180,20,fill='fireBrick',border='black')
mobility_icon = Circle(235,180,20,fill='lightSkyBlue',border='black')
precision_icon = Circle(305,180,20,fill='darkOrange',border='black')

stat_window.add(durability_icon)
stat_window.add(power_icon)
stat_window.add(mobility_icon)
stat_window.add(precision_icon)

current_skill_point_counter = Label("Current Skill Points: 0",200,300,size=20)
next_skill_point_counter = Label("Next Score until SP gain: 500",200,315,size=10)

stat_window.add(current_skill_point_counter)
stat_window.add(next_skill_point_counter)

stat_up_dura = Label("+",95,230,fill='green',size=50,font='monospace')
stat_up_powr = Label("+",165,230,fill='green',size=50,font='monospace')
stat_up_mobl = Label("+",235,230,fill='green',size=50,font='monospace')
stat_up_prec = Label("+",305,230,fill='green',size=50,font='monospace')

stat_window.add(stat_up_dura)
stat_window.add(stat_up_powr)
stat_window.add(stat_up_mobl)
stat_window.add(stat_up_prec)

stat_down_dura = Label("-",95,270,fill='red',size=50,font='monospace')
stat_down_powr = Label("-",165,270,fill='red',size=50,font='monospace')
stat_down_mobl = Label("-",235,270,fill='red',size=50,font='monospace')
stat_down_prec = Label("-",305,270,fill='red',size=50,font='monospace')

stat_window.add(stat_down_dura)
stat_window.add(stat_down_powr)
stat_window.add(stat_down_mobl)
stat_window.add(stat_down_prec)

app.shield_placeholder_one = 'Shield'
app.shield_placeholder_two = 'Icon'
app.bullet_placeholder_one = 'Bullet'
app.bullet_placeholder_two = 'Icon'
app.run_placeholder_one = 'Flying'
app.run_placeholder_two = 'Plane'
app.run_placeholder_three = 'Icon'
app.target_placeholder_one = 'Gun'
app.target_placeholder_two = 'Corsair'
app.target_placeholder_three = 'Icon'

shield_icon_one = Label(app.shield_placeholder_one,95,177,size=9)
shield_icon_two = Label(app.shield_placeholder_two,95,185,size=9)
bullet_icon_one = Label(app.bullet_placeholder_one,165,177,size=8)
bullet_icon_two = Label(app.bullet_placeholder_two,165,185,size=8)
run_icon_one = Label(app.run_placeholder_one,235,173,size=8)
run_icon_two = Label(app.run_placeholder_two,235,181,size=8)
run_icon_three = Label(app.run_placeholder_three,235,187,size=8)
target_icon_one = Label(app.target_placeholder_one,305,174,size=8)
target_icon_two = Label(app.target_placeholder_two,305,180,size=8)
target_icon_three = Label(app.target_placeholder_three,305,186,size=8)

stat_window.add(shield_icon_one)
stat_window.add(shield_icon_two)
stat_window.add(bullet_icon_one)
stat_window.add(bullet_icon_two)
stat_window.add(run_icon_one)
stat_window.add(run_icon_two)
stat_window.add(run_icon_three)
stat_window.add(target_icon_one)
stat_window.add(target_icon_two)
stat_window.add(target_icon_three)
stat_window.visible = False
version_num = Label("Ver 0.0.2.1",350,390,fill='white',font='monospace',bold=True,italic=True) # After Pre-Alpha, Alpha Version 2.1
tip = Label("Click to fire Bullets!",
60,390,fill='white',font='monospace',size=8,bold=True,italic=True,opacity=50)
# We're DONNEEEE :D
# For now... 
# 17/1/26
cmu_graphics.run()