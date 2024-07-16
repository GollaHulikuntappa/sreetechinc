from django.db import models

# Create your models here.

class cablematrix(models.Model):
    ticket_type=[
        ('email','EMAIL'),
        ('ess','ESS'),
        ('itons','ITONS'),
        ('aorts','AORTS'),
    ]
    
    status_type=[
        ('active','ACTIVE'),
        ('inprogress','INPROGRESS'),
        ('completed','COMPLETED'),
        ('onhold','ONHOLD'),
        ('cancelled','CANCELLED'),
        ('yettowork','Yet To Work'),
        ('notrequired','Not Required'),
    ]
    
    planner_type=[
        ('kalasapati venkata srivalli','KALASAPATI, VENKATA SRIVALLI'),
        ('dharanidhar mandala','DHARANIDHAR MANDALA'),
        ('syed khaja hussain','SYED, KHAJA HUSSAIN'),
        ('pasunuru santosh','PASUNURU, SANTOSH'),
        ('ravipati pavan kumar','RAVIPATI, PAVAN KUMAR'),
        ('ravilisetty satya madhav','RAVILISETTY, SATYA MADHAV'),
        ('tharigopula narendra reddy','THARIGOPULA, NARENDRA REDDY'),
        ('sangisetti pranay teja','SANGISETTI, PRANAY TEJA'),
        
    ]
    requestor=models.CharField(max_length=1000,null=True, blank=True)
    requesttypedatafeedmgmtcables=models.CharField(max_length=1000,null=True, blank=True)
    existingdevicehostname=models.CharField(max_length=1000,null=True, blank=True)
    existingdevicemodel=models.CharField(max_length=1000,null=True, blank=True)
    requirementreceiveddate=models.DateField(null=True, blank=True)
    implementationpmattno=models.CharField(max_length=1000,null=True, blank=True)
    capitalpmattno=models.CharField(max_length=1000,null=True, blank=True)
    projectname=models.CharField(max_length=1000,null=True, blank=True)
    projectmanager=models.CharField(max_length=1000,null=True, blank=True)
    newdevicehostname=models.CharField(max_length=1000,null=True, blank=True)
    newdevicemodel=models.CharField(max_length=1000,null=True, blank=True)
    location=models.CharField(max_length=1000,null=True, blank=True)
    clli=models.CharField(max_length=1000,null=True, blank=True)
    domain=models.CharField(max_length=1000,null=True, blank=True)
    planner=models.CharField(max_length=1000,choices=planner_type,null=True, blank=True)
    dcsrequesteddate=models.DateField(null=True, blank=True)
    dcsrequestid=models.CharField(max_length=1000,null=True, blank=True)
    dcsrequestapproveddate=models.DateField(null=True, blank=True)
    dcsrequeststatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    powercabinetstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    rackstackstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    cabletracerequesteddate=models.DateField(null=True, blank=True)
    cabletracereceiveddate=models.DateField(null=True, blank=True)
    cabletraceticketsrequired=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    cabletraceticketrequesteddate=models.DateField(null=True, blank=True)
    cabletraceticketrequestedid=models.CharField(max_length=1000,null=True, blank=True)
    cabletraceticketcloseddate=models.DateField(null=True, blank=True)
    cabletracestatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    networkdesignstartdate=models.DateField(null=True, blank=True)
    networkdesigncloseddate=models.DateField(null=True, blank=True)
    networkdesignstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    cablematrixstarteddate=models.DateField(null=True, blank=True)
    cablematrixcompleteddate=models.DateField(null=True, blank=True)
    cablematrixstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    deviceinstallationrequesteddate=models.DateField(null=True, blank=True)
    deviceinstallationticketrequired=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    deviceinstallationticketrequesteddate=models.DateField(null=True, blank=True)
    deviceinstallationticketrequestid=models.CharField(max_length=1000,null=True, blank=True)
    deviceinstallationticketcloseddate=models.DateField(null=True, blank=True)
    deviceinstallationstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    deviceinstallationcompletiondate=models.DateField(null=True, blank=True)
    portassignmentticketrequired=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    portassignmentticketrequesteddate=models.DateField(null=True, blank=True)
    portassignmentticketrequestid=models.CharField(max_length=1000,null=True, blank=True)
    portassignmentstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    portassignmentticketcloseddate=models.DateField(null=True, blank=True)
    cablemeasurementticketrequired=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    cablemeasurementticketrequesteddate=models.DateField(null=True, blank=True)
    cablemeasurementticketrequestedid=models.CharField(max_length=1000,null=True, blank=True)
    cablemeasurementstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    cablemeasurementticketcloseddate=models.DateField(null=True, blank=True)
    dateofordercables=models.DateField(null=True, blank=True)
    dateofordersfps=models.DateField(null=True, blank=True)
    deliveryetacables=models.DateField(null=True, blank=True)
    deliveryetasfps=models.DateField(null=True, blank=True)
    cablesfporderstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    bladecablefibersfpinstallationticketrequired=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    bladecablefibersfpinstallationticketrequesteddate=models.DateField(null=True, blank=True)
    bladecablefibersfpinstallationticketrequestedid=models.CharField(max_length=1000,null=True, blank=True)
    bladecablefibersfpinstallationstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    bladecablefibersfpinstallationticketcloseddate=models.DateField(null=True, blank=True)
    oobamityticket=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    oobamityticketrequesteddate=models.DateField(null=True, blank=True)
    oobamityticketrequestedid=models.CharField(max_length=1000,null=True, blank=True)
    oobamityticketstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    oobamityticketcloseddate=models.DateField(null=True, blank=True)
    subnetvlanticketrequired=models.CharField(max_length=1000,choices=ticket_type,null=True, blank=True)
    subnetvlanticketrequesteddate=models.DateField(null=True, blank=True)
    subnetvlanticketrequestedid=models.CharField(max_length=1000,null=True, blank=True)
    subnetvlanticketrequeststatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    subnetvlanticketcloseddate=models.DateField(null=True, blank=True)
    subnetvlanipsrequesteddate=models.DateField(null=True, blank=True)
    subnetvlanipsrequeststatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    subnetvlandnsrequesteddate=models.DateField(null=True, blank=True)
    subnetvlandnsrequeststatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    portturnupticketrequired=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    portturnupticketrequesteddate=models.DateField(null=True, blank=True)
    portturnupticketrequestedid=models.CharField(max_length=1000,null=True, blank=True)
    portturnupmgmtstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    portturnupdatafeedstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    portturnupticketcloseddate=models.DateField(null=True, blank=True)
    fwsvtstarteddate=models.DateField(null=True, blank=True)
    fwsvtstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    fwsvtcompleteddate=models.DateField(null=True, blank=True)
    turnoverdocumentstarteddate=models.DateField(null=True, blank=True)
    turnoverdocumentstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    turnoverdocumentcompleteddate=models.DateField(null=True, blank=True)
    fwmigrationpolicyimportdate=models.DateField(null=True, blank=True)
    fwmigrationproductiondate=models.DateField(null=True, blank=True)
    fwmigrationstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
    fwdecommissioneddate=models.DateField(null=True, blank=True)
    fwdecommissionstatus=models.CharField(max_length=1000,choices=status_type,null=True, blank=True)
