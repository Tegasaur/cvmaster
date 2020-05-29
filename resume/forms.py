from django import forms
from .models import *


class PersonalInfoForm(forms.ModelForm):
    profile_image = forms.ImageField(label='Profile Pic',
                             widget=forms.FileInput(attrs={'class': '','style':'background: #ef6603; border: solid 0.5px grey; border-radius: 100px;'}))                            
    balanced_image = forms.ImageField(label='Background Pic',
                             widget=forms.FileInput(attrs={'class': '','style':'background: #ef6603; border: solid 0.5px grey; border-radius: 100px;'}))

    class Meta: 
        model=PersonalInfoModel
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(PersonalInfoForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(PersonalInfoForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst


class EducationForm(forms.ModelForm):

    class Meta:
        model=EducationModel
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        #self._user = kwargs.pop('user')
        super(EducationForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     inst = super(EducationForm, self).save(commit=False)
    #     # inst.user = self._user
    #     if commit:
    #         inst.save()
    #         self.save_m2m()
    #     return inst


class ExperienceForm(forms.ModelForm):
    Startdate= forms.DateField(widget=forms.DateInput(format=('%m/%d/%Y'),
                               attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
                               label="Start Date")
    Enddate= forms.DateField(widget=forms.DateInput(format=('%m/%d/%Y'), 
                             attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
                             label="End Date")

    class Meta:
        model=ExperienceModel
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        #self._user = kwargs.pop('user')
        super(ExperienceForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     inst = super(ExperienceForm, self).save(commit=False)
    #     # inst.user = self._user
    #     if commit:
    #         inst.save()
    #         self.save_m2m()
    #     return inst


class  ProjectForm(forms.ModelForm):
    class Meta:
        model=ProjectModel
        exclude=('user',)

    def __init__(self, *args, **kwargs):
        #self._user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     inst = super(ProjectForm, self).save(commit=False)
    #     # inst.user = self._user
    #     if commit:
    #         inst.save()
    #         self.save_m2m()
    #     return inst


class InvolvementForm(forms.ModelForm):
    Startdate= forms.DateField(widget=forms.DateInput(format=('%m/%d/%Y'),
                               attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
                               label="Start Date")
    Enddate= forms.DateField(widget=forms.DateInput(format=('%m/%d/%Y'), 
                             attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
                             label="End Date")

    class Meta:
        model=InvolvementModel
        exclude=('user',)
    
    def __init__(self, *args, **kwargs):
        #self._user = kwargs.pop('user')
        super(InvolvementForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     inst = super(InvolvementForm, self).save(commit=False)
    #     # inst.user = self._user
    #     if commit:
    #         inst.save()
    #         self.save_m2m()
    #     return inst


class SkillForm(forms.ModelForm):
    class Meta:
        model=SkillModel
        exclude=('user',)
    
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(SkillForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(SkillForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

class TemplateForm(forms.ModelForm):
    class Meta:
        model = TemplateModel
        fields = ['Temp']

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(TemplateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(TemplateForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst