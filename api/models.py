from django.db import models

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

    class Meta:
        verbose_name = 'NewsCategory'
        verbose_name_plural = 'NewsCategories'

    def __str__(self):
        return self.type  
   
   
    
class News(models.Model):
    type_choices = (
        ('Corporation', 'Corporation'),
        ('Creative', 'Creative'),
        ('Clothing', 'Clothing'),
        ('Company', 'Company'),
    )
    
    title= models.CharField("title", max_length=255)
    category=models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True)
    cover_img=models.ImageField(upload_to='news/')
    desc=models.TextField()
    type= models.CharField(max_length=255,choices=type_choices)
    created_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.type  
    
       
      
class Image(models.Model):
    img= models.ImageField(upload_to='news/')
    news=models.ForeignKey(News, on_delete=models.CASCADE,
                                 db_index=True, related_name='images')
    is_published = models.BooleanField(default=False)


    class Meta:
            verbose_name = 'Image'
            verbose_name_plural = 'Images'
            
            
    
