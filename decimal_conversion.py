from math import radians, cos, sin, asin, sqrt, fabs
from app.models import *
from django.db import transaction

@transaction.commit_manually
def manual_transaction():
    dec_cords = {}
    avaluos = Avaluo.objects.all()
    def iround(x):
        """iround(number) -> integer
        Round a number to the nearest integer."""
        y = round(x) - .5
        return int(y) + (y > 0)
    for avaluo in avaluos:
        if avaluo.LatitudG and avaluo.LatitudM and avaluo.LatitudS and avaluo.LongitudG and avaluo.LongitudM and avaluo.LongitudS:
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

            
            avaluo.Declat = declat
            avaluo.Declon = declon
            avaluo.save()
            #print avaluo.FolioK, avaluo.Declat, avaluo.Declon
            transaction.commit()
        else:
            avaluo.Declat = 0
            avaluo.Declat = 0
            avaluo.save()
            #print avaluo.FolioK, avaluo.Declat, avaluo.Declon
            transaction.commit()
        