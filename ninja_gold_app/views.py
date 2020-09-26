from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    print('The form has been submitted')
    print(request.POST)
    if request.POST['building'] == 'farm':
        num = random.randint(10,20)
        request.session['gold']+= num
        request.session['activities'].append("You earned "+ str(num) +"gold!" )
    elif request.POST['building'] == 'cave':
        num = random.randint(5,10)
        request.session['gold']+= num
        request.session['activities'].append("You earned "+ str(num) +"gold!" )
    elif request.POST['building'] == 'house':
        num = random.randint(2,5)
        request.session['gold']+= num
        request.session['activities'].append("You earned "+ str(num) +"gold!" )
    elif request.POST['building'] == 'casino': 
        num = random.randint(-50,50)
        if num > 0:
            request.session['gold'] += num
            request.session['activities'].append("You earned "+ str(num)+ " gold")
        elif num < 0:
            request.session['gold'] += num
            request.session['activities'].append("You lost "+ str(num)+ " gold")
        else:
            request.session['activities'].append("You broke even")
    print('You now have '+str(request.session['gold']) +'gold')
    return redirect('/') 