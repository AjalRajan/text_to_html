from django.shortcuts import render
from .models import Editor
from .forms import editform

def index(requset):

	form = editform()

	return render(requset , 'index.html', {'form':form})
# Create your views here.
