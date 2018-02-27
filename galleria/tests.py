from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.firstimg = Image( image_name = 'firstimg', image_description = "blaaaaaaaaaaah")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.firstimg,Image))

    #Testing Save Method
    def test_save_image(self):
        self.firstimg.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
 
    