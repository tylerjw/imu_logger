import numpy as np
import matplotlib.pyplot as plt 
import cv2

image_fname = 'GOPR2889.JPG'
degree_sign= u'\N{DEGREE SIGN}'

def pol2cart(rho, phi):
  x = rho * np.cos(phi-90)
  y = rho * np.sin(phi-90)
  return (x,y)

def pitch_box1(x,y,width,height,margin):
  #top
  ptch_edge = 45
  rect_width = width + margin*2
  y1 = y - height
  x1 = x - width/2 - margin
  return plt.Rectangle((x1,y1),rect_width,height,fill=False)

def pitch_rect(pitch, x, y, width, height):
  rect_height = int(abs(pitch) * height/45)

  x1 = x - width/2
  y1 = y - rect_height
  c = 'blue'
  #lower left
  if(pitch < 0):
    y1 = y
    c = 'red'
  return plt.Rectangle((x1,y1),width,rect_height,color=c,fill=True)


def pitch_box2(x,y,width,height,margin):
  #bottom
  ptch_edge = 45
  rect_width = width + margin*2
  y1 = y
  x1 = x - width/2 - margin
  return plt.Rectangle((x1,y1),rect_width,height,fill=False)

def roll_box1(x,y,width,height,margin):
  #left
  roll_edge = 45
  rect_height = height + margin*2
  x1 = x - width
  y1 = y - height/2 - margin
  return plt.Rectangle((x1,y1),width,rect_height,fill=False)

def roll_box2(x,y,width,height,margin):
  #right
  roll_edge = 45
  side = width/2
  rect_height = height + margin*2
  x1 = x
  y1 = y - height/2 - margin
  return plt.Rectangle((x1,y1),width,rect_height,fill=False)

def roll_rect(roll, x, y, width, height):
  rect_width = int(abs(roll) * width/45)
  x1 = x
  y1 = y - height/2 # plus is down in an image
  c = 'blue'
  #lower left
  if(roll < 0):
    x1 = x - rect_width
    c = 'red'
  return plt.Rectangle((x1,y1),rect_width,height,color=c,fill=True)


def hud(yaw, pitch, roll):

  img = cv2.imread(image_fname)
  height, width = img.shape[:2]


  fig, ax = plt.subplots(1,1)
  # fig.clf()

  # draw the image
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  
  #draw yaw plot
  x = 400
  y = height-400
  u,v = pol2cart(300,yaw)
  ax.add_artist(plt.Circle((x,y),300,fill=False))
  ax.quiver(x,y,u,v,color='r',angles='xy',scale_units='xy',scale=1)
  ax.text(400,height-800, u'Yaw: {}{}'.format(yaw,degree_sign), horizontalalignment='center',color='r',fontsize=15)
  
  #draw pitch
  rect_width = height/20
  edge = 45 # degrees
  rect_height = int(abs(edge) * (width)/180)
  margin = 30
  x = width - rect_width - margin*2
  y = height/2 
  ax.add_artist(pitch_rect(pitch,x,y,rect_width,rect_height))
  ax.add_artist(pitch_box1(x,y,rect_width,rect_height,margin))
  ax.add_artist(pitch_box2(x,y,rect_width,rect_height,margin))
  ax.text(width-200,height-rect_width*2,u'Pitch: {}{}'.format(pitch,degree_sign), horizontalalignment='right',color='r',fontsize=15)
  
  #draw roll
  x = width/2
  y = height-rect_width
  ax.add_artist(roll_rect(roll,x,y,rect_height,rect_width))
  ax.add_artist(roll_box1(x,y,rect_height,rect_width,margin))
  ax.add_artist(roll_box2(x,y,rect_height,rect_width,margin))
  ax.text(x,y-rect_width,u'Roll: {}{}'.format(roll,degree_sign), horizontalalignment='center',color='r',fontsize=15)
  
  # plt.axis('off')

  fig.savefig('output.png')

if __name__ == '__main__':
  hud(45,-15, -48)

  