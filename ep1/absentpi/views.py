from django.shortcuts import render

def index(request):
    context = {
        'foo': 'bar'
    }
    return render(request, 'absentpi/index.html', context)
