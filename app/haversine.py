from math import radians, cos, sin, asin, sqrt, fabs

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

    return [declat,declon]


"""
var latsign = 1;
if( {{avaluo.LatitudG}} < 0){
  latsign = -1;
}
var lonsign = 1;
if( {{avaluo.LongitudG}} < 0){
  lonsign = -1;
}
var declat = Math.round(
 Math.abs( Math.round({{avaluo.LatitudG}}* 1000000.00)) +
 (Math.abs(Math.round({{avaluo.LatitudM}}* 1000000.00))/60) +
 (Math.abs(Math.round({{avaluo.LatitudS}}* 1000000.00))/3600)
 ) * latsign/1000000;

var declon = Math.round(
 Math.abs( Math.round(({{avaluo.LongitudG}})* 1000000.00)) +
 (Math.abs(Math.round(({{avaluo.LongitudM}})* 1000000.00))/60) +
 (Math.abs(Math.round(({{avaluo.LongitudS}})* 1000000.00))/3600)
 ) * lonsign/1000000;


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

    """