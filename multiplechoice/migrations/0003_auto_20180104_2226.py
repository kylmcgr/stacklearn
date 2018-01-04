# Generated by Django 2.0.1 on 2018-01-04 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiplechoice', '0002_auto_20180104_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='answer1',
        ),
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='answer2',
        ),
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='answer3',
        ),
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='answer4',
        ),
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='multiplechoiceanswer',
            name='raw_answer',
            field=models.IntegerField(choices=[(0, 0), (0, 0), (0, 0), (150, 150)], max_length=50),
        ),
    ]
