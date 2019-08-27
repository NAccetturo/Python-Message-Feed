from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import user, message, comment
from time import gmtime, strftime
import random, datetime, bcrypt

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    if 'logged_in_id' in request.session:
        return redirect("/success")
    else:
        return render(request,'the_wall_app/register.html')

def success(request):
    if 'logged_in_id' in request.session:
        this_message = user.objects.all()
        grab_id = request.session['logged_in_id']
        context = {
            "user": user.objects.filter(id = grab_id),
            "messages": message.objects.all()
        }
        print("In like Flynn")
        return render(request,'the_wall_app/wall.html', context)
    else:
        return render(request,'the_wall_app/register.html')

def validate_login(request):
    if request.method == "POST":
        errors = user.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                error.error(request, value)
            return redirect("/")
        request.session['user'] = user.objects.filter(email= request.POST['email'])[0].first_name
        request.session['logged_in_id'] = user.objects.filter(email= request.POST['email'])[0].id
        return redirect("/success")
            # return redirect("/sign_in_user")

def create_new_message(request):
    if request.method == "POST":
        print(request.POST)
        errors = message.objects.message_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                error.error(request, value)
            return redirect("/")
        else:
            print("before message create")
            grab_id = request.session['logged_in_id']
            message_sender = user.objects.filter(id= grab_id)
            message.objects.create(message_content= request.POST['message_content'], message_owner= user.objects.filter(id= grab_id)[0])
            # the_message = message.objects.last()
            #  message_owner= message_sender[0].id
            # the_message.message_owner.add()
            return redirect("/")
    return redirect("/")

def create_new_comment(request):
    if request.method == "POST":
        print(request.POST)
        errors = message.objects.comment_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                error.error(request, value)
            return redirect("/")
        else:
            print("before comment create")
            grab_id = request.session['logged_in_id']
            comment_sender = user.objects.filter(id= grab_id)
            print(request.POST['message_comment'])
            message_id = request.POST['message_comment']
            this_message = message.objects.filter(id = message_id)
            comment.objects.create(comment_content= request.POST['comment_content'], comment_owner= user.objects.filter(id= grab_id)[0], message_attached= message.objects.filter(id = message_id)[0])
            # the_message = message.objects.last()
            #  message_owner= message_sender[0].id
            # the_message.message_owner.add()
            return redirect("/")
    return redirect("/")

def create_new_user(request):
    if request.method == "POST":
        print(request.POST)
        errors = user.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                error.error(request, value)
            return redirect("/")
        else:
            print("before user create")
            password = request.POST['password']
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            # new_user = {
            #     "first_name": request.POST['first_name'],
            #     "last_name": request.POST['last_name'],
            #     "email": request.POST['email'],
            #     "password": hashed_password,
            # }
            user.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], email= request.POST['email'], password= hashed_password)
            print("Ran past user create")
    print("finished create new user")
    request.session['user'] = request.POST["first_name"]
    new_user = user.objects.last()
    request.session['logged_in_id'] = new_user.id
    return redirect("/success")

def reset(request):
    if 'logged_in_id' in request.session:
        del request.session['logged_in_id']
    else:
        print("NO LOGGY")
    if 'user' in request.session:
        del request.session['user']
    else:
        print("NO LOGGY")
    return redirect("/")
