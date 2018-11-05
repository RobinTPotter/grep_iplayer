#! /usr/bin/python3

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
font_size = 12 
font = pg.font.SysFont(None, font_size)
size_screen = [640,480]

squares = [4,4]
size_small = (int(size_screen[0]/squares[0]),int(size_screen[1]/squares[1]))


# corner offset for text
corner_x = 2
corner_y = 2


print (size_screen)
print (size_small)

maxshown = squares[0]*squares[1]
listoffset = 0

browse = 'browse'
pick = 'pick'
modes = [browse, pick]
mode = browse
mode_current = 0

pick_x = 0
pick_y = 0

screen = pg.display.set_mode(size_screen)
pg.display.update()

main_list = None
with open('cache/main','r') as m:
    main_list = m.readlines()
    # produce entity list from main file, including placeholders for caching of image and restructured names
    main_list = [{  'image_surf': None,
                    'corner_text': None, 
                    'description': None, 
                    'url': m.replace('\n',''), 
                    'pid': m.split('/')[5], 
                    'name': m.split('/')[6].replace('\n','')}
                for m in main_list]

# helper function to generate restructed name, from url
def generate_corner_text(name):
    titles = name.split('-')
    nn = 3
    numparts = int(len(titles) / nn) +1        
    t = []
    for r in range(0,nn):
        end = (r+1)*numparts            
        t.append(' '.join(titles[r*numparts:end]))
    return t

# helper function to load image from cache/images
def image(pid):
    image_surf = None   
    try:
        image_surf = pg.image.load(os.path.join('cache/images','{0}.jpg'.format(pid)))
        image_surf = pg.transform.scale(image_surf, size_small)
    except Exception as e:
        pass
        
    return image_surf

# initialize clock for FPS
clock = pg.time.Clock()

# keep the loop going
done = False

while not done:

    # key events listened for, assumes arrow keys and enter to change mode / take action
    for event in pg.event.get(): # User did something
        if event.type == pg.QUIT or ( event.type == pg.KEYDOWN and event.key == 27 ):
            done = True
        elif ( event.type == pg.KEYDOWN ):
        
            print (event.key)
            
            if event.key == 274:
                #down
                if mode is browse:
                    listoffset += squares[0]
                    print (listoffset)
                elif mode is pick:
                    pick_y += 1
                    if pick_y >= squares[1]: pick_y = 0
                    
            elif event.key == 273:
                #up
                if mode is browse:
                    listoffset -= squares[0]
                    if listoffset<0: listoffset=0
                    print (listoffset)    
                elif mode is pick:
                    pick_y -= 1
                    if pick_y <0: pick_y = squares[1]-1   

            elif event.key == 275: 
                if mode is pick:
                    pick_x += 1
                    if pick_x >= squares[0]: pick_x = 0
                    
            elif event.key == 276: 
                if mode is pick:
                    pick_x -= 1
                    if pick_x < 0: pick_x = squares[0]-1
    
            elif event.key == 13:
                #enter
                mode_current += 1
                if mode_current >= len(modes): mode_current = 0
                mode = modes[mode_current]
    
    # clean screen
    screen.fill((0, 0, 0)) 
 
    # actual screen coordinates of rectangle / image
    x = 0
    y = 0
    
    # keep track of the cursor square
    cx = 0 
    cy = 0
    
    # counters for debug to check whats loaded what's not etc
    count = 0
    loaded = 0
    
    # go through entire list entity by entity
    for i in main_list[listoffset:listoffset+maxshown]:
    
        # create image surface and cache in memor
        if i['image_surf'] is None:
            image_surf = image(i['pid'])
            i['image_surf'] = image_surf
        else:
            image_surf = i['image_surf']
            
        # print to screen if loaded
        if image_surf is not None:
            screen.blit(image_surf,(x,y))
            loaded += 1
            #print (x,y)
        
        # generate text based on name if not existing in entity
        if i['corner_text'] is None:
            i['corner_text'] = generate_corner_text(i['name'])
        
        # write out lines of text, row used to nudge each line down
        row = 0
        for t in i['corner_text']:
            textsurface = font.render(t, True, (0, 0, 0),(255,255,255))
            screen.blit(textsurface,(x+corner_x,y+corner_y+(font_size+1)*row))
            row += 1
        
        if mode==pick:
            if (cx is pick_x and cy is pick_y):
                pg.draw.rect(screen, (255,255,0), (x,y,size_small[0],size_small[1]), 1)
                pickme = listoffset+pick_y*squares[1]+pick_x
                #print (pickme)
                #print (main_list[pickme])
                #print (i['name'])
        
        #print(x,y)
        count += 1
        x += size_small[0]
        cx += 1
        #print (x,size_screen[0])
        if x>=size_screen[0]-10:
            x=0
            cx = 0
            y += size_small[1]
            cy += 1
        
    #print('image count {0}, loaded {0}'.format(count,loaded))
    ## added a clock to control FPS
    clock.tick(15)    
    ## update screen
    pg.display.flip()


pg.quit()
