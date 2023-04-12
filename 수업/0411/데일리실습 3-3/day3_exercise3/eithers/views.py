from django.shortcuts import render
from .models import Question
from .forms import QuestionForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.mothod == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = 
    else:
        form = QuestionForm()
    
    context = {'form': form}
    return render(request, 'eithers/create.html', context)

def random(request):
    return

def detail(request):
    return

def comment(request):
    return