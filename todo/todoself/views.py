from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from .models import task

from django.views.generic import  ListView
from django.views.generic.detail import  DetailView
from django.views.generic import UpdateView




# Create your
#
#
#     model = task views here.
def home(request):
    task1 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task2=task(name=name,priority=priority,date=date)
        task2.save()

    return render(request,'home.html',{'task':task1})
class  tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'task'
class detailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'
class taskupdateveiw(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = 'name','priority','date'
def get_success_url(self):
    return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class deleteveiw(DetailView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

# def details(request):
#
#     return render(request,'details.html')
def delete(request,taskid):
    task3=task.objects.get(id=taskid)
    if request.method=='POST':
        task3.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task3=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=task3)
    if f .is_valid():

        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task3})