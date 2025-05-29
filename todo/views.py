from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# create todo_list

class CreateTodoView(LoginRequiredMixin, generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# read list detail
class TodoListView(LoginRequiredMixin, generic.ListView):
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'
    model = models.TodoModel
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by('-id')
 
    
class TodoDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo_id'
    
    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id, user=self.request.user)
    
# update todo
class UpdateTodoView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'
    
    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id, user=self.request.user)

    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)


# delete TodoTask
class DeleteTodoView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'
    
    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id, user=self.request.user)