from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import occupation_model
from .models import patient_model
from .models import complaint_model
from .models import HPI_model,cervicalspinemotion_model,ROM_model
from .models import PMHM_model,SocialHistory_model,objectiveassessment_model,ROMtype_model
from .models import MMT_model,MMTmotion_model,SPTE_model,PALPATION_model,NEUROASS_model
from .models import FUNCTIONLIM_model,DIAGNOS_model,IMPRESSION_model,PHYSIOGOALS_model
from .models import PLANOFCARE_model,PATIENTEDUCATION_model,FOLLOWUPPLAN_model,FALLRISKSCREENING_model
from .models import CRITERIAsection_model,CATEGORY_model,TOTALSCORE_model,TS1_model,Apppointment_model
from .occupationform import occupationform
from .patientform import patientform
from .complaintform import complaintform
from .HPIform import HPIform
from .PMHMform import PMHMform
from .socialhistoryform import socialhistoryform
from .objectiveassessmentform import objectiveassessmentform
from .ROMtypeform import ROMtypeform
from .cervicalspinemotionform import cervicalspinemotionform
from .ROMform import ROMform
from .MMTform import MMTform
from .MMTmotionform import MMTmotionform
from .SPTEform import SPTEform
from .PALPATIONform import PALPATIONform
from .NEUROASSform import NEUROASSform
from .FUNLIMform import FUNLIMform
from .DIAGNOSform import DIAGNOSform
from .IMPRESSIONform import IMPRESSIONform
from .PHYSIOGOALSform import PHYSIOGOALSform
from .PLANOFCAREform import PLANOFCAREform
from .PATIENTEDUCATIONform import PATIENTEDUCATIONform
from .FOLLOWUPPLANform import FOLLOWUPPLANform
from .FALLRISKSCREENINGform import FALLRISKSCREENINGform
from .CRITERIAsectionform import CRITERIAsectionform
from .CATEGORYform import CATEGORYform
from .TOTALSCOREform import TOTALSCOREform
from .TS1form import TS1form
# Create your views here.
def homee(request):
    return render(request, "managerheader.html")

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def testimonial(request):
    return render(request, "testimonial.html")

def contact(request):
    return render(request, "contact.html")


    return HttpResponse("hi<br>"
                        #"<a href='emp'>stay healthy</a><br>"
                        #"<a href='patientinsert'>insert patient</a><br>"
                        #"<a href='patientview'>view patient</a><br>"
                        #"<a href='complaintinsert'>insert complaint</a><br>"
                        #"<a href='complaintview'>view complaint</a><br>"
                        #"<a href='HPIinsert'>insert HPI</a><br>"
                        #"<a href='ROMtypeinsert'>insert ROMtype</a><br>"
                        #"<a href='cervicalspinemotioninsert'>insert cervspinemot</a><br>"
                        #"<a href='ROMin'>in ROM</a><br>"
                        #"<a href='ROMinsert'>insert ROM</a><br>"
                        #"<a href='MMTinsert'>insert MMT</a><br>"
                        #"<a href='MMTmotionview'>view MMTmotion</a><br>"
                        #"<a href='MMTmotionview'>view MMTmotion</a><br>"
                        #"<a href='SPTEinsert'>insert SPTE</a><br>"
                        #"<a href='SPTEview'>view SPTE</a><br>"
                        #"<a href='PALPATIONinsert'>insert PALPATION</a><br>"
                        #"<a href='NEUROASSinsert'>insert NEUROASS</a><br>"
                        #"<a href='FUNLIMinsert'>insert FUNLIM</a><br>"
                        #"<a href='FUNLIMview'>view FUNLIM</a><br>"
                        #<a href='DIAGNOSinsert'>insert DIAGNOS</a><br>"
                        #"<a href='IMPRESSIONinsert'>insert IMPRESSION</a><br>"
                        #"<a href='IMPRESSIONview'>view IMPRESSION</a><br>"
                        #"<a href='PHYSIOGOALSinsert'>insert PHYSIOGOALS</a><br>"
                        #"<a href='PLANCAREinsert'>insert PLANCARE</a><br>"
                        #"<a href='PATIENTEDUCATIONinsert'>insert PATIENTEDUCATION</a><br>"
                        #"<a href='PATIENTEDUCATIONview'>view PATIENTEDUCATION</a><br>"
                        #"<a href='FOLLOWUPPLANinsert'>insert FOLLOWUPPLAN</a><br>"
                        #"<a href='FALLRISKSCREENINGinsert'>insert FALLRISKSCREENING</a><br>"
                        #"<a href='CRITERIAinsert'>insert CRITERIA</a><br>"
                        #"<a href='CATEGORYinsert'>insert CATEGORY</a><br>"
                        #"<a href='CATEGORYview'>view CATEGORY</a><br>"
                        #"<a href='TOTALSCOREinsert'>insert TOTALSCORE</a><br>"
                        #"<a href='TS1insert'>insert TS1</a><br>"
                        #"<a href='TS1view'>view TS1</a><br>"

                        )

