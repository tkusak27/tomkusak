from django.db import models
import datetime
from django_editorjs import EditorJsField

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    create_date = models.DateField('First Published', default = datetime.date.today)
    bodytext = models.TextField('Page Content', blank=True)

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    post=models.TextField('')

class Project(models.Model):
    title = models.CharField(max_length=60)
    description = EditorJsField(editorjs_config={
            "tools": {
                "Table": {
                    "disabled": False,
                    "inlineToolbar": True,
                    "config": {"rows": 2, "cols": 3,},
                }
            }
        }
    )

class Career(models.Model):
    interests = models.TextField('Interests')
    past_experience = models.TextField('Past Experiences')
    upcoming = models.TextField('Upcoming')
