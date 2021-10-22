import random
from django.shortcuts import render, redirect

def index1(request):
    request.session['total_gold']=0
    request.session['grammar_nazi']='coins'
    request.session['your_actions'] = []
    return redirect("/redirect")

def index6(request):
    return render(request,"main_page.html")

def index7(request):
    new_list = request.session['your_actions']
    if request.POST['income'] == "farm":
        new_list = request.session['your_actions']
        earned_gold=random.randint(10,20)
        new_list.append(f'Visited farm, earned {earned_gold} gold coins')
        request.session['total_gold']+=earned_gold
        request.session['your_actions'] = new_list
    elif request.POST['income'] == "cave":
        new_list = request.session['your_actions']
        earned_gold=random.randint(5,10)
        new_list.append(f'Visited cave, earned {earned_gold} gold coins')
        request.session['total_gold']+=earned_gold
        request.session['your_actions'] = new_list
    elif request.POST['income'] == "house":
        new_list = request.session['your_actions']
        earned_gold=random.randint(2,5)
        new_list.append(f'Visited house, earned {earned_gold} gold coins')
        request.session['total_gold']+=earned_gold
        request.session['your_actions'] = new_list
    else: #request.POST['income'] == "casino":
        new_list = request.session['your_actions']
        earned_gold=random.randint(-50,50)
        if earned_gold<0:
            lost_gold=earned_gold*(-1)
            if lost_gold == 1:
                new_list.append(f'Visited casino, lost {lost_gold} gold coin')
            else:
                new_list.append(f'Visited casino, lost {lost_gold} gold coins')
        else:
            if earned_gold == 1:
                new_list.append(f'Visited casino, earned {earned_gold} gold coin')  
            else:          
                new_list.append(f'Visited casino, earned {earned_gold} gold coins')  
        request.session['total_gold']+=earned_gold
        request.session['your_actions'] = new_list
    if request.session['total_gold'] == 1 or request.session['total_gold'] == -1:
        request.session['grammar_nazi'] = 'coin'
    else:
        request.session['grammar_nazi'] = 'coins'
    return redirect("/redirect")




