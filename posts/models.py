from django.db import models

class Post(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    name = models.CharField(max_length=100)
    sake_name = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    purchase_location = models.CharField(max_length=200, blank=True, null=True)
    drinking_occasion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.created_at}'
