from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class Client(models.Model):
    name=models.CharField( max_length=30)
    phone=models.PositiveIntegerField(unique=True)
    client_id_no=models.IntegerField(null=True ,blank=True)
    email=models.CharField(max_length=20,unique=True)
    def save(self,*args,**kwargs):
        if self.client_id_no is None:
            last_data=Client.objects.last()
            if last_data:
                self.client_id_no=last_data.client_id_no + 1
            else:
                self.client_id_no=1
        super(Client,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
    def client_id(self):
        return(f"{self.name[:4]}-FT-{self.client_id_no}")
    
class Course(models.Model):
    category=models.CharField(max_length=20)
    description=models.TextField()
    highlight=models.TextField()
    price=models.FloatField()
    photo=models.FileField(upload_to='images/',null=True,blank=True)
    def __str__(self):
       return self.category 
class Course_content(models.Model):
    category=models.ForeignKey(Course,on_delete=models.CASCADE)
    video_name=models.CharField(max_length=30)
    video=models.FileField(upload_to='videos/')
    def __str__(self):
        return self.video_name
    def categ(self):
        return self.category.category

class Student(models.Model):
    client=models.OneToOneField(Client,on_delete=models.CASCADE)
    course_obj=models.ForeignKey(Course,on_delete=models.CASCADE)
    amount_paid=models.FloatField()
    def password(self):
        return(f"{self.client.client_id_no}&&{self.client.email[:5]}")
    def user_id(self):
        return (f"{self.client.name[:4]}-FT-{self.client.client_id_no}")
    def __str__(self):
        return self.client.name
    def name(self):
        return self.client.name
    def course(self):
        return self.course_obj.category
    def remaining(self):
        x=float(self.course_obj.price)
        y=float(self.amount_paid)
        return (x-y)
class Leads(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__(self):
        return self.name
    