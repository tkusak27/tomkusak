# Generated by Django 4.1.3 on 2024-03-13 12:25

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_blogpost_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=django_editorjs.fields.EditorJsField(default=2),
            preserve_default=False,
        ),
    ]
