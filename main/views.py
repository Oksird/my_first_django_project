from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm

tasks = Task.objects.order_by('-id')
task_id = 0


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверное'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create.html', context)


def delete_task(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()

    return redirect('home')


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm(instance=task)

        return render(request, 'main/update_task.html',{'form':form})


def error_404_view(request, exception):
    return render(request, 'main/404.html')


