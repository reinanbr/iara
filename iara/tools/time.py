import time as tm
from ..system.cmd import terminal
#sleep
def cronus(t:int,text_count:str='',text_final:str='',cls:bool=True,dt:float=1.)->bool:
   """
   This is a explained timer counter
   t: int (seg)
   text_count: text for counter (str)
   text_final; text print final (str)
   Example:
   cronus(3,'for sex...','is now!')
   output:
      3 seg for sex...
      2 seg for sex...
      1 seg for sex...
      0 seg for sex...
      is now!
      
   """
   s = t/dt
   while(True):
      #f = t
      if(cls): terminal('clear')
      
      m = (s // 60)
      mRest = s%60
      h = (m // 60)
      hRest = m%60
      
      if(m>0):
             m = f'{int(hRest)}min :'
      else:
             m=''
      if(h>0):
             h=f'{int(h)}hours :'
      else:
             h=''
      mili = int((s*dt)*100%100)
      print_cronus=f'[{h}{m}{int(mRest)}seg] {text_count}...'
      print(print_cronus)
      tm.sleep(dt)
      s -= dt
      #s = dt
      if(s<=0):
         print(text_final)
         break
   return True
