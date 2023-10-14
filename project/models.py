from django.db import models

# Create your models here.
class Icecreams(models.Model):
    icecream_ID=models.IntegerField(primary_key=True)
    icecream_name=models.CharField(max_length=20)

    def __str__(self):
        return self.icecream_name
    
    class Meta:
        verbose_name_plural = "Ice creams"

class Products(models.Model):
    product_ID=models.IntegerField(primary_key=True)
    icecream_ID=models.ForeignKey(Icecreams,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=15)
    quantity=models.FloatField()
    units=models.CharField(max_length=10,default="litre")
    cost_per_item=models.FloatField()
    date_time=models.CharField(max_length=20)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Products"

class Outlets(models.Model):
    outlet_ID=models.IntegerField(primary_key=True)
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "Outlets"

class Outlets_Purchase(models.Model):
    outlet_PID=models.IntegerField(primary_key=True)
    outlet_ID=models.ForeignKey(Outlets,on_delete=models.CASCADE)
    icecream_ID=models.ForeignKey(Icecreams,on_delete=models.CASCADE)
    quantity_of_purchase=models.FloatField()
    date_time1=models.CharField(max_length=50)

    

    class Meta:
        verbose_name_plural = "outlets purchase"

class Extra_Cost(models.Model):
    cost_ID=models.IntegerField(primary_key=True)
    water_bill=models.FloatField()
    electricity_bill=models.FloatField()
    maintanence_bill=models.FloatField()
    transportation_cost=models.FloatField()

    def __str__(self):
        return self.cost_ID

    class Meta:
        verbose_name_plural = "extra cost"

class Login(models.Model):
    ID=models.IntegerField(primary_key=True)
    login_ID=models.CharField(max_length=30)
    password_user=models.CharField(max_length=10,default="anything")

    def __str__(self):
        return self.login_ID

    class Meta:
        verbose_name_plural = "Login"

class Workers(models.Model):
    worker_ID=models.IntegerField(primary_key=True)
    outlet_ID=models.ForeignKey(Outlets,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=10)
    middle_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=1)
    email_id=models.CharField(max_length=30)
    contact_no=models.CharField(max_length=10)
    salary=models.FloatField()
    post=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Workers"

class Outlet_Sales(models.Model):
    outlet_SID=models.IntegerField(primary_key=True)
    outlet_ID=models.ForeignKey(Outlets,on_delete=models.CASCADE)
    icecream_ID=models.ForeignKey(Icecreams,on_delete=models.CASCADE)
    units_sold=models.IntegerField(default=1)
    date_time2=models.CharField(max_length=50)

    
    
    class Meta:
        verbose_name_plural = "outlet sales"

