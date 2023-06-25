from django.db import models


class Document(models.Model):
    contractNumber = models.CharField(max_length=500, unique=True)
    employer = models.CharField(blank=True, null=True, max_length=50)
    type_form = models.BooleanField(blank=True, null=True, max_length=50)
    dateContract = models.DateField()
    contractPrice = models.CharField(max_length=50)
    durationContract = models.CharField(max_length=50)
    prePaidPrice = models.CharField(max_length=50)
    goodPrice = models.CharField(max_length=50)
    typeBail1 = models.CharField(max_length=50)
    firstBail = models.CharField(max_length=50)
    secondBail = models.CharField(max_length=50)
    commitmentPrice = models.CharField(max_length=50)
    typeBail2 = models.CharField(max_length=50)
    firstBail2 = models.CharField(max_length=50)
    secondBail2 = models.CharField(max_length=50)
    topicContract = models.CharField(max_length=50)
    typeContract = models.CharField(max_length=50)
    clearedDate = models.DateField(blank=True, null=True)
    receivedDocument = models.BooleanField(default=False, blank=True, null=True)
    clearedStatus = models.BooleanField(default=False, blank=True, null=True)
    doc_1 = models.TextField(blank=True, null=True)
    doc_2 = models.TextField(blank=True, null=True)
    doc_3 = models.TextField(blank=True, null=True)
    doc_4 = models.TextField(blank=True, null=True)
    doc_bail_1 = models.TextField(blank=True, null=True)
    doc_bail_2 = models.TextField(blank=True, null=True)

    def _str_(self):
        return self.contractNumber
