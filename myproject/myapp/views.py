from django.http import HttpResponse
from myapp.models import person
from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):
    all_persons = person.objects.all()
    return render(request, "index.html", {"all_person": all_persons, "message": None})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        # Get data from form
        name = request.POST.get("name")
        age = request.POST.get("age")
        print(name, age)

        # Save data to database
        p = person(name=name, age=age)
        try:
            p.save()
            messages.success(request, "Data saved successfully")
        except Exception as e:
            messages.error(request, "Data not saved. Error: {}".format(e))

        return redirect("/")

    else:
        return render(request, "form.html")
    
def edit(request, person_id):
    if request.method == "POST":
        # Get data from form
        name = request.POST.get("name")
        age = request.POST.get("age")
        print(name, age)

        # Save data to database
        p = person.objects.get(id=person_id)
        p.name = name
        p.age = age
        try:
            p.save()
            messages.success(request, "Data updated successfully")
        except Exception as e:
            messages.error(request, "Data not saved. Error: {}".format(e))

        return redirect("/")
    else:
        person_obj = person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person_obj})

def delete(request, person_id):
    p = person.objects.get(id=person_id)
    p.delete()
    messages.success(request, "Data deleted successfully")
    return redirect("/")
