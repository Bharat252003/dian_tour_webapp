from django.db import models

# Create your models here.

class Contact(models.Model):
    yourName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.yourName


# class Destination(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.IntegerField(default = 50000)
#     days = models.IntegerField(default=1)
#     desc = models.TextField()
#     offer = models.BooleanField(default=False)
#     Domestic = models.BooleanField(default=False)
#     International = models.BooleanField(default=False)
#     img1=models.ImageField(upload_to='pics')
#     img2 = models.ImageField(upload_to='pics')
#     img3 = models.ImageField(upload_to='pics')
#     day1= models.CharField(max_length=200, blank=True, null=True)
#     day2 = models.CharField(max_length=200, blank=True, null=True)
#     day3 = models.CharField(max_length=200, blank=True, null=True)
#     day4 = models.CharField(max_length=200, blank=True, null=True)
#     day5 = models.CharField(max_length=200, blank=True, null=True)
#     day6 = models.CharField(max_length=200, blank=True, null=True)
#     day7 = models.CharField(max_length=200, blank=True, null=True)
#     day8 = models.CharField(max_length=200, blank=True, null=True)
#     day9 = models.CharField(max_length=200, blank=True, null=True)
#     day10 = models.CharField(max_length=200, blank=True, null=True)
#     day11 = models.CharField(max_length=200, blank=True, null=True)
#     day12 = models.CharField(max_length=200, blank=True, null=True)
#     day13 = models.CharField(max_length=200, blank=True, null=True)
#     day14 = models.CharField(max_length=200, blank=True, null=True)
#     day15 = models.CharField(max_length=200, blank=True, null=True)
#     day16 = models.CharField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.name
class Packages(models.Model):
    # pkg_id=models.IntegerField()
    offer = models.BooleanField(default=False)
    Domestic = models.BooleanField(default=0)
    International = models.BooleanField(default=0)
    pkg_type=models.CharField(max_length=30)
    pkg_title=models.CharField(max_length=30)
    dep_date=models.DateField()
    pkg_from=models.CharField(max_length=20)
    pkg_to=models.CharField(max_length=20)
    pkg_pic=models.ImageField(default='package.jpg',upload_to='package_imgs')
    pkg_dec=models.TextField()
    pkg_price=models.IntegerField()
    pkg_days=models.IntegerField()
    pkg_night=models.IntegerField()
    # tota_seats=models.IntegerField()
    # avil_seats=models.IntegerField()
    # pkg_img=models.ImageField(upload_to='pics',default='destination.jpg')
    day1_title= models.CharField(max_length=50, blank=True, null=True)
    day1_desc= models.TextField( blank=True, null=True)
    day2_title= models.CharField(max_length=50, blank=True, null=True)
    day2_desc= models.TextField( blank=True, null=True)
    day3_title= models.CharField(max_length=50, blank=True, null=True)
    day3_desc= models.TextField( blank=True, null=True)
    day4_title= models.CharField(max_length=50, blank=True, null=True)
    day4_desc= models.TextField( blank=True, null=True)
    day5_title= models.CharField(max_length=50, blank=True, null=True)
    day5_desc= models.TextField( blank=True, null=True)
    day6_title = models.CharField(max_length=200, blank=True, null=True)
    day6_desc= models.TextField( blank=True, null=True)
    day7_title = models.CharField(max_length=200, blank=True, null=True)
    day7_desc= models.TextField( blank=True, null=True)
    day8_title = models.CharField(max_length=200, blank=True, null=True)
    day8_desc= models.TextField( blank=True, null=True)
    day9_title = models.CharField(max_length=200, blank=True, null=True)
    day9_desc= models.TextField( blank=True, null=True)
    day10_title = models.CharField(max_length=200, blank=True, null=True)
    day10_desc= models.TextField( blank=True, null=True)
    day11_title = models.CharField(max_length=200, blank=True, null=True)
    day11_desc= models.TextField( blank=True, null=True)
    day12_title = models.CharField(max_length=200, blank=True, null=True)
    day12_desc= models.TextField( blank=True, null=True)
    day13_title = models.CharField(max_length=200, blank=True, null=True)
    day13_desc= models.TextField( blank=True, null=True)
    day14_title = models.CharField(max_length=200, blank=True, null=True)
    day14_desc= models.TextField( blank=True, null=True)
    day15_title = models.CharField(max_length=200, blank=True, null=True)
    day15_desc= models.TextField( blank=True, null=True)
    day16_title = models.CharField(max_length=200, blank=True, null=True)
    day16_desc= models.TextField( blank=True, null=True)
    pkg_status=models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.pkg_title

class ConfirmBooking(models.Model):
    fullName = models.CharField(max_length=200,default="")
    fromCity = models.CharField(max_length=100)
    toCity = models.CharField(max_length=100)
    pkg_title=models.CharField(max_length=100,default='')
    depatureDate = models.DateField()
    days = models.IntegerField(default=1)
    noOfRooms = models.IntegerField()
    noOfAdults = models.IntegerField()
    noOfChildren = models.IntegerField()
    email = models.EmailField(max_length=254)
    phoneNo = models.CharField(max_length=12)
    amountPerPerson = models.IntegerField(default=0)
    totalAmount = models.FloatField(default=0)
    userName = models.CharField(max_length=200, default="")
    date = models.DateField(("Date"), auto_now_add=True)
    cancel=models.BooleanField(default=0)
    cancel_reason=models.TextField(default='')


    def __str__(self):
        return self.fullName

#class Payment(models.Model):
#     payment_id=models.AutoField(primary_key=True)
#     customer_name=models.ForeignKey(ConfirmBooking,on_delete=models.CASCADE, related_name='payments_by_customer_num',
#         verbose_name=('Customer Number'))
#     customer_num=models.ForeignKey(ConfirmBooking,on_delete=models.CASCADE, related_name='payments_by_customer_name',verbose_name=('Customer Name'))
#     payment_amount=models.IntegerField()
#     paid=models.BooleanField(default=False)

#     class meta:
#         verbose_name = ('Payment')
#         verbose_name_plural = ('Payments') 

class Payment(models.Model):
    payment_id=models.AutoField(primary_key=True)
    name=models.ForeignKey(ConfirmBooking,on_delete=models.CASCADE, related_name='payments_by_customer_num',
        verbose_name=('Customer Number'))
    num=models.ForeignKey(ConfirmBooking,on_delete=models.CASCADE, related_name='payments_by_customer_name',verbose_name=('Customer Name'))
    payment_amount=models.IntegerField()
    paid=models.BooleanField(default=False)
    razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_sign=models.CharField(max_length=100,null=True,blank=True)

    class meta:
        verbose_name = ('Payment')
        verbose_name_plural = ('Payments')
 
class Feedback(models.Model):
    name=models.CharField(max_length=20)
    message=models.TextField()
