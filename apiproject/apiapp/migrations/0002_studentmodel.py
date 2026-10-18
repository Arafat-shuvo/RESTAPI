from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.CreateModel(
                    name='StudentModel',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('name', models.CharField(max_length=100)),
                        ('email', models.EmailField(max_length=254, unique=True)),
                        ('address', models.TextField()),
                        ('phone_number', models.CharField(max_length=15)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                    ],
                ),
            ],
            state_operations=[
                migrations.DeleteModel(name='ProductModel'),
                migrations.CreateModel(
                    name='StudentModel',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('name', models.CharField(max_length=100)),
                        ('email', models.EmailField(max_length=254, unique=True)),
                        ('address', models.TextField()),
                        ('phone_number', models.CharField(max_length=15)),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                    ],
                ),
            ],
        ),
    ]
