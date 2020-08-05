from django.db import models

class Location(models.Model):
    name = models.CharField(max_length =25) 
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()    

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length =25)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

    def __str__(self):
        return self.name
   

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    image_name = models.CharField(max_length =25)
    image_description = models.TextField(max_length =250)
    image_location = models.ForeignKey(Location,on_delete=callable)
    image_category = models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()  

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(image_category__name__icontains=search_term)
        return gallery      

    @classmethod
    def retrive_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.get(pk=id)
        return images