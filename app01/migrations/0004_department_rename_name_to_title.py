# Generated to rename Department.name -> Department.title
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='title',
        ),
    ]
