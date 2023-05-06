from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeamForm, UserForm, UserLoginForm
from .models import Teams, Users
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate
#home view for posts. Posts are displayed in a list
class TeamIndexView(ListView):
    template_name='Crud/index.html'
    context_object_name = 'team_list'
    def get_queryset(self):
        return Teams.objects.all()
#Detail view (view post detail)
class TeamDetailView(DetailView):
    model=Teams
    template_name = 'Crud/team-detail.html'
#New post view (Create new post)
def teamview(request):
 if request.method == 'POST':
  form = TeamForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index')
 form = TeamForm()
 return render(request,'Crud/team.html',{'form': form})
#Edit a post
def edit(request, pk, template_name='Crud/edit.html'):
    post= get_object_or_404(Teams, pk=pk)
    form = TeamForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})
#Delete team
def delete(request, pk, template_name='Crud/confirm_delete.html'):
    post= get_object_or_404(Teams, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object':post})

class UserIndexView(ListView):
    template_name='Crud/index1.html'
    context_object_name = 'user_list'
    def get_queryset(self):
        return Users.objects.all()
#Detail view (view post detail)
class UserDetailView(DetailView):
    model=Users
    context_object_name = 'user_list'
    template_name = 'Crud/user-detail.html'
#New post view (Create new post)
def userview(request):
 if request.method == 'POST':
  form = UserForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('index1')
 form = UserForm()
 return render(request,'Crud/user.html',{'form': form})
#Edit a post
def edit1(request, pk, template_name='Crud/edit_user.html'):
    post= get_object_or_404(Users, pk=pk)
    form = UserForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index1')
    return render(request, template_name, {'form':form})
#Delete team
def delete1(request, pk, template_name='Crud/confirm_delete_user.html'):
    post= get_object_or_404(Users, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('index1')
    return render(request, template_name, {'object':post})

def links(request):
    context = {
        'links': [
            {'name': '/login', 'url': 'http://127.0.0.1:8000/login/'},
            {'name': '/user', 'url': 'http://127.0.0.1:8000/users/'},
            {'name': '/team', 'url': 'http://127.0.0.1:8000/teams/'}
        ]
    }
    return render(request, 'Crud/links.html', context)

def home(request):
    return render(request, 'Crud/home.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['UserName']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('links')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'Crud/login.html', {'form': form})