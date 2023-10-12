from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.


def index(response, id):
    todo_list = TodoList.objects.get(id=id)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):

            for item in todo_list.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                todo_list.item_set.create(text=txt, complete=False)
            else:
                print("Invalid input")

    return render(response, "main/list.html", {"todo_list": todo_list})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        t = None

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
