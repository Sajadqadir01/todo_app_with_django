from django.shortcuts import render, redirect
from . models import Task
from .forms import CreateForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
# rendering home page and create new task
def index(request):

    form = CreateForm()
    if request.method == "GET":
        form = CreateForm(data=request.GET)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            task = Task.objects.create(title=title, user_id=request.user.id)
            task.save()
            return redirect('/')

    return render(request, 'index.html', {"form":form})

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

            context['search_input'] = search_input
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'main/task_form.html'
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')
