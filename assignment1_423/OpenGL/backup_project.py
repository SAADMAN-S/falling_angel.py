from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

array=[]
speed=0.9
ball_array=[]
size=2
time_step = 0.01
score=0
temp=0
click_flag=False
click_counts=0
game_over=False
pause_flag=False
exit_flag=False
red_centre=[random.randint(10,490),500,random.choice([0,1])]
red_flag=False
red_count=0
triangle_tip=[random.randint(1,450),500]
green_flag=False
green_count=0
pl_start=0
pl_end=80
step=30
position=0
ball_count=0
bullet_wait=0
bullet_flag=False
bullet=15
bullet_position=(pl_start+pl_end)//2
shoot=False
light=False
light_coordinates=None
droplet_flag=False
droplet_array=[None]*4
end_flag=False
def populate_droplets():
    global droplet_flag,droplet_array

    droplet_array[0]=[random.randint(40,90),500]
    droplet_array[1] = [random.randint(110, 160), 500]
    droplet_array[2] = [random.randint(180, 230), 500]
    droplet_array[3] = [random.randint(250, 300), 500]
populate_droplets()


def draw_droplets():
    global droplet_flag,droplet_array
    if droplet_flag==True:


        if droplet_array[0]!=None:
            glColor3f(1, 0, 0)
            midpoint(droplet_array[0][0],droplet_array[0][1],droplet_array[0][0],droplet_array[0][1]+40)
        if droplet_array[1] != None:
            glColor3f(0, 1, 0)
            midpoint(droplet_array[1][0], droplet_array[1][1], droplet_array[1][0], droplet_array[1][1] + 40)
        if droplet_array[2] != None:
            glColor3f(0, 0, 1)
            midpoint(droplet_array[2][0], droplet_array[2][1], droplet_array[2][0], droplet_array[2][1] + 40)
        if droplet_array[3] != None:
            glColor3f(1, 0.7, 0.2)
            midpoint(droplet_array[3][0], droplet_array[3][1], droplet_array[3][0], droplet_array[3][1] + 40)


def move_droplets():
    global droplet_flag,droplet_array
    if droplet_flag==True:
        for i in range(len(droplet_array)):
            if droplet_array[i]!=None:
                droplet_array[i][1]-=0.4


def end():
    global end_flag
    if end_flag==True:
        glColor3f(1, 0, 0)
        midpoint(40, 250,40 , 180)
        midpoint(40, 250, 90, 250)
        midpoint(40, 180, 90, 180)
        midpoint(90, 180, 90, 215)
        midpoint(60, 215, 90, 215)
        glColor3f(0, 1, 0)
        midpoint(110, 180, 110, 250)
        midpoint(160, 180, 160, 250)
        midpoint(110, 250, 160, 250)
        midpoint(110, 215, 160, 215)
        glColor3f(0, 0, 1)
        midpoint(180, 180, 180, 250)
        midpoint(230, 250, 230, 180)
        midpoint(180, 250, 205, 215)
        midpoint(230, 250, 205, 215)
        glColor3f(1, 0.7, 0.2)
        midpoint(250, 180, 300, 180)
        midpoint(250, 250, 300, 250)
        midpoint(250, 250,250,180)
        midpoint(250, 215, 290, 215)
        glColor3f(1, 1, 0)
        midpointCircle(30, [60, 130])
        glColor3f(1, 0, 1)
        midpoint(110, 160, 135, 100)
        midpoint(160, 160, 135, 100)
        glColor3f(0, 1, 1)
        midpoint(180, 160, 230, 160)
        midpoint(180, 160, 180, 100)
        midpoint(180, 130, 220, 130)
        midpoint(180, 100, 230, 100)
        glColor3f(0.6, 0.2, 0.4)
        midpoint(250, 160, 250, 100)
        midpoint(250, 130, 300, 100)
        midpoint(250, 130, 300, 130)
        midpoint(300, 130, 300, 160)
        midpoint (250, 160,300,160)
def reappear(points):
    global light
    if light==True:
        light=False
    glutPostRedisplay()


