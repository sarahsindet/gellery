from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImageTestClass(TestCase):

    #setup method
     '''
    Set up method to run before each test cases.
    '''
    def setUp(self):
        naivasha = Location(name='kenya')
        naivasha.save()
        cat = Category(name='flowers')
        cat.save()
        
        self.lilies= Image(image = 'jpg', image_name= 'lilies', image_description= 'flowers', image_location= naivasha,image_category=cat)
        self.lilies.save()

    #test instance
    def test_instance(self):
    '''
    This test tests if an object is initialized properly.
    '''
        self.assertTrue(isinstance(self.lilies,Image))

    #save method
    def test_save_method(self):
    '''
    This is to to test if images are saved.
    '''    
        self.lilies.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    
    #delete method
    def delete_image_method(self):
    '''
    This is to test if an image can be deleted.
    '''    
        self.lilies.save_image()
        self.lilies.delete_image()
        images = Image.objects.all()   
        self.assertTrue(len(images) == 0) 

    # retrieve all images
    def test_can_retrieve_all_images(self):
    '''
    This is to test if one can retrieve all images.
    '''    
        self.lilies.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 1) 

    # test update method
    def test_can_update_images(self):
    '''
    This is to test if one can update images.
    '''    
        self.lilies.save_image()
        cat = Image.objects.filter(image_name='Lilies').update(image_name= 'LILIES')
        fetch_cat = Image.objects.get(image_name='LILIES')
        self.assertEqual(fetch_cat.image_name,'LILIES')
       

class LocationTestClass(TestCase):
    def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
        self.naivasha = Location(name = 'Naivasha')
       
    def test_save_method(self):
    '''
    Save method to save locations.
    '''    
        self.naivasha.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    #delete method
    def delete_location_method(self):
    '''
    Delete method to delete locations.
    '''    
        self.naivasha.save_location()
        self.naivasha.delete_location()
        locations = Location.objects.all()   
        self.assertTrue(len(locations) == 0)     

class CategoryTestClass(TestCase):
    def setUp(self):
    '''
    Set up method to run before each test cases.
    '''    
       self.flowers = Category(name='flowers')

    #save method
    def test_save_method(self):
    '''
    Save method to save all categories.
    '''    
        self.nature.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) > 0)

    #delete method
    def test_delete_method(self):
    '''
    Delete method to delete categories.
    '''    
        self.nature.save_category()
        self.nature.delete_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys) == 0)     
