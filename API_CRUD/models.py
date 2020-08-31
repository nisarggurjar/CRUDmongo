from djongo import models

class Article(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=254, blank=True, null=True)
    author = models.CharField(max_length=254, blank=True, null=True)
    email = models.EmailField()
    
    def __str__(self):
        return self.title
    

