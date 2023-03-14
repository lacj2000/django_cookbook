from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# from django.template import loader
# Create your views here.

def hello(request):
    number_worlds = int(request.GET.get('number')) if request.GET.get('number') else 1
    plural = 's' if number_worlds != 1 else ''
    template = "<h1>Hello, %d world%s!<h1>" % (number_worlds, plural)
    return HttpResponse(template)

def hi(request):
    # template = loader.get_template('hi.html')
    # return HttpResponse(template.render())
    return render(request, 'hi.html')


class OurView(View):
  def get(self, request, *args, **kwargs):
    return HttpResponse("Hello, there!!!")

