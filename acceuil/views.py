from django.shortcuts import render

# Create your views here.

  
# create a function
def index(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "index.html", context)


  
# create a function
def about(request):
    return render(request, "about.html")


# create a function
def formation(request):
    return render(request, "formation.html")

# create a function
def startup(request):
    return render(request, "startup.html")

# create a function
def incubateur(request):
    return render(request, "incubateur.html")

# create a function
def webdeveloper(request):
    return render(request, "webdeveloper.html")

def mobiledeveloper(request):
    return render(request, "mobiledeveloper.html")

def bigdata(request):
    return render(request, "bigdata.html")

def datascience(request):
    return render(request, "datascience.html")
