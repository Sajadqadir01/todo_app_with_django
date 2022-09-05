from django.shortcuts import render
from . models import Task
from .forms import CreateForm

# rendering home page and create new task
def index(request):
    query_set = Task.objects.all()
    form = CreateForm()
    if request.method == "GET":
        form = CreateForm(data=request.GET)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            task = Task.objects.create(title=title, user_id=request.user.id, complete=False)
            task.save()

    return render(request, 'index.html', {"tasks": query_set, "form":form})