from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
	role=models.CharField(max_length=20,blank=True,null=True)

class Normal_User(models.Model):
	user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
	mobile=models.IntegerField()

class Whole_Seller(models.Model):
	user=models.ForeignKey(User,related_name="whole_seller",on_delete=models.CASCADE)
	city=models.CharField(max_length=200)
	mobile=models.IntegerField()
	zip_code=models.IntegerField()
	gst_no=models.CharField(max_length=100)
class Products(models.Model):
	user=models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
	product_name=models.CharField(max_length=200)
	product_price=models.IntegerField()
	product_quantity=models.IntegerField()
	product_description=models.TextField()
	product_image=models.ImageField(upload_to='uploads/')
	product_image1=models.ImageField(upload_to='uploads/',blank=True,null=True)
	product_image2=models.ImageField(upload_to='uploads/',blank=True,null=True)
class Bank_Detail(models.Model):
	user=models.ForeignKey(User,related_name='bank_detail',on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	acc_no=models.IntegerField()
	ifcs_code=models.CharField(max_length=11)
	branch_name=models.CharField(max_length=200)
	bank_name=models.CharField(max_length=100)
class WishListss(models.Model):
	user=models.ForeignKey(User,related_name='wishlistadd',on_delete=models.CASCADE)
	product_id=models.IntegerField()
class Review(models.Model):
	user=models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
	p_id=models.IntegerField()
	headline=models.CharField(max_length=500)
	description=models.TextField()
class Blogs(models.Model):
	blog_title=models.CharField(max_length=200)
	blog_name=models.CharField(max_length=200)
	description=models.TextField()
	create_date=models.CharField(max_length=200)
	blog_image=models.ImageField(upload_to='blog/',blank=True,null=True)
class Contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	message=models.TextField()
class Query(models.Model):
	name=models.CharField(max_length=220)
	question=models.TextField()
	query_image=models.ImageField(upload_to='queryimage/',blank=True,null=True)
class Scientist_Register(models.Model):
	user=models.ForeignKey(User,related_name="Scientist",on_delete=models.CASCADE)
	mobile=models.IntegerField()
	designation=models.CharField(max_length=500)
	description=models.TextField()
class Farming_Technique(models.Model):
	user=models.ForeignKey(User,related_name="Farming_Technique",on_delete=models.CASCADE)
	heading=models.CharField(max_length=500)
	youtube_link=models.CharField(max_length=500)
	farming_description=models.TextField()
	farm_image=models.ImageField(upload_to='farm_image/',blank=True,null=True)