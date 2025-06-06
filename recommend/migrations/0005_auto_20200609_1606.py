import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0004_auto_20200609_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrating',
            name='like',
        ),
        migrations.AddField(
            model_name='movie',
            name='watch',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myrating',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
