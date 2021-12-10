from django.db import models
from loginSignup.models import MyUser
# Create your models here.

def upload_path_handler(instance, filename): 
    return "Recipe_Image/{title}/{file}".format(
        title=instance.Recipe.recipe_name, file=filename
    )
"""
class Region(models.Model):
    region_id   = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=50,choices=REGION_CHOICES)
    def __str__(self):
        return self.region_name
        """
#For v2
# class Category:
#     category_id   = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=50)#Eg-Breakfast,Lunch etc.
#     def __str__(self):
#         return self.category_name



class Recipe(models.Model):
    REGION_CHOICES=(
    ('No State','No State'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal')
)
    recipe_id          = models.AutoField(primary_key=True)
    #used_by            = models.ManyToManyField(MyUser)
    owned_by           = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    recipe_name        = models.CharField(max_length=255)
    
    recipe_steps       = models.TextField()
    recipe_image       = models.ImageField(null=True,blank=True)
    recipe_description = models.TextField()
    #recipe_category   = models.ForeignKey(Category)
    recipe_region      = models.CharField(max_length=255,choices=REGION_CHOICES,default='No State')
    cooking_time       = models.CharField(max_length=255) #should make this into a integer or decimal field 
    recipe_added_at    = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.recipe_name
    class Meta:
        ordering=['recipe_added_at',]

#FAQ's will be general for v1
class Faqs(models.Model):
    question_id = models.AutoField(primary_key=True)
    question    = models.CharField(max_length=255)
    answer=models.TextField(null=False,blank=False)
    def __str__(self):
        return self.question

class Ingredients(models.Model):
    ingredient_id   = models.AutoField(primary_key=True)
    recipe_id=models.IntegerField()
    ingredient_name = models.CharField(max_length=50)
    def __str__(self):
        return self.ingredient_name