def draw_ten(x,y):
    global light
    if light==True:
        glColor3f(1, 1, 1)
        midpoint(x, y, x , y+10)
        midpoint(x, y-10, x, y )
        midpoint(x, y, x+8, y )
        midpoint(x-8, y, x, y)
        midpoint(x +20, y+15, x+20, y-15 )
        midpoint(x + 16, y + 12, x + 20, y + 15)
        midpoint(x + 18, y - 15, x + 20, y - 15)
        midpoint(x + 22, y - 15, x + 20, y - 15)
        midpointCircle(13, [x+41,y])





def fire_bullet():
    global speed,bullet,bullet_position,shoot,pause_flag
    if pause_flag==False:
        #if bullet_flag==True:
            if shoot==True:
                bullet += speed*10
                #print(bullet)
                #print(bullet_position)
def draw_bullet(radius,centre):
    global pause_flag
    glColor3f(1, 0.7, 0.2)
    midpointCircle(radius, centre)

def draw_plate(x):
    global game_over
    if game_over == True:
        glColor3f(1, 0, 0)
    elif game_over == False:
        glColor3f(1, 1, 1)
    midpoint(x, 10, x + 80, 10)
    midpoint(x, 10, x + 5, 0)
    midpoint(x + 5, 0, x + 75, 0)
    midpoint(x + 75, 0, x + 80, 10)
def specialKeyListener(key, x, y):
    global speed,pl_start,pl_end,position, pause_flag,step,game_over
    if key == GLUT_KEY_LEFT:
        position = 0
        if pl_start-step > 0:
            if pause_flag == False and game_over==False:
                pl_start -= step
                pl_end-=step
        else:
            if pause_flag == False and game_over==False:
                pl_start = 0
                pl_end=80
        position = pl_start

    elif key == GLUT_KEY_RIGHT:
        position = 0
        if pl_end+step < 500:
            if pause_flag == False and game_over==False:
                pl_start += step
                pl_end+=step
        else:
            if pause_flag == False and game_over==False:
                pl_start = 420
                pl_end=500
        position = pl_start
    glutPostRedisplay()
def keyboardListener(key, x, y):
    global step,bullet_flag,bullet_position,game_over,pause_flag,pl_start,pl_end,shoot
    if key == b' ':
        if bullet_flag==True:
            if game_over == False:
                if pause_flag == False:
                    print(bullet_flag)
                    #draw_bullet(5, [bullet_position, bullet])
                    bullet_flag = False
                    fire_bullet()
                    print("bullet fired")
                    #bullet_flag=False
                    bullet_position=(pl_start+pl_end)//2
                    shoot=True
                    print(bullet_flag)
    glutPostRedisplay()




def green_triangle():
    global triangle_tip
    glColor3f(0, 1, 0)
    j=0
    i=0
    while i<=25:
        midpoint(triangle_tip[0]+i,triangle_tip[1]+j,triangle_tip[0]+50-i,triangle_tip[1]+j)
        i+=1
        j=j+1
def move_triangle():
    global triangle_tip
    triangle_tip[1]-=speed

