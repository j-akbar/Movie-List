import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_myrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myrating',
            name='like',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
    ]
