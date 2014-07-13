from django.http import HttpResponse
from app.models import Avaluo

def monto_inline(request, task_id=None):#if task_id is optional, set it to =None or something
    if request.is_ajax():
    	avaluo=Avaluo.objects.filter(avaluo_id=request.POST.get('pk'))
    	result=avaluo.update(Importe=request.POST.get('value'))
    	if result:
    		return HttpResponse(status=200)
    	else:
    		return HttpResponse(status=500)
