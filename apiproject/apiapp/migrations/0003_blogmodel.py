from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_studentmodel'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.CreateModel(
                    name='BlogModel',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('title', models.CharField(max_length=200)),
                        ('author', models.CharField(max_length=100)),
                        ('content', models.TextField()),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                    ],
                ),
            ],
            state_operations=[
                migrations.DeleteModel(name='StudentModel'),
                migrations.CreateModel(
                    name='BlogModel',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('title', models.CharField(max_length=200)),
                        ('author', models.CharField(max_length=100)),
                        ('content', models.TextField()),
                        ('created_at', models.DateTimeField(auto_now_add=True)),
                        ('updated_at', models.DateTimeField(auto_now=True)),
                    ],
                ),
            ],
        ),
    ]
