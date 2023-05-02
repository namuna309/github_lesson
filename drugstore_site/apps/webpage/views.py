from django.shortcuts import render


# Create your views here.
def hello_view(request):
    context = {'hello': 'hola!'}
    return render(request, 'webpage/index.html', context)