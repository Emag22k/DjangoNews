from django.db import models

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=64)
    date_name = models.DateTimeField()

    def __str__(self):
        return str(self.category_name)

class News(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.title)


