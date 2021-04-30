from django.http import HttpResponse


def homepage_view(request):
    return HttpResponse('Django says: Hello world!')