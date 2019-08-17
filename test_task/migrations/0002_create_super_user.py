from django.db import migrations
from django.contrib.auth.models import User


def create_admin_user(apps, schema_editor):
    # Creating a super user 'admin' if it's not present
    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_user(username='admin', password='admin')
        user.is_superuser = True
        user.is_staff = True
        user.save()


def delete_admin_user(apps, schema_editor):
    # Deleting the super user 'admin'
    User.objects.filter(username='admin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0001_initial')
    ]

    operations = [
        migrations.RunPython(code=create_admin_user, reverse_code=delete_admin_user)
    ]

