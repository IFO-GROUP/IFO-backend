from django.db import models

# import os, stat

# Create your models here.



class Subscriber(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
    
    
class Project(models.Model):
    title = models.CharField("title", max_length=100)
    cover_img = models.ImageField(upload_to='projects/')
    desc=models.TextField(verbose_name="Description")
    detail_img=models.ImageField(upload_to='projects/')
    text=models.TextField(verbose_name="Text")
    link=models.URLField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
    
    
    
class CoFounder(models.Model):
    full_name= models.CharField("full name", max_length=100)
    img = models.ImageField(upload_to='cofounders/')
    desc=models.TextField(verbose_name="Description",blank=True,null=True)


    class Meta:
        verbose_name = 'CoFounder'
        verbose_name_plural = 'CoFounders'

    def __str__(self):
        return self.full_name
    
    # def save(self, *args, **kwargs):
    #     if self.img:
    #         os.chmod(self.img.path, stat.S_IRWXO)

    #     super(CoFounder, self).save(*args, **kwargs)
    
    
class ShareHolder(models.Model):
    full_name= models.CharField("full name", max_length=100)
    img = models.ImageField(upload_to='cofounders/')
    desc=models.TextField(verbose_name="Description",blank=True,null=True)


    class Meta:
        verbose_name = 'ShareHolder'
        verbose_name_plural = 'ShareHolders'

    def __str__(self):
        return self.full_name
    
    
    
class CareerCategory(models.Model):
    type= models.CharField("type", max_length=100)

    class Meta:
        verbose_name = 'CareerCategory'
        verbose_name_plural = 'CareerCategories'

    def __str__(self):
        return self.type  
    
    
    
class Career(models.Model):
    category=models.ForeignKey(CareerCategory, on_delete=models.SET_NULL, null=True)
    name= models.CharField("name", max_length=100)
    email=models.EmailField(max_length=255, unique=True)
    phone=models.CharField(max_length=50)
    location=models.CharField(max_length=255)
    ln_link=models.URLField(max_length=255)
    comment=models.TextField()


    class Meta:
        verbose_name = 'Career'
        verbose_name_plural = 'Careers'

    def __str__(self):
        return self.name



class NewsCategory(models.Model):
    type= models.CharField("type", max_length=100)
    bg_color=models.CharField("background color", max_length=100)
    class Meta:
        verbose_name = 'NewsCategory'
        verbose_name_plural = 'NewsCategories'

    def __str__(self):
        return self.type  
   
   
    
class News(models.Model):
    title= models.CharField("title", max_length=255)
    category=models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True)
    cover_img=models.ImageField(upload_to='news/')
    desc=models.TextField()
    img1=models.ImageField(upload_to='news/',null=True, blank=True)
    img2=models.ImageField(upload_to='news/',null=True, blank=True)
    img3=models.ImageField(upload_to='news/',null=True, blank=True)
    img4=models.ImageField(upload_to='news/',null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    
       
      

class Coin(models.Model):
    title= models.CharField("title", max_length=255,null=True, blank=True)
    img=models.ImageField(upload_to='coins/',null=True, blank=True)
    desc=models.TextField()
    ln_link=models.URLField(max_length=255)

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'

    def __str__(self):
        return self.title
    
    
class CoinField(models.Model):
    title= models.CharField("title", max_length=255,null=True, blank=True)
    img=models.ImageField(upload_to='coins/',null=True, blank=True)
    desc=models.TextField()

    class Meta:
        verbose_name = 'CoinField'
        verbose_name_plural = 'CoinFields'

    def __str__(self):
        return self.title
    


    
class CoinDeadline(models.Model):
     deadline=models.DateTimeField(null=True)

     class Meta:
        verbose_name = 'CoinDeadline'
        verbose_name_plural = 'CoinDeadlines'
        
        
        
class CoinFeature(models.Model):
    feature= models.CharField("feature", max_length=255)
    count=models.IntegerField('count')


    class Meta:
        verbose_name = 'CoinFeature'
        verbose_name_plural = 'CoinFeatures'

    def __str__(self):
        return self.feature
    
    

class AllocationFund(models.Model):
    title= models.CharField("title", max_length=255)


    class Meta:
        verbose_name = 'AllocationFund'
        verbose_name_plural = 'AllocationFunds'

    def __str__(self):
        return self.title
    
  
  
class TimeLine(models.Model):
    title= models.CharField("title", max_length=255)
    desc=models.TextField()
    created_at=models.DateTimeField()


    class Meta:
        verbose_name = 'TimeLine'
        verbose_name_plural = 'TimeLines'

    def __str__(self):
        return self.title  
    


    
class Partner(models.Model):
    title= models.CharField("title", max_length=255)
    logo=models.ImageField(upload_to='partners/')
    cover_img=models.ImageField(upload_to='partners/')
    short_desc=models.TextField()
    desc=models.TextField()
    img1=models.ImageField(upload_to='news/',null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.title


    

    
