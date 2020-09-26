from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    return render(request, "index.html")

def process_money(request):
    print('The form has been submitted')
    print(request.POST)
    if request.POST['building'] == 'farm':
        print("the farm has been visited")
    elif request.POST['building'] == 'cave':
        print("the cave has bee visited")
    elif request.POST['building'] == 'house':
        print("the house has bee visited")
    elif request.POST['building'] == 'casino':
        print("the casino has bee visited")
    
    return redirect('/') 