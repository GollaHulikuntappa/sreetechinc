from django.shortcuts import render,redirect
from cablematrix.models import cablematrix
from django.db.models import Q
from cablematrix.forms import RequestModelForm,PortModelForm,DCSModelForm,TraceModelForm,DesignModelForm,MatrixModelForm,InstallationModelForm,MeasurementModelForm,SfpModelForm,BcsfpModelForm,OobModelForm,SubnetModelForm,PtModelForm
from cablematrix.forms import SvtModelForm,TurnModelForm,MigrationModelForm,DecommModelForm,SearchForm,PhaseForm,SortForm
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def error(request):
    return render(request,'cablematrix/error.html')

def success(request):
    return render(request,'cablematrix/success.html')

def completedetails(request):
    c=cablematrix.objects.count()
    d= cablematrix.objects.filter(fwdecommissionstatus="completed").count()
    # values={'name':'hulikuntappa','age':26,'location':'hyderabad'}
    # print(c)
    values={'cablematrix':c,'cablematrixcompleted':d}
    return render(request,'cablematrix/completedetails.html',values)


def requestinformation(request):
    success=""
    if request.method == "POST":
        form = RequestModelForm(request.POST)
        if form.is_valid():
            a=form.cleaned_data['existingdevicehostname']
            b=form.cleaned_data['newdevicehostname']
            s1=cablematrix.objects.filter(existingdevicehostname=a)
            s2=cablematrix.objects.filter(newdevicehostname=b)
            if ((len(s1) == 0) or (len(s2)==0)):
                form.save()
                success="Data is saved in the database"
            else:
                success="Data is already present in the database"
                
            
            # form.save()
            # return success(request)  # assuming 'homepage' is the name of your homepage view
        else:
            # print("form is not valid")
            print(form.errors)
            # form.errors
    
    else:
        form = RequestModelForm()        
    return render(request,'cablematrix/requestinformation.html',{'form':form,'success':success})

def dcsrequest(request):
    if request.method == "POST":
        form = DCSModelForm(request.POST)
        if form.is_valid():
            # form.save()   
            a=form.cleaned_data['existingdevicehostname']  
            b=form.cleaned_data['newdevicehostname']  
            s=cablematrix.objects.get(existingdevicehostname=a)
            s1=cablematrix.objects.get(newdevicehostname=b)
            # print(s.id)
            # print(s1.id)
            if s.id == s1.id:
                s.dcsrequesteddate=form.cleaned_data['dcsrequesteddate']
                s.dcsrequestid=form.cleaned_data['dcsrequestid']
                s.dcsrequestapproveddate=form.cleaned_data['dcsrequestapproveddate']
                s.dcsrequeststatus=form.cleaned_data['dcsrequeststatus']
                s.powercabinetstatus=form.cleaned_data['powercabinetstatus']
                s.rackstackstatus=form.cleaned_data['rackstackstatus']
                s.save()
                return success(request)
            else:
                return error(request)
                
                            
            # return homepage(request)  # assuming 'homepage' is the name of your homepage view
        else:
            # print("form is not valid")
            # print(form.errors)
            form.errors
            
    else:
        form = DCSModelForm()
    return render(request,'cablematrix/dcsrequest.html',{'form':form})    

def ccmd(request):
    s=cablematrix.objects.all()
    dicts={'alls':s}
    return render(request,'cablematrix/ccmd.html',dicts)


def completedevicedetails(request):
    pf=SortForm
    s=""
    data=""
    if request.method == 'POST':
        form=SortForm(request.POST)
        if form.is_valid():
            a=form.cleaned_data['existingdevicename']
            s=cablematrix.objects.filter(Q(existingdevicehostname=a))
            if (len(s) == 0):
                data="Device is not found in the database"
            else:
                data="Device is found in the database"
                
                 
    dictd={"form":pf, "alld":s,"data":data}       
    return render(request,'cablematrix/completedevicedetails.html',dictd)
    

def updatephasedetails(request,id):
    s=cablematrix.objects.get(id = id)
    form=RequestModelForm(instance=s)
    dform={'form':form}
    if request.method == "POST":
        form = RequestModelForm(request.POST,instance=s)
        # for field_name, field_value in request.POST.items():
        #     print(f"{field_name}: {field_value}")
        # print("data is getting successfully")
        if form.is_valid():
            form.save()
            return success(request)
    #         print("data is coming successfully")
        else:
            return error(request)
    #         print(form.errors)
    return render(request,'cablematrix/updaterequest.html',dform)

    
