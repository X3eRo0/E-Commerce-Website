from django.db import models

import random
import os



def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext



def upload_image_path(instance,filename):
    new_filename=random.randint(1,3901029312)
    name,ext=get_filename_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "image_url/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename)


class ProductManager(models.Manager):
    def get_by_id(self,id):
       if qs.count()==1:
           return qs.first()
       return None

# Create your models here.
class Product(models.Model):
    brand=models.CharField(max_length=120)
    title=models.CharField(max_length=120)
    processor=models.CharField(max_length=120)
    RAM= models.CharField(max_length=120)
    storage=models.CharField(max_length=120)
    OS=models.CharField(max_length=120)
    image1=models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    image2=models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    image3=models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    slug=models.SlugField(blank=True,null=True,unique=True)
    #featured=models.BooleanField(default=False)
    objects=ProductManager()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "product/{slug}/".format(slug=self.slug)
    

