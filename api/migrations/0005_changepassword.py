# Generated by Django 4.0.5 on 2022-08-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_employeetask_taskid'),
    ]

    operations = [
        migrations.CreateModel(
            name='changePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
