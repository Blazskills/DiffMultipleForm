from unicodedata import name
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from hymnbookapp.forms import (
    ApprovedSector,
    ApprovedSector2,
    ContactForm,
    ContactForm2,
    MembershipForm,
    ProfileRegistrationForm,
    SnippetForm,
)
from hymnbookapp.models import Approved_Sector, Members, Profile, Snippet
from django.views.generic import View

# Create your views here.


def home2(request):
    context = {
        "msg": "hello world",
    }
    return render(request, "./second_template/index.html", context)


# Main page starts here


def home(request):
    context = {
        "msg": "hello world",
    }
    return render(request, "index.html", context)


def login(request):
    context = {
        "msg": "hello world",
    }
    return render(request, "login.html", context)


def approved_sector(request):
    if request.method == "POST":
        form = ApprovedSector(request.POST)
        if form.is_valid():
            sectorname = form.cleaned_data["sector_name"]
            print(sectorname)
            return redirect("approved-sector")
        print(form.errors.as_json())

    # # context = {"msg": "hello world", "formtyp": "approved_sector"}
    # form = ApprovedSector()
    # context = {"form": form, "formtyp": "approved_sector"}
    return render(request, "approved_sector/index.html")


def investor(request):
    context = {"msg": "hello world", "formtyp": "investor"}
    return render(request, "multi-form.html", context)


def startup(request):
    context = {"msg": "hello world", "formtyp": "startup"}
    return render(request, "multi-form.html", context)


# Forms.form format
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            print(name, email)
    form = ContactForm()
    return render(request, "contact.html", {"form": form})


