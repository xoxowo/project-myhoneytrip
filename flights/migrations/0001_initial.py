# Generated by Django 4.0.6 on 2022-08-02 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo_url', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'airlines',
            },
        ),
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('airplane_code', models.CharField(max_length=50)),
                ('number_of_seats', models.IntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.airline')),
            ],
            options={
                'db_table': 'airplane',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('airport_code', models.CharField(max_length=50)),
                ('airport_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='LocationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_url', models.CharField(max_length=300)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.location')),
            ],
            options={
                'db_table': 'location_images',
            },
        ),
        migrations.CreateModel(
            name='FlightRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10)),
                ('airpalne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.airplane')),
                ('departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure', to='flights.location')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='flights.location')),
            ],
            options={
                'db_table': 'flight_routes',
            },
        ),
        migrations.CreateModel(
            name='FlightDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('remaining_seats', models.IntegerField()),
                ('reserved_seats', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('flight_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flightroute')),
            ],
            options={
                'db_table': 'flight_details',
            },
        ),
    ]