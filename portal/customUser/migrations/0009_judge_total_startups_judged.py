# Generated by Django 4.2.1 on 2023-06-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0008_remove_judge_data_judge_startups_judged'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='total_startups_judged',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
