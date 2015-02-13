from celery import Celery
import redis
from app.models import Avaluo
celery = Celery('app.tasks', broker='django://')
@celery.task
def add(x, y):

    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    cantidad_proceso = avaluos.count()

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('chat', cantidad_proceso)



    return x + y