def draw_points(x,y,size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
def populate_balls():
    global ball_array,ball_count
    for i in range(5):
        ball_count+=1
        ball_array.append([random.randint(5,495),random.randint(250,490),random.choice([-1,1]),random.choice([-1,1])])
    return ball_array

populate_balls()
print(ball_array)
def draw_balls():
    global ball_array
    glColor3f(1, 1, 1)
    for i in range(len(ball_array)):
        if ball_array[i]!=None:
            j=1
            while j<=5:
                midpointCircle(j, [ball_array[i][0],ball_array[i][1]])
                j+=0.1
def red_circle():
    global red_centre
    if red_centre[2]==0:
        glColor3f(1, 0, 0)
    elif red_centre[2]==1:
        glColor3f(0, 0, 1)



    j=1
    while j <= 10:
        midpointCircle(j,[red_centre[0],red_centre[1]])
        j += 0.1
def move_red():
    global red_centre,red_flag,speed
    if red_flag==True:
        red_centre[1]-=speed



def move_balls():
    global ball_array,array,last_update_time,pl_start,pl_end,position,ball_count
    current_time = time.time()
    if 'last_update_time' not in globals():
        last_update_time = current_time
    elapsed_time = current_time - last_update_time
    last_update_time = current_time
    for i in range(len(ball_array)):
        if ball_array[i]!=None:

            ball_array[i][0] += elapsed_time * ball_array[i][2] * 80
            ball_array[i][1] += elapsed_time * ball_array[i][3] * 80

            # Check for boundary collisions
            if ball_array[i][0] - 5 < 1 or ball_array[i][0] + 5 > 499:
                # Reverse horizontal velocity to rebound
                ball_array[i][2] *= -1

                # Move the ball slightly inside the boundaries to avoid getting trapped
                if ball_array[i][0] - 5 < 1:
                    ball_array[i][0] = 6
                else:
                    ball_array[i][0] = 494

            if ball_array[i][1] + 5 > 499: #or ball_array[i][1] - 5 < 1:
                # Reverse vertical velocity to rebound
                ball_array[i][3] *= -1

                # Move the ball slightly inside the boundaries to avoid getting trapped
                if ball_array[i][1] + 5 > 499:
                    ball_array[i][1] = 494

            if math.floor(ball_array[i][1] - 5 )<10:
                if position-10<= ball_array[i][0] <= position+90:
                    ball_array[i][3] *= -1
                    if ball_array[i][1] - 5 <10:
                        ball_array[i][1] = 13





                else:
                    if math.ceil(ball_array[i][1] + 5) <= 2:
                    # Ball falls out of the screen, remove it
                        ball_array[i]=None
                        ball_count-=1
                    # Since the list is modified, decrease the loop counter






def move_diamond():
    global array
    for i in range(len(array)):
        if array[i]!=None:
            array[i][1] -= array[i][2]


def to_zero(x,y,val):
    if val==0:
        return [x,y]
    elif val==1:
        return [y,x]
    elif val==2:
        return [y,-1*x]
    elif val==3:
        return [-1*x,y]
    elif val==4:
        return [-1*x,-1*y]
    elif val==5:
        return [-1*y,-1*x]
    elif val==6:
        return [-1*y,x]
    elif val==7:
        return [x,-1*y]
    else:
        return [x,y]
def from_zero(x,y,val):
    if val==0:
        return [x,y]
    elif val==1:
        return [y,x]
    elif val==2:
        return [-1*y,x]
    elif val==3:
        return [-1*x,y]
    elif val==4:
        return [-1*x,-1*y]
    elif val==5:
        return [-1*y,-1*x]
    elif val==6:
        return [y,-1*x]
    elif val==7:
        return [x,-1*y]
    else:
        return [x, y]

def findzone(X1,Y1,X2,Y2):
    dx=X2-X1
    dy=Y2-Y1
    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            return 0
        elif dx<0 and dy>0:
            return 3
        elif dx<0 and dy<0:
            return 4
        elif dx>0 and dy<0:
            return 7
    else:
        if dx>=0 and dy>0:
            return 1
        elif dx<0 and dy>0:
            return 2
        elif dx<0 and dy<0:
            return 5
        elif dx>=0 and dy<0:
            return 6

def midpoint(X1,Y1,X2,Y2):
    zone=findzone(X1,Y1,X2,Y2)
    start=to_zero(X1,Y1,zone)
    end=to_zero(X2,Y2,zone)
    x1=start[0]
    y1=start[1]
    x2=end[0]
    y2=end[1]
    dx=x2-x1
    dy=y2-y1
    d=2*dy-dx
    incrE=2*dy
    incrNE=2*(dy-dx)
    x=x1
    y=y1
    pixel = from_zero(x, y, zone)
    draw_points(pixel[0], pixel[1], 2)
    while x<x2:
        if d<=0:
            d=d+incrE
            x=x+1
        elif d>0:
            d=d+incrNE
            x=x+1
            y=y+1
        pixel = from_zero(x, y, zone)
        draw_points(pixel[0], pixel[1], 2)

def populate(coordinate,diamond_tip,speed,color):
    global array
    array.append([coordinate,diamond_tip,speed,color])
populate(50,500,speed,random.randint(1,7))


def draw_diamond(x, y,color):
    global val
    if color==1:
        glColor3f(0,0,1)
    elif color==2:
        glColor3f(0,1,0)
    elif color==3:
        glColor3f(0,1,1)
    elif color==4:
        glColor3f(1,0,0)
    elif color==5:
        glColor3f(1,0,1)
    elif color==6:
        glColor3f(1,1,0)
    elif color==7:
        glColor3f(1,1,1)

    i=0
    while i<11:
        midpoint(x - 50, y+i, x, y+i)
        i+=2


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def midpointCircle(radius,centre):
    d=1-radius
    x=0
    y=radius
    for i in range(0,8):
        circlepoints(x,y,i,centre)
    while x<y:
        if d<0:
            d=d+(2*x)+3
            x=x+1
        else:
            d=d+2*x-2*y+5
            x=x+1
            y=y-1
        for i in range(0, 8):
            circlepoints(x, y, i,centre)
def circlepoints(x,y,zone,centre):
    global size
    if zone==1:
        draw_points(x+centre[0], y+centre[1], size)
    elif zone==0:
        draw_points(y+centre[0], x+centre[1], size)
    elif zone==7:
        draw_points(y+centre[0], -1*x+centre[1], size)
    elif zone==6:
        draw_points(x+centre[0], -1*y+centre[1], size)
    elif zone==5:
        draw_points(-1*x+centre[0], -1*y+centre[1], size)
    elif zone==4:
        draw_points(-1*y+centre[0], -1*x+centre[1], size)
    elif zone==3:
        draw_points(-1*y+centre[0], x+centre[1], size)
    elif zone==2:
        draw_points(-1*x+centre[0], y+centre[1], size)



def showScreen():
    global end_flag,droplet_flag,droplet_array,game_over,light_coordinates,light,bullet_position,bullet_wait,bullet_flag,pl_start,position,pl_end,array,speed,ball_array,score,click_flag,temp,click_counts,red_flag,red_count,red_centre,green_flag,green_count,triangle_tip,ball_count,shoot,bullet
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glClearColor(0, 0, 0, 0)
    if game_over==False:
        if math.floor(red_centre[1]-10)<=10 and (pl_start-8<=math.ceil(red_centre[0])<=pl_end+8):
            print("Red Centre X:", red_centre[0])
            print("Plate Start X:", pl_start)
            print("Plate End X:", pl_end)
            game_over=True


        if shoot==True:
          draw_bullet(5, [bullet_position, bullet])
        if math.ceil(bullet)>=495:
            bullet = 15
            shoot = False
            bullet_wait=0

        for i in range(len(array)):
            if array[i] != None:
                diamond_x = array[i][0]
                diamond_y = array[i][1]
                if (diamond_x - 50 <= bullet_position <= diamond_x + 5 and
                        diamond_y - 5 <= bullet <= diamond_y + 15):
                    bullet = 15
                    if shoot==True:
                        light = True
                    shoot = False
                    bullet_wait = 0
                    score+=10
                    light_coordinates=[diamond_x+10,diamond_y]


                    array[i]=None
                    if array[len(array) - 1] == None:
                        populate(random.randint(50, 500), 500, speed, random.randint(1, 7))
                    break


        if light==True:
            if light_coordinates!=None:
                draw_ten(light_coordinates[0], light_coordinates[1])
                glutTimerFunc(200, reappear, 0)
        for i in range(len(array)):
            if array[i]!=None:
                draw_diamond(array[i][0], array[i][1],array[i][3])
        if array[len(array) - 1] !=None:
            if math.ceil(array[len(array)-1][1])==460 or math.floor(array[len(array)-1][1])==460  :

                populate(random.randint(50,500), 500, speed,random.randint(1,7))
                array[i][2]+=1

        for i in range(len(array)):
            if array[i] is not None:
                diamond_x = array[i][0]
                diamond_y = array[i][1]
                for j in range(len(ball_array)):
                    if ball_array[j]!=None:
                        ball_x = ball_array[j][0]
                        ball_y = ball_array[j][1]
                        if (diamond_x - 50 <= ball_x <= diamond_x + 5 and
                                diamond_y - 5 <= ball_y <= diamond_y + 15):
                            array[i]=None

                            if red_flag==False:
                                red_count+=1
                            score+=1
                            temp+=1
                            if green_flag== False:
                               green_count += 1
                            if bullet_flag==False:
                                bullet_wait+=1
                                #print("yes,increased")



                            print("Collision detected")
                            print(score)
                            print(temp)
                            print(red_count)
                            print(green_count)
                            print("bullet wait",bullet_wait)

                            if array[len(array)-1]==None:
                                populate(random.randint(50, 500), 500, speed, random.randint(1, 7))
                            break

        if temp==10:
            temp=0
            click_flag=True
            print("click_flag is activated")
        if click_counts==2:
            click_flag=False
            click_counts=0
            temp=0
        if red_count==5:
            red_count=0
            red_flag=True
            print("Red flag is activated")
        if red_flag==True:
            red_circle()
            move_red()
        if green_count == 6:
            green_count = 0
            green_flag = True
            print("Green flag is activated")
        if bullet_wait >= 0:
            bullet_wait=0
            bullet_flag = True
            #print("Bullet flag is activated")


        if green_flag==True:
            green_triangle()
            move_triangle()

        if math.floor(red_centre[1]-5)==0:
            red_flag=False
            red_centre = [random.randint(10, 490), 500,random.choice([0,1])]

        if math.floor(triangle_tip[1]) == 5:
            green_flag = False
            triangle_tip = [random.randint(1, 450), 500]

        for j in range(len(ball_array)):
            if ball_array[j]!=None:
                ball_x = ball_array[j][0]
                ball_y = ball_array[j][1]
                if (red_centre[0] - 10 <= ball_x <= red_centre[0] + 10) and (
                        red_centre[1] - 10 <= ball_y <= red_centre[1] + 10):
                    if red_centre[2]==0:
                        #ball_array.pop(j)  # Remove the collided ball
                        red_flag = False
                        red_count=0
                        red_centre = [random.randint(10, 490), 500,random.choice([0,1])]
                        score+=3
                        print(score)
                        print("Shot a red")
                        break
                    elif red_centre[2]==1:
                        ball_array.pop(j)
                        score-=2
                        print(score)
                        print("Shot a blue")
                        ball_count-=1
                        break

        for i in range(len(ball_array)):
            if ball_array[i]!=None:
                ball_x = ball_array[i][0]
                ball_y = ball_array[i][1]

                # Check if the ball is inside the green triangle
                if (triangle_tip[0] <= ball_x <= triangle_tip[0] + 50 and
                        triangle_tip[1] <= ball_y <= triangle_tip[1] + 25):

                    green_flag=False
                    green_count=0
                    triangle_tip = [random.randint(1, 450), 500]
                    print("New ball regenerated as green triangle is hit")
                    if ball_count<8:
                        ball_count+=1
                        ball_array.append(
                        [random.randint(5, 495), random.randint(250, 490), random.choice([-1, 1]), random.choice([-1, 1])])
                    break
        draw_balls()
        move_balls()
        if ball_count==0:
            game_over=True
    draw_plate(pl_start)
    if game_over==True:
        droplet_flag = True
        if droplet_flag==True:
            #populate_droplets()
            draw_droplets()
            move_droplets()
            for i in range(len(droplet_array)):
                if droplet_array[i]!=None:
                    if droplet_array[i][1]<250:
                        end_flag = True
                        droplet_array[i][1]=500
        if end_flag==True:
            end()
        for i in range(len(droplet_array)):
            if droplet_array[i] != None:
                if math.ceil(droplet_array[i][1]+4)==500:
                    end_flag=False









    glutSwapBuffers()

def animate():
    fire_bullet()
    move_diamond()
    glutPostRedisplay()
def mouse(button, state, x, y):
    global array, temp, click_flag, score,click_counts
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        #print("Mouse clicked at (x, y):", x, 500-y)
        if click_flag==True:
            for i in range(len(array)):
                if array[i] != None:
                    #print("Diamond:", array[i])
                    if (array[i][0] - 50) <= x <= (array[i][0] + 20) and (array[i][1] - 50) <= 500-y <= (array[i][1] + 50):
                        print("")
                        array[i] = None
                        score += 5
                        click_counts+=1
                        print("Score:", score)
                        if array[len(array)-1]==None:
                            populate(random.randint(50, 500), 500, speed, random.randint(1, 7))
                        break
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Falling angel")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutMouseFunc(mouse)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutTimerFunc(200, reappear, 0)
glutMainLoop()


