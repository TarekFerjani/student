
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def home_view(request):
 
    # logic of view will be implemented here
    return render(request, "index.html")