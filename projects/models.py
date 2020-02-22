from django.db import models
from django.utils import timezone
from employee.models import SuperVisors,labour
# Create your models here.

class Tender(models.Model):
    tender_number = models.CharField('Tender Number',max_length=500)
    tender_name = models.CharField('Name of Work',max_length=500)
    tender_submission_date = models.DateField('Tender Submission Date',default=timezone.now)
    tender_purchase_reciept = models.FileField('Tender Purchase Reciept')
    tender_confirmation_reciept = models.FileField('Tender Confirmation Reciept')
    physical_submission_date = models.DateField('Physical Submission Date',default=timezone.now)
    tech_bid_opening_date = models.DateField('Technical Bid Opening Bid',default=timezone.now)
    Yes = 'Yes'
    No = 'No'
    status = [(Yes, 'Yes'),(No, 'No')]
    bid_status = models.CharField('Bid Status',max_length=10,choices=status,default=No)
    prize_bid = models.CharField('Prize Bid',max_length=50)

    def __str__(self):
        return self.tender_number
    
    class Meta:
        verbose_name = 'Tender Lists'
        verbose_name_plural = 'Tender Lists'



class other_contractors_bid(models.Model):
    tender = models.ForeignKey(Tender,on_delete=models.CASCADE)
    contractor_info = models.CharField('Other Contractors Information',max_length=500)
    contractor_price = models.CharField('Bid',max_length=50)

    def __str__(self):
        return self.contractor_info+'  |  '+self.contractor_price
    
    class Meta:
        verbose_name = 'Other Contractors'
        verbose_name_plural = 'Other Contractors'

class Projects(models.Model):
    tender = models.ForeignKey(Tender,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=50)
    start_date = models.DateField('Start Date',default=timezone.now)
    supervisor = models.ForeignKey(SuperVisors,on_delete=models.CASCADE)
    labours = models.ManyToManyField(labour)

    def __str__(self):
        return self.tender.tender_number+" - "+self.project_name
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'


class Permissions(models.Model):
    edit_attendance = models.BooleanField()
    add_labour = models.BooleanField()
    delete_labour = models.BooleanField()

    class Meta:
        verbose_name = 'Permissions'
        verbose_name_plural = 'Permissions'