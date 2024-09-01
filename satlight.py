import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 600

satnum = 10
satli = []
lines = []
next = 0

for i in range (10):
    s = Actor("spacelight")
    s.pos = random.randint(30, 570), random.randint(30, 570)
    satli.append(s)

start_time = time.time()

def draw():
    global next
    screen.blit("spacebg1", (0,0))

    index = 1
    for i in satli:
        i.draw()
        screen.draw.text(str(index),(i.pos[0], i.pos[1]+20))
        index = index+1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    if next < satnum:
        total_time = time.time()-start_time

    screen.draw.text(str(round(total_time)),(5,5))

def on_mouse_down(pos):
    global next, lines, satli
    if next < satnum:
        if satli[next].collidepoint(pos):
            if next!=0:
                lines.append((satli[next-1].pos, satli[next].pos))
                next = next + 1
                print(next)
        else:
            lines = []
            next = 0

def update():
    pass


pgzrun.go()
