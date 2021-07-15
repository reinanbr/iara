from iara.system.date import date_base as date
from iara.system.info import ram

__cpu_show__ = False

def puts(args,sep:str=' ',path_file:str=None)->None:
  input = args
  cpu = f'[CPU: {ram()[2]}%_{ram()[3]}ms]\n' if(__cpu_show__) else ''
  text = (f'{cpu}{date()}-> {input}')
  print(text)
  if path_file:
    path = open(path_file,'a',encoding='utf-8')
    with open(path,'a') as file_p:
      file_p.write(text+'\n')
      # TODO: write code...
 
