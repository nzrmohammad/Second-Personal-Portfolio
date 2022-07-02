from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone

# 1 - Home Page 1 - Home Page 1 - Home Page 1 - Home Page 1 - Home Page
class Home(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    title3 = models.CharField(max_length=50)
    description = models.TextField(max_length=350)
    name = models.CharField(max_length=50)
    sidebarimage = models.ImageField(upload_to='Home/')
    image = models.ImageField(upload_to='Home/')
    updated = models.DateTimeField(auto_now=True)

    def show_photo(self):
        return mark_safe('<img src="{}" width="125" />'.format(self.image.url))
    show_photo.short_description = 'Image Preview'
    show_photo.allow_tags = True

    class Meta:
        verbose_name_plural = '1 - Home'

    def __str__(self):
        return self.title1


# 2 - About Page 2 - About Page 2 - About Page 2 - About Page 2 - About Page
class About(models.Model):
    description = models.TextField(max_length=350)
    image = models.ImageField(upload_to='About/')
    image2 = models.ImageField(upload_to='About/')
    updated = models.DateTimeField(auto_now=True)

    def show_photo(self):
        return mark_safe('<img src="{}" width="250" />'.format(self.image.url))
    show_photo.short_description = 'Image Preview'
    show_photo.allow_tags = True

    class Meta:
        verbose_name_plural = '2 - About'

    # def __str__(self):
    #     return self.name

class Skill(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    percent = models.CharField(max_length=3)

    def __str__(self):
        return self.name


# 3 - Service Page 3 - Service Page 3 - Service Page 3 - Service Page 3 - Service Page
class Service(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '3 - Service'

    def __str__(self):
        return self.title


# 4 - Testimonial Page 4 - Testimonial Page 4 - Testimonial Page 4 - Testimonial Page 4 - Testimonial Page
class Testimonial(models.Model):
    image = models.ImageField(upload_to='Testimonial/')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def show_photo(self):
        return mark_safe('<img src="{}" width="150" />'.format(self.image.url))
    show_photo.short_description = 'Image Preview'
    show_photo.allow_tags = True

    class Meta:
        verbose_name_plural = '4 - Testimonial'

    def __str__(self):
        return self.name


# 5 - Category Page 5 - Category Page 5 - Category Page 5 - Category Page 5 - Category Page
class Category(models.Model):
    name = models.CharField(max_length=35)

    class Meta:
        verbose_name_plural = '5 - Category'

    def __str__(self):
        return self.name

# 6 - Portfolio Page 6 - Portfolio Page 6 - Portfolio Page 6 - Portfolio Page 6 - Portfolio Page
class Portfolio(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField(max_length=300)
    result = models.TextField(max_length=300)
    publish = models.DateTimeField(default=timezone.now)
    client = models.CharField(max_length=35)
    url = models.URLField(max_length=35)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Portfolio/')


    def show_photo(self):
        return mark_safe('<img src="{}" width="250" />'.format(self.image.url))
    show_photo.short_description = 'Image Preview'
    show_photo.allow_tags = True

    class Meta:
        verbose_name_plural = '6 - Portfolio'

    def __str__(self):
        return self.name


# 7 - Article # 7 - Article # 7 - Article # 7 - Article # 7 - Article # 7 - Article
class Article(models.Model):
    description = models.TextField(max_length=200)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, editable=False, default=1)
    title = models.CharField(max_length = 150)
    description = models.TextField()
    image = models.ImageField(upload_to="Blog_Image")
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title     

    class Meta:
        verbose_name_plural = '7 - Article'


# 8 - ContactUs Page 8 - ContactUs Page 8 - ContactUs Page 8 - ContactUs Page 8 - ContactUs Page
class ContactUs(models.Model):
    name = models.CharField(max_length=35)
    email = models.CharField(max_length=35)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    is_read = models.BooleanField(default=False , verbose_name='Read / Unread')

    class Meta:
        verbose_name = 'CONTACT US'
        verbose_name_plural = '8 - Contact Us'

    def __str__(self):
        return "Message From" + " -----> " + self.email

# 9 - Contact Page 9 - Contact Page 9 - Contact Page 9 - Contact Page 9 - Contact Page
class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '9 - Contact'

    def __str__(self):
        return self.email

class Social_Profile(models.Model):
    name = models.CharField(max_length=20)
    link = models.URLField()

    class Meta:
        verbose_name_plural = 'Social_Profile'

    def __str__(self):
        return self.name