from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myrating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('like', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommend.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
