from cmu_graphics import *

app.playerID = [0]
app.blue_dot_id_obtained = False
app.red_dot_id_obtained = False
app.yellow_dot_id_obtained = False
app.blue_dot_list = [534, 866, 115, 327, 453]
app.red_dot_list = [673, 891, 223, 510, 583]
app.yellow_dot_list = [903, 413, 586, 213, 755]
# Test Code: 0 534 673 213

def generate_blue_dot_id():
    
    blue_dot_nums = [534, 866, 115, 327, 453]
    
    chosen_id_num = choice(blue_dot_nums)
    if app.playerID.count(534) < 1 and app.playerID.count(867) < 1 and app.playerID.count(115) < 1 and app.playerID.count(327) < 1 and app.playerID.count(453) < 1:
        app.playerID.append(chosen_id_num)
        print("Blue Dot Press Saving...")
        
    app.blue_dot_id_obtained = True


def generate_red_dot_id():

    red_dot_nums = [673, 891, 223, 510, 583]
    
    chosen_id_num = choice(red_dot_nums)
    if app.playerID.count(673) < 1 and app.playerID.count(891) < 1 and app.playerID.count(223) < 1 and app.playerID.count(510) < 1 and app.playerID.count(583) < 1:
        app.playerID.append(chosen_id_num)
        print("Red Dot Press Saving...")
        
    app.red_dot_id_obtained = True


def generate_yellow_dot_id():
    
    yellow_dot_nums = [903, 413, 586, 213, 755]
    
    chosen_id_num = choice(yellow_dot_nums)
    if app.playerID.count(903) < 1 and app.playerID.count(413) < 1 and app.playerID.count(586) < 1 and app.playerID.count(213) < 1 and app.playerID.count(755) < 1:
        app.playerID.append(chosen_id_num)
        print("Yellow Dot Press Saving...")
        
    app.yellow_dot_id_obtained = True


def get_player_id():
    ID = ""
    for index in range(0, len(app.playerID)):
        digits = str(app.playerID[index])
        if index == 0:
            ID = digits
        else:
            ID = ID+"-"+digits
    print(ID)
    return ID
    
def load_save():
    useable_number = False
    no_spaces = True
    
    input_id = app.getTextInput('Type In Your Former ID (MAKE SURE TO INCLUDE SPACES, INSTEAD OF DASHES)')
    
    player_id = app.playerID
    
    print("before "+input_id)
    if " " in input_id:
        no_spaces = False
    
    
    input_id = input_id.split()
    for index in range (len(input_id)):
        input_id[index] = int(input_id[index])
    
    print("after "+str(input_id))
    print("what it should look like -> "+str(player_id))
    
    print(input_id[0])
        
    if no_spaces == True:
        print("I said add spaces, try again -_-")
    else:
        if input_id[0] != 0:
            print("Incorrect Format")
        else:
            useable_number = True
   
    if useable_number == True:
        for index in range (len(input_id)):
            print(str(index))
            if input_id[index] in app.blue_dot_list:
                print("You've Touched a Blue Dot!")
                if app.blue_dot_id_obtained == False:
                    app.blue_dot_id_obtained = True
                    player_id.append(input_id[index])
            
            if input_id[index] in app.red_dot_list:
                print("You've Touched a Red Dot!")
                if app.red_dot_id_obtained == False:
                    app.red_dot_id_obtained = True
                    player_id.append(input_id[index])
            
            if input_id[index] in app.yellow_dot_list:
                print("You've Touched a Yellow Dot!")
                if app.yellow_dot_id_obtained == False: 
                    app.yellow_dot_id_obtained = True
                    player_id.append(input_id[index])
                


app.mouse_press_count = 0
app.player_id_text = Label("Your Id Number is: "+get_player_id(),200,330,size=20)

def onMousePress(mouseX, mouseY):
    app.mouse_press_count += 1

    if blue_dot.hits(mouseX, mouseY):
        if app.blue_dot_id_obtained == False:
            generate_blue_dot_id()
            print("Blue Dot Press Saved")
            
    if red_dot.hits(mouseX, mouseY):
        if app.red_dot_id_obtained == False:
            generate_red_dot_id()
            print("Red Dot Press Saved")
            
    if yellow_dot.hits(mouseX, mouseY):
        if app.yellow_dot_id_obtained == False:
            generate_yellow_dot_id()
            print("Yellow Dot Press Saved")
    
    if load_save_button.hits(mouseX, mouseY):
        print("Load Save Pressed")
        load_save()
        print(app.playerID)
    
    player_id_number = get_player_id()
    app.player_id_text.value = "Your Id Number is: "+player_id_number
    if app.blue_dot_id_obtained == True:
        blue_dot_notifcation.visible = True
        
    if app.red_dot_id_obtained == True:
        red_dot_notifcation.visible = True
        
    if app.yellow_dot_id_obtained == True:
        yellow_dot_notifcation.visible = True

blue_dot = Circle(100,100,35,fill = 'blue',border='black')
red_dot = Circle(200,100,35,fill = 'red',border='black')
yellow_dot = Circle(300,100,35,fill = 'yellow',border='black')


load_save_button = Group()
load_save_button.add(Rect(160,180,80,40,fill='white',border='black'))
load_save_button.add(Label('Load Save?',200,200))

blue_dot_notifcation = Label("You've Touched the Blue Dot",200,250,fill='skyBlue',size=10,visible=False)
red_dot_notifcation = Label("You've Touched the Red Dot",200,265,fill='fireBrick',size=10,visible=False)
yellow_dot_notifcation = Label("You've Touched the Yellow Dot",200,280,fill='gold',size=10,visible=False)

cmu_graphics.run()