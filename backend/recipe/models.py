from django.db import models
from django.core.files import File

from PIL import Image
from io import BytesIO

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name
    
    def url(self):
        return f'{self.slug}/'
    
class Recipe(models.Model):
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
            img.convert('RGB')
            img.thumbnail((300, 200))
            thumb_io = BytesIO()
            img.save(thumb_io, 'JPEG', quality=85)

            self.thumbnail = File(thumb_io, name=self.image.name)