# Generated by Django 3.2.9 on 2022-07-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0011_ratingreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingreview',
            name='overall_fun',
            field=models.CharField(blank=True, choices=[(1, 'VERY POOR'), (2, 'POOR'), (3, 'MEDIOCRE'), (4, 'GOOD'), (5, 'EXCELLENT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ratingreview',
            name='safety',
            field=models.CharField(blank=True, choices=[(1, 'VERY POOR'), (2, 'POOR'), (3, 'MEDIOCRE'), (4, 'GOOD'), (5, 'EXCELLENT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ratingreview',
            name='sanitization',
            field=models.CharField(blank=True, choices=[(1, 'VERY POOR'), (2, 'POOR'), (3, 'MEDIOCRE'), (4, 'GOOD'), (5, 'EXCELLENT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='ratingreview',
            name='security',
            field=models.CharField(blank=True, choices=[(1, 'VERY POOR'), (2, 'POOR'), (3, 'MEDIOCRE'), (4, 'GOOD'), (5, 'EXCELLENT')], max_length=100),
        ),
    ]
