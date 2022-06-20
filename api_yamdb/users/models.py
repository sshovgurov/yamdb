from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    USER = 'user' 
    ADMIN = 'admin' 
    MODERATOR = 'moderator' 
    CHOICES = ( 
        (USER, 'user'), 
        (ADMIN, 'admin'), 
        (MODERATOR, 'moderator'), 
    ) 
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.TextField(max_length=1, choices=CHOICES, default=USER)

    def is_admin(self): 
        return self.role == self.ADMIN 
 
    def is_moderator(self): 
        return self.role == self.MODERATOR 

    def is_user(self): 
        return self.role == self.USER