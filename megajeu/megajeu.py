import os
import pygame as pg
import pygame.freetype  # Import the freetype module.
import random
import time
import sys


class Game(object):
    def __init__(self,screen_size):
        pg.init()
        os.environ["SDL_VIDEO_CENTERED"] = "TRUE"
        self.screen = pg.display.set_mode(screen_size)
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60.0
        self.done = False
        self.bQuick = False # when user click it render the question directly
        
        self.w = screen_size[0]
        self.h = screen_size[1]

        
        pg.font.init()


    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True
                    
            if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                if event.type == pg.MOUSEBUTTONDOWN:
                    pass
                elif event.type == pg.MOUSEBUTTONUP:
                    pass

    def update(self):
        pass
        

        

    def draw(self):
        #~ self.screen.blit(self.background, (0,0))
        #~ self.screen.fill( pg.Color("lightslategrey") )
        
        colBackground = (247,247,247)
        colLight1 = (220,220,220)
        colBlack = (0,0,0)
        colDark1 = (22,22,22)
        colBlue1 = (164,194,244)

        
        #~ fontSys = pygame.freetype.Font("../fonts/SF-UI-Display-Regular.otf", 20)

        rTime = pg.time.get_ticks()/1000
        
        w = self.w
        h = self.h
        
        self.screen.fill( colBackground )

        
        terrain_l = 1000
        terrain_h = 500

        centre_x = w//2
        centre_y = h//2
        
        # animation de debut
        cercle_rayon = 200
        reduit_ligne = 0
        rTimeIntro = 1.5
        if rTime < rTimeIntro:
            cercle_rayon = (rTime/rTimeIntro)*cercle_rayon
            reduit_ligne = (1-(rTime/rTimeIntro))*(terrain_h//8)
            terrain_l = (rTime/rTimeIntro)*terrain_l
            terrain_h = (rTime/rTimeIntro)*terrain_h

        terrain_x = (w-terrain_l)//2
        terrain_y = (h-terrain_h)//2
        terrain_y2 = terrain_y+terrain_h
        
        pg.draw.rect( self.screen, colBlack, (terrain_x,terrain_y,terrain_l,terrain_h),2 )
        pg.draw.circle( self.screen,colBlack,( centre_x,centre_y),cercle_rayon,2)
        pg.draw.line( self.screen,colBlack,( centre_x,terrain_y+reduit_ligne),(centre_x,terrain_y2-reduit_ligne),2)  
        
        if rTime > rTimeIntro:
            # dessine les buts
            
        
    # draw - end


    def main_loop(self):
        random.seed(0)
 
        
        nCpt = 0
        timeFps = time.time()
        nCptImageTotal = 0
        while not self.done:
            self.event_loop()
            rTime = pg.time.get_ticks()/1000
            nTime = int(rTime)

            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)
            nCpt += 1
            if nCpt > 200:
                duration = time.time() - timeFps
                print("INF: fps: %5.1f" % (nCpt/duration) )
                nCpt = 0
                timeFps = time.time()
                
                    
            nCptImageTotal += 1
                
#class Game - end

def runGame():
    g = Game((1366,768))
    g.main_loop()
    pg.quit()
    
if __name__ == "__main__":
    runGame()
    sys.exit()