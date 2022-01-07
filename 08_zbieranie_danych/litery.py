import pygame
import time

pygame.init()

X = 600
Y = 600
timer = 1000
pauseletter = 4

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
lightgrey = (200, 200, 200)
orange = (255, 179, 102)

screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('wybor liter')
font = pygame.font.Font('freesansbold.ttf', 32)
LETTEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(LETTEREVENT, timer)
screen.fill(lightgrey)

def colordelay(color, time):
    screen.fill(color)
    pygame.display.update()
    pygame.time.delay(time)

def writecenter(txt, color):
    text = font.render(txt, True, color)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    screen.blit(text, textRect)

i = 97
n = 0
first = True
firstpause = True
t_start = 0
t_end = 0
t_delay_start = 0
t_delay_end = 0
t0 = 0
timetable = []
delay_timetable= []
print(pygame.time.get_ticks())
t0 = int(pygame.time.get_ticks())
a = "A"

while True:

    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.WINDOWLEAVE)
    pygame.event.set_blocked(pygame.WINDOWENTER)

    if pygame.event.get(LETTEREVENT):
        if first == True:
            t_start = t0
            first = False
            with open("moje_dane.txt", "a") as myfile:
                myfile.write("start\n")
        print("started event", i, "at ",pygame.time.get_ticks())

        if n%pauseletter == 0:
            t_end = pygame.time.get_ticks()
            t_delay_start = pygame.time.get_ticks()
            print("delayed at ", pygame.time.get_ticks())
            screen.fill(black)
            writecenter("2",white)
            pygame.display.update()
            pygame.time.delay(1000)
            screen.fill(black)
            writecenter("1",white)
            pygame.display.update()
            pygame.time.delay(1000)
            print("reset at ", pygame.time.get_ticks())
            t_delay_end = pygame.time.get_ticks()
            delay_timetable.append((t_delay_start, t_delay_end))
        else:
            t_end = pygame.time.get_ticks()

        if firstpause == False:
            print("saved letter ", a, " at ", t_start, " to ", t_end)
            timetable.append((t_start, t_end))
        firstpause = False
        print(pygame.time.get_ticks())
        screen.fill(lightgrey)
        a = chr(i).upper()
        print(a)
        writecenter(a, black)
        i += 1
        n += 1
        if i == 123:
            i = 97
        pygame.display.update()
        print("showed letter", a, " at ", pygame.time.get_ticks())
        t_start = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            t_end = pygame.time.get_ticks()
            print("t0 is ", t0)
            print(t_start)
            print(t_end)
            print("timetable")
            print(timetable)
            print("delay_timetable")
            print(delay_timetable)
            with open("czasy.txt", "a") as myfile:
                myfile.write("t0\n")
                myfile.write(str(t0))
                myfile.write("\n")
                myfile.write("timetable\n")
                myfile.write(str(timetable))
                myfile.write("\n")
                myfile.write("delay_timetable\n")
                myfile.write(str(delay_timetable))
                myfile.write("\n")
            pygame.quit()
            quit()


        pygame.display.update()
    pygame.display.update()

