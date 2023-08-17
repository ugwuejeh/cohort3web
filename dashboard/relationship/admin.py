from django.contrib import admin
from relationship.models import GeneratorSet

from .models import User, UserProfile, Author, Book, Buyer, GeneratorSet, Generator
# Register your models here.
@admin.register(UserProfile)
class Mymodel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_picture')
    
    @admin.register(User)
    class Mymodel(admin.ModelAdmin):
       list_display = ('username', 'phone_number', 'passward')
    
       @admin.register(Author)
       class Mymodel(admin.ModelAdmin):
           list_display = ('name', 'bio',)
    
           @admin.register(Book)
           class Mymodel(admin.ModelAdmin):
              list_display = ('title', 'publication_date') 
    
@admin.register(Buyer)
class Mymodel(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_n', 'address')
    
@admin.register(GeneratorSet)
class GeneratorSetAdmin(admin.ModelAdmin):
    list_display = ('name',) 

    
@admin.register(Generator)
class GeneratorAdmin(admin.ModelAdmin):
    list_display = ('model', 'capacity', 'price', 'picture')   
    
    
