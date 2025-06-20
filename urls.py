<<<<<<< HEAD
"""
URL configuration for DRPclinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doctor.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from .import views
from django.urls import path
urlpatterns=[
    path('',views.homee,name='homee'),
    path('index',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('appointmentinsert',views.appointmentinsert,name='appointmentinsert'),
    path('contact',views.contact,name='contact'),
    path('emp',views.emp,name='emp'),
    path('occupationinsert',views.occupationinsert,name='occupationinsert'),
    path('occupationedit/<occid>',views.occupationedit,name='occupationedit'),
    path('occupationdel/<occid>',views.occupationdel,name='occupationdel'),
    path('patientinsert',views.patientinsert,name='patientinsert'),
    path('patientview',views.patientview,name='patientview'),
    path('patientedit/<patid>',views.patientedit,name='patientedit'),
    path('patientdel/<patid>',views.patientdel,name='patientdel'),
    path('complaintinsert',views.complaintinsert,name='complaintinsert'),
    path('complaintview',views.complaintview,name='complaintview'),
    path('complaintedit/<comid>',views.complaintedit,name='complaintedit'),
    path('complaintdel/<comid>', views.complaintdel, name='complaintdel'),
    path('HPIinsert', views.HPIinsert, name='HPIinsert'),
    path('HPIdetails/<int:id>/', views.HPIdetails, name='HPIdetails'),
    path('HPIedit/<HPIid>', views.HPIedit, name='HPIedit'),
    path('HPIdel/<HPIid>', views.HPIdel, name='HPIdel'),
    path('MedHisdetails/<int:id>/', views.MedHisdetails, name='MedHisdetails'),
    path('MedHisedit/<MHid>',views.MedHisedit,name='MedHisedit'),
    path('MedHisdel/<MHid>', views.MedHisdel, name='MedHisdel'),
    path('SocialHisdetails/<int:id>/', views.SocialHisdetails, name='SocialHisdetails'),
    path('SocialHisedit/<SHid>',views.SocialHisedit,name='SocialHisedit'),
    path('SocialHisdel/<SHid>', views.SocialHisdel, name='SocialHisdel'),
    path('obbassinsert/<int:id>/',views.obbassinsert,name='obbassinsert'),
    path('obbassedit/<OAid>',views.obbassedit,name='obbassedit'),
    path('obbassdel/<OAid>', views.obbassdel, name='obbassdel'),
    path('ROMtypeinsert', views.ROMtypeinsert, name='ROMtypeinsert'),
    path('ROMtypeedit/<Rid>',views.ROMtypeedit,name='ROMtypeedit'),
    path('ROMtypedel/<Rid>', views.ROMtypedel, name='ROMtypedel'),
    path('cervicalspinemotioninsert', views.cervicalspinemotioninsert, name='cervicalspinemotioninsert'),
    path('cervicalspinemotionedit/<CSid>',views.cervicalspinemotionedit,name='cervicalspinemotionedit'),
    path('cervicalspinemotiondel/<CSid>', views.cervicalspinemotiondel, name='cervicalspinemotiondel'),
    path('ROMin', views.ROMin, name='ROMin'),
    path('ROMedit/<rid>', views.ROMedit, name='ROMedit'),
    path('ROMdel/<rid>', views.ROMdel, name='ROMdel'),
    path('ROMinsert', views.ROMinsert, name='ROMinsert'),
    path('ROMdetails/<int:id>/', views.ROMdetails, name='ROMdetails'),
    path('MMTinsert', views.MMTinsert, name='MMTinsert'),
    path('MMTedit/<Mid>', views.MMTedit, name='MMTedit'),
    path('MMTdel/<Mid>', views.MMTdel, name='MMTdel'),
    path('MMTmotioninsert', views.MMTmotioninsert, name='MMTmotioninsert'),
    path('MMTmotionedit/<Mmid>',views.MMTmotionedit,name='MMTmotionedit'),
    path('MMTmotiondel/<Mmid>', views.MMTmotiondel, name='MMTmotiondel'),
    path('MMTmotionview', views.MMTmotionview, name='MMTmotionview'),
    path('MMTmotiondetails/<int:id>/', views.MMTmotiondetails, name='MMTmotiondetails'),
    path('SPTEinsert', views.SPTEinsert, name='SPTEinsert'),
    path('SPTEview', views.SPTEview, name='SPTEview'),
    path('SPTEdetails/<int:id>/', views.SPTEdetails, name='SPTEdetails'),
    path('SPTEedit/<STid>',views.SPTEedit,name='SPTEedit'),
    path('SPTEdel/<STid>', views.SPTEdel, name='SPTEdel'),
    path('PALPATIONinsert', views.PALPATIONinsert, name='PALPATIONinsert'),
    path('PALPATIONdetails/<int:id>/', views.PALPATIONdetails, name='PALPATIONdetails'),
    path('PALPATIONedit/<Pid>',views.PALPATIONedit,name='PALPATIONedit'),
    path('PALPATIONdel/<Pid>', views.PALPATIONdel, name='PALPATIONdel'),
    path('NEUROASSinsert', views.NEUROASSinsert, name='NEUROASSinsert'),
    path('NEUROASSdetails/<int:id>/', views.NEUROASSdetails, name='NEUROASSdetails'),
    path('NEUROASSedit/<NAid>',views.NEUROASSedit,name='NEUROASSedit'),
    path('NEUROASSdel/<NAid>', views.NEUROASSdel, name='NEUROASSdel'),
    path('FUNLIMinsert', views.FUNLIMinsert, name='FUNLIMinsert'),
    path('FUNLIMview', views.FUNLIMview, name='FUNLIMview'),
    path('FUNLIMdetails/<int:id>/', views.FUNLIMdetails, name='FUNLIMdetails'),
    path('FUNLIMedit/<FLid>',views.FUNLIMedit,name='FUNLIMedit'),
    path('FUNLIMdel/<FLid>', views.FUNLIMdel, name='FUNLIMdel'),
    path('DIAGNOSinsert', views.DIAGNOSinsert, name='DIAGNOSinsert'),
    path('DIAGNOSdetails/<int:id>/', views.DIAGNOSdetails, name='DIAGNOSdetails'),
    path('DIAGNOSedit/<DGid>',views.DIAGNOSedit,name='DIAGNOSedit'),
    path('DIAGNOSdel/<DGid>', views.DIAGNOSdel, name='DIAGNOSdel'),
    path('IMPRESSIONinsert', views.IMPRESSIONinsert, name='IMPRESSIONinsert'),
    path('IMPRESSIONview', views.IMPRESSIONview, name='IMPRESSIONview'),
    path('IMPRESSIONdetails/<int:id>/', views.IMPRESSIONdetails, name='IMPRESSIONdetails'),
    path('IMPRESSIONedit/<IMid>',views.IMPRESSIONedit,name='IMPRESSIONedit'),
    path('IMPRESSIONdel/<IMid>', views.IMPRESSIONdel, name='IMPRESSIONdel'),
    path('PHYSIOGOALSinsert', views.PHYSIOGOALSinsert, name='PHYSIOGOALSinsert'),
    path('PHYSIOGOALSdetails/<int:id>/', views.PHYSIOGOALSdetails, name='PHYSIOGOALSdetails'),
    path('PHYSIOGOALSedit/<PGid>',views.PHYSIOGOALSedit,name='PHYSIOGOALSedit'),
    path('PHYSIOGOALSdel/<PGid>', views.PHYSIOGOALSdel, name='PHYSIOGOALSdel'),
    path('PLANCAREinsert', views.PLANCAREinsert, name='PLANCAREinsert'),
    path('PLANCAREdetails/<int:id>/', views.PLANCAREdetails, name='PLANCAREdetails'),
    path('PLANCAREedit/<PCid>',views.PLANCAREedit,name='PLANCAREedit'),
    path('PLANCAREdel/<PCid>', views.PLANCAREdel, name='PLANCAREdel'),
    path('PATIENTEDUCATIONinsert', views.PATIENTEDUCATIONinsert, name='PATIENTEDUCATIONinsert'),
    path('PATIENTEDUCATIONview', views.PATIENTEDUCATIONview, name='PATIENTEDUCATIONview'),
    path('PATIENTEDUCATIONdetails/<int:id>/', views.PATIENTEDUCATIONdetails, name='PATIENTEDUCATIONdetails'),
    path('PATIENTEDUCATIONedit/<PEid>',views.PATIENTEDUCATIONedit,name='PATIENTEDUCATIONedit'),
    path('PATIENTEDUCATIONdel/<PEid>', views.PATIENTEDUCATIONdel, name='PATIENTEDUCATIONdel'),
    path('FOLLOWUPPLANinsert', views.FOLLOWUPPLANinsert, name='FOLLOWUPPLANinsert'),
    path('FOLLOWUPPLANdetails/<int:id>/', views.FOLLOWUPPLANdetails, name='FOLLOWUPPLANdetails'),
    path('FOLLOWUPPLANedit/<FUid>',views.FOLLOWUPPLANedit,name='FOLLOWUPPLANedit'),
    path('FOLLOWUPPLANdel/<FUid>', views.FOLLOWUPPLANdel, name='FOLLOWUPPLANdel'),
    path('FALLRISKSCREENINGinsert', views.FALLRISKSCREENINGinsert, name='FALLRISKSCREENINGinsert'),
    path('FALLRISKSCREENINGedit/<FRid>',views.FALLRISKSCREENINGedit,name='FALLRISKSCREENINGedit'),
    path('FALLRISKSCREENINGdel/<FRid>', views.FALLRISKSCREENINGdel, name='FALLRISKSCREENINGdel'),
    path('CRITERIAinsert', views.CRITERIAinsert, name='CRITERIAinsert'),
    path('CRITERIAedit/<Cid>', views.CRITERIAedit, name='CRITERIAedit'),
    path('CRITERIAdel/<Cid>', views.CRITERIAdel, name='CRITERIAdel'),
    path('CATEGORYinsert', views.CATEGORYinsert, name='CATEGORYinsert'),
    path('CATEGORYview', views.CATEGORYview, name='CATEGORYview'),
    path('CATEGORYdetails/<int:id>/', views.CATEGORYdetails, name='CATEGORYdetails'),
    path('CATEGORYedit/<CAid>',views.CATEGORYedit,name='CATEGORYedit'),
    path('CATEGORYdel/<CAid>', views.CATEGORYdel, name='CATEGORYdel'),
    path('TOTALSCOREinsert', views.TOTALSCOREinsert, name='TOTALSCOREinsert'),
    path('TOTALSCOREedit/<TSid>',views.TOTALSCOREedit,name='TOTALSCOREedit'),
    path('TOTALSCOREdel/<TSid>', views.TOTALSCOREdel, name='TOTALSCOREdel'),
    path('TS1insert', views.TS1insert, name='TS1insert'),
    path('TS1view',views.TS1view,name='TS1view'),
    path('TS1details/<int:id>/', views.TS1details, name='TS1details'),
    path('TS1edit/<TS1id>',views.TS1edit,name='TS1edit'),
    path('TS1del/<TS1id>', views.TS1del, name='TS1del'),
    path('get_patient/', views.get_patient, name='get_patient'),
]
>>>>>>> b4a25de (final file)
