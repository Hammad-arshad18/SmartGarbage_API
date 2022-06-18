from django.shortcuts import render, HttpResponse


# Create your views here.

def api(request, id):
    if id is not None:
        if id == "354fe0f8":
            return render(request, 'api/index.html')
        else:
            return HttpResponse("404 Error Please Request Admin For API Key")
    else:
        return HttpResponse("404 Error Page Not Found")


def index(request):
    return render(request, 'api/index.html')


def detail(request):
    return render(request, 'api/Details.html')


def document(request):
    data = {}
    if request.method == "POST":
        key = request.POST.get('key')
        if key is not None:
            if key == "SE-17":
                data = {'confirmation': 'true'}
            else:
                data = {'confirmation': 'false'}

    return render(request, 'api/Document.html', data)
