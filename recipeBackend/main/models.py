from django.db import models
from loginSignup.models import MyUser
# Create your models here.
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

def upload_path_handler(instance, filename): 
    return "Recipe_Image/{title}/{file}".format(
        title=instance.Recipe.recipe_name, file=filename
    )



class Region:
    region_id   = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=50,choices=REGION_CHOICES)
    def __str__(self):
        return self.region_name

#For v2
# class Category:
#     category_id   = models.AutoField(primary_key=True)
#     category_name = models.CharField(max_length=50)#Eg-Breakfast,Lunch etc.
#     def __str__(self):
#         return self.category_name

class Ingredients:
    ingredient_id   = models.AutoField(primary_key=True)
    ingredient_name = models.CharField(max_length=50)
    def __str__(self):
        return self.ingredient_name

class Recipe:
    recipe_id          = models.AutoField(primary_key=True)
    used_by            = models.ManyToManyField(MyUser)
    owned_by           = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    recipe_name        = models.CharField(max_length=255)
    recipe_ingredients = models.ManyToManyField(Ingredients)
    recipe_steps       = models.TextField()
    recipe_image       = models.ImageField(null=True,blank=True)
    recipe_description = models.TextField()
    #recipe_category   = models.ForeignKey(Category)
    recipe_region      = models.ForeignKey(Region,null=True,blank=True)
    cooking_time       = models.TimeField()
    recipe_added_at    = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.recipe_name
    class Meta:
        ordering=['recipe_added_at',]

#FAQ's will be general for v1
class Faqs:
    question_id = models.AutoField(primary_key=True)
    question    = models.CharField(max_length=255)
    answer=models.TextField(null=False,blank=False)
    def __str__(self):
        return self.question

