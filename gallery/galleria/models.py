from django.db import models

# Create your models here.
 

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name   

class Category(models.Model):
    category_title = models.CharField(max_length = 30)        

class Image(models.Model):
    image = models.ImageField(upload_to = '^$')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =100)
    image_location = models.ForeignKey(Location, null=True,blank=True)
    image_category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True, null=True,blank=True)

    def __str__(self):
        return self.image_name

    
    def save_image(self):
        self.save()
    @classmethod
    def search_by_category(cls,search_term):
        galleria = cls.objects.filter(image_category__icontains=search_term)

        return galleria
