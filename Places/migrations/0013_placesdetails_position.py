from django.db import migrations
import django.utils.timezone
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0012_auto_20220718_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='placesdetails',
            name='position',
            field=geoposition.fields.GeopositionField(default=django.utils.timezone.now, max_length=42),
            preserve_default=False,
        ),
    ]
