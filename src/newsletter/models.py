from django.db import models

# Create your models here.
class SignUp(models.Model):
    """docstring for newsletter.models.model  def __init__(self, arg):
        super(newsletter,models.model.__init__()
        self.arg = arg"""
    email = models.EmailField()
    full_name = models.CharField(max_length=128,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated =  models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email
