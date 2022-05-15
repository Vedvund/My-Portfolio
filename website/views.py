from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Renders website home page
    """
    return render(request, 'website/index.html')
