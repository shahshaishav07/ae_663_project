import pygame, sys
import random
from pygame.locals import *
from pygame.transform import scale
import math,subprocess
import os
import serge
import constant as c
target_object=[]
  #====================================================
def display_init(screen_x,screen_y):
  pygame.init()
  DISPLAYSURF = pygame.display.set_mode((screen_x, screen_y), 0, 32)
  pygame.display.set_caption(c.terminal_name)
  return DISPLAYSURF
  #====================================================
  
  #====================================================
def msg_text(text,x,y):  
 FONT = pygame.font.Font('freesansbold.ttf', 16)
 Surf = FONT.render(text, 1, c.DARKGRAY)
 Rect = Surf.get_rect()
 Rect.topleft = (x, y - 25) 
 return Surf,Rect
  #====================================================

  #====================================================
  #====================================================

  #====================================================
class make_fire(object):
  def __init__(self,sourcex,sourcey,screen_x):
      self.x, self.y = sourcex,sourcey+20
      self.valid=True
      self.screen_x=screen_x
  
  def fire_load(self):
      return self.x,self.y
  
  def fire_now(self):
    if self.valid:
      self.x+=5
  def destroy_fire(self,fire_object):
    fire_object.remove(self)
      
  #====================================================
class Enemy(object):
  def __init__(self):
    self.x, self.y = 0,0
    self.valid = True
    self.score = 0 
    self.color = c.color[random.randrange(0,len(c.color))] # put a random number here between number of colours
    #self.target_surf,self.target_xy=msg_text('destroyed',targetx,targety)
    self.e = 0
  def make_target(self,screen_x,screen_y,current_level):
    self.x, self.y = screen_x,random.randrange(40,screen_y-100)
    self.valid = True
    self.color = c.color[random.randrange(0,len(c.color))] # put a random number here between number of colours
    #self.target_surf,self.target_xy=msg_text('destroyed',targetx,targety)
    self.e += 1
    if self.e>len(c.exam)-1:
      self.e=0
      current_level=current_level+1
      if current_level>len(c.level)-1:
	current_level=0
    self.score = c.score[self.e]
  def move_target(self):
    if self.valid:
      self.x-=5
      
  def destroy_target(self,fire_object,score):
    target_object.pop(k)
    score+= self.score
    
  #====================================================
def display_screen(clock,score,current_level,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object):
  s="score-"+str(score)
  Scoresurf,scoreRect=msg_text(s,1000,40)
  
  player.handle_event(event,current_level)
  DISPLAYSURF.blit(target_surf, target_xy)
  DISPLAYSURF.blit(infoSurf, infoRect)
  DISPLAYSURF.blit(Scoresurf, scoreRect)
  #DISPLAYSURF.blit(image, (20,40))
  #DISPLAYSURF.blit(image, (sourcex,sourcey))
  DISPLAYSURF.blit(player.image, player.rect)

  #pygame.draw.circle(surface, color, center_point, radius, width)
  for j in range(len(fire_object)):
    if fire_object[j].x!=sourcex:
      pygame.draw.circle(DISPLAYSURF, c.RED, (fire_object[j].x,fire_object[j].y), 8, 0)

  pygame.draw.rect(DISPLAYSURF,target.color,(target.x,target.y,24,24))
  #pygame.draw.rect(DISPLAYSURF,BLACK,(sourcex,sourcey,20,40))
  clock.tick(c.tick[c.level[current_level]])
  pygame.display.update()
  #====================================================
  
  #====================================================
def main(screen_x,screen_y):
  
  #================define terminal size================
  DISPLAYSURF = display_init(screen_x,screen_y)
  #====================================================
  
  
  #===============define background image===============
  #catImg = pygame.image.load('mario.png')
  #====================================================
  
  
  score = 0
  sourcex = 10
  sourcey = 10
  fire_object=[]
  player = serge.Serge((sourcex, sourcey))
  clock=pygame.time.Clock()
  #target = c.left
  #target.x,target.y=screen_x,random.randrange(40,screen_y-100)
  kill=c.missed
  f=0
  color_counter=0
  current_level=0
  target_delay=0
  target = Enemy()
  #========================the main game loop========================
  while True:
    sourcex = player.rect[0]
    sourcey = player.rect[1]
    #===============Reload the display===============
    DISPLAYSURF.fill(c.WHITE)
    #================================================
    
    infoSurf,infoRect=msg_text(c.terminal_name,10,screen_y)
    
    if target_delay>0:
      target_delay=target_delay-1
    else:
      target.x-=5
      if target.x<0:
	target.make_target(screen_x,screen_y,current_level)
      target_surf,target_xy=msg_text(c.exam[target.e],target.x,target.y)
     
      
	  
	
      
      
	
	
	
	
      for fire in fire_object:
	if fire.valid:
	  fire.fire_now()
	  if fire.x < target.x+24 and fire.x > target.x and fire.y < target.y+24 and fire.y > target.y:
	    fire.destroy_fire(fire_object)
	    target_surf,target_xy=msg_text('destroyed',target.x,target.y)
	    target_delay=c.delay[current_level]
	    target.make_target(screen_x,screen_y,current_level)
	    score+= target.score
	    
	    
	  if fire.x >= screen_x:
	    fire.destroy_fire(fire_object)
	    
      
      
      for event in pygame.event.get():
	if event.type == QUIT:
	  pygame.quit()
	  sys.exit()
	  
	if event.type==pygame.KEYDOWN:
	  if event.key==pygame.K_f:
	    fire_object.append(make_fire(sourcex,sourcey,screen_x))
	    
	    
	    
	  	  
	  if event.key==pygame.K_DOWN:
	    sourcey+=24
	    if sourcey>screen_y-50:
	      sourcey=screen_y-50
	  if event.key==pygame.K_UP:
	    sourcey-=24
	    if sourcey<10:
	      sourcey=10
    
    
    display_screen(clock,score,current_level,player,event,DISPLAYSURF,target_surf,target_xy,infoSurf,infoRect,sourcex,target,fire_object)
  #==================================================================
    



main(1200,700)