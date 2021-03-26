from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20201228_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Terrariums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100)),
                ('slug', models.SlugField(blank=True, default='', unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='diy',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Diy'),
        ),
        migrations.AlterField(
            model_name='post',
            name='getting_started',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='core.GettingStarted'),
        ),
        migrations.AlterField(
            model_name='post',
            name='gardens',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='core.Terrariums'),
        ),
    ]
