from django.http import HttpResponse
from django.template import loader

from . import views

def index(request):
    template = loader.get_template('answer_generator/index.html')
    context = {
        'company_name': 'Hunar smart',
    }
    return HttpResponse(template.render(context, request))