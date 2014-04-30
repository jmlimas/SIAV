from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render

def not_found_error(request, template_name='home/errors/404.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context: None
    """
    return render(request, template_name, locals())