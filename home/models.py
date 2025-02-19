from django.db import models

# Create your models here.
class Header(models.Model):
    logo = models.ImageField(upload_to='logo/')
    logo_2 = models.ImageField(upload_to='logo/')
    color = models.CharField(max_length=150)
    
    def __str__(self):
        return self.color
    
        
    class Meta:
        verbose_name_plural='1. Header'

class Web_Slider(models.Model):
    web_image = models.ImageField(upload_to='logo/')
    mobile_image = models.ImageField(upload_to='logo/')
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return self.title
    
        
    class Meta:
        verbose_name_plural='2. Web Slider'