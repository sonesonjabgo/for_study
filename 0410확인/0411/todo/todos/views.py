from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-pk')
    context = {'todos': todos}
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        # request에서 데이터 받아와서 db에 저장
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            # author가 user 모델을 참조하기 때문에 null값임
            # null 값으로 두면 안되기 때문에 저장 전에 author에 값을
            todo.author = request.user
            todo.save()
            return redirect('todos:detail', todo.pk)
            # return redirect('todos:index')

    else:
        # todo를 입력할 수 있는 화면 보여주기
        form = TodoForm()
    context = {'form': form}
    return render(request, 'todos/create.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {'todo': todo}
    return render(request, 'todos/detail.html', context)

@require_POST
def update(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.author == request.user:
        todo.completed = not todo.completed
        todo.save()
        return redirect('todos:detail', todo.pk)
    else:
        return redirect('todos:index')

@require_POST
def delete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.author == request.user:
        todo.delete()
    return redirect('todos:index')