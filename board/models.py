from django.db import models
from django.db.models.deletion import CASCADE

from member.models import User


class Board(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d/orig',blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BoardComment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    board_id = models.ForeignKey(Board,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)




