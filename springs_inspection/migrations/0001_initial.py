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
            name='Springs',
            fields=[
                ('spring_id', models.IntegerField(primary_key=True, serialize=False)),
                ('spring_name', models.CharField(blank=True, max_length=7, null=True)),
                ('position', models.CharField(blank=True, max_length=300, null=True)),
                ('geomorph', models.CharField(blank=True, max_length=150, null=True)),
                ('head', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('spring_type', models.SmallIntegerField(blank=True, null=True)),
                ('regime', models.SmallIntegerField(blank=True, null=True)),
                ('natural_monument_status', models.CharField(max_length=5)),
                ('spna_id', models.IntegerField()),
                ('geom', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'springs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpringsInspectionAttach',
            fields=[
                ('attachmentid', models.AutoField(primary_key=True, serialize=False)),
                ('rel_objectid', models.IntegerField()),
                ('content_type', models.CharField(max_length=150)),
                ('att_name', models.CharField(max_length=250)),
                ('data_size', models.IntegerField()),
                ('data', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'springs_inspection_attach',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpringsRate',
            fields=[
                ('date', models.DateField()),
                ('spring_rate', models.DecimalField(decimal_places=3, max_digits=6)),
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'springs_rate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpringsSample',
            fields=[
                ('sample_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sample_name', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'springs_sample',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SpringsTemperature',
            fields=[
                ('date', models.DateField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=6)),
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'springs_temperature',
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
            name='SpringsInspection',
            fields=[
                ('date', models.DateField()),
                ('weather', models.CharField(blank=True, max_length=100, null=True)),
                ('usage', models.SmallIntegerField()),
                ('captage_condition', models.SmallIntegerField()),
                ('captage_description', models.CharField(blank=True, max_length=300, null=True)),
                ('area_condition', models.SmallIntegerField()),
                ('agreed', models.SmallIntegerField()),
                ('area_description', models.CharField(blank=True, max_length=300, null=True)),
                ('improve_description', models.CharField(blank=True, max_length=150, null=True)),
                ('comments', models.CharField(blank=True, max_length=150, null=True)),
                ('recommendations', models.CharField(blank=True, max_length=200, null=True)),
                ('doc', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='springs_inspection.documents')),
            ],
            options={
                'db_table': 'springs_inspection',
                'ordering': ('-date',),
                'managed': False,
            },
        ),
    ]
