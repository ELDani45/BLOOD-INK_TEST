from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm


# def login_user(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = AuthenticationForm()
#     return render(request, "login", {"form": form})


# def logout_user(request):
#     logout(request)
#     return redirect("logout")

def login(request):
    return render(request, "login.html")
