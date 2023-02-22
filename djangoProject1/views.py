from django.shortcuts import render
from .forms import UserReg
from .forms import MembersReg

def reg(request):
    submit_button = request.POST.get("christine")
    name = ''
    email = ''
    password = ''

    reg_form = UserReg(request.POST or None)
    if reg_form.is_valid():
        name = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
    context = { 'reg_form'  : reg_form, 'name': name, 'email' :email, 'submit_button':   submit_button }
    return render(request, 'register.html', context)

def reg_members(request):
    submit_members = request.POST.get("members")
    name=''
    age=''
    phone=''
    city=''
    country=''

    reg_members_form =MembersReg(request.POST or None)
    if reg_members_form.is_valid():
        name = reg_members_form.cleaned_data.get("name")
        age= reg_members_form.cleaned_data.get("age")
        phone = reg_members_form.cleaned_data.get("phone")
        city = reg_members_form.cleaned_data.get("city")
        country= reg_members_form.cleaned_data.get("country")

    context ={'reg_members_form': reg_members_form,
              'name':name,
              'phone':phone,
              'city':city,
              'country':country
              }
    return render(request, 'members.html', context)