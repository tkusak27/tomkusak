# Generated by Django 4.1.3 on 2024-03-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_page_remove_comment_post_remove_post_categories_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
