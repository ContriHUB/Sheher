# Generated by Django 3.2.9 on 2022-06-25 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0005_placesdetails_day_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placesdetails',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/Places/profile'),
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/Places')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Places.placesdetails')),
            ],
        ),
    ]
