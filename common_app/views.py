from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'main_home.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app')
    else:
        form = UserCreationForm()
        context = {'form': form}

        return render(request, 'registration.html', context=context)
