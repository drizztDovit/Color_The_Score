from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.cache import cache_control


def postsign(request):
    return HttpResponse("the first page")


# Rendering home page
@cache_control(no_cache=False, must_revalidate=True, no_store=True)
def home(request):
    print("home-webapp")
    return render(request, "dashboard.html")
    # if request.method == "GET":
    #     print(request.session.get('uid'))
    #     if request.session.get('uid'):
    #         return render(request, "dashboard.html")
    #     else:
    #         return redirect("/")


def user_logout():
    return None


def register():
    return None
