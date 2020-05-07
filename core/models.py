from django.db import models

# Create your models here.
class profile(models.Model): 
    name = models.CharField(max_length = 200) 
    img = models.ImageField(null=True, verbose_name="") 
    cover_img=models.ImageField( null=True, verbose_name="") 
    discription=models.CharField(max_length = 2000)
    education=models.CharField(max_length = 2000)
    experience=models.CharField(max_length = 2000)
    skills=models.CharField(max_length = 2000,null=True)
    linkedin_url=models.CharField(max_length = 200,null=True)

    def __str__(self): 
        return self.name
