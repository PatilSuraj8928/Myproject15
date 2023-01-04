from django.shortcuts import render

# Create your views here.
def second(request):
    return render(request, 'html2.html')