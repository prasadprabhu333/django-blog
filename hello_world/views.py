from django.shortcuts import render

# Create your views here.


def hello_world(request):
    print("Inisde hello world view method")
    return render(request, 'hello_world.html', {})


def alvida(request):
    print("Inside the alvida handler")
    print(f"request={request}")
    return render(request, 'alvida.html', {})
