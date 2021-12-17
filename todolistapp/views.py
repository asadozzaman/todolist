from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from  .models import Task
from .forms import TaskForm

# Create your views here.
@login_required
def index(request):
        task_list = Task.objects.all()
        # template = loader.get_template('food/index.html')
        context = {
                'task_list': task_list
        }
        # return HttpResponse(template.render(context,request))
        return render(request, 'index.html', context)

@login_required
def create_item(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return  redirect('todolistapp:index')

    return render(request,'task-form.html',{'form': form})