# Generated by Django 2.2.8 on 2019-12-19 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_membermodel_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='types',
            field=models.CharField(choices=[('photo', '婚摄'), ('dress', '装扮')], db_column='type', default='dress', max_length=20, verbose_name='类型'),
        ),
    ]
