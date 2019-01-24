add_library('minim')
headx = [None] * 3000
heady = [None] * 3000
mode = "home"

re_cycle = True
stop_game = False

def setup():
    global dead_bg, start_bg, main_music, home_music

    size(640, 480)
    textAlign(CENTER)
    dead_bg = loadImage("background.jpg")
    start_bg = loadImage("startpage.jpg")
    minim = Minim(this)
    main_music = minim.loadFile('sound.mp3')
    home_music = minim.loadFile('main_music.mp3')
    
    try:
        if mode == "home":
            background(start_bg)    
            home_music.play()
            main_music.pause()
    except:
        start_game()
        
    
    
def draw():
    global time, main_music, home_music
    
    if mode == "play":
        time += 1
    
        if time % 5 == 0 and stop_game != True:
        
            main_music.play()
            home_music.pause()
            
        # Draw apple
            fill(255, 0, 0)
            stroke(0)
            rect(applex, appley, 10, 10)
        
        # draw the frame of the window
            fill(0)
            stroke(0)
            rect(0, 0, width, 10)
            rect(0, height - 10, width, 10)
            rect(0, 0, 10, height)
            rect(width - 10, 0, 10, height)
            
            try:
                snake_move()
                eat_apple()
                check_if_dead()
            except SystemExit:
                pass
        
def start_game():
    global applex, appley, snakesize, time, angle, apple, apple_cood
    background(255)

    headx[1] = 200
    heady[1] = 200
    
    for i in range(2, 1000):
        headx[i] = 0
        heady[i] = 0
    
    applex = (round(random(60))) * 10
    appley = (round(random(40))) * 10
    snakesize = 6
    time = 0
    angle = 0
    apple = 0
    stop_game = False
    re_cycle = True

    
def snake_move():
    for i in range(snakesize, 0, -1):
        if i != 1:
            headx[i] = headx[i - 1]
            heady[i] = heady[i - 1]
        else:
            if angle == 0:
                headx[1] += 10
                break
            elif angle == 90:
                heady[1] -= 10
                break
            elif angle == 180:
                headx[1] -= 10
                break
            elif angle == 270:
                heady[1] += 10
                break

def eat_apple():
    global headx, heady, applex, appley, snakesize, apple
    if headx[1] == applex and heady[1] == appley:
        snakesize += 1
        apple += 1
        
        re_cycle = True
        while re_cycle:
            applex = (round(random(60))) * 10
            appley = (round(random(40))) * 10
            
            for i in range(1, snakesize):
                if applex == headx[i] and appley == heady[i]:
                    re_cycle = True
                else:
                    re_cycle = False
                    
    stroke(255)
    fill(0)
    rect(headx[1], heady[1], 10, 10)
    fill(255)
    rect(headx[snakesize], heady[snakesize], 10, 10)
    
def check_if_dead():
    for i in range(2, snakesize + 1): 
        if headx[1] == headx[i] and heady[1] == heady[i]: # eat itself
            home_music.play()
            main_music.pause()
            
            background(dead_bg)
            noFill() 
            rect(120, 160, 400, 160) 
            fill(255) 
            textSize(20)
            text("GAME OVER", 300, 200) 
            text("Score: " + str(apple) + " apple(s) eaten", 305, 250) 
            text("To restart, press Ctrl.", 310, 300)
            stop_game = True
            break
        
        elif headx[1] >= (width - 10) or heady[1] >= (height - 10) or headx[1] <= 0 or heady[1] <= 0:
            home_music.play()
            main_music.pause()
            
            background(dead_bg)
            noFill() 
            rect(120, 160, 400, 160) 
            fill(255) 
            textSize(20)
            text("GAME OVER", 300, 200) 
            text("Score: " + str(apple) + " apple(s) eaten", 305, 250) 
            text("Press Ctrl to RESTART", 310, 300) 
            stop_game = True
            break

        
def keyPressed():
    global angle
    
    if key == CODED:
        if keyCode == UP and angle != 270 and heady[1] - 10 != heady[2]: #make sure it's not downward
            angle = 90
        elif keyCode == DOWN and angle != 90 and headx[1] + 10 != heady[2]:
            angle = 270
        elif keyCode == LEFT and angle != 0 and headx[1] - 10 != headx[2]:
            angle = 180
        elif keyCode == RIGHT and angle != 180 and headx[1] + 10 != headx[2]:
            angle = 0
        elif keyCode == CONTROL:
            start_game()
            
def mousePressed():
    global mode
    if mode == "home":
        mode = "play"
        start_game()
    elif mode == "play":
        pass
