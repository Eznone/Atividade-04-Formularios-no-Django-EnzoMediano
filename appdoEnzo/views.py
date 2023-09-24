from django.shortcuts import render, redirect
from .models import Lived, Schools


# Create your views here.
def home(request):
  lived = Lived.objects.all()
  schools = Schools.objects.all()
  print(lived)
  return render(request, "home.html", context = {
    "liveds": lived, 
    "schools": schools
  })

def create_lived(request):
  print("entrei aqui")
  if request.method == "POST": 
    print(request.POST)
    Lived.objects.create(
      titulo = request.POST["Titulo"],
      country = request.POST["Country"],
      state = request.POST["State"],
      years = request.POST["Years"],
    )
    return redirect("home")
  return render(request, "forms.html")


def update_lived(request, id):
  lived = Lived.objects.get(id = id)
  if request.method == "POST": 
    lived.titulo = request.POST["Titulo"]
    lived.country = request.POST["Country"]
    lived.state = request.POST["State"]
    lived.years = request.POST["Years"]
    lived.save()
    return redirect("home")
  return render(request, "forms.html", context = {"action": "Atualizar", "lived": lived})



def delete_lived(request, id):
  lived = Lived.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      lived.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context = {"item": lived})



def create_school(request):
  if request.method == "POST":
    print(f"\n\n\n{request.POST}\n\n\n")
    Schools.objects.create(
      name = request.POST["Name"],
      level = request.POST["Level"],
      city = request.POST["City"],
      country = request.POST["Country"],
      state = request.POST["State"],      
    )
    return redirect("home")
  return render(request, "formsSchool.html", context = {"action": "Adicionar"})



def update_school(request, id):
  School = Schools.objects.get(id = id)
  if request.method == "POST":
    School.name = request.POST["Name"]
    School.level = request.POST["Level"]
    School.city = request.POST["City"]
    School.country = request.POST["Country"]
    School.state = request.POST["State"]
    School.save()

    return redirect("home")
  return render(request, "formsSchool.html", context = {"action": "Atualizar", "School": School})



def delete_school(request, id):
  School = Schools.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      School.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context = {"item": School})
    