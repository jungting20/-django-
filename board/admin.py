from django.contrib import admin

from board.models import Board,BoardComment

# Register your models here.

# @admin.register(Board)
# class boardadmin(admin.ModelAdmin):
#     list_display = ('id','title','content','created_at')


admin.site.register(Board)
admin.site.register(BoardComment)
