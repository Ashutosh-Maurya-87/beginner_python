
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello Ashutosh')

def about(request):
    return HttpResponse('About the Ashutosh Maurya')

def withHtml(request):
    return HttpResponse('<h2> this is h2 tag </h2>')