from django.shortcuts import render
from django.http import HttpResponse

# controller
# input: request 
# output: response
# class base view
# functional base view
def say_hello(request):
    return HttpResponse("Welcome to the django course")

def say_bye(request):
    context = {'name': 'mohammad', 'products': [
        {'name': 'product1', 'price': 12}
    ]}
    return render(request, 'bye.html', context=context)