def phasedetails(request):
    pf=SortForm
    
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "DEVICE DETAILS":
            return redirect('/cable/completedevicedetails/')
    
    if request.method=="POST":
        action = request.POST.get('action')
        if action == "CREATE":
            return redirect('/cable/requestinformation/')
        elif action== "UPDATE":
            s=cablematrix.objects.all()[:15]
            dictr={'alldictr':s,"form":pf}
            return render(request,'cablematrix/phasesearch.html/',dictr)
        
            
        else:
            data=""
            s=cablematrix.objects.all()[:15]
            form=SortForm(request.POST)
            if form.is_valid():
                a= form.cleaned_data['existingdevicename']
                s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
                if (len(s1) == 0):
                    s=cablematrix.objects.all()[:15]
                    data="Data is not found in the database"
                else:
                    s=s1
                dictr={'alldictr':s,"form":pf,"data":data}
                return render(request,'cablematrix/phasesearch.html/',dictr)
            # form=PhaseForm
            # dform={'form':form}
            # if request.method == "POST":
            #     form=PhaseForm(request.POST)
            #     if form.is_valid():
            #         a=form.cleaned_data['existingdevicename']
            #         b=form.cleaned_data['newdevicename']
            #         # print(a)
            #         # print(b)
            #         s1=cablematrix.objects.get(existingdevicehostname=a)
            #         s2=cablematrix.objects.get(newdevicehostname=b)
            #         # print(s1.id)
            #         # print(s2.id)
            #         if s1.id == s2.id:
            #             return redirect('/cable/updatephasedetails/%s' % s1.id)
            #             # sc=cablematrix.objects.get(id = s1.id)
            #             # form=RequestModelForm(instance=sc)
            #             # dform={'form':form}
            #             # return render(request,'cablematrix/updaterequest.html',dform)
            # return render(request,'cablematrix/phasesearch.html',dform)
        
    c=cablematrix.objects.count()
    dcsrequest=cablematrix.objects.filter(dcsrequeststatus='active').count()
    trace=cablematrix.objects.filter(cabletracestatus='active').count()
    networkdesign=cablematrix.objects.filter(networkdesignstatus='active').count()
    matrix=cablematrix.objects.filter(cablematrixstatus='active').count()
    deviceinstallation=cablematrix.objects.filter(deviceinstallationstatus='active').count()
    cablemeasurement=cablematrix.objects.filter(cablemeasurementstatus='active').count()
    sfp=cablematrix.objects.filter(cablesfporderstatus='active').count()
    bcfsi=cablematrix.objects.filter(bladecablefibersfpinstallationstatus='active').count()
    oob=cablematrix.objects.filter(oobamityticketstatus='active').count()
    subnetvlan=cablematrix.objects.filter(subnetvlanipsrequeststatus='active').count()
    portassignment=cablematrix.objects.filter(portassignmentstatus='active').count()
    portturnup=cablematrix.objects.filter(portturnupmgmtstatus='active').count()
    fwsvt=cablematrix.objects.filter(fwsvtstatus='active').count()
    turnover=cablematrix.objects.filter(turnoverdocumentstatus='active').count()
    fwmigration=cablematrix.objects.filter(fwmigrationstatus='active').count()
    fwdecomm=cablematrix.objects.filter(fwdecommissionstatus='active').count()
    # fda= cablematrix.objects.filter(fwdecommissionstatus="completed").count()
    
    # values={'name':'hulikuntappa','age':26,'location':'hyderabad'}
    # print(c)
    values={'cablematrix':c,'dcsrequest':dcsrequest,'trace':trace,'networkdesign':networkdesign,'matrix':matrix,
            'deviceinstallation':deviceinstallation,'cablemeasurement':cablemeasurement,'sfp':sfp,'bcfsi':bcfsi,
            'oob':oob,'subnetvlan':subnetvlan,'portassignment':portassignment,'portturnup':portturnup,
            'fwsvt':fwsvt,'turnover':turnover,'fwmigration':fwmigration,'fwdecomm':fwdecomm}
    return render(request,'cablematrix/phasedetails.html',values)


