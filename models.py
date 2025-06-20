import uuid
import django
from datetime import datetime
from django.db import models
from django import forms


# Create your models here.
class occupation_model(models.Model):
    occupation=models.CharField(max_length=20,unique=True,null=True)

    class Meta:
        db_table="occupation"

    def __str__(self):
        return self.occupation

class patient_model(models.Model):
    name=models.CharField(max_length=20)
    age = models.IntegerField()
    gender=models.CharField(max_length=20)
    dob=models.DateField()
    mob=models.IntegerField()
    occupation=models.ForeignKey(occupation_model,on_delete=models.CASCADE,null=True)
    regno=models.IntegerField()
    regdate=models.DateField(max_length=20,default=django.utils.timezone.now)
    Docname=models.CharField(max_length=20)

    class Meta:
        db_table="patient"

    def __str__(self):
        return self.name

class complaint_model(models.Model):
    name=models.ForeignKey(patient_model,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=225,null=True)

    class Meta:
        db_table="complaint"

    def __str__(self):
        return self.complaint

class HPI_model(models.Model):
    name=models.ForeignKey(patient_model,on_delete=models.CASCADE,null=True)
    onset=models.DateField(max_length=20)
    current_date=models.DateField(max_length=20,default=django.utils.timezone.now)
    painscore=models.IntegerField()
    Duration=models.CharField(max_length=100)
    POS=models.CharField(max_length=200)
    Aggr=models.CharField(max_length=200)
    Relf=models.CharField(max_length=200)

    class Meta:
        db_table="HPI"

class PMHM_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    rmc=models.CharField(max_length=225,null=True)
    surgeries=models.CharField(max_length=225)
    Injuries=models.CharField(max_length=225)
    medications=models.CharField(max_length=225)

    class Meta:
        db_table="PMHM"

class SocialHistory_model(models.Model):
    name=models.ForeignKey(patient_model,on_delete=models.CASCADE,null=True)
    lifestyle=models.CharField(max_length=225)
    activitylevels=models.CharField(max_length=225)
    habits=models.CharField(max_length=225)
    healthissues=models.CharField(max_length=225)

    class Meta:
        db_table="SH"

class objectiveassessment_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    postureandmovement=models.TextField(max_length=225)

    class Meta:
        db_table="ObjAss"

class ROMtype_model(models.Model):
    typename=models.CharField(max_length=20)

    class Meta:
        db_table="ROMT"

    def __str__(self):
        return self.typename

class cervicalspinemotion_model(models.Model):
    motionname=models.CharField(max_length=30)
    typename=models.ForeignKey(ROMtype_model,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table="CS"

    def __str__(self):
        return self.motionname

class ROM_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    typename = models.ForeignKey(ROMtype_model, on_delete=models.CASCADE, null=True)
    motionname=models.ForeignKey(cervicalspinemotion_model,on_delete=models.CASCADE,null=True)
    normal=models.IntegerField()
    left=models.IntegerField()
    right=models.IntegerField()

    class Meta:
        db_table="ROM"

class MMT_model(models.Model):
    typename=models.CharField(max_length=20)

    class Meta:
        db_table="MMT"

    def __str__(self):
        return self.typename

class MMTmotion_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    typename=models.ForeignKey(MMT_model,on_delete=models.CASCADE,null=True)
    motionname=models.CharField(max_length=30)

    class Meta:
        db_table="MM"

    def __str__(self):
        return self.motionname

class SPTE_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    testname=models.CharField(max_length=200)

    class Meta:
        db_table="ST"

    def __str__(self):
        return self.testname

class PALPATION_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    tenderness=models.CharField(max_length=100)
    swelling=models.CharField(max_length=100)
    muscletone = models.CharField(max_length=100)

    class Meta:
        db_table="PALP"

class NEUROASS_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    reflexes=models.CharField(max_length=100)
    sensation=models.CharField(max_length=100)
    nervefunction=models.CharField(max_length=100)

    class Meta:
        db_table="NEURO"

class FUNCTIONLIM_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    assessmentofcondition=models.CharField(max_length=200)
    activitiesofdailyiving=models.CharField(max_length=200)

    class Meta:
        db_table="FUNLIM"

class DIAGNOS_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    Xrays=models.CharField(max_length=200)
    MRI = models.CharField(max_length=200)
    CT= models.CharField(max_length=200)
    lab=models.CharField(max_length=200)

    class Meta:
        db_table="DIAGNOS"

class IMPRESSION_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    summary=models.CharField(max_length=225)
    provisionaldiagnos=models.CharField(max_length=225)

    class Meta:
        db_table="IMPRESSION"

class PHYSIOGOALS_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    shorttermgoals=models.CharField(max_length=225)
    longtermgoals=models.CharField(max_length=225)

    class Meta:
        db_table="PHYSIO"

class PLANOFCARE_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    treatmentstrategies=models.CharField(max_length=225)
    modalities=models.CharField(max_length=225)
    exercises = models.CharField(max_length=225)

    class Meta:
        db_table="PLANCARE"

class PATIENTEDUCATION_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    explanationofcondition = models.CharField(max_length=225)
    prognosis = models.CharField(max_length=225)
    selfmanagement = models.CharField(max_length=225)

    class Meta:
        db_table="PATIENTEDUCATION"

class FOLLOWUPPLAN_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    frequencyofvisits = models.CharField(max_length=225)
    reassessment = models.CharField(max_length=225)
    modifications = models.CharField(max_length=225)

class FALLRISKSCREENING_model(models.Model):
    criteriatype=models.CharField(max_length=20)

    class Meta:
        db_table="FALLRISKSCREENING"

    def __str__(self):
        return self.criteriatype

class CRITERIAsection_model(models.Model):
    criteriatype= models.ForeignKey(FALLRISKSCREENING_model, on_delete=models.CASCADE, null=True)
    sectionname=models.CharField(max_length=20)

    class Meta:
        db_table="CRITERIA"

    def __str__(self):
        return self.sectionname

class CATEGORY_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    criteriatype = models.ForeignKey(FALLRISKSCREENING_model, on_delete=models.CASCADE, null=True)
    sectionname=models.ForeignKey(CRITERIAsection_model,on_delete=models.CASCADE,null=True)
    score=models.IntegerField(null=True)
    Date=models.DateField(max_length=20,null=True)


    class Meta:
        db_table="CATEGORY"

class TOTALSCORE_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    range=models.IntegerField()

    def __str__(self):
        return str(self.range)

    class Meta:
        db_table="TOTALSCORE"

class TS1_model(models.Model):
    name = models.ForeignKey(patient_model, on_delete=models.CASCADE, null=True)
    range=models.ForeignKey(TOTALSCORE_model,on_delete=models.CASCADE,null=True)
    risk=models.CharField(max_length=20,null=True)
    facility=models.CharField(max_length=225,null=True)

    class Meta:
        db_table="TS1"

class Apppointment_model(models.Model):
    name=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    phone=models.IntegerField()
    Gender = models.CharField(max_length=20)
    Dob = models.DateField()
    Department=models.CharField(max_length=30)
    Message=models.TextField(max_length=220,null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table="Appointment"

class Contact_model(models.Model):
    name=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    contactnumber=models.IntegerField()
    Clinicname=models.CharField(max_length=30)
    Message=models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table="Contact"
