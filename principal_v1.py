import paq1.biblioratos
from paq3 import solteronas, secretaria
import estribillo

paq1.biblioratos.biblioratos()
paq1.biblioratos.minifaldas()

estribillo.estribillo(2)
secretaria.secretaria()
estribillo.estribillo(1)
solteronas.solteronas()
estribillo.estribillo(2)
solteronas.solteronas()

print("")
print("Pruebas:") #para probar si se puede ejecutar individualmente o no a la función _doctor()
#solteronas._doctor()    #ejecuta la funcion
#_doctor()               #no ejecuta la funciona
