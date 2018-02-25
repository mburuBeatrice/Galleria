from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.new_image = Image( image_name = 'firstimg', image_description = "blaaaaaaaaaaah")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    #Testing Save Method
    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 

    def test_delete_image(self):
        self.new_image.save_image()
        test_image =  Image( image_name = 'secondimg', image_description = "blah")
        test_image.save_image()

        self.new_image.delete_image()# Deleting a contact object
        self.assertEqual(len(images),1)    
    