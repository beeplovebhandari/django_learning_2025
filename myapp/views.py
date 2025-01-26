
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    table_heading = "Student Information"
    people_info = [
        {"first": "Jon", "last": "harris", "address": "KTM"},
        {"first": "Jane", "last": "Bolton", "address": "PKR"},
        {"first": "Ken", "last": "", "address": "BKT"},
        {"first": "Harry", "last": "Wayne", "address": "KTM"},     
]
    return render (request, template_name="myapp/home.html", context={"heading": table_heading, "infos":people_info})

def test(request):
    return HttpResponse("Hello World")

def python(request):
     return render (request, template_name="myapp/python.html")
   
# def home(request):
#     content = """
#     <h1>Hello World</h1>
#     <h2>This my home page</h2>
#     <p>Python and django are awesome</p>
#     """
#     return HttpResponse(content)

def name(request):
    # We can send query strings / query parameters in the urls
    # Everything sent after "?" in the url is querrystring
    # Query strings can be multiple and are seperated by ampersand (&)
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"<h1>Hello my name is {name} and age is {age} </h1>")



def temp1(request):
    return HttpResponse("I'am test temp from views ")

def portfolio(request):
    return render (request, template_name="myapp/portfolio.html")


def login(request):
    return render (request, template_name="myapp/login.html")

def test1(request):
    return HttpResponse("Hello ")
