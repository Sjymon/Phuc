from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=200, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    slug = models.SlugField()
    
    class Meta:
        unique_together = ('slug', 'parent')
        verbose_name_plural = "categories"
    
    def __str__(self):
        full_path = [self.name]

        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent
        
        return ' -> '.join(full_path[::-1])


class Authors(models.Model):
    name = models.CharField(max_length=200, blank=False)
    status = models.BooleanField(default=True)

class Books(models.Model):
    full_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_updated = models.DateTimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

class Chapters(models.Model):
    name = models.CharField(max_length=220, blank=False)
    story_id = models.IntegerField(default=0)
    link_img = models.ImageField()
    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.BooleanField(default=True)
    ordering = models.IntegerField(default=0)

class Generals(models.Model):
    # Tên website
    name = models.CharField(max_length=220)
    # Giới thiệu tóm tắt về website
    description = models.TextField()
    # keyword của website
    keywords = models.TextField()
    # email của website
    email = models.CharField(max_length=220)
    # Tên công ty
    site_name = models.TextField()
    # địa chỉ facebook
    facebook = models.CharField(max_length=225)
    # số điện thoại hotline của công ty
    hotline = models.CharField(max_length=225)
    # địa chỉ công ty
    address = models.TextField()
    # số điện thoại công ty
    phone = models.CharField(max_length=225)
    # số fax công ty
    fax = models.CharField(max_length=225)
    # logo công ty
    logo = models.ImageField()

class Stories(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.BooleanField(default=True)
    view = models.IntegerField(default=0)
