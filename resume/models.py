from django.db import models
from django.contrib.auth.models import User



class ModelQuerySet(models.QuerySet):

    def UsersAccount(self,user):
        return self.filter(user=user)

class PersonalInfoModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, default="")
    balanced_image = models.ImageField(blank=True, default="")
    Profile = models.TextField( verbose_name="Profile")
    Name=models.CharField(max_length=30, default="")
    Number=models.IntegerField(default="")
    Email=models.EmailField(default="")
    Address=models.CharField(max_length=150,default="")
    LinkedIn=models.CharField(max_length=50,default="")
    object=ModelQuerySet.as_manager()
    

class EducationModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    School=models.CharField(max_length=50)
    Major=models.CharField(max_length=30)
    Minor=models.CharField(max_length=30, default="")
    Coursework=models.TextField( verbose_name="Course Work")
    object=ModelQuerySet.as_manager()

class ExperienceModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Organization=models.CharField(max_length=50)
    Startdate=models.DateField(verbose_name="Start Date")
    Enddate=models.DateField(verbose_name="End Date")
    Role=models.CharField(max_length=50)
    Information=models.TextField( verbose_name="Details")
    object=ModelQuerySet.as_manager()

class ProjectModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=30,default="")
    Infromation=models.TextField(default="", verbose_name="Details")
    object=ModelQuerySet.as_manager()

class InvolvementModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Organization=models.CharField(max_length=50)
    Startdate=models.DateField(verbose_name="Start Date")
    Enddate=models.DateField(verbose_name="End Date")
    Role=models.CharField(max_length=50)
    Information=models.TextField( verbose_name= "Details")
    object=ModelQuerySet.as_manager()

class SkillModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Information=models.TextField(verbose_name= "Details")
    object=ModelQuerySet.as_manager()

TEMP_CHOICES = (
    ('lumia','Lumia'),
    ('office','Office'),
    ('personal','Personal'),
    ('iportfolio','IPortfolio'),
    ('dewi','Dewi')
)
class TemplateModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Temp = models.CharField(max_length=30,choices=TEMP_CHOICES, default='',verbose_name="Pick Your Template")
    object = ModelQuerySet.as_manager()

