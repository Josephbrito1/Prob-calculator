import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.contents=[]
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
        print(self.contents)
        
  def draw(self, numero):
    remover_todo=[]
    if (numero > len(self.contents)):
      return self.contents
    for i in range(numero):
      remover=self.contents.pop(int(random.random()*len(self.contents)))
      remover_todo.append(remover)
    return remover_todo

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  contador= 0
  for i in range(num_experiments):
    copia_pelotas=copy.deepcopy(expected_balls) #main: "blue": 2,
                                                 #"red": 1
    copia_sombrero=copy.deepcopy(hat) #tiene a mi objeto sombrero de la clase padre 
    color_obtenido=copia_sombrero.draw(num_balls_drawn) #main put 4(have the 4 balls draw)

        
    for color in color_obtenido:
      #el color optenido tiene las 4 pelotas eliminadas
      #el color optenido se almacenara en cada variable
      #"color" si cada de esta misma vairable esta en:
      #copia_pelotas (esto es igual a: "blue": 2, "red": 1)          
      if(color in copia_pelotas):
        copia_pelotas[color]-=1
        
        
       
                
    if (all(x<= 0 for x in copia_pelotas.values())):
      contador +=1
                    
  return contador / num_experiments 

# miobjeto=Hat(blanco=3, rojo=1, rosado=6)  
# probability = experiment(
#     hat=miobjeto,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=1000)

