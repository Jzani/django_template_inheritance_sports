from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def main_page(request):
    return render(request, 'main.html')

def kabbadi_page(request):
    return render(request, 'kabbadi.html')

def cricket_page(request):
    return render(request, 'cricket.html')

def basketball_page(request):
    return render(request, 'basketball.html')

def volleyball_page(request):
    return render(request, 'volleyball.html')

from django.shortcuts import render
from django.http import HttpResponse

def input_names(request):
    if request.method == "POST":
        senior_name = request.POST.get("senior_name")
        junior_name = request.POST.get("junior_name")

        # Validate input (ensure only alphabets)
        if senior_name.isalpha() and junior_name.isalpha():
            return render(request, "success.html", {"message": "Saved Successfully!"})
        else:
            return render(request, "input_names.html", {"error": "Please enter valid names (alphabets only)."})
    return render(request, "input_names.html")


from django.shortcuts import render

def cricket(request):
    return render(request, "cricket.html")

def basketball(request):
    return render(request, "basketball.html")

def volleyball(request):
    return render(request, "volleyball.html")

def kabaddi(request):
    return render(request, "kabaddi.html")
