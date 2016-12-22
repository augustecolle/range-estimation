import numpy as np


#---------------Fixed parameters-------------
g = 9.81
Crol =  0.01 	    #Rol-weerstandscoefficient
Mfietser =  70    #Onderstaande 5 parameters zijn massa's
Mframe =  22 	    #Bullitt frame + wielen
Mmateriaal =  10  #Bagage
Mpaneel =  12 	    
Mmotor =  7 	    #Zoals gewogen in het labo
RhoLucht =  1.2   #Dichtheid van de lucht in kg/m³
S =  0.75 	      #Frontaal oppervlak van fietser + fiets (m²)
Clucht =  0.9 	  #Weerstandscoefficient van de lucht, afhankelijk van de vorm van het object.
                  #Dit wensen we te optimaliseren aan de hand van de aerodynamische studie
a =  0 	          #Versnelling, onderstellen we voor de eenvoud = 0, is toch maar gedurende korte tijd
Pelek =  10 	    #Vermogen van aanwezige elektronica (gsm,gps,lichten, ...)
Psfietser =  100  #Vermogen dat constant door de fietser kan geleverd worden
capKg =  120 	    #Capaciteitsdichtheid van de batterij (Wh/kg)
Nmotor =  0.86 	  #Rendement van de motor
Ngen =  0.86 	    #Rendement van de generator
#--------------------------------------------


#-------------Parameters to be dymensioned------------
Afstand =  130 	  #Totale afstand van een trip, in het vervolg ook in te lezen met de coordinaten en de hoogtes
wensSnelheid = 7  #Gemiddelde gewenste snelheid, parameter enkel nodig om batterijpakket te bepalen. Eens het batterijpakket
                  #gedimensioneerd is, wordt eigenlijk omgekeerd gerekend en is net de output de ideale snelheid om te rijden, om het
                  #gebruikte vermogen uit de batterij enigszins constant te houden
Whbat = 1000      #Capaciteit van de batterij
Ppaneel =  200 	  #Piekvermogen van het zonnepaneel, de derde parameter die we graag dynamisch maken ifv het tijdstip en de bewolking
h =  0 	          #Hellingsgraad (%), wordt dynamisch gemaakt in programma
Vw =  0.1 	      #Snelheid tegenwind, wensen we ook een dynamische parameter van te maken
#-----------------------------------------------------


#---------------Calculated values-------------
Mtot = Mfietser + Mframe + Mmateriaal + Mpaneel + Mmotor
Pfietser = Mfietser*Psfietser
hrad = np.arctan(h/100)
#---------------------------------------------
