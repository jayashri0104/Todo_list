from django.shortcuts import render,redirect, get_object_or_404
from  django.views.generic import ListView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm 

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
    form_class = TaskForm 
    template_name = "edit.html" 
    
    success_url = reverse_lazy('list')