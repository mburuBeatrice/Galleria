from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = '^$')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =100)
    # location = models.ForeignKey(Location)
    # category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
    # class Meta:
    #     ordering = ['name']    
    # try:
    #     imagey = Image.objects.get(image_description = 'xoxoxoxox')
    #     print('Image found')
    # except DoesNotExist:
    #     print('Image not found.Sorry.')    

class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.location_name      
    
