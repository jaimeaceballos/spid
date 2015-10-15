# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuantes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('funcion', models.IntegerField()),
                ('documento', models.IntegerField(unique=True, max_length=8)),
                ('apeynombres', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['documento'],
                'db_table': 'actuantes',
            },
        ),
        migrations.CreateModel(
            name='Ampliacion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=2000)),
                ('fecha_autorizacion', models.DateTimeField(null=True, blank=True)),
                ('cierre_causa', models.BooleanField(default=False)),
                ('fecha_cierre', models.DateTimeField(null=True, blank=True)),
                ('fin_edicion', models.BooleanField(default=False)),
                ('sendwebservice', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'ampliacion',
            },
        ),
        migrations.CreateModel(
            name='Armas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('modelo', models.CharField(max_length=100, null=True, blank=True)),
                ('calibre', models.CharField(max_length=10, null=True, blank=True)),
                ('nro_arma', models.CharField(max_length=50, null=True, blank=True)),
                ('nro_doc', models.IntegerField(max_length=8, null=True, blank=True)),
                ('propietario', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha_carga', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['tipos', 'subtipos', 'marcas'],
                'db_table': 'armas',
            },
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('idBarrio', models.AutoField(serialize=False, primary_key=True)),
                ('idLocalidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'barrio',
            },
        ),
        migrations.CreateModel(
            name='Calles',
            fields=[
                ('idCalle', models.AutoField(serialize=False, primary_key=True)),
                ('idLocalidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'calles',
            },
        ),
        migrations.CreateModel(
            name='Comisarias',
            fields=[
                ('idorganismo', models.AutoField(serialize=False, primary_key=True)),
                ('idLocalidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'comisarias',
            },
        ),
        migrations.CreateModel(
            name='Dependencias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'dependencias',
            },
        ),
        migrations.CreateModel(
            name='Detenidos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fechahoradetencion', models.DateTimeField(null=True, blank=True)),
                ('fechahoralibertad', models.DateTimeField(null=True, blank=True)),
                ('libertad', models.CharField(max_length=1, null=True, blank=True)),
                ('observaciones', models.CharField(max_length=800, null=True, blank=True)),
                ('borrado', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'detenidos',
            },
        ),
        migrations.CreateModel(
            name='Domicilios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altura', models.CharField(default='0', max_length=4, blank=True)),
                ('fecha_desde', models.DateField(null=True, blank=True)),
                ('fecha_hasta', models.DateField(null=True, blank=True)),
                ('fecha_actualizacion', models.DateField(null=True, blank=True)),
                ('departamento', models.CharField(default='', max_length=10, null=True, blank=True)),
                ('piso', models.CharField(default='0', max_length=4, blank=True)),
                ('lote', models.CharField(default='0', max_length=4, blank=True)),
                ('sector', models.CharField(default='', max_length=10, null=True, blank=True)),
                ('manzana', models.CharField(default='0', max_length=4, blank=True)),
            ],
            options={
                'ordering': ['-fecha_desde'],
                'db_table': 'domicilios',
            },
        ),
        migrations.CreateModel(
            name='Drogas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_carga', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'drogas',
            },
        ),
        migrations.CreateModel(
            name='Elementos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=150)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('borrado', models.CharField(max_length=1, null=True, blank=True)),
                ('observaciones', models.CharField(max_length=800, null=True, blank=True)),
                ('cargado_prev', models.BooleanField(default=False)),
                ('ampliacion', models.ForeignKey(blank=True, to='preventivos.Ampliacion', null=True)),
            ],
            options={
                'ordering': ['tipo', 'descripcion'],
                'db_table': 'elementos',
            },
        ),
        migrations.CreateModel(
            name='Elementosarmas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('idarma', models.ForeignKey(to='preventivos.Armas')),
                ('idelemento', models.ForeignKey(related_name='relelem', to='preventivos.Elementos')),
            ],
            options={
                'ordering': ['idelemento'],
                'db_table': 'elementosarmas',
            },
        ),
        migrations.CreateModel(
            name='Elementoscars',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('idelemento', models.ForeignKey(to='preventivos.Elementos')),
            ],
            options={
                'db_table': 'elementoscars',
            },
        ),
        migrations.CreateModel(
            name='Elementosdrogas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('droga', models.ForeignKey(to='preventivos.Drogas')),
                ('idelemento', models.ForeignKey(to='preventivos.Elementos')),
            ],
        ),
        migrations.CreateModel(
            name='EnvioAmpJudicial',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_envio', models.DateTimeField(auto_now=True)),
                ('fecha_autorizacion', models.DateTimeField(null=True, blank=True)),
                ('enviado', models.IntegerField(default=0)),
                ('ampliacion', models.ForeignKey(blank=True, to='preventivos.Ampliacion', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['fecha_envio'],
                'db_table': 'envioampjudicial',
            },
        ),
        migrations.CreateModel(
            name='EnvioPreJudicial',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_autorizacion', models.DateTimeField(null=True)),
                ('fecha_envio', models.DateTimeField(auto_now=True)),
                ('enviado', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['fecha_envio'],
                'db_table': 'envioprejudicial',
            },
        ),
        migrations.CreateModel(
            name='Estadocivil',
            fields=[
                ('idEstadoCivil', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'Estadocivil',
            },
        ),
        migrations.CreateModel(
            name='Hechos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_carga', models.DateTimeField(null=True, blank=True)),
                ('descripcion', models.CharField(max_length=2000, null=True, blank=True)),
                ('fecha_desde', models.DateTimeField()),
                ('fecha_hasta', models.DateTimeField()),
                ('fecha_esclarecido', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['fecha_carga', 'preventivo'],
                'db_table': 'hechos',
            },
        ),
        migrations.CreateModel(
            name='HechosDelito',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('borrado', models.CharField(max_length=1, null=True, blank=True)),
                ('hechos', models.ForeignKey(related_name='hechos', to='preventivos.Hechos')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'hechos_delito',
            },
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('idLocalidad', models.AutoField(serialize=False, primary_key=True)),
                ('idProvincia', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'Localidad',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altura', models.IntegerField(default='0', null=True, blank=True)),
                ('latitud', models.CharField(max_length=50)),
                ('longitud', models.CharField(max_length=50)),
                ('lote', models.CharField(default='0', max_length=45, null=True, blank=True)),
                ('manzana', models.CharField(default='0', max_length=45, null=True, blank=True)),
                ('sector', models.CharField(default='', max_length=45, null=True, blank=True)),
                ('departamento', models.CharField(default='', max_length=45, null=True, blank=True)),
                ('piso', models.CharField(default='0', max_length=45, null=True, blank=True)),
                ('nro_casa', models.IntegerField(default='0', null=True, blank=True)),
                ('edificio', models.CharField(default='', max_length=45, null=True, blank=True)),
                ('escalera', models.CharField(default='', max_length=45, null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'lugar',
            },
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('idNacionalidad', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'nacionalidad',
            },
        ),
        migrations.CreateModel(
            name='Padres',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('padre_nombres', models.CharField(default='', max_length=150, null=True, blank=True)),
                ('padre_apellidos', models.CharField(default='', max_length=100, null=True, blank=True)),
                ('madre_apellidos', models.CharField(default='', max_length=100, null=True, blank=True)),
                ('madre_nombres', models.CharField(default='', max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'padres',
            },
        ),
        migrations.CreateModel(
            name='PersInvolucradas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('juridica', models.CharField(default='no', max_length=2, blank=True, choices=[('si', 'SI'), ('no', 'NO')])),
                ('razon_social', models.CharField(max_length=150, null=True, blank=True)),
                ('menor', models.CharField(default='no', max_length=2, blank=True, choices=[('si', 'SI'), ('no', 'NO')])),
                ('detenido', models.CharField(default='si', max_length=2, blank=True, choices=[('si', 'SI'), ('no', 'NO')])),
                ('tentativa', models.CharField(default='no', max_length=2, blank=True, choices=[('si', 'SI'), ('no', 'NO')])),
                ('infraganti', models.CharField(default='no', max_length=2, blank=True, choices=[('si', 'SI'), ('no', 'NO')])),
                ('fechahoradetencion', models.DateTimeField(null=True, blank=True)),
                ('fechahoralibertad', models.DateTimeField(null=True, blank=True)),
                ('cargado_prev', models.BooleanField(default=False)),
                ('nrocuit', models.CharField(default=0, unique=True, max_length=11)),
                ('ampliacion', models.ForeignKey(blank=True, to='preventivos.Ampliacion', null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'persinvolucradas',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('legajo', models.CharField(max_length=6)),
                ('credencial', models.IntegerField()),
                ('nro_cuenta_bco', models.CharField(max_length=20)),
                ('nro_seros', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'personal',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('apellidos', models.CharField(max_length=100, verbose_name='apellidos')),
                ('nombres', models.CharField(max_length=150, verbose_name='nombres')),
                ('nro_doc', models.CharField(unique=True, max_length=50)),
                ('cuit', models.CharField(default=0, max_length=11, null=True, blank=True)),
                ('celular', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha_nac', models.DateField()),
                ('alias', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'ordering': ['apellidos'],
                'db_table': 'personas',
            },
        ),
        migrations.CreateModel(
            name='Preventivos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nro', models.PositiveIntegerField(verbose_name='Nro. :', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999999)])),
                ('anio', models.PositiveIntegerField(verbose_name='A\xf1o :', validators=[django.core.validators.MinValueValidator(2012), django.core.validators.MaxValueValidator(2025)])),
                ('caratula', models.CharField(max_length=250)),
                ('fecha_carga', models.DateTimeField(default=0)),
                ('fecha_denuncia', models.DateTimeField(default=0)),
                ('fecha_autorizacion', models.DateTimeField(null=True)),
                ('fecha_cierre', models.DateTimeField(null=True)),
                ('sendwebservice', models.IntegerField(default=0)),
                ('actuante', models.ForeignKey(related_name='Actuante', on_delete=django.db.models.deletion.PROTECT, verbose_name='Actuante', to='preventivos.Actuantes')),
            ],
            options={
                'ordering': ['nro', 'anio', 'dependencia'],
                'db_table': 'preventivos',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idProvincia', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'provincias',
            },
        ),
        migrations.CreateModel(
            name='RefAutoridad',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=300, verbose_name='e mail')),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_autoridad',
            },
        ),
        migrations.CreateModel(
            name='RefBarrios',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100L)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_barrios',
            },
        ),
        migrations.CreateModel(
            name='RefCalles',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=150L)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_calles',
            },
        ),
        migrations.CreateModel(
            name='RefCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100L, verbose_name='Ingrese Categoria :')),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_category',
            },
        ),
        migrations.CreateModel(
            name='RefCiudades',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=80L)),
                ('lat', models.CharField(max_length=50, null=True, blank=True)),
                ('longi', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_ciudades',
            },
        ),
        migrations.CreateModel(
            name='RefComunidades',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=10, choices=[('1', 'Urbana'), ('2', 'Sub-urbana'), ('3', 'Rural'), ('4', 'Costa')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_comunidades',
            },
        ),
        migrations.CreateModel(
            name='RefCondclimas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=150L, blank=True)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_condclimas',
            },
        ),
        migrations.CreateModel(
            name='RefDelito',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_delito',
            },
        ),
        migrations.CreateModel(
            name='RefDepartamentos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=45L, verbose_name='Ingrese Departamento :')),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_departamentos',
            },
        ),
        migrations.CreateModel(
            name='RefDivisionJerarquia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_division_jerarquia',
            },
        ),
        migrations.CreateModel(
            name='RefEstadosciv',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=10, choices=[('0', 'NO REGISTRA'), ('1', 'SOLTERO'), ('2', 'CONCUBINO'), ('3', 'CASAD0'), ('4', 'DIVORCIADO'), ('5', 'VIUDO'), ('6', 'SEPARADO')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_estadociv',
            },
        ),
        migrations.CreateModel(
            name='RefEstudios',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=13, choices=[('1', 'PRIMARIO'), ('2', 'SECUNDARIO'), ('3', 'TERCIARIO'), ('4', 'UNIVERSITARIO')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_estudios',
            },
        ),
        migrations.CreateModel(
            name='RefHogares',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100L, blank=True)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_hogares',
            },
        ),
        migrations.CreateModel(
            name='RefItems',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100L)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_items',
            },
        ),
        migrations.CreateModel(
            name='RefJerarquias',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=45)),
                ('ref_division_jerarquia', models.ForeignKey(to='preventivos.RefDivisionJerarquia', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_jerarquias',
            },
        ),
        migrations.CreateModel(
            name='RefLugares',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100L, blank=True)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_lugares',
            },
        ),
        migrations.CreateModel(
            name='RefModosHecho',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=80)),
                ('delito', models.ForeignKey(to='preventivos.RefDelito', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'ref_modos_hecho',
            },
        ),
        migrations.CreateModel(
            name='RefMotivosHecho',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'ref_motivos_hecho',
            },
        ),
        migrations.CreateModel(
            name='RefOcupacion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_ocupacion',
            },
        ),
        migrations.CreateModel(
            name='RefPaises',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=45L, verbose_name='Seleccione Pais :')),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_paises',
            },
        ),
        migrations.CreateModel(
            name='RefPeople',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=150L, verbose_name='Involucrados - Tipos :')),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_people',
            },
        ),
        migrations.CreateModel(
            name='RefProvincia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=45L, verbose_name='Ingrese Provincia :')),
                ('pais', models.ForeignKey(to='preventivos.RefPaises', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_provincia',
            },
        ),
        migrations.CreateModel(
            name='RefSexo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=10, choices=[('1', 'Femenino'), ('2', 'Masculino')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_sexo',
            },
        ),
        migrations.CreateModel(
            name='RefSistemadis',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_sistemadis',
            },
        ),
        migrations.CreateModel(
            name='RefSubtiposa',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=100L, verbose_name='Ingrese Sub-Tipo :')),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_subtiposa',
            },
        ),
        migrations.CreateModel(
            name='RefTipoDelitos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_tipo_delito',
            },
        ),
        migrations.CreateModel(
            name='RefTipoDocumento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=8, choices=[('1', 'DNI'), ('2', 'LC'), ('3', 'LE'), ('4', 'CI'), ('5', 'PAS'), ('6', 'NO POSEE')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_tipodocumento',
            },
        ),
        migrations.CreateModel(
            name='RefTipodrogas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=50, choices=[('1', 'Marihuana'), ('2', 'Cocaina'), ('3', 'Inhalantes'), ('4', 'Paco'), ('5', 'Energizantes'), ('6', 'Extasis'), ('7', 'Otros')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'reftipodrogas',
            },
        ),
        migrations.CreateModel(
            name='RefTipoelementos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=50, choices=[('1', 'DENUNCIADOS'), ('2', 'SECUESTRADOS'), ('3', 'UTILIZADOS'), ('4', 'UTILIZADOS/SECUESTRADOS')])),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'reftipoelementos',
            },
        ),
        migrations.CreateModel(
            name='RefTipoJerarquia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_tipo_jerarquia',
            },
        ),
        migrations.CreateModel(
            name='RefTiposarmas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_tiposarmas',
            },
        ),
        migrations.CreateModel(
            name='RefTrademark',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'ref_trademark',
            },
        ),
        migrations.CreateModel(
            name='RefUnidadmedidas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'refunidadmedidas',
            },
        ),
        migrations.CreateModel(
            name='Registrouser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=50)),
                ('tablas', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=50)),
                ('session', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Registrouser',
            },
        ),
        migrations.CreateModel(
            name='RolPersonas',
            fields=[
                ('idRolPersonas', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'rolpersonas',
            },
        ),
        migrations.CreateModel(
            name='Tipodocumentos',
            fields=[
                ('idtipodocumento', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'Tipodocumentos',
            },
        ),
        migrations.CreateModel(
            name='TipoOcupacion',
            fields=[
                ('idtipoocupacion', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'tipocupacion',
            },
        ),
        migrations.CreateModel(
            name='UnidadesRegionales',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=80L)),
                ('ciudad', models.ForeignKey(to='preventivos.RefCiudades', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['descripcion'],
                'db_table': 'unidades_regionales',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_login', models.BooleanField(default=True)),
                ('depe', models.ForeignKey(blank=True, to='preventivos.Dependencias', null=True)),
                ('ureg', models.ForeignKey(blank=True, to='preventivos.UnidadesRegionales', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserProfile',
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('dominio', models.CharField(max_length=10, null=True, blank=True)),
                ('anio', models.IntegerField(null=True, blank=True)),
                ('nmotor', models.CharField(max_length=100, null=True, blank=True)),
                ('nchasis', models.CharField(max_length=100, null=True, blank=True)),
                ('tipov', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50, null=True, blank=True)),
                ('fecha_carga', models.DateTimeField(auto_now=True)),
                ('nro_doc', models.IntegerField(max_length=8, null=True, blank=True)),
                ('propietario', models.CharField(max_length=100, null=True, blank=True)),
                ('idmarca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefTrademark', null=True)),
            ],
            options={
                'ordering': ['dominio'],
                'db_table': 'vehiculos',
            },
        ),
        migrations.AlterUniqueTogether(
            name='refunidadmedidas',
            unique_together=set([('descripcion',)]),
        ),
        migrations.AddField(
            model_name='refsubtiposa',
            name='tipo',
            field=models.ForeignKey(related_name='tiposub', on_delete=django.db.models.deletion.PROTECT, to='preventivos.RefTiposarmas'),
        ),
        migrations.AlterUniqueTogether(
            name='refsistemadis',
            unique_together=set([('descripcion',)]),
        ),
        migrations.AddField(
            model_name='refjerarquias',
            name='ref_tipo_jerarquia',
            field=models.ForeignKey(to='preventivos.RefTipoJerarquia', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='refdepartamentos',
            name='provincia',
            field=models.ForeignKey(to='preventivos.RefProvincia', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='refdelito',
            name='tipo_delito',
            field=models.ForeignKey(to='preventivos.RefTipoDelitos', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='refciudades',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefDepartamentos', null=True),
        ),
        migrations.AddField(
            model_name='refciudades',
            name='pais',
            field=models.ForeignKey(to='preventivos.RefPaises', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='refciudades',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefProvincia', null=True),
        ),
        migrations.AddField(
            model_name='refcategory',
            name='rubro',
            field=models.ForeignKey(related_name='rubcategory', on_delete=django.db.models.deletion.PROTECT, to='preventivos.RefItems'),
        ),
        migrations.AddField(
            model_name='refcalles',
            name='ciudad',
            field=models.ForeignKey(related_name='ciucalle', on_delete=django.db.models.deletion.PROTECT, to='preventivos.RefCiudades'),
        ),
        migrations.AddField(
            model_name='refbarrios',
            name='ciudad',
            field=models.ForeignKey(to='preventivos.RefCiudades', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='refautoridad',
            name='ciudades',
            field=models.ManyToManyField(related_name='ciu_autori', null=True, to='preventivos.RefCiudades', blank=True),
        ),
        migrations.AddField(
            model_name='preventivos',
            name='autoridades',
            field=models.ManyToManyField(to='preventivos.RefAutoridad', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preventivos',
            name='dependencia',
            field=models.ForeignKey(blank=True, to='preventivos.Dependencias', null=True),
        ),
        migrations.AddField(
            model_name='preventivos',
            name='preventor',
            field=models.ForeignKey(related_name='Preventor', on_delete=django.db.models.deletion.PROTECT, verbose_name='Preventor', to='preventivos.Actuantes'),
        ),
        migrations.AddField(
            model_name='personas',
            name='ciudad_nac',
            field=models.ForeignKey(related_name='ciudad_nac', on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefCiudades', null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='ciudad_res',
            field=models.ForeignKey(related_name='ciudad_res', on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefCiudades', null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='estado_civil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefEstadosciv', null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefOcupacion', null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='pais_nac',
            field=models.ForeignKey(related_name='pais_nac', on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefPaises', null=True),
        ),
        migrations.AddField(
            model_name='personas',
            name='sexo_id',
            field=models.ForeignKey(to='preventivos.RefSexo', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='personas',
            name='tipo_doc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='tipo documento', to='preventivos.RefTipoDocumento'),
        ),
        migrations.AddField(
            model_name='personal',
            name='persona_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='preventivos.Personas'),
        ),
        migrations.AddField(
            model_name='persinvolucradas',
            name='cuit',
            field=models.ForeignKey(verbose_name='cuit', blank=True, to='preventivos.RefTipoDocumento', null=True),
        ),
        migrations.AddField(
            model_name='persinvolucradas',
            name='hechos',
            field=models.ForeignKey(related_name='involu', to='preventivos.Hechos'),
        ),
        migrations.AddField(
            model_name='persinvolucradas',
            name='persona',
            field=models.ForeignKey(related_name='perso', to='preventivos.Personas'),
        ),
        migrations.AddField(
            model_name='persinvolucradas',
            name='roles',
            field=models.ForeignKey(related_name='rol', default=0, to='preventivos.RefPeople'),
        ),
        migrations.AddField(
            model_name='padres',
            name='persona',
            field=models.ForeignKey(related_name='padre', to='preventivos.Personas'),
        ),
        migrations.AddField(
            model_name='lugar',
            name='barrio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefBarrios', null=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='calle',
            field=models.ForeignKey(related_name='calle_hecho', on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefCalles', null=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='cond_climaticas',
            field=models.ManyToManyField(related_name='condiciones', null=True, to='preventivos.RefCondclimas', blank=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='delito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefDelito', null=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='dependencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.Dependencias', null=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='hecho',
            field=models.ForeignKey(related_name='lugar_hecho', on_delete=django.db.models.deletion.PROTECT, to='preventivos.Hechos', unique=True),
        ),
        migrations.AddField(
            model_name='lugar',
            name='tipo_lugar',
            field=models.ForeignKey(to='preventivos.RefLugares', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='lugar',
            name='zona',
            field=models.ForeignKey(to='preventivos.RefComunidades', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='hechosdelito',
            name='refdelito',
            field=models.ForeignKey(related_name='delis', to='preventivos.RefDelito'),
        ),
        migrations.AddField(
            model_name='hechosdelito',
            name='refmodoshecho',
            field=models.ForeignKey(related_name='modus', blank=True, to='preventivos.RefModosHecho', null=True),
        ),
        migrations.AddField(
            model_name='hechos',
            name='motivo',
            field=models.ForeignKey(to='preventivos.RefMotivosHecho', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='hechos',
            name='preventivo',
            field=models.ForeignKey(related_name='hecho', on_delete=django.db.models.deletion.PROTECT, to='preventivos.Preventivos', unique=True),
        ),
        migrations.AddField(
            model_name='envioprejudicial',
            name='preventivo',
            field=models.ForeignKey(to='preventivos.Preventivos'),
        ),
        migrations.AddField(
            model_name='envioprejudicial',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='elementoscars',
            name='idvehiculo',
            field=models.ForeignKey(to='preventivos.Vehiculos'),
        ),
        migrations.AddField(
            model_name='elementos',
            name='categoria',
            field=models.ForeignKey(to='preventivos.RefCategory', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='elementos',
            name='hechos',
            field=models.ForeignKey(related_name='eleinvolu', on_delete=django.db.models.deletion.PROTECT, to='preventivos.Hechos'),
        ),
        migrations.AddField(
            model_name='elementos',
            name='rubro',
            field=models.ForeignKey(to='preventivos.RefItems', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='elementos',
            name='tipo',
            field=models.ForeignKey(to='preventivos.RefTipoelementos', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='elementos',
            name='unidadmed',
            field=models.ForeignKey(to='preventivos.RefUnidadmedidas', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='drogas',
            name='idtipo',
            field=models.ForeignKey(to='preventivos.RefTipodrogas'),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='barrio_codigo',
            field=models.ForeignKey(blank=True, to='preventivos.RefBarrios', null=True),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='calle',
            field=models.ForeignKey(related_name='domicilio', blank=True, to='preventivos.RefCalles', null=True),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='entre',
            field=models.ForeignKey(related_name='interseccion', blank=True, to='preventivos.RefCalles', null=True),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='personas',
            field=models.ForeignKey(related_name='persodom', to='preventivos.Personas'),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='ref_ciudades',
            field=models.ForeignKey(blank=True, to='preventivos.RefCiudades', null=True),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='ref_zona',
            field=models.ForeignKey(blank=True, to='preventivos.RefComunidades', null=True),
        ),
        migrations.AddField(
            model_name='domicilios',
            name='tipos_domicilio',
            field=models.ForeignKey(blank=True, to='preventivos.RefHogares', null=True),
        ),
        migrations.AddField(
            model_name='detenidos',
            name='hechos',
            field=models.ForeignKey(to='preventivos.Hechos'),
        ),
        migrations.AddField(
            model_name='detenidos',
            name='persona',
            field=models.ForeignKey(to='preventivos.Personas'),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='ciudad',
            field=models.ForeignKey(to='preventivos.RefCiudades', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='dependencias',
            name='unidades_regionales',
            field=models.ForeignKey(related_name='unidades', on_delete=django.db.models.deletion.PROTECT, to='preventivos.UnidadesRegionales'),
        ),
        migrations.AddField(
            model_name='armas',
            name='marcas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefTrademark', null=True),
        ),
        migrations.AddField(
            model_name='armas',
            name='sistema_disparo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, blank=True, to='preventivos.RefSistemadis', null=True),
        ),
        migrations.AddField(
            model_name='armas',
            name='subtipos',
            field=models.ForeignKey(to='preventivos.RefSubtiposa', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='armas',
            name='tipos',
            field=models.ForeignKey(to='preventivos.RefTiposarmas', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='ampliacion',
            name='autoridades',
            field=models.ManyToManyField(to='preventivos.RefAutoridad', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ampliacion',
            name='preventivo',
            field=models.ForeignKey(related_name='ampli', to='preventivos.Preventivos'),
        ),
        migrations.AddField(
            model_name='actuantes',
            name='dependencia_id',
            field=models.ForeignKey(to='preventivos.Dependencias', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='actuantes',
            name='jerarquia_id',
            field=models.ForeignKey(to='preventivos.RefJerarquias', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='actuantes',
            name='persona_id',
            field=models.ForeignKey(to='preventivos.Personas', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='actuantes',
            name='unidadreg_id',
            field=models.ForeignKey(to='preventivos.UnidadesRegionales', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterUniqueTogether(
            name='unidadesregionales',
            unique_together=set([('descripcion', 'ciudad')]),
        ),
        migrations.AlterUniqueTogether(
            name='refsubtiposa',
            unique_together=set([('descripcion', 'tipo')]),
        ),
        migrations.AlterUniqueTogether(
            name='refprovincia',
            unique_together=set([('descripcion', 'pais')]),
        ),
        migrations.AlterUniqueTogether(
            name='refmodoshecho',
            unique_together=set([('descripcion', 'delito')]),
        ),
        migrations.AlterUniqueTogether(
            name='refdelito',
            unique_together=set([('descripcion', 'tipo_delito')]),
        ),
        migrations.AlterUniqueTogether(
            name='refciudades',
            unique_together=set([('pais', 'provincia', 'departamento', 'descripcion')]),
        ),
        migrations.AlterUniqueTogether(
            name='refcategory',
            unique_together=set([('descripcion', 'rubro')]),
        ),
        migrations.AlterUniqueTogether(
            name='refcalles',
            unique_together=set([('descripcion', 'ciudad')]),
        ),
        migrations.AlterUniqueTogether(
            name='refbarrios',
            unique_together=set([('descripcion', 'ciudad')]),
        ),
        migrations.AlterUniqueTogether(
            name='personas',
            unique_together=set([('tipo_doc', 'nro_doc', 'apellidos', 'nombres')]),
        ),
        migrations.AlterUniqueTogether(
            name='persinvolucradas',
            unique_together=set([('hechos', 'persona', 'roles', 'cargado_prev', 'ampliacion')]),
        ),
        migrations.AlterUniqueTogether(
            name='padres',
            unique_together=set([('persona', 'padre_nombres', 'padre_apellidos', 'madre_nombres', 'madre_apellidos')]),
        ),
        migrations.AlterUniqueTogether(
            name='hechosdelito',
            unique_together=set([('hechos', 'refdelito', 'refmodoshecho')]),
        ),
        migrations.AlterUniqueTogether(
            name='domicilios',
            unique_together=set([('personas', 'ref_ciudades', 'barrio_codigo', 'fecha_desde', 'calle', 'altura')]),
        ),
        migrations.AlterUniqueTogether(
            name='detenidos',
            unique_together=set([('hechos', 'persona')]),
        ),
        migrations.AlterUniqueTogether(
            name='dependencias',
            unique_together=set([('descripcion', 'unidades_regionales', 'ciudad')]),
        ),
    ]
