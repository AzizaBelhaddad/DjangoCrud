# Generated by Django 4.0 on 2021-12-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='state',
        ),
        migrations.AddField(
            model_name='article',
            name='state',
            field=models.IntegerField(choices=[{0, 'disable'}, {1, 'enable'}], default=0),
        ),
    ]