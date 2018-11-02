import pygame as pg
import os

## demo, pygame init
## use of font
## loading image
## resize image
## loop to print text, print image
## escape window

pg.init()
pg.font.init()
font = pg.font.SysFont(None, 12)
size_screen = [640,480]
#pg.display.set_mode(size_screen, pg.FULLSCREEN)
pg.display.set_mode(size_screen)
squares = [4,4]
size_small = (int(size_screen[0]/squares[0]),int(size_screen[1]/squares[1]))
print (size_screen)
print (size_small)

screen = pg.display.set_mode(size_screen)
pg.display.update()

main_list = None
with open('cache/main','r') as m:
    main_list = m.readlines()
    main_list = [{ 'url': m.replace('\n',''), 'pid': m.split('/')[5], 'name': m.split('/')[6].replace('\n','')} for m in main_list]

#print (main_list)

def image(pid):
    image_surf = None   
    try:
        image_surf = pg.image.load(os.path.join('cache\images','{0}.jpg'.format(pid)))
        #print (0,image_surf.get_rect())
        image_surf = pg.transform.scale(image_surf, size_small)
        #print (1,image_surf.get_rect())
    except Exception as e:
        pass
        
    return image_surf

clock = pg.time.Clock()

done = False

while not done:
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT or ( event.type == pg.KEYDOWN and event.key == 27 ):
            done = True
    
    screen.fill((0, 0, 0)) 
    
    textsurface = font.render('hello', True, (0, 0, 0),(255,255,255))
    
    screen.blit(textsurface,(0,0)) 
 
    x = 0
    y = 0
    
    for i in main_list:    
        image_surf = image(i['pid'])
        if image_surf is not None: screen.blit(image_surf,(x,y))  
        #print(x,y)
        x += size_small[0]
        if x>size_screen[0]:
            x=0
            y += size_small[1]
        
    ## added a clock to control FPS
    clock.tick(15)    
    ## update screen
    pg.display.flip()


pg.quit()
