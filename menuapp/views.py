from django.shortcuts import render


def first_page(request):
    template_name = 'menuapp/first_page.html'
    return render(request, template_name)


def second_page(request):
    template_name = 'menuapp/second_page.html'
    return render(request, template_name)