# ModelForm format
def snippest_details(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            body = form.cleaned_data["body"]
            compayname = form.data.get("company_name")
            context = {"name": name, "body": body, "company_name": compayname}
            print(context)
            snippest_save = Snippet.objects.create(
                name=name,
                body=body,
            )
            snippest_save.save()
            return redirect("snippest")
        print(form.errors.as_json())
        return render(request, "contact.html", {"form": form})
    form = SnippetForm()
    return render(request, "contact.html", {"form": form})


# Inline format Django Form

# Class based view


class inlineformatview(View):
    def get(self, request, *args, **kwargs):
        return render(request, "inline_format/index.html")

    def post(self, request, *args, **kwargs):
        form = ContactForm2(request.POST)
        if form.is_valid():
            print(form.cleaned_data["name"], form.cleaned_data["email"])
            return redirect("inlineformat")
        return render(request, "inline_format/index.html", {"form": form})


# Sector registration here
class ApprovedSectorview(View):
    def get(self, request, *args, **kwargs):
        return render(request, "approved_sector/index.html")

    def post(self, request, *args, **kwargs):
        form = ApprovedSector2(request.POST)
        if form.is_valid():
            sectorname = form.cleaned_data["sectorname"]
            sectornamecheck = Approved_Sector.objects.create(
                sector_name=sectorname,
            )
            sectornamecheck.save()
            return redirect("approvedsector")
        print(form.errors.as_json())
        print("not valid")
        return render(request, "approved_sector/index.html", {"form": form})


# Profile registration view here
class Register_Profilesview(View):
    def get(self, request, *args, **kwargs):
        form = ProfileRegistrationForm()
        return render(request, "inline_format/profileform.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ProfileRegistrationForm(request.POST)
        if form.is_valid():
            print('valid')
            print(form.cleaned_data["startup_name"])
            print(form.cleaned_data["startup_sector"])

            print(form.cleaned_data["account_type"])

            if form.cleaned_data["startup_name"] == '' and form.cleaned_data["startup_sector"] ==None and form.cleaned_data["account_type"] =='Investor':
                print(form.cleaned_data["startup_name"],form.cleaned_data["account_type"])
                investor_startup_profile=form.save(commit=False)
                investor_startup_profile.startup_name= form.cleaned_data["account_type"]
                investor_startup_profile.save()
                print('Investor account created successfully')
                # print('startup name is empty')
            # if form.cleaned_data["startup_name"] == 'StartUp' and form.cleaned_data["account_type"] =='Investor':
            #     print('startup can not select investor as account type')
            # if form.cleaned_data["startup_name"] != '' and form.cleaned_data["account_type"] =='StartUp':
            #     # print('Startup namd is empty')
            #     print('Startup account created successfully')
            #     form.save()
            # if form.cleaned_data["startup_name"] == '' and form.cleaned_data["account_type"] =='StartUp':
            #     print('Startup name is required.')
            # else:
            #     print('Kindly file the form correctly.')      
            return redirect('profile-registeration')
        print(form.errors.as_json())
        print("not valid")
        return render(request, "inline_format/profileform.html", {"form": form})
    
    
from django.forms import formset_factory    
    
def index2(request):
    MembershipFormSet = formset_factory(MembershipForm, extra=2, max_num=20)
    if request.method == 'POST':
        print(request.POST)
        return HttpResponseRedirect('index2')
        # TODO
    else:
        initial=[]
        mydata=Members.objects.all()
        for m_data in mydata:
            initial.append({'name': m_data.name,
                            'jobs': m_data.jobs,
                            'gender': m_data.gender,
                            'email': m_data.email,
                            'phone': m_data.phone,
                            })
        formset = MembershipFormSet(initial=initial)
    return render(request,'online/index.html',{'formset':formset})
 
    





def index3(request):
    extra_forms = 1
    MembershipFormSet = formset_factory(MembershipForm, extra=extra_forms, max_num=None, can_delete=True
                                        )
    if request.method == 'POST':
        # print(request.POST)
        if 'additems' in request.POST and request.POST['additems'] == 'true':
            formset_dictionary_copy = request.POST.copy()
            formset_dictionary_copy['form-TOTAL_FORMS'] =int(formset_dictionary_copy['form-TOTAL_FORMS']) + extra_forms
            formset = MembershipFormSet(formset_dictionary_copy)
        else:
            formset = MembershipFormSet(request.POST)
            if formset.is_valid():
                for all_formaudit in formset:
                    if all_formaudit.cleaned_data:
                        Members.objects.create(
                                        name = all_formaudit.cleaned_data['name'],
                                        jobs = all_formaudit.cleaned_data['jobs'],
                                        gender = all_formaudit.cleaned_data['gender'],
                                        email = all_formaudit.cleaned_data['email'],
                                        phone = all_formaudit.cleaned_data['phone']
                                        )
                        print(all_formaudit.cleaned_data.get('name'))
                        print('form valid')
                return render(request, 'online/thanks.html')
            print('form not valid')
            print(formset.errors)
            return redirect(request.META.get('HTTP_REFERER'))
            
    else:
        initial=[]
        mydata=Members.objects.all()
        for m_data in mydata:
            initial.append({'name': m_data.name,
                            'jobs': m_data.jobs,
                            'gender': m_data.gender,
                            'email': m_data.email,
                            'phone': m_data.phone,
                            })
        formset = MembershipFormSet(initial=initial)
    return render(request,'online/index3.html',{'formset':formset})






def index4(request):
    extra_forms = 0
    MembershipFormSet = formset_factory(MembershipForm, extra=extra_forms, max_num=None
                                        )
    if request.method == 'POST':
            print(request.POST)
            formset = MembershipFormSet(request.POST)
            if all([formset.is_valid()]):
                for all_formaudit in formset:
                    if all_formaudit.cleaned_data:
                       all_formaudit.save()
                return render(request, 'online/thanks.html')
            print('form not valid')
            print(formset.errors)
            return redirect(request.META.get('HTTP_REFERER'))
             
    else:
        initial=[]
        mydata=Members.objects.all()
        for m_data in mydata:
            initial.append({'name': m_data.name,
                            'jobs': m_data.jobs,
                            'gender': m_data.gender,
                            'email': m_data.email,
                            'phone': m_data.phone,
                            })
        # formset = MembershipFormSet(initial=initial)
        formset = MembershipFormSet()
    return render(request,'online/index4.html',{'formset':formset})