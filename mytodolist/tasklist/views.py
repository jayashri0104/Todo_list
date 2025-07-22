from django.shortcuts import render,redirect, get_object_or_404
from  django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Task
from django.urls import reverse_lazy

from django.views import View  

class listView(ListView):
    model = Task
    template_name = "list.html"
    context_object_name ='tasks'
    
class DeleteView(DeleteView):
    model = Task
    template_name = "delete.html"  
    success_url = reverse_lazy('list')
    
class UpdateView(UpdateView):
    model = Task
    fields = ['title']
    template_name = "edit.html" 
    success_url = reverse_lazy('list')
    
class cheack(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done 
        task.save()
        return redirect(reverse_lazy('list'))

class Create(CreateView): 
    model = Task
    fields = ['title']
    template_name = "create.html" 
    success_url = reverse_lazy('list')