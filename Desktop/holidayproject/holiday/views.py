from django.shortcuts import render
import secrets

# Create your views here.
def index(request):
    return render(request, "holiday/index.html")



def random(request):
    countries = ["United States", "United Kindgom", "India", "France", "Germany"]
    result = secrets.choice(countries)
    return render(request, "holiday/random.html", {
        "country":result
    })
