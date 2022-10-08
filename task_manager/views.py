from django.http.response import HttpResponse


def home(request):
    return HttpResponse('Hello, user!', content_type='text/plain')
