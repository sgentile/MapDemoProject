from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100, default='')
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'note'

    def __unicode__(self):
        return self.title
