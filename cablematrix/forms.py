from django import forms
from cablematrix.models import cablematrix

class RequestModelForm(forms.ModelForm):
    requirementreceiveddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['requestor','requesttypedatafeedmgmtcables','existingdevicehostname','existingdevicemodel',
                'requirementreceiveddate','implementationpmattno','capitalpmattno','projectname','projectmanager',
                'newdevicehostname','newdevicemodel','location','clli','domain','planner']
        
        
        
class DCSModelForm(forms.ModelForm):
    dcsrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    dcsrequestapproveddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','dcsrequesteddate','dcsrequestid','dcsrequestapproveddate',
                'dcsrequeststatus','powercabinetstatus','rackstackstatus']     
        
        
class TraceModelForm(forms.ModelForm):
    cabletracerequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    cabletracereceiveddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    cabletraceticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    cabletraceticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','cabletracerequesteddate','cabletracereceiveddate',
                'cabletraceticketsrequired','cabletraceticketrequesteddate','cabletraceticketrequestedid',
                'cabletraceticketcloseddate','cabletracestatus']



class DesignModelForm(forms.ModelForm):
    networkdesignstartdate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    networkdesigncloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','networkdesignstartdate','networkdesigncloseddate',
                'networkdesignstatus']    

class MatrixModelForm(forms.ModelForm):
    cablematrixstarteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    cablematrixcompleteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','cablematrixstarteddate','cablematrixcompleteddate',
                'cablematrixstatus']
        
class InstallationModelForm(forms.ModelForm):
    deviceinstallationrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    deviceinstallationticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    deviceinstallationticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    deviceinstallationcompletiondate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','deviceinstallationrequesteddate','deviceinstallationticketrequired',
                'deviceinstallationticketrequesteddate','deviceinstallationticketrequestid','deviceinstallationticketcloseddate',
                'deviceinstallationstatus','deviceinstallationcompletiondate']
            

class MeasurementModelForm(forms.ModelForm):
    cablemeasurementticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    cablemeasurementticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','cablemeasurementticketrequired','cablemeasurementticketrequesteddate',
                'cablemeasurementticketrequestedid','cablemeasurementstatus','cablemeasurementticketcloseddate']


class SfpModelForm(forms.ModelForm):
    dateofordercables = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    dateofordersfps = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    deliveryetacables = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    deliveryetasfps = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','dateofordercables','dateofordersfps','deliveryetacables','deliveryetasfps','cablesfporderstatus']
             
class PortModelForm(forms.ModelForm):
    portassignmentticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    portassignmentticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','portassignmentticketrequired','portassignmentticketrequesteddate','portassignmentticketrequestid',
                'portassignmentstatus','portassignmentticketcloseddate']


class BcsfpModelForm(forms.ModelForm):
    bladecablefibersfpinstallationticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    bladecablefibersfpinstallationticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','bladecablefibersfpinstallationticketrequired','bladecablefibersfpinstallationticketrequesteddate',
                'bladecablefibersfpinstallationticketrequestedid','bladecablefibersfpinstallationstatus','bladecablefibersfpinstallationticketcloseddate']
        


class OobModelForm(forms.ModelForm):
    oobamityticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    oobamityticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','oobamityticket','oobamityticketrequesteddate','oobamityticketrequestedid',
                'oobamityticketstatus','oobamityticketcloseddate']
        
        
class SubnetModelForm(forms.ModelForm):
    subnetvlanticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    subnetvlanticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    subnetvlanipsrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    subnetvlandnsrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','subnetvlanticketrequired','subnetvlanticketrequesteddate',
                'subnetvlanticketrequestedid','subnetvlanticketrequeststatus','subnetvlanticketcloseddate',
                'subnetvlanipsrequesteddate','subnetvlanipsrequeststatus','subnetvlandnsrequesteddate','subnetvlandnsrequeststatus']
        
class PtModelForm(forms.ModelForm):
    portturnupticketrequesteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    portturnupticketcloseddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','portturnupticketrequired','portturnupticketrequesteddate',
                'portturnupticketrequestedid','portturnupmgmtstatus','portturnupdatafeedstatus','portturnupticketcloseddate']
        
class SvtModelForm(forms.ModelForm):
    fwsvtstarteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    fwsvtcompleteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','fwsvtstarteddate','fwsvtstatus','fwsvtcompleteddate']

class TurnModelForm(forms.ModelForm):
    turnoverdocumentstarteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    turnoverdocumentcompleteddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','turnoverdocumentstarteddate','turnoverdocumentstatus','turnoverdocumentcompleteddate']
            
            
class MigrationModelForm(forms.ModelForm):
    fwmigrationpolicyimportdate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    fwmigrationproductiondate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','fwmigrationpolicyimportdate','fwmigrationproductiondate','fwmigrationstatus']
        
        
class DecommModelForm(forms.ModelForm):
    fwdecommissioneddate = forms.DateField(
        input_formats=['%m/%d/%Y'],
        widget=forms.DateInput(format='%m/%d/%Y',attrs={'class': 'date-input','placeholder': 'MM/DD/YYYY'})
    )
    class Meta:
        model=cablematrix
        fields=['existingdevicehostname','newdevicehostname','fwdecommissioneddate','fwdecommissionstatus']
        
class SearchForm(forms.Form):
    existingdevicename = forms.CharField(max_length=100)
    newdevicename = forms.CharField(max_length=100)
    ticketid = forms.CharField(max_length=100)
    
class PhaseForm(forms.Form):
    existingdevicename=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Existing device name'}))
    newdevicename=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'New device name'}))
    

class SortForm(forms.Form):
    existingdevicename=forms.CharField(max_length=1000,widget=forms.TextInput(attrs={'placeholder': 'Existing device name'}))
    