def updatedcsrequest(request,id):
    s=cablematrix.objects.get(id = id)
    form=DCSModelForm(instance=s)
    dform={'form':form}
    if request.method == "POST":
        form = DCSModelForm(request.POST,instance=s)
        # for field_name, field_value in request.POST.items():
        #     print(f"{field_name}: {field_value}")
        # print("data is getting successfully")
        if form.is_valid():
            form.save()
            return success(request)
    #         print("data is coming successfully")
        else:
            return error(request)
    #         print(form.errors)
    return render(request,'cablematrix/updatedcs.html',dform)

def dcsdetails(request):
    s1=0
    s=cablematrix.objects.all()[:10]
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a=form.cleaned_data['existingdevicename']
            # b=form.cleaned_data['newdevicename']
            # print(a)
            # print(b)
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            # s2=cablematrix.objects.filter(Q(newdevicehostname__startswith=b))
            # print(s1.id)
            # print(s2.id)
            # for i in s1:
            #     print(i.id)
            if (len(s1) == 0):
                s=cablematrix.objects.all()
            else:
                s=s1
            
            
            
                
        
    pf=SortForm
    # s=cablematrix.objects.all()
    sa=cablematrix.objects.filter(dcsrequeststatus='active').count()
    sc=cablematrix.objects.filter(dcsrequeststatus='completed').count()
    soh=cablematrix.objects.filter(dcsrequeststatus='onhold').count()
    scc=cablematrix.objects.filter(dcsrequeststatus='cancelled').count()
    syt=cablematrix.objects.filter(dcsrequeststatus='yettowork').count()
    dicts={'alldcs':s,"active":sa,'completed':sc,'onhold':soh,'cancelled':scc,'yettowork':syt,"form":pf}
    if (request.method=="POST"):
        action = request.POST.get('action')
        if action == "CREATE":
            return redirect('/cable/dcsrequest/')
        elif action== "UPDATE":
            form=SearchForm
            dform={'form':form}
            if request.method == "POST":
                form=SearchForm(request.POST)
                if form.is_valid():
                    a=form.cleaned_data['existingdevicename']
                    b=form.cleaned_data['newdevicename']
                    s1=cablematrix.objects.get(existingdevicehostname=a)
                    s2=cablematrix.objects.get(newdevicehostname=b)
                    
                    if s1.id == s2.id:
                        return redirect('/cable/updatedcsrequest/%s' % s1.id)
                                        
                else:
                    print("form is invalid")
                    print(form.errors)
            return render(request,'cablematrix/search.html',dform)
            
    return render(request,'cablematrix/dcsrequestdetails.html',dicts)
    
    




