from django.db import models

# Create your models here.


class ImagesModel(models.Model):
    img_url = models.URLField(verbose_name='图片地址', null=True, blank=True)
    img_path = models.CharField(max_length=255, verbose_name='图片路径', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='图片名称', null=True, blank=True)
    status = models.CharField(choices=[('enabled', '启用'), ('disabled', '禁用')], default='enabled')
    type1 = models.CharField(choices=[('banner', '轮播'), ('show', '首图')], default='show', db_column='type')
    description = models.CharField(max_length=500, verbose_name='详情', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', null=True, blank=True)

    class Meta:
        db_table = 'images'

class ImagesManyModel(models.Model):
    pass