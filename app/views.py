from django.shortcuts import render
from django.http import HttpResponseRedirect
from app import forms

def index(request):
    if request.method == "POST":
        authUserForm = forms.AuthUserForm(request.POST)
        if authUserForm.is_valid():
            request.session['emailUser'] = authUserForm.cleaned_data["email"]
            request.session['psswdUser'] = authUserForm.cleaned_data["psswd"]
        else:
            try:
                del request.session['emailUser']
                del request.session['psswdUser']
            except KeyError:
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')


    else:
        authUserForm = forms.AuthUserForm()

    return render(
        request,
        "app/index.html",
        {"email": request.session.get('emailUser', False),
         "psswd": request.session.get('psswdUser', False),
         "statusBtnAuth": True,
         "authUserForm": authUserForm}
    )

def TeamMembers(request):
    names = ["Leha", "Doner"]
    surnames = ["Verstapen", "Hemelton"]
    data = {"names": names, "surnames": surnames, "authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/TeamMembersPage.html",
        context = data
    )

def ProjectInformation(request):
    data = {"authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/ProjectInformationPage.html",
        context=data
    )

def TeamInfo(request):
    data = {"authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/TeamInformationPage.html",
        context=data
    )

def Vacancy(request, id_vacancy):
    data = {"something": id_vacancy, "authUserForm": forms.AuthUserForm}
    return render(
        request,
        "app/Vacancy.html",
        context=data
    )

def Registration(request, type_registration):
    if request.method == "POST":
        regUserForm = forms.RegistrationUserForm(request.POST)
        regCompForm = forms.RegistrationCompanyForm(request.POST)

        if regUserForm.is_valid():
            i = 1
        else:
            i = 2
    else:
        regUserForm = forms.RegistrationUserForm()
        regCompForm = forms.RegistrationCompanyForm()

    return render(
        request,
        "app/RegistrationPage.html",
        {
        "statusBtnAuth": False,
        "regUserForm": regUserForm,
        "regCompForm": regCompForm,
        "type_registration": type_registration}
    )