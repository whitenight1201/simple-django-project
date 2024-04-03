from django.http import HttpResponse
from django.template import loader
from .models import Member


# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {"mymembers": mymembers}
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, Django!")


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template("details.html")
    context = {"mymember": mymember}
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
    }
    return HttpResponse(template.render(context, request))


def setcookie(request):
    html = HttpResponse("<h1>Welcome to TechVidvan Employee Portal</h1>")
    if request.COOKIES.get("visits"):
        html.set_cookie("TechVidvan", "Welcome Back")
        value = int(request.COOKIES.get("visits"))
        html.set_cookie("visits", value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie("visits", value)
        html.set_cookie("TechVidvan", text)
    return html


def showcookie(request):
    if request.COOKIES.get("visits") is not None:
        value = request.COOKIES.get("visits")
        text = request.COOKIES.get("TechVidvan")
        html = HttpResponse(
            "<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(
                text, value
            )
        )
        html.set_cookie("visits", int(value) + 1)
        return html
    else:
        return redirect("/setcookie")


def updating_cookie(request):
    html = HttpResponse("We are updating  the cookie which is set before")
    html.set_cookie("TechVidvan", "Updated Successfully")
    return html


def deleting_cookie(request):
    html = HttpResponse("Deleting the cookie which is set")
    html.delete_cookie("TechVidvan", "Updated Successfully")
    return html
