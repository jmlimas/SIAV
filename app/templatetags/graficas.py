from django import template
from app.models import *
from django.db.models import Sum, Count, Q

register = template.Library()

def grafica_por_facturar(dollars):
    total_general = 0.0	
    por_facturar = (Avaluo.objects
               .filter(Estatus='CONCLUIDO')
               .filter(Q(Salida__isnull=False))
               .filter(Q(Factura='') | Q(Factura__isnull=True))
               .filter(Q(Pagado=False) | Q(Pagado__isnull=True)))
    por_facturar = por_facturar.order_by('-Salida')
    suma_de_monto = por_facturar.values('Cliente__Cliente').order_by('Cliente').annotate(total=Sum('Importe'))

    for x in suma_de_monto:
        if not x['total']:
            total_general += 0.00
            x['Total'] = 0.00
        else:
            total_general += float(str(x['total']))    

    return suma_de_monto


def grafica_por_liquidar(dollars):
    total_general = 0.0
    por_liquidar = (Avaluo.objects
               .filter(Estatus='CONCLUIDO')
               .filter(Q(Factura__isnull=False))
               .filter(Q(Pagado=0) | Q(Pagado__isnull=True))
               .exclude(Q(Factura__exact='')))
    por_liquidar = por_liquidar.order_by('-Salida')
    suma_de_monto = por_liquidar.values('Factura','Cliente__Cliente').order_by('Cliente').annotate(total=Sum('Importe'))

    for x in suma_de_monto:
        if not x['total']:
            total_general += 0.00
            x['total'] = 0.00
        else:
            total_general += float(str(x['total']))


    return suma_de_monto

register.filter('grafica_por_facturar', grafica_por_facturar)
register.filter('grafica_por_liquidar', grafica_por_liquidar)