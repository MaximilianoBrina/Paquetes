from paq1.biblioratos import *
from paq3.solteronas import *
from paq3.secretaria import *
import estribillo

biblioratos()
minifaldas()
estribillo.estribillo(2)
secretaria()
estribillo.estribillo(1)
solteronas()
estribillo.estribillo(2)
solteronas()

print("")
print("Pruebas:") #para probar si se puede ejecutar individualmente o no a la función _doctor()
#solteronas._doctor()   #no ejecuta la función
#solteronas()           #ejecuta la función
#_doctor()              #no ejecuta la función