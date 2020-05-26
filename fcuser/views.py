from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser

# Create your views here.

def login(request):
  if request.method == "GET":
    return render(request, 'login.html')
  elif request.method == "POST":
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    res_data = {}

    if not (username and password):
      res_data['error'] = '모든 값을 입력해야 합니다.'
    else:
      fcuser = Fcuser.objects.get(username=username)
      if check_password(password, fcuser.password):
        request.session('user')
        return redirect('/')                 # go to home 
        # Password match, process login!
        # Session!
        pass
      else:
        res_data['error'] = '비밀번호를 틀렸습니다.'

    return render(request, 'login.html', res_data)


def register(request):
  if request.method == "GET":
    return render(request, 'register.html')
  elif request.method == "POST":

    # Get value of the key & store value to variable 
    username = request.POST.get('username', None)           # POST is a dictionary type  
    useremail = request.POST.get('useremail', None)
    password = request.POST.get('password', None) 
    re_password = request.POST.get('re-password', None)

    res_data = {}

    if not (username and useremail and password and re_password):
      res_data['error'] = '모든 값을 입력해야 합니다.'
    elif password != re_password:
      res_data['error'] = '비밀번호가 다릅니다.'
    else:
      fcuser = Fcuser(
        username = username,
        useremail = useremail,
        password = make_password(password)
      )

      fcuser.save()

    return render(request, 'register.html', res_data)
  