# Generated by Django 4.2.1 on 2023-06-19 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0009_judge_total_startups_judged'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='rank',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='total_score',
            field=models.FloatField(default=0, null=True),
        ),
    ]