def emp(request):
    return render(request,"sample.html")

def appointmentinsert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('Email')
        phone = request.POST.get('phone')
        gender = request.POST.get('Gender')
        dob = request.POST.get('Dob')
        department = request.POST.get('Department')
        message = request.POST.get('Message')


        Apppointment_model.objects.create(
            name=name,
            Email=email,
            phone=phone,
            Gender=gender,
            Dob=dob,
            Department=department,
            Message=message
        )

        return redirect('appointmentinsert')
    data = Apppointment_model.objects.all()
    return render(request, 'appointment_insert.html', {'dataset': data})

def contactinsert(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('Email')
        number = request.POST.get('contactnumber')
        clinic = request.POST.get('Clinicname')
        message = request.POST.get('Message')


        Contact_model.objects.create(
            name=name,
            Email=email,
            contactnumber=number,
            Clinicname=clinic,
            Message=message
        )

        return redirect('contactinsert')
    data = Contact_model.objects.all()
    return render(request, 'contact.html', {'dataset': data})




def occupationinsert(request):
    context = {}
    form = occupationform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(occupationinsert)
    context['form'] = form
    context["dataset"] = occupation_model.objects.all()
    return render(request, "occupation_insert.html", context)

def occupationedit(request,occid):
    context = {}
    obj = get_object_or_404 (occupation_model, id=occid)
    form = occupationform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(occupationinsert)
    context['form'] = form
    return render(request, 'occupation_edit.html', context)



def occupationdel(request,occid):
    context = {}
    obj = get_object_or_404(occupation_model, id=occid)
    obj.delete()
    return redirect(occupationinsert)

def patientinsert(request):
    context = {}
    form = patientform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(patientinsert)
    context['form'] = form
    return render(request, "patient_insert.html", context)

def patientview(request):
    context = {}
    context["dataset"] = patient_model.objects.all()
    return render(request, "patient_view.html", context)

def patientedit(request,patid):
    context = {}
    obj = get_object_or_404 (patient_model, id=patid)
    form = patientform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(patientview)
    context['form'] = form
    return render(request, 'patient_edit.html', context)

def patientdel(request,patid):
    context = {}
    obj = get_object_or_404(patient_model, id=patid)
    obj.delete()
    return redirect(patientinsert)

def complaintinsert(request):
    context = {}
    form = complaintform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(complaintinsert)
    context['form'] = form
    return render(request, "complaint_insert.html", context)

def complaintview(request):
    context={}
    context["dataset"]=complaint_model.objects.all()
    return render(request,"complaint_view.html",context)

def complaintedit(request,comid):
    context = {}
    obj = get_object_or_404 (complaint_model, id=comid)
    form = complaintform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(complaintview)
    context['form'] = form
    return render(request, 'complaint_edit.html', context)

def complaintdel(request,comid):
    context={}
    obj = get_object_or_404(complaint_model, id=comid)
    obj.delete()
    return redirect(complaintview)

def HPIinsert(request):

    return render(request, "HPI_insert.html")

def HPIdetails(request,id):
    context = {}
    form = HPIform(request.POST or None, request.FILES or None)
    duration = None
    onset=None
    try:
        patientid=id
        patientobj=patient_model.objects.get(id=patientid)
        onset =patientobj.regdate
        cu_da = request.POST.get('current_date')

        currentdate = datetime.today().date()
        duration = currentdate - onset



        # if onset:
        #     onset = datetime.strptime(onset, '%Y-%m-%d').date()  # Convert to date object
        # else:
        #     raise ValueError("Onset date is not provided or is invalid.")

        form = HPIform(request.POST or None, request.FILES or None, initial={'Duration':duration,'onset': onset})



        # if patient_model.objects.filter(name=patientid).exists():



        if form.is_valid():
            obj=form.save()
            patient_instance = patient_model.objects.get(id=patientid)
            obj.name = patient_instance
            obj.save()
            return redirect('HPIdetails',patientid)
        # else:
        #     if form.is_valid():
        #         obj=form.save()
        #         patient_instance = patient_model.objects.get(id=patientid)
        #         obj.name = patient_instance
        #         obj.save()
        #         return redirect('HPIdetails',patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context["dataset"] = HPI_model.objects.filter(name=patientid)
    context['Duration']=duration


    context['f'] = form

    return render(request, "HPI_details.html",context)

def HPIedit(request,HPIid):
    context = {}
    obj = get_object_or_404 (HPI_model, id=HPIid)
    form = HPIform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(HPIdetails)
    context['form'] = form
    return render(request, 'HPI_edit.html', context)

def HPIdel(request,HPIid):
    context={}
    obj = get_object_or_404(HPI_model, id=HPIid)
    obj.delete()
    return redirect(HPIdetails,obj.name.id)

def MedHisdetails(request,id):
    context={}
    patientid=id
    form=PMHMform(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj=form.save()
        patient_instance = patient_model.objects.get(id=patientid)
        obj.name=patient_instance
        obj.save()
        return redirect('MedHisdetails', patientid)
    context['form'] = form
    context["dataset"] = PMHM_model.objects.filter(name=patientid)
    return render(request, "MedHis_details.html", context)

def MedHisedit(request,MHid):
    context = {}
    obj = get_object_or_404 (PMHM_model, id=MHid)
    form = PMHMform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(MedHisdetails)
    context['form'] = form
    return render(request, 'MedHis_edit.html', context)

def MedHisdel(request,MHid):
    context={}
    obj = get_object_or_404(PMHM_model, id=MHid)
    obj.delete()
    return redirect(MedHisdetails,obj.name.id)

def SocialHisdetails(request,id):
    context = {}
    patientid = id
    form = socialhistoryform(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save()
        patient_instance = patient_model.objects.get(id=patientid)
        obj.name = patient_instance
        obj.save()
        return redirect('SocialHisdetails', patientid)
    context['form'] = form
    context["dataset"] = SocialHistory_model.objects.filter(name=patientid)
    return render(request, "SocialHis_details.html", context)

def SocialHisedit(request,SHid):
    context = {}
    obj = get_object_or_404 (SocialHistory_model, id=SHid)
    form = socialhistoryform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(SocialHisdetails)
    context['form'] = form
    return render(request, 'SocialHis_edit.html', context)

def SocialHisdel(request,SHid):
    context={}
    obj = get_object_or_404(SocialHistory_model, id=SHid)
    obj.delete()
    return redirect(SocialHisdetails,obj.name.id)

def obbassinsert(request,id):
    context={}
    patientid=id
    form=objectiveassessmentform(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj=form.save()
        patient_instance = patient_model.objects.get(id=patientid)
        obj.name=patient_instance
        obj.save()
        return redirect('obbassinsert', patientid)
    context['form'] = form
    context["dataset"] = objectiveassessment_model.objects.filter(name=patientid)
    return render(request, "obbass_insert.html", context)

def obbassedit(request,OAid):
    context = {}
    obj = get_object_or_404 (objectiveassessment_model, id=OAid)
    form = objectiveassessmentform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(obbassinsert)
    context['form'] = form
    return render(request, 'obbass_edit.html', context)

def obbassdel(request,OAid):
    context={}
    obj = get_object_or_404(objectiveassessment_model, id=OAid)
    obj.delete()
    return redirect(obbassinsert,obj.name.id)

def ROMtypeinsert(request):
    context = {}
    form = ROMtypeform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(ROMtypeinsert)
    context['form'] = form
    context["dataset"] = ROMtype_model.objects.all()
    return render(request, "ROMtype_insert.html", context)



def ROMtypeedit(request,Rid):
    context = {}
    obj = get_object_or_404 (ROMtype_model, id=Rid)
    form = ROMtypeform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(ROMtypeinsert)
    context['form'] = form
    return render(request, 'ROMtype_edit.html', context)

def ROMtypedel(request,Rid):
    context={}
    obj = get_object_or_404(ROMtype_model, id=Rid)
    obj.delete()
    return redirect(ROMtypeinsert)

def cervicalspinemotioninsert(request):
    context = {}
    form = cervicalspinemotionform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(cervicalspinemotioninsert)
    context['form'] = form
    context["dataset"] = cervicalspinemotion_model.objects.all()
    return render(request, "cervicalspinemotion_insert.html", context)

def cervicalspinemotionedit(request,CSid):
    context = {}
    obj = get_object_or_404 (cervicalspinemotion_model, id=CSid)
    form = cervicalspinemotionform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(cervicalspinemotioninsert)
    context['form'] = form
    return render(request, 'cervicalspinemotion_edit.html', context)

def cervicalspinemotiondel(request,CSid):
    context={}
    obj = get_object_or_404(cervicalspinemotion_model, id=CSid)
    obj.delete()
    return redirect(cervicalspinemotioninsert)

def ROMin(request):
    context = {}
    form = ROMform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(ROMin)
    context['form'] = form
    return render(request, "ROMin.html", context)

def ROMinsert(request):

    return render(request, "ROM_insert.html")

def ROMdetails(request,id):
    context = {}
    form = ROMform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj=form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('ROMdetails',patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname']=patient_instance
    context["dataset"] = ROM_model.objects.filter(name=patientid)

    return render(request, "ROM_details.html",context)



def ROMedit(request,rid):
    context = {}
    obj = get_object_or_404 (ROM_model, id=rid)
    form = ROMform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(ROMin)
    context['form'] = form
    return render(request, 'ROM_edit.html', context)

def ROMdel(request,rid):
    context={}
    obj = get_object_or_404(ROM_model, id=rid)
    obj.delete()
    return redirect(ROMin)

def MMTinsert(request):
    context = {}
    form = MMTform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(MMTinsert)
    context['form'] = form
    context["dataset"] = MMT_model.objects.all()
    return render(request, "MMT_insert.html", context)


def MMTedit(request, Mid):
    context = {}
    obj = get_object_or_404(MMT_model, id=Mid)
    form = MMTform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(MMTinsert)
    context['form'] = form
    return render(request, 'MMT_edit.html', context)


def MMTdel(request, Mid):
    context = {}
    obj = get_object_or_404(MMT_model, id=Mid)
    obj.delete()
    return redirect(MMTinsert)

def MMTmotioninsert(request):
    context = {}
    form = MMTmotionform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(MMTmotioninsert)
    context['form'] = form
    return render(request, "MMTmotion_insert.html", context)

def MMTmotionview(request):

    return render(request,'MMTmotion_view.html')

def MMTmotiondetails(request,id):
    context = {}
    form = MMTmotionform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj=form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('MMTmotiondetails',patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname']=patient_instance
    context["dataset"] = MMTmotion_model.objects.filter(name=patientid)

    return render(request, "MMTmotion_details.html",context)

def MMTmotionedit(request, Mmid):
    context = {}
    obj = get_object_or_404(MMTmotion_model, id=Mmid)
    form = MMTmotionform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(MMTmotioninsert)
    context['form'] = form
    return render(request, 'MMTmotion_edit.html', context)


def MMTmotiondel(request, Mmid):
    context = {}
    obj = get_object_or_404(MMTmotion_model, id=Mmid)
    obj.delete()
    return redirect(MMTmotioninsert)

def SPTEinsert(request):
    context = {}
    form = SPTEform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(SPTEinsert)
    context['form'] = form
    return render(request, "SPTE_insert.html", context)

def SPTEview(request):

    return render(request,"SPTE_view.html")

def SPTEdetails(request,id):
    context = {}
    form = SPTEform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('SPTEdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = SPTE_model.objects.filter(name=patientid)

    return render(request, "SPTE_details.html", context)

def SPTEedit(request, STid):
    context = {}
    obj = get_object_or_404(SPTE_model, id=STid)
    form = SPTEform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(SPTEinsert)
    context['form'] = form
    return render(request, 'SPTE_edit.html', context)


def SPTEdel(request, STid):
    context = {}
    obj = get_object_or_404(SPTE_model, id=STid)
    obj.delete()
    return redirect(SPTEinsert)

def PALPATIONinsert(request):
    context = {}
    form = PALPATIONform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(PALPATIONinsert)
    context['form'] = form
    return render(request, "PALPATION_insert.html", context)

def  PALPATIONdetails(request,id):
    context = {}
    form = PALPATIONform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('PALPATIONdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = PALPATION_model.objects.filter(name=patientid)

    return render(request, "PALPATION_details.html", context)

def PALPATIONedit(request, Pid):
    context = {}
    obj = get_object_or_404(PALPATION_model, id=Pid)
    form = SPTEform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(PALPATIONinsert)
    context['form'] = form
    return render(request, 'PALPATION_edit.html', context)


def PALPATIONdel(request, Pid):
    context = {}
    obj = get_object_or_404(PALPATION_model, id=Pid)
    obj.delete()
    return redirect(PALPATIONinsert)

def NEUROASSinsert(request):
    context = {}
    form = NEUROASSform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(NEUROASSinsert)
    context['form'] = form
    return render(request, "NEOROASS_insert.html", context)

def  NEUROASSdetails(request,id):
    context = {}
    form = NEUROASSform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('NEUROASSdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = NEUROASS_model.objects.filter(name=patientid)

    return render(request, "NEUROASS_details.html", context)

def NEUROASSedit(request, NAid):
    context = {}
    obj = get_object_or_404(NEUROASS_model, id=NAid)
    form = NEUROASSform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(NEUROASSinsert)
    context['form'] = form
    return render(request, 'NEUROASS_edit.html', context)


def NEUROASSdel(request, NAid):
    context = {}
    obj = get_object_or_404(NEUROASS_model, id=NAid)
    obj.delete()
    return redirect(NEUROASSinsert)

def FUNLIMinsert(request):
    context = {}
    form = FUNLIMform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(FUNLIMinsert)
    context['form'] = form
    return render(request, "FUNLIM_insert.html", context)

def FUNLIMview(request):

    return render(request,"FUNLIM_view.html")

def  FUNLIMdetails(request,id):
    context = {}
    form = FUNLIMform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('FUNLIMdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = FUNCTIONLIM_model.objects.filter(name=patientid)

    return render(request, "FUNLIM_details.html", context)

def FUNLIMedit(request, FLid):
    context = {}
    obj = get_object_or_404(FUNCTIONLIM_model, id=FLid)
    form = FUNLIMform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(FUNLIMinsert)
    context['form'] = form
    return render(request, 'FUNLIM_edit.html', context)


def FUNLIMdel(request, FLid):
    context = {}
    obj = get_object_or_404(FUNCTIONLIM_model, id=FLid)
    obj.delete()
    return redirect(FUNLIMinsert)

def DIAGNOSinsert(request):
    context = {}
    form = DIAGNOSform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(DIAGNOSinsert)
    context['form'] = form
    return render(request, "DIAGNOS_insert.html", context)

def  DIAGNOSdetails(request,id):
    context = {}
    form = DIAGNOSform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('DIAGNOSdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = DIAGNOS_model.objects.filter(name=patientid)

    return render(request, "DIAGNOS_details.html", context)

def DIAGNOSedit(request, DGid):
    context = {}
    obj = get_object_or_404(DIAGNOS_model, id=DGid)
    form = DIAGNOSform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(DIAGNOSinsert)
    context['form'] = form
    return render(request, 'DIAGNOS_edit.html', context)


def DIAGNOSdel(request, DGid):
    context = {}
    obj = get_object_or_404(DIAGNOS_model, id=DGid)
    obj.delete()
    return redirect(DIAGNOSinsert)

def IMPRESSIONinsert(request):
    context = {}
    form = IMPRESSIONform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(IMPRESSIONinsert)
    context['form'] = form
    return render(request, "IMPRESSION_insert.html", context)

def IMPRESSIONview(request):

    return render(request,"IMPRESSION_view.html")

def  IMPRESSIONdetails(request,id):
    context = {}
    form = IMPRESSIONform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('IMPRESSIONdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = IMPRESSION_model.objects.filter(name=patientid)

    return render(request, "IMPRESSION_details.html", context)

def IMPRESSIONedit(request, IMid):
    context = {}
    obj = get_object_or_404(IMPRESSION_model, id=IMid)
    form = IMPRESSIONform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(IMPRESSIONinsert)
    context['form'] = form
    return render(request, 'IMPRESSION_edit.html', context)


def IMPRESSIONdel(request, IMid):
    context = {}
    obj = get_object_or_404(IMPRESSION_model, id=IMid)
    obj.delete()
    return redirect(IMPRESSIONinsert)

def PHYSIOGOALSinsert(request):
    context = {}
    form = PHYSIOGOALSform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(PHYSIOGOALSinsert)
    context['form'] = form
    return render(request, "PHYSIOGOALS_insert.html", context)

def  PHYSIOGOALSdetails(request,id):
    context = {}
    form = PHYSIOGOALSform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('PHYSIOGOALSdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = PHYSIOGOALS_model.objects.filter(name=patientid)

    return render(request, "PHYSIOGOALS_details.html", context)


def PHYSIOGOALSedit(request, PGid):
    context = {}
    obj = get_object_or_404(PHYSIOGOALS_model, id=PGid)
    form = IMPRESSIONform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(PHYSIOGOALSinsert)
    context['form'] = form
    return render(request, 'PHYSIOGOALS_edit.html', context)


def PHYSIOGOALSdel(request, PGid):
    context = {}
    obj = get_object_or_404(PHYSIOGOALS_model, id=PGid)
    obj.delete()
    return redirect(PHYSIOGOALSinsert)

def PLANCAREinsert(request):
    context = {}
    form = PLANOFCAREform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(PLANCAREinsert)
    context['form'] = form
    return render(request, "PLANCARE_insert.html", context)

def  PLANCAREdetails(request,id):
    context = {}
    form = PLANOFCAREform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('PLANCAREdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = PLANOFCARE_model.objects.filter(name=patientid)

    return render(request, "PLANCARE_details.html", context)

def PLANCAREedit(request,PCid):
    context = {}
    obj = get_object_or_404(PLANOFCARE_model, id=PCid)
    form = PLANOFCAREform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(PLANCAREinsert)
    context['form'] = form
    return render(request, 'PLANCARE_edit.html', context)


def PLANCAREdel(request, PCid):
    context = {}
    obj = get_object_or_404(PLANOFCARE_model, id=PCid)
    obj.delete()
    return redirect(PLANCAREinsert)

def PATIENTEDUCATIONinsert(request):
    context = {}
    form = PATIENTEDUCATIONform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(PATIENTEDUCATIONinsert)
    context['form'] = form
    return render(request, "PATIENTEDUCATION_insert.html", context)

def PATIENTEDUCATIONview(request):

    return render(request,"PATIENTEDUCATION_view.html")

def  PATIENTEDUCATIONdetails(request,id):
    context = {}
    form = PATIENTEDUCATIONform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('PATIENTEDUCATIONdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = PATIENTEDUCATION_model.objects.filter(name=patientid)

    return render(request, "PATIENTEDUCATION_details.html", context)

def PATIENTEDUCATIONedit(request,PEid):
    context = {}
    obj = get_object_or_404(PLANOFCARE_model, id=PEid)
    form = PATIENTEDUCATIONform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(PATIENTEDUCATIONinsert)
    context['form'] = form
    return render(request, 'PATIENTEDUCATION_edit.html', context)


def PATIENTEDUCATIONdel(request, PEid):
    context = {}
    obj = get_object_or_404(PATIENTEDUCATION_model, id=PEid)
    obj.delete()
    return redirect(PATIENTEDUCATIONinsert)

def FOLLOWUPPLANinsert(request):
    context = {}
    form = FOLLOWUPPLANform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(FOLLOWUPPLANinsert)
    context['form'] = form
    return render(request, "FOLLOWUPPLAN_insert.html", context)

def  FOLLOWUPPLANdetails(request,id):
    context = {}
    form = FOLLOWUPPLANform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj = form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('FOLLOWUPPLANdetails', patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname'] = patient_instance
    context["dataset"] = FOLLOWUPPLAN_model.objects.filter(name=patientid)

    return render(request, "FOLLOWUPPLAN_details.html", context)

def FOLLOWUPPLANedit(request,FUid):
    context = {}
    obj = get_object_or_404(FOLLOWUPPLAN_model, id=FUid)
    form = FOLLOWUPPLANform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(FOLLOWUPPLANinsert)
    context['form'] = form
    return render(request, 'FOLLOWUPPLAN_edit.html', context)


def FOLLOWUPPLANdel(request, FUid):
    context = {}
    obj = get_object_or_404(FOLLOWUPPLAN_model, id=FUid)
    obj.delete()
    return redirect(FOLLOWUPPLANinsert)

def FALLRISKSCREENINGinsert(request):
    context = {}
    form = FALLRISKSCREENINGform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(FALLRISKSCREENINGinsert)
    context['form'] = form
    context["dataset"] = FALLRISKSCREENING_model.objects.all()
    return render(request, "FALLRISKSCREENING_insert.html", context)

def FALLRISKSCREENINGedit(request,FRid):
    context = {}
    obj = get_object_or_404 (FALLRISKSCREENING_model, id=FRid)
    form = FALLRISKSCREENINGform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(FALLRISKSCREENINGinsert)
    context['form'] = form
    return render(request, 'FALLRISKSCREENING_edit.html', context)

def FALLRISKSCREENINGdel(request,FRid):
    context={}
    obj = get_object_or_404(FALLRISKSCREENING_model, id=FRid)
    obj.delete()
    return redirect(FALLRISKSCREENINGinsert)

def CRITERIAinsert(request):
    context = {}
    form = CRITERIAsectionform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(CRITERIAinsert)
    context['form'] = form
    context["dataset"] = CRITERIAsection_model.objects.all()
    return render(request, "CRITERIA_insert.html", context)

def CRITERIAedit(request,Cid):
    context = {}
    obj = get_object_or_404 (CRITERIAsection_model, id=Cid)
    form = cervicalspinemotionform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(CRITERIAinsert)
    context['form'] = form
    return render(request, 'CRITERIA_edit.html', context)

def CRITERIAdel(request,Cid):
    context={}
    obj = get_object_or_404(CRITERIAsection_model, id=Cid)
    obj.delete()
    return redirect(CRITERIAinsert)

def CATEGORYinsert(request):
    context = {}
    form = CATEGORYform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(CATEGORYinsert)
    context['form'] = form
    return render(request, "CATEGORY_insert.html", context)

def CATEGORYview(request):

    return render(request, "CATEGORY_view.html")

def CATEGORYdetails(request,id):
    context = {}
    form = CATEGORYform(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj=form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('CATEGORYdetails',patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname']=patient_instance
    context["dataset"] = CATEGORY_model.objects.filter(name=patientid)

    return render(request, "CATEGORY_details.html",context)

def CATEGORYedit(request,CAid):
    context = {}
    obj = get_object_or_404 (CATEGORY_model, id=CAid)
    form = CATEGORYform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(CATEGORYinsert)
    context['form'] = form
    return render(request, 'CATEGORY_edit.html', context)

def CATEGORYdel(request,CAid):
    context={}
    obj = get_object_or_404(CATEGORY_model, id=CAid)
    obj.delete()
    return redirect(CATEGORYinsert)

def TOTALSCOREinsert(request):
    context = {}
    form = TOTALSCOREform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(TOTALSCOREinsert)
    context['form'] = form
    return render(request, "TOTALSCORE_insert.html", context)



def TOTALSCOREedit(request,TSid):
    context = {}
    obj = get_object_or_404 (TOTALSCORE_model, id=TSid)
    form = CATEGORYform(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(TOTALSCOREinsert)
    context['form'] = form
    return render(request, 'TOTALSCORE_edit.html', context)

def TOTALSCOREdel(request,TSid):
    context={}
    obj = get_object_or_404(TOTALSCORE_model, id=TSid)
    obj.delete()
    return redirect(TOTALSCOREinsert)

def TS1insert(request):
    context = {}
    form = TS1form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(TS1insert)
    context['form'] = form
    return render(request, "TS1_insert.html", context)

def TS1view(request):

    return render(request,"TS1_view.html")

def TS1details(request,id):
    context = {}
    form = TS1form(request.POST or None, request.FILES or None)
    try:
        patientid = id
        patient_instance = patient_model.objects.get(id=patientid)
        if form.is_valid():
            obj=form.save()
            obj.name = patient_instance
            obj.save()
            return redirect('TS1details',patientid)
    except Exception as e:
        messages.error(request, e)

    context['form'] = form
    context['patientname']=patient_instance
    context["dataset"] = TS1_model.objects.filter(name=patientid)

    return render(request, "TS1_details.html",context)

def TS1edit(request,TS1id):
    context = {}
    obj = get_object_or_404 (TS1_model, id=TS1id)
    form = TS1form(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(TS1insert)
    context['form'] = form
    return render(request, 'TS1_edit.html', context)

def TS1del(request,TS1id):
    context={}
    obj = get_object_or_404(TS1_model, id=TS1id)
    obj.delete()
    return redirect(TS1insert)




def get_patient(request):
    patientid = request.GET.get('selected_value')
    print(patientid, 'patientid')
    data = patient_model.objects.filter(id=patientid)
    data_list1 = [{'id':obj.id,'name':obj.name,'age': obj.age, 'gender': obj.gender,'mobile':obj.mob} for obj in data]
    return JsonResponse({'data': data_list1})