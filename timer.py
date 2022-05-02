# importa el módulo de tiempo y sonido
import time
from playsound import playsound 
  
# define la función de temporizador de cuenta regresiva
def countdown_timer(seconds):
    
    while seconds > 0:       

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer)
        
        seconds -= 1
      
    print('¡Se acabó el tiempo!')

    playsound('mixkit-sound.wav')
  
  
# input tiempo en segundos.
seconds = input("Escribe el tiempo en numeros de segundos: ")
  
# Llama a la función
countdown_timer(int(seconds))
