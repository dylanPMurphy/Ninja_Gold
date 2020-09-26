from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "index.html")

def process_money(request):
    print('The form has been submitted')
    print(request.POST)
    if request.POST['building'] == 'farm':
        request.session['gold']+= random.randint(10,20)
        print("the farm has been visited")
    elif request.POST['building'] == 'cave':
        request.session['gold']+= random.randint(5,10)
        print("the cave has bee visited")
    elif request.POST['building'] == 'house':
        request.session['gold']+= random.randint(2,5)
        print("the house has bee visited")
    elif request.POST['building'] == 'casino':
        request.session['gold']+= random.randint(-50,50)
        print("the casino has bee visited")
    print('You now have '+str(request.session['gold']) +'gold')
    return redirect('/') 