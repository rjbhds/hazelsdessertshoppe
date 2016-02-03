# import string
import os

from hazelsdessertshoppe.utils import get_guid32, get_ext

from django.db import models

def get_default_category():
    
    return Category.objects.get(category='Miscellaneous')

def get_image_file_path(instance, filename):

    file_folder = "products"
    file_name = '{}.{}'.format(get_guid32(),get_ext(filename))
    
    return os.path.join(file_folder, file_name)
    
class Category(models.Model):
    
    category = models.CharField(
        max_length = 40
    )

    def __str__(self):
        
        return self.category
    
class Product(models.Model):
    
    name = models.CharField(
        max_length = 100
    )
    description = models.CharField(
        max_length = 300
    )
    price = models.FloatField(
        max_length = 300
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET(get_default_category)
    )
    image = models.ImageField(
        upload_to=get_image_file_path,
        null=True,
        blank=True
    )
    not_in_season = models.BooleanField(
        default = False
    )

#     def image_name(self):
#         
#         retval = self.name.lower()
#         transtable = str.maketrans(' ','_', string.punctuation)
#         retval = retval.translate(transtable).replace('__','_')
# 
#         return retval
#     
    def __str__(self):
        
        return self.name
    
# if __name__ == '__main__':
#     
#     s = 'This.  String-Has! \'Punc_tu$a%tion/'.lower()
#     transtable = str.maketrans(' ','_', string.punctuation)
#     s = s.translate(transtable).replace('__','_')
#     print(s)
#     