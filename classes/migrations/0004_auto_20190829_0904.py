# Generated by Django 2.1.5 on 2019-08-29 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classes.Classroom'),
        ),
        migrations.AddField(
            model_name='student',
            name='exam_grade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
