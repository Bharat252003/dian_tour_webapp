from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from .forms import myform
from dian.models import Packages
# from accounts.models import User
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    cuser=User.objects.get(id=request.user.id)
    context={'pagename':'dashboard','cuser':cuser}
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.user.is_authenticated:
        return render(request,'dashboard.html',context)

def profile(request):
    context={'pagename':'profile'}
    return render(request,'profile.html',context)
def add_package(request):
    pass
#     if request.method == 'POST':
#         form = myform(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to success page or home page
#     else:
#         form = myform()
#     context={'pagename':'Create Package','form': form}
#     return render(request, 'addpackage.html',context)

def package_list(request):
    pkgs=Packages.objects.all()
    context={'pagename':'packages','packages':pkgs}
    return render(request,'package_list.html',context)

def user_list(request):
    user=User.objects.all()
    context={'pagename':'Users list','users':user}
    return render(request,'user_list.html',context)
# class PackageList(LoginRequiredMixin,ListView)
# class DeleteView(LoginRequiredMixin, DeleteView):
#     model = User
#     context_object_name = 'user'
#     template_name='user_list.html'
#     success_url = reverse_lazy('user_list')
#     def get_queryset(self):
#         owner = self.request.user
#         return self.model.objects.filter(user=owner)

def deleteUser(request, pk):
    user = User.objects.get(id=pk)

    # if request.user != User.:
    #     return HttpResponse('Your are not allowed here!!')

    # if request.method == 'POST':
    user.delete()
    return redirect('user_list')

def deletePackage(request, pk):
    package = Packages.objects.get(id=pk)
    package.delete()
    return redirect('package_list')
    return render(request, 'user_list.html', {'obj': user})

# class TaskList(LoginRequiredMixin, ListView):
#     # model = Task
#     # context_object_name = 'tasks'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = context['tasks'].filter(user=self.request.user)
#         context['count'] = context['tasks'].filter(complete=False).count()

#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['tasks'] = context['tasks'].filter(
#                 title__contains=search_input)

#         context['search_input'] = search_input

#         return context