# Generated by Django 3.2.13 on 2022-06-09 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AquiferCodes',
            fields=[
                ('aquifer_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('aquifer_name', models.CharField(max_length=150)),
                ('aquifer_index', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'aquifer_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('doc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('doc_type', models.SmallIntegerField()),
                ('reg_status', models.SmallIntegerField()),
                ('reg_number', models.CharField(blank=True, max_length=15, null=True)),
                ('reg_date', models.DateField(blank=True, null=True)),
                ('reg_worker', models.SmallIntegerField(blank=True, null=True)),
                ('doc_source', models.SmallIntegerField(blank=True, null=True)),
                ('doc_name', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_org', models.CharField(blank=True, max_length=50, null=True)),
                ('author1', models.SmallIntegerField(blank=True, null=True)),
                ('author2', models.SmallIntegerField(blank=True, null=True)),
                ('author3', models.SmallIntegerField(blank=True, null=True)),
                ('author4', models.SmallIntegerField(blank=True, null=True)),
                ('creation_place', models.CharField(blank=True, max_length=50, null=True)),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('number_of_pages', models.SmallIntegerField(blank=True, null=True)),
                ('number_of_graphic', models.SmallIntegerField(blank=True, null=True)),
                ('paper_version', models.CharField(blank=True, max_length=5, null=True)),
                ('digital_version', models.CharField(blank=True, max_length=5, null=True)),
                ('secrecy', models.SmallIntegerField(blank=True, null=True)),
                ('storage', models.CharField(blank=True, max_length=50, null=True)),
                ('comments', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'documents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentsAttach',
            fields=[
                ('attachmentid', models.AutoField(primary_key=True, serialize=False)),
                ('rel_objectid', models.IntegerField()),
                ('content_type', models.CharField(max_length=150)),
                ('att_name', models.CharField(max_length=250)),
                ('data_size', models.IntegerField()),
                ('data', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'documents_attach',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubsurfaceSites',
            fields=[
                ('subsurface_site_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subsurface_site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mineral', models.SmallIntegerField()),
                ('deposit_site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=300, null=True)),
                ('deposit', models.IntegerField()),
                ('gmsn_id', models.IntegerField(blank=True, null=True)),
                ('uib_id', models.BigIntegerField(blank=True, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
                ('objectid', models.IntegerField(unique=True)),
                ('gdb_geomattr_data', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'subsurface_sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wells',
            fields=[
                ('well_id', models.IntegerField(primary_key=True, serialize=False)),
                ('well_name', models.CharField(blank=True, max_length=50, null=True)),
                ('well_type', models.SmallIntegerField()),
                ('position', models.CharField(blank=True, max_length=300, null=True)),
                ('geomorph', models.CharField(blank=True, max_length=300, null=True)),
                ('head', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('moved', models.SmallIntegerField()),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wells',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WellsTemperature',
            fields=[
                ('date', models.DateField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=6)),
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'wells_temperature',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WellsWaterdepth',
            fields=[
                ('date', models.DateField()),
                ('water_depth', models.DecimalField(decimal_places=2, max_digits=6)),
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'wells_waterdepth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('worker_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('name_1', models.CharField(max_length=50)),
                ('name_2', models.CharField(max_length=50)),
                ('name_3', models.CharField(blank=True, max_length=50, null=True)),
                ('birth_date', models.DateField()),
                ('post', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('phone_personal', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_work', models.SmallIntegerField(blank=True, null=True)),
                ('e_mail', models.CharField(blank=True, max_length=50, null=True)),
                ('e_mail_work', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'workers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WellsPumping',
            fields=[
                ('date', models.DateField()),
                ('test_type', models.SmallIntegerField()),
                ('pump_type', models.SmallIntegerField(blank=True, null=True)),
                ('pump_depth', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pump_time', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('recovery_time', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('flow_rate', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('depression', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('comments', models.CharField(blank=True, max_length=150, null=True)),
                ('doc', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='wells_pumping.documents')),
            ],
            options={
                'db_table': 'wells_pumping',
                'ordering': ('-date',),
                'managed': False,
            },
        ),
    ]
