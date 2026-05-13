from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_admin', '0015_event_progress_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='progress_status',
            field=models.CharField(
                choices=[
                    ('not_started', 'Chưa diễn ra'),
                    ('postponed', 'Hoãn'),
                    ('over_budget', 'Vượt ngân sách'),
                    ('100', '100%'),
                    ('90', '90%'),
                    ('80', '80%'),
                    ('70', '70%'),
                    ('60', '60%'),
                    ('50', '50%'),
                    ('40', '40%'),
                    ('30', '30%'),
                    ('20', '20%'),
                    ('10', '10%'),
                ],
                default='10',
                max_length=20,
            ),
        ),
    ]
