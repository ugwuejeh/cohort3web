from django.db import models


class User(models.Model):
    username= models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    passward = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    
     
class UserProfile(models.Model):
   
    # Fields for user profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    
    def __str__(self):
       return self.first_name
   

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    phone_n = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    
   
    

    def __str__(self):
        return self.name

class GeneratorSet(models.Model):
    name = models.CharField(max_length=100)
    generators = models.ManyToManyField('relationship.Generator', related_name='generator_sets')
   # Ensure this field is defined correctly

    def __str__(self):
        return self.name

class Generator(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='generator_pictures', null=True, blank=True)
    buyers = models.ManyToManyField(Buyer)
    
    
    
    def __str__(self):
        return self.capacity
    

  



