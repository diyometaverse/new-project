from django.shortcuts import render

# Create your views here

def ordering_list(request):
    return render(request, 'ordering.html')