def cabletracedetails(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(cabletracestatus='active').count()
    sc=cablematrix.objects.filter(cabletracestatus='completed').count()
    soh=cablematrix.objects.filter(cabletracestatus='onhold').count()
    scc=cablematrix.objects.filter(cabletracestatus='cancelled').count()
    syt=cablematrix.objects.filter(cabletracestatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Data is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt}
    return render(request,'cablematrix/cabletracedetails.html',dictr)

def updatetracedetails(request,id):
    s=cablematrix.objects.get(id = id)
    form=TraceModelForm(instance=s)
    dform={'form':form}
    if request.method == "POST":
        form = TraceModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return success(request)
        else:
            return error(request)
        
    return render(request,'cablematrix/updatetracedetails.html',dform)
        
        
def networkdesign(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(networkdesignstatus='active').count()
    sc=cablematrix.objects.filter(networkdesignstatus='completed').count()
    soh=cablematrix.objects.filter(networkdesignstatus='onhold').count()
    scc=cablematrix.objects.filter(networkdesignstatus='cancelled').count()
    syt=cablematrix.objects.filter(networkdesignstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/networkdesign.html',dictr)
    
    

def updatenetworkdesign(request,id):
    s=cablematrix.objects.get(id = id)
    form=DesignModelForm(instance=s)
    # data=""
    if request.method == "POST":
        form = DesignModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/networkdesign/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatenetworkdesign.html',dform)
    
    
    
def matrix(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(cablematrixstatus='active').count()
    sc=cablematrix.objects.filter(cablematrixstatus='completed').count()
    soh=cablematrix.objects.filter(cablematrixstatus='onhold').count()
    scc=cablematrix.objects.filter(cablematrixstatus='cancelled').count()
    syt=cablematrix.objects.filter(cablematrixstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/matrix.html',dictr)
    
def updatecablematrix(request,id):
    s=cablematrix.objects.get(id = id)
    form=MatrixModelForm(instance=s)
    # data=""
    if request.method == "POST":
        form = MatrixModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/matrix/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatecablematrix.html',dform)
      
def installation(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(deviceinstallationstatus='active').count()
    sc=cablematrix.objects.filter(deviceinstallationstatus='completed').count()
    soh=cablematrix.objects.filter(deviceinstallationstatus='onhold').count()
    scc=cablematrix.objects.filter(deviceinstallationstatus='cancelled').count()
    syt=cablematrix.objects.filter(deviceinstallationstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/installation.html',dictr)


def updateinstallation(request,id):
    s=cablematrix.objects.get(id = id)
    form=InstallationModelForm(instance=s)
    if request.method == "POST":
        form = InstallationModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/installation/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updateinstallation.html',dform)


def portassignment(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(portassignmentstatus='active').count()
    sc=cablematrix.objects.filter(portassignmentstatus='completed').count()
    soh=cablematrix.objects.filter(portassignmentstatus='onhold').count()
    scc=cablematrix.objects.filter(portassignmentstatus='cancelled').count()
    syt=cablematrix.objects.filter(portassignmentstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/portassignment.html',dictr)

def updateportassignment(request,id):
    s=cablematrix.objects.get(id = id)
    form=PortModelForm(instance=s)
    if request.method == "POST":
        form = PortModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/portassignment/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updateportassignment.html',dform)


def measurement(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(cablemeasurementstatus='active').count()
    sc=cablematrix.objects.filter(cablemeasurementstatus='completed').count()
    soh=cablematrix.objects.filter(cablemeasurementstatus='onhold').count()
    scc=cablematrix.objects.filter(cablemeasurementstatus='cancelled').count()
    syt=cablematrix.objects.filter(cablemeasurementstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/measurement.html',dictr)

def updatemeasurement(request,id):
    s=cablematrix.objects.get(id = id)
    form=MeasurementModelForm(instance=s)
    if request.method == "POST":
        form = MeasurementModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/measurement/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatemeasurement.html',dform)

def sfporder(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(cablesfporderstatus='active').count()
    sc=cablematrix.objects.filter(cablesfporderstatus='completed').count()
    soh=cablematrix.objects.filter(cablesfporderstatus='onhold').count()
    scc=cablematrix.objects.filter(cablesfporderstatus='cancelled').count()
    syt=cablematrix.objects.filter(cablesfporderstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/sfporder.html',dictr)

def updatesfporder(request,id):
    s=cablematrix.objects.get(id = id)
    form=SfpModelForm(instance=s)
    if request.method == "POST":
        form = SfpModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/sfporder/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatesfporder.html',dform)

def bcsfp(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(bladecablefibersfpinstallationstatus='active').count()
    sc=cablematrix.objects.filter(bladecablefibersfpinstallationstatus='completed').count()
    soh=cablematrix.objects.filter(bladecablefibersfpinstallationstatus='onhold').count()
    scc=cablematrix.objects.filter(bladecablefibersfpinstallationstatus='cancelled').count()
    syt=cablematrix.objects.filter(bladecablefibersfpinstallationstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/bcsfp.html',dictr)

def updatebcsfp(request,id):
    s=cablematrix.objects.get(id = id)
    form=BcsfpModelForm(instance=s)
    if request.method == "POST":
        form = BcsfpModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/bcsfp/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatebcsfp.html',dform)


def oob(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(oobamityticketstatus='active').count()
    sc=cablematrix.objects.filter(oobamityticketstatus='completed').count()
    soh=cablematrix.objects.filter(oobamityticketstatus='onhold').count()
    scc=cablematrix.objects.filter(oobamityticketstatus='cancelled').count()
    syt=cablematrix.objects.filter(oobamityticketstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/oob.html',dictr)

def updateoob(request,id):
    s=cablematrix.objects.get(id = id)
    form=OobModelForm(instance=s)
    if request.method == "POST":
        form = OobModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/oob/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updateoob.html',dform)

def subnet(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(subnetvlanipsrequeststatus='active').count()
    sc=cablematrix.objects.filter(subnetvlanipsrequeststatus='completed').count()
    soh=cablematrix.objects.filter(subnetvlanipsrequeststatus='onhold').count()
    scc=cablematrix.objects.filter(subnetvlanipsrequeststatus='cancelled').count()
    syt=cablematrix.objects.filter(subnetvlanipsrequeststatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/subnet.html',dictr)

def updatesubnet(request,id):
    s=cablematrix.objects.get(id = id)
    form=SubnetModelForm(instance=s)
    if request.method == "POST":
        form = SubnetModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/subnet/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatesubnet.html',dform)

    
def pt(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(portturnupmgmtstatus='active').count()
    sc=cablematrix.objects.filter(portturnupmgmtstatus='completed').count()
    soh=cablematrix.objects.filter(portturnupmgmtstatus='onhold').count()
    scc=cablematrix.objects.filter(portturnupmgmtstatus='cancelled').count()
    syt=cablematrix.objects.filter(portturnupmgmtstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/pt.html',dictr)

def updatept(request,id):
    s=cablematrix.objects.get(id = id)
    form=PtModelForm(instance=s)
    if request.method == "POST":
        form = PtModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/pt/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatept.html',dform)

def svt(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(fwsvtstatus='active').count()
    sc=cablematrix.objects.filter(fwsvtstatus='completed').count()
    soh=cablematrix.objects.filter(fwsvtstatus='onhold').count()
    scc=cablematrix.objects.filter(fwsvtstatus='cancelled').count()
    syt=cablematrix.objects.filter(fwsvtstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/svt.html',dictr)

def updatesvt(request,id):
    s=cablematrix.objects.get(id = id)
    form=SvtModelForm(instance=s)
    if request.method == "POST":
        form = SvtModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/svt/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatesvt.html',dform)

def turn(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(turnoverdocumentstatus='active').count()
    sc=cablematrix.objects.filter(turnoverdocumentstatus='completed').count()
    soh=cablematrix.objects.filter(turnoverdocumentstatus='onhold').count()
    scc=cablematrix.objects.filter(turnoverdocumentstatus='cancelled').count()
    syt=cablematrix.objects.filter(turnoverdocumentstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/turn.html',dictr)

def updateturn(request,id):
    s=cablematrix.objects.get(id = id)
    form=TurnModelForm(instance=s)
    if request.method == "POST":
        form = TurnModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/turn/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updateturn.html',dform)

    
def migration(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(fwmigrationstatus='active').count()
    sc=cablematrix.objects.filter(fwmigrationstatus='completed').count()
    soh=cablematrix.objects.filter(fwmigrationstatus='onhold').count()
    scc=cablematrix.objects.filter(fwmigrationstatus='cancelled').count()
    syt=cablematrix.objects.filter(fwmigrationstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/migration.html',dictr)

def updatemigration(request,id):
    s=cablematrix.objects.get(id = id)
    form=MigrationModelForm(instance=s)
    if request.method == "POST":
        form = MigrationModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/migration/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatemigration.html',dform)


def decomm(request):
    s=cablematrix.objects.all()[:15]
    sa=cablematrix.objects.filter(fwdecommissionstatus='active').count()
    sc=cablematrix.objects.filter(fwdecommissionstatus='completed').count()
    soh=cablematrix.objects.filter(fwdecommissionstatus='onhold').count()
    scc=cablematrix.objects.filter(fwdecommissionstatus='cancelled').count()
    syt=cablematrix.objects.filter(fwdecommissionstatus='yettowork').count()
    pf=SortForm
    data=""
    if request.method == "POST":
        form=SortForm(request.POST)
        if form.is_valid():
            a= form.cleaned_data['existingdevicename']
            s1=cablematrix.objects.filter(Q(existingdevicehostname__startswith=a))
            if (len(s1) == 0):
                s=cablematrix.objects.all()[:15]
                data="Device is not found in the database"
            else:
                s=s1
    dictr={'alldictr':s,"form":pf,"data":data,"active":sa,"complete":sc,'onhold':soh,'cancel':scc,'yettowork':syt,"data":data}
    return render(request,'cablematrix/decomm.html',dictr)

def updatedecomm(request,id):
    s=cablematrix.objects.get(id = id)
    form=DecommModelForm(instance=s)
    if request.method == "POST":
        form = DecommModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('/cable/decomm/')
    
    dform={'form':form}    
    return render(request,'cablematrix/updatedecomm.html',dform)

def deletedcsrequest(request,id):
    s=cablematrix.objects.get(id=id)
    s.delete()
    return redirect('/cable/phasedetails/')