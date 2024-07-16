from django.urls import path
from cablematrix.views import portassignment,requestinformation,dcsrequest,networkdesign,matrix,installation,measurement,sfporder,bcsfp,oob,subnet,pt
from cablematrix.views import svt,turn,migration,decomm,completedetails,ccmd,phasedetails,cabletracedetails,dcsdetails,updatedcsrequest,updatephasedetails,deletedcsrequest
from cablematrix.views import updatetracedetails,completedevicedetails,updatenetworkdesign,updatecablematrix,updateinstallation,updateportassignment,updatemeasurement,updatesfporder
from cablematrix.views import updatebcsfp,updateoob,updatesubnet,updatept,updatesvt,updateturn,updatemigration,updatedecomm
urlpatterns = [
   path('portassignment/',portassignment),
   path('requestinformation/',requestinformation),
   path('dcsrequest/',dcsrequest),
   path('networkdesign/',networkdesign),
   path('matrix/',matrix),
   path('installation/',installation),
   path('measurement/',measurement),
   path('sfporder/',sfporder),
   path('bcsfp/',bcsfp),
   path('oob/',oob),
   path('subnet/',subnet),
   path('pt/',pt),
   path('svt/',svt),
   path('turn/',turn),
   path('migration/',migration),
   path('decomm/',decomm),
   path('details/',completedetails),
   path('ccmd/',ccmd),
   path('phasedetails/',phasedetails),
   path('dcsdetails/',dcsdetails),
   path('cabletracedetails/',cabletracedetails),
   path('updatedcsrequest/<int:id>',updatedcsrequest),
   path('updatephasedetails/<int:id>',updatephasedetails),
   path('updatetracedetails/<int:id>',updatetracedetails),
   path('updatenetworkdesign/<int:id>',updatenetworkdesign),
   path('updatecablematrix/<int:id>',updatecablematrix),
   path('updateinstallation/<int:id>',updateinstallation),
   path('updateportassignment/<int:id>',updateportassignment),
   path('updatemeasurement/<int:id>',updatemeasurement),
   path('updatesfporder/<int:id>',updatesfporder),
   path('updatebcsfp/<int:id>',updatebcsfp),
   path('updateoob/<int:id>',updateoob),
   path('updatesubnet/<int:id>',updatesubnet),
   path('updatept/<int:id>',updatept),
   path('updateturn/<int:id>',updateturn),
   path('updatesvt/<int:id>',updatesvt),
   path('updatemigration/<int:id>',updatemigration),
   path('updatedecomm/<int:id>',updatedecomm),
   path('deletedcsrequest/<int:id>',deletedcsrequest),
   path('completedevicedetails/',completedevicedetails),
]
