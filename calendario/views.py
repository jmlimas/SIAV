from django.shortcuts import render
from calendario.models import Evento
from app.models import Avaluo
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
import json as simplejson
# Create your views here.

def calendario(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)
    avaluos = avaluos.order_by('-Solicitud')
    return render_to_response('home/calendario.html', {'avaluos': avaluos}, context_instance=RequestContext(request))


@csrf_exempt
def cargaEventos(request):
	start = request.POST.get("start", "")
	end = request.POST.get("end", "")
	eventos = Evento.objects.all()

	data = {}
	eventos_json = []
	for e in eventos:
		data["id"] = int(e.evento_id)
		data['title'] = str(e.avaluo.FolioK)
		data['start'] = e.Inicio.strftime("%Y-%m-%dT%H:%M:%S")
		data['end'] = e.Fin.strftime("%Y-%m-%dT%H:%M:%S")
		data['allDay'] = "false"
		eventos_json.append(data)
		data = {}

	#eventos_json = simplejson.dumps([{"id":2,"title":"Test Event","start":"2015-02-01T11:00:00","end":"2015-02-28T16:00:00","allDay":"false"}])
	return HttpResponse(simplejson.dumps(eventos_json))
	#works
	#				[{"start": "2015-02-01T11:00:00", "allDay": "false", "end": "2015-02-28T16:00:00", "id": 2, "title": "Test Event"}]
	#eventos_json = [{'start': '2015-02-01T00:00:00', 'allDay': 'false', 'end': '2015-02-28T00:00:00', 'id': 1, 'title': '@1'}]


