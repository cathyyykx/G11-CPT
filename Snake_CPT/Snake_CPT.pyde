angle = 0
snakesize = 5
time = 0
headx = []
heady = []
for i in range(3000):
    headx.append(i)
for j in range(3000):
    heady.append(j)
applex = (round(random(62)) + 1) * 10
appley = (round(random(46)) + 1) * 10
re_cycle = True
stop_game = False

def setup():
    start_game()
    size(640, 480)
    
def draw():
    global time
    time += 1
    
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
    
    if time % 5 == 0:
        snake_move()
        eat_apple()
        check_if_dead()
        
def start_game():
    background(255)
    headx[1] = 200
    heady[1] = 200
    
    for i in range(2, 1000):
        headx[i] = 0
        heady[i] = 0
    
    stop_game = False
    applex = (round(random(62)) + 1) * 10
    appley = (round(random(46)) + 1) * 10
    snakesize = 5
    time = 0
    angle = 0
    re_cycle = True
    
def snake_move():
    for i in range(int(snakesize), 0, -1):
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
    global headx, heady, applex, appley, snakesize
    if headx[1] == applex and heady[1] == appley:
        snakesize += 2
        re_cycle = True
        
        while re_cycle:
            applex = (round(random(62)) + 1) * 10
            appley = (round(random(46)) + 1) * 10
            
            for i in range(1, int(snakesize)):
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
    #global headx, heady
    for i in range(2, int(snakesize)): 
        if headx[1] == headx[i] and heady[1] == heady[i]: # eat itself
            background(0)
            stop_game = True
        if headx[1] >= (width - 8) or heady[1] >= (height - 8) or headx[1] <= 0:
            background(0)
            stop_game = True
        
def keyPressed():
    global angle
    if key == CODED:
        if keyCode == UP and angle != 270 and heady[1] - 10 != heady[2]:
            angle == 90
        elif keyCode == DOWN and angle != 90 and headx[1] + 10 != heady[2]:
            angle == 270
        elif keyCode == LEFT and angle != 0 and headx[1] - 10 != headx[2]:
            angle == 180
        elif keyCode == RIGHT and angle != 180 and headx[1] + 10 != headx[2]:
            angle == 0
        elif keyCode == CONTROL:
            start_game()
        
