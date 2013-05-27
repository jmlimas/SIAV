from math import radians, cos, sin, asin, sqrt, fabs
from app.models import *

def decimal_conversion(avaluo):

    def iround(x):
        """iround(number) -> integer
        Round a number to the nearest integer."""
        y = round(x) - .5
        return int(y) + (y > 0)

    latsign = 1
    if(avaluo.LatitudG < 0):
        latsign = -1

    lonsign = 1
    if(avaluo.LongitudG < 0):
        lonsign = -1

    declat = round((
    fabs(iround(float(avaluo.LatitudG)* 1000000.00)) +
    (fabs(iround(float(avaluo.LatitudM)* 1000000.00))/60) +
    (fabs(iround(float(avaluo.LatitudS)* 1000000.00))/3600)
    )*latsign/1000000,5)

    declon = round((
    fabs(iround(float(avaluo.LongitudG)* 1000000.00)) +
    (fabs(iround(float(avaluo.LongitudM)* 1000000.00))/60) +
    (fabs(iround(float(avaluo.LongitudS)* 1000000.00))/3600)
    )*lonsign/1000000,5)

    dec_cords = {}
    dec_cords ['declat'] = declat
    dec_cords ['declon'] = declon
    return dec_cords 


def haversine(lon1, lat1, lon2, lat2):
    
    #Calculate the great circle distance between two points 
    #on the earth (specified in decimal degrees)
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km 


def find_closest(avaluo):
    cercanos = []
    #Encuentra los 10 puntos mas cercanos 
    #avaluo = Avaluo.objects.get(FolioK='OLI20032')
    orig = decimal_conversion(avaluo)
    avaluos_todos = Avaluo.objects.all()
    for a in avaluos_todos:
            if a.LatitudG and a.LatitudM and a.LatitudS and a.LongitudG and a.LongitudM and a.LongitudS:
                dest = decimal_conversion(a)
                distancia = haversine(orig['declat'], orig['declon'], dest['declat'], dest['declon'])
                if len(cercanos) <= 15:
                    cercanos.append((distancia,a.avaluo_id, dest['declon'], dest['declat']))
                else:
                    if distancia < max(cercanos) and distancia > 0.0:
                        cercanos.remove(max(cercanos))
                        cercanos.append((distancia,a.avaluo_id, dest['declon'], dest['declat']))
    #for x in cercanos:
        #print x
    #print "El mas grande", max(cercanos)   
    return cercanos     
    
