# Generated by Django 4.2.1 on 2023-06-02 06:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0010_judge_alter_customuser_user_alter_participant_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='judge_username',
            field=models.CharField(null=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='participant',
            name='para1',
            field=models.IntegerField(null=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='judge',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='participant',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]