from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.forms import *
from functools import partial, wraps
from .forms import *
from .models import *

def welcome(request):
    try:
        t = TemplateModel.object.filter(user = request.user).values()[0]['Temp']
        t = "True"
    except:
        t = "False"
    
    return render(request, "resume/welcome.html", {"flag":t})

def link(request, user_username):
    link = f"https://tegacvmaster.herokuapp.com/{request.user.username}/template"
    return render(request, "resume/link.html", {"link":link})

def template(request, user_username):
    person = PersonalInfoModel.object.filter(user = request.user)
    numberst = str(person.values()[0]['Number'])
    number1 = numberst[0:3]
    number2 = numberst[3:6]
    number3 = numberst[6:10]
    education = EducationModel.object.filter(user = request.user)
    experience = ExperienceModel.object.filter(user = request.user)
    project = ProjectModel.object.filter(user = request.user)
    involve = InvolvementModel.object.filter(user = request.user)
    skill = SkillModel.object.filter(user = request.user)
    template = TemplateModel.object.filter(user = request.user)
    t = TemplateModel.object.filter(user = request.user).values()[0]['Temp']
    return render(request, "lumia"+"/index.html", {'education':education, 
                                                    'experience':experience,
                                                    'proj':project,
                                                    'involve':involve,
                                                    'person':person,
                                                    'skill':skill,
                                                    'temp':template,
                                                    'number1':number1,
                                                    'number2':number2,
                                                    'number3':number3,})

@login_required
def register_edu (request):

    #Education
    education = modelformset_factory(model = EducationModel, form = EducationForm, exclude=('user',))

    if request.method == 'POST':

        EducationModel.object.filter(user = request.user).delete()
        education_set = education(request.POST, prefix = "education")

        if education_set.is_valid():

            for e in education_set:
                inst = e.save(commit = False)
                inst.user = request.user
                inst.save()
            
    else:

        education_set = education(queryset = EducationModel.object.none(), prefix = "education")

    #Experience
    experience = modelformset_factory(model = ExperienceModel, form = ExperienceForm, exclude=('user',))

    if request.method == 'POST':

        ExperienceModel.object.filter(user = request.user).delete()
        experience_set = experience(request.POST, prefix = "experience")

        if experience_set.is_valid():

            for ex in experience_set:
                inst = ex.save(commit = False)
                inst.user = request.user
                inst.save()

    else:

        experience_set=experience(queryset = ExperienceModel.object.none(), prefix = "experience")

    #Project
    proj = modelformset_factory(model = ProjectModel, form = ProjectForm, exclude=('user',))

    if request.method == 'POST':

        ProjectModel.object.filter(user = request.user).delete()
        proj_set = proj(request.POST, prefix = "project")

        if proj_set.is_valid():

            for pr in proj_set:
                inst = pr.save(commit = False)
                inst.user = request.user
                inst.save()

    else:

        proj_set=proj(queryset = ProjectModel.object.none(), prefix = "project")

    #Involve
    involve = modelformset_factory(model = InvolvementModel, form = InvolvementForm, exclude=('user',))

    if request.method == 'POST':

        InvolvementModel.object.filter(user = request.user).delete()
        involve_set = involve(request.POST, prefix = "involve")

        if involve_set.is_valid():

            for i in involve_set:
                inst = i.save(commit = False)
                inst.user = request.user
                inst.save()

    else:

        involve_set=involve(queryset = InvolvementModel.object.none(), prefix = "involve")

    #Personal
    if request.method == 'POST':

        PersonalInfoModel.object.filter(user = request.user).delete()
        person=PersonalInfoForm(request.POST, request.FILES, user=request.user)

        if person.is_valid():
            person.save()

    else:
        person=PersonalInfoForm(user=request.user)

    #Skills
    if request.method == 'POST':

        SkillModel.object.filter(user = request.user).delete()
        skill=SkillForm(request.POST, user=request.user)

        if skill.is_valid():
            skill.save()
            
    else:
        skill=SkillForm(user=request.user)

    #Templates
    if request.method == 'POST':

        TemplateModel.object.filter(user = request.user).delete()
        temp=TemplateForm(request.POST, user=request.user)

        if temp.is_valid():
            temp.save()

        t = TemplateModel.object.filter(user = request.user).values()[0]['Temp']
        return redirect(f"/{request.user.username}/link", user=request.user)

    else:
        temp=TemplateForm(user=request.user)

    return render(request, "resume/register.html", {'education':education_set, 
                                                    'experience':experience_set,
                                                    'proj':proj_set,
                                                    'involve':involve_set,
                                                    'person':person,
                                                    'skill':skill,
                                                    'temp':temp})











