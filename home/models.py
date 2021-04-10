from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Assignment(models.Model):
    title = models.CharField(null=False,blank=False,max_length=500)
    paper = models.FileField(upload_to="assignment/%Y/%m/%d/",null=True,blank=True)
    remark = models.CharField(null=False,blank=False,max_length=500)
    due_date = models.DateField(blank=False)
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
        
class Submission(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    paper = models.FileField(upload_to="assignment_submission/%Y/%m/%d/",blank=False)
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)