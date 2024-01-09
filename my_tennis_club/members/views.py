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
    html = HttpResponse("<h1>Welcome to Cookie</h1>")
    html.set_cookie("TechVidvan", "We are setting a cookie", max_age=None)
    return html


def showcookie(request):
    show = request.COOKIES["TechVidvan"]
    html = "<center> New Page <br>{0}</center>".format(show)
    return HttpResponse(html)


def updating_cookie(request):
    html = HttpResponse("We are updating  the cookie which is set before")
    html.set_cookie("TechVidvan", "Updated Successfully")
    return html


def deleting_cookie(request):
    html = HttpResponse("Deleting the cookie which is set")
    html.delete_cookie("TechVidvan", "Updated Successfully")
    return html
