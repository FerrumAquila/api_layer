# App Imports
from services import views as service_views
from apis import views as api_views

# Django Imports
from django.contrib import auth
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return render_to_response("core/home.html", {})


def sign_in(request):
    if request.method == "POST" and request.user.id is None:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(data={"success": True})
        else:
            return JsonResponse(data={"error": "wrong username and password"})
    else:
        return render(request, "core/sign-in.html")


# For Logout, Just LogOut User
def sign_out(request):
    auth.logout(request)
    response = HttpResponseRedirect(reverse("core-sign-in"))
    response.set_cookie(key='token', value='')
    return response


@login_required(login_url='/login/')
def dashboard(request):
    services_dashboard = service_views.ServicesListDashboard.as_view()(request)
    apis_dashboard = api_views.APIListDashboard.as_view()(request)
    services_dashboard.render()
    apis_dashboard.render()
    return render_to_response("core/dashboard.html", {
        'services_dashboard': services_dashboard,
        'apis_dashboard': apis_dashboard
    })
