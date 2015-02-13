from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from datetime import datetime
from app.models import Avaluo
 
 
logger = get_task_logger(__name__)

@periodic_task(run_every=10)
def realtime(request):

    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Salida__isnull=True)
    cantidad_proceso = avaluos.count()


    # Enviar notificación a usuarios
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('chat', cantidad_proceso)
    logger.info("Task finished: result = %i" % result)

