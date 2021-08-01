from django.db import models

# List of models
# 1.About
# 2.Blog
# 3.Team
# 4.ComapnyInfo
# 5.Feature
# 6.Review
# 7.Services
# 8.SocialMedia
# 9.Listing
# 10.Package


class About(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=430)
    image = models.ImageField(upload_to='apps/about', null=True, blank=True,
                              default='http://www.dar-elweb.com/demos/zarest/assets/img/tableB4.svg')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/service', null=True, blank=True,
                              default='https://laxmanbaralblog.com/wp-content/uploads/2020/06/what-is-a-blog.png')
    description = models.TextField()
    written_by = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/team', null=True, blank=True,
                              default='img/team/01.jpg')
    post = models.CharField(max_length=40)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    gmail = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class ComapnyInfo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_num = models.CharField(max_length=50)
    cell_num = models.CharField(max_length=50)
    email_us = models.CharField(max_length=100)
    office_time = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company Information"


class Feature(models.Model):
    icon = models.CharField(max_length=100, null=True,
                            blank=True, default="wrench")
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    image = models.ImageField(upload_to='media/pricing', null=True, blank=True,
                              default='http://www.dar-elweb.com/demos/zarest/assets/img/tableB4.svg')
    description = models.TextField()
    client_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Service(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=400, null=True, blank=True)
    image = models.CharField(max_length=100, null=True,
                             blank=True, default="wrench")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SocialMedia(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=250)
    visible = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Listing(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Package features"


class Package(models.Model):
    plan_title = models.CharField(max_length=200)
    mbps = models.IntegerField()
    description = models.ManyToManyField(
        Listing)
    price = models.IntegerField()
