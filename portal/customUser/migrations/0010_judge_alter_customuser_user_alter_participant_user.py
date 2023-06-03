# Generated by Django 4.2.1 on 2023-06-02 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0009_participant_data_alter_customuser_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='judge',
            fields=[
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('data', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
