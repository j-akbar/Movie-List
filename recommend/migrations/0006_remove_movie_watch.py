from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0005_auto_20200609_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watch',
        ),
    ]
