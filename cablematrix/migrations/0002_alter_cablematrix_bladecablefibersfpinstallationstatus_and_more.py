# Generated by Django 5.0.6 on 2024-06-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cablematrix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cablematrix',
            name='bladecablefibersfpinstallationstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='bladecablefibersfpinstallationticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='bladecablefibersfpinstallationticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='bladecablefibersfpinstallationticketrequestedid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='bladecablefibersfpinstallationticketrequired',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablematrixcompleteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablematrixstarteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablematrixstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablemeasurementstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablemeasurementticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablemeasurementticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablemeasurementticketrequestedid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablemeasurementticketrequired',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cablesfporderstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cabletracereceiveddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cabletracerequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cabletracestatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cabletraceticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cabletraceticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='cabletraceticketrequestedid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='capitalpmattno',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='clli',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='dateofordercables',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='dateofordersfps',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='dcsrequestapproveddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='dcsrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='dcsrequestid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='dcsrequeststatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deliveryetacables',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deliveryetasfps',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationcompletiondate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationticketrequestid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='deviceinstallationticketrequired',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='domain',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='existingdevicehostname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='existingdevicemodel',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwdecommissioneddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwmigrationpolicyimportdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwmigrationproductiondate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwmigrationstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwsvtcompleteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwsvtstarteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='fwsvtstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='implementationpmattno',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='location',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='networkdesigncloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='networkdesignstartdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='networkdesignstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='newdevicehostname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='newdevicemodel',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='oobamityticket',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='oobamityticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='oobamityticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='oobamityticketrequestedid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='oobamityticketstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portassignmentstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portassignmentticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portassignmentticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portassignmentticketrequestid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portassignmentticketrequired',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portturnupdatafeedstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portturnupmgmtstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portturnupticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portturnupticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portturnupticketrequestedid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='portturnupticketrequired',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='powercabinetstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='projectmanager',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='projectname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='rackstackstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='requestor',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='requesttypedatafeedmgmtcables',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='requirementreceiveddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlandnsrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlandnsrequeststatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanipsrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanipsrequeststatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanticketcloseddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanticketrequesteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanticketrequestedid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanticketrequeststatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='subnetvlanticketrequired',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='ticketsrequired',
            field=models.CharField(blank=True, choices=[('email', 'EMAIL'), ('ess', 'ESS'), ('itons', 'ITONS'), ('aorts', 'AORTS')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='turnoverdocumentcompleteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='turnoverdocumentstarteddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cablematrix',
            name='turnoverdocumentstatus',
            field=models.CharField(blank=True, choices=[('active', 'ACTIVE'), ('inprogress', 'INPROGRESS'), ('completed', 'COMPLETED'), ('onhold', 'ONHOLD'), ('cancelled', 'CANCELLED')], max_length=1000, null=True),
        ),
    ]
