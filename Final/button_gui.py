# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 16:09:27 2014

@author: abigail
"""


import pygame, Buttons#, string, welcome
from pygame.locals import *
import eztext, sttt, welcome 
# initialize the pygame module
pygame.init()


class new_button:
       
    def __init__(self,num_players):
        self.num_players = num_players
        self.main()
    
    #Create a display
    def display(self):
        # create a surface on screen that has the size of 800 x 800
        self.screen = pygame.display.set_mode((800,800))

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
              return event.key
            else:
              pass
    def display_box(self, screen, message):
      fontobject = pygame.font.Font(None,30)
      if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (0,0,0)),
                    (200, 240))
      pygame.display.flip()
      
    def ask(self, screen, question):
        pygame.font.init()
        current_string = []
        self.display_box(self.screen, question + ": " + string.join(current_string,""))
        while 1:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            inkey = self.get_key()
            if inkey == K_BACKSPACE:
                pygame.draw.rect(self.screen, (255,255,255), (200, 240, 400, 80), 0)
                current_string = current_string[0:-1]
            elif inkey == K_ESCAPE:
                pygame.quit()
                return
            elif inkey == K_RETURN:
                break
            elif inkey == K_MINUS:
                current_string.append("_")
            elif inkey <= 127:
                current_string.append(chr(inkey))

            self.display_box(self.screen, question + ": " + string.join(current_string,""))
        return string.join(current_string,"")
        #print new_button.ask(self.screen, "Player 1 Name") + " was entered"
        pygame.display.flip()

      
    def update_display(self):
        # load the image
        background_image = pygame.image.load("spiderweb.jpg")
        background_image = pygame.transform.scale(background_image,(800, 800))
        pygame.display.set_icon(background_image)
        pygame.display.set_caption("Spyder Tic-Tac-Toe")
        self.screen.blit(background_image,[0,0])
        # draw a rectangle (x,y,length,height) where upper left corner position = x,y and extends to the right (width,height)
        #pygame.draw.rect(screen, (255,255,255), (0, 0, 150, 80), 0)
        #pygame.draw.rect(screen, (255,255,255),(650, 720, 150,80), 0)
        self.backbutton.create_button(self.screen,(255,255,255), 0, 0, 150, 80, 0, "Back",(0, 0, 0))
        self.nextbutton.create_button(self.screen,(255,255,255), 650, 720, 150, 80, 0, "Play",(0, 0, 0))
        #               call function (surface, (R,G,B), x, y, length, height, width, text on button, text color)
        
        # Using num_players creates appropriate number of text inputs fields
        total_height = self.num_players * 200
        
        for i in range (200,total_height,150):
            pygame.draw.rect(self.screen, (255,255,255), (200, i, 400, 80), 0)
            
        if self.num_players == 3:
            self.player1.create_button(self.screen, (255,255,255), 200, 200, 100, 80, 0, "Player 1", (0,0,0))
            self.player2.create_button(self.screen, (255,255,255), 200, 350, 100, 80, 0, "Player 2", (0,0,0))
            self.player3.create_button(self.screen, (255,255,255), 200, 500, 100, 80, 0, "Player 3", (0,0,0))
            
        else:
            self.player1.create_button(self.screen, (255,255,255), 200, 200, 100, 80, 0, "Player 1", (0,0,0))
            self.player2.create_button(self.screen, (255,255,255), 200, 350, 100, 80, 0, "Player 2", (0,0,0))
        #pygame.display.flip() 
         
    # define a variable to control the main loop
    def main(self):
        self.backbutton = Buttons.Button()
        self.nextbutton = Buttons.Button()
        self.player1 = Buttons.Button()
        self.player2 = Buttons.Button()
        self.player3 = Buttons.Button()
        self.display()
        txtbx = eztext.Input(x = 350, y = 225, maxlength = 45, color = (0,0,0))
        txtbx2 = eztext.Input(x = 350, y = 375, maxlength = 45, color = (0,0,0))
        if self.num_players == 3:
            txtbx3 = eztext.Input(x = 350, y = 525, maxlength = 45, color = (0,0,0))
        leave = 0
        while True:
            
            #print self.ask(self.screen, "Player 1 Name")
            
            events = pygame.event.get()

            for event in events:
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    if self.backbutton.pressed(pygame.mouse.get_pos()):
                        print "Previous page!"
                        welcome.welcome_main()
                        return
                    elif self.nextbutton.pressed(pygame.mouse.get_pos()):
                        print "Play game!!!"
                        names = [txtbx.value, txtbx2.value]
                        if self.num_players == 3:
                            names.append(txtbx3.value)
                        sttt.stttmain(names)
                        return 

                    elif self.player1.pressed(pygame.mouse.get_pos()):
                        leave = 1
                        #print leave
                        #self.write()
                        break
                    elif self.player2.pressed(pygame.mouse.get_pos()):
                        leave = 2
                        break
                    elif self.player3.pressed(pygame.mouse.get_pos()):
                        leave = 3
                        break
                        
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return
            
            
            if leave == 1:
                #self.update_display()
                txtbx.update(events)
                txtbx.draw(self.screen)
                txtbx2.draw(self.screen)
                if self.num_players == 3:                
                    txtbx3.draw(self.screen)
                #print txtbx.value
            elif leave == 2:
                #self.update_display()
                txtbx2.update(events)
                txtbx.draw(self.screen)
                txtbx2.draw(self.screen)
                if self.num_players == 3:
                    txtbx3.draw(self.screen)
                #print txtbx.value
            elif leave == 3:
                txtbx3.update(events)
                txtbx.draw(self.screen)
                txtbx2.draw(self.screen)
                if self.num_players == 3:
                    txtbx3.draw(self.screen)
            pygame.display.flip()
            self.update_display()
                
# run the main function only if this module is executed as the main script
if __name__=="__main__":
    # call the main function
    num_players = 3
    obj = new_button(num_players)
    #main()