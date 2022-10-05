from django.shortcuts import render, redirect
from .models import Show, User
from django.contrib import messages
import bcrypt


def new(request):
    return render(request, "new.html")

def shows(request):
    shows = Show.objects.all()
    context = {
        'shows':shows
    }
    return render(request, "shows.html",context)

def create(request):
    errors = Show.objects.validate_show(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')

    else:
        show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']
            )
        messages.success(request, "Show successfully added")

        return redirect('/shows/'+str(show.id))

def show(request,id):
    show = Show.objects.get(id = id)
    context = {
        'show': show,
    }
    return render(request,'show.html', context)

def edit(request,id):
    show = Show.objects.get(id = id)
    context = {
        'show': show,
    }
    return render(request,'edit.html', context)

def update(request,id):
    errors = Show.objects.validate_show(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(id)+'/edit')

    else:
        show = Show.objects.get(id = id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
    return redirect('/shows/'+str(id))

def destroy(id):
    show = Show.objects.get(id = id)
    show.delete()
    return redirect('/shows')

def index(request):
    return render(request,'index.html')

def success(request):
    return render(request,'success.html')

def logreg(request):
    if request.POST['logreg']== 'reg':
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name = request.POST['first_name'],
                               last_name = request.POST['last_name'],
                               email = request.POST['email'],
                               password = pw_hash
        )
        request.session['user'] = request.POST['first_name']
        return redirect('/success')
    if request.POST['logreg']== 'log':
        user  = User.objects.get(email = request.POST['email'])  
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user'] = user.first_name
            return redirect('/success')    
    return redirect('/')

def logout(request):
    del request.session['user']
    request.session.save()
    return redirect('/')

