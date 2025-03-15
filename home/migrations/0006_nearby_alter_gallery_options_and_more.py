# Generated by Django 5.0.2 on 2025-03-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_site_ddress_setting_site_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nearby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('CONNECTIVITY', 'CONNECTIVITY'), ('HOTELS', 'HOTELS'), ('EDUCATIONAL INSTITUTIONS', 'EDUCATIONAL INSTITUTIONS'), ('SHOPPING & ENTERTAINMENT', 'SHOPPING & ENTERTAINMENT'), ('HEALTHCARE', 'HEALTHCARE'), ('LANDMARKS', 'LANDMARKS')], max_length=100)),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': '9. Nearby',
            },
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': '8. Gallery'},
        ),
        migrations.AddField(
            model_name='setting',
            name='footer_copyright',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='footer_description',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='footer_title',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='nearby_description',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='nearby_image',
            field=models.ImageField(blank=True, null=True, upload_to='logo/'),
        ),
        migrations.AddField(
            model_name='setting',
            name='nearby_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
