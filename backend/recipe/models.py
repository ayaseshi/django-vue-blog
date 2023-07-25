from django.db import models
from django.core.files import File
from django.contrib.auth.models import User

from PIL import Image
from io import BytesIO

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
    
    def url(self):
        return f'{self.slug}/'
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    ingredients = models.JSONField()
    instructions = models.JSONField()
    date_added = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='image/')
    thumbnail = models.ImageField(upload_to='image/', blank=True, null=True)
    option = models.CharField(max_length=10, choices=(
        ('option1', 'Easy'),
        ('option2', 'Medium'),
        ('option3', 'Hard'),
        )
    )
    tag = models.ForeignKey(Tag, related_name='recipes', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta():
        ordering = ('-date_added', )

    def __str__(self):
        return self.name

    def url(self):
        return f'/{self.tag.slug}/{self.slug}/'
    
    def get_image_url(self):
        return self.img.url
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            img = Image.open(self.img)
            img = img.convert('RGB')
            img.thumbnail((300, 200))
            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG', quality=85)
            self.thumbnail.save(
                self.img.name.split('/')[-1].split('.')[0] + '_thumb.jpg',
                File(thumb_io),
                save=False
            )
            self.save()
            return self.thumbnail.url