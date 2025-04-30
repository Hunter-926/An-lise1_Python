from datetime import datetime, time

print(datetime.now().time())
if datetime.now().time() >= time(00,45,0):
  print('Pode')
else:
  print('Não pode')
