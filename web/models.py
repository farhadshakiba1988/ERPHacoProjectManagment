from django.db import models


class AbstractBaseModel(models.Model):
    """AbstractBaseModel contains common fields between models

    All models should extend this class
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(AbstractBaseModel):
    """Department represents the sector a set of employees belongs to."""

    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Employee(AbstractBaseModel):
    """Employee represents the people from a given department"""

    name = models.CharField(max_length=250, db_index=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlaceType(models.Model):
    placeTypeCode = models.CharField(max_length=50, blank=True)
    placeTypeName = models.CharField(max_length=50, blank=True)
    finishedGoodProductAccountCode = models.CharField(max_length=50, blank=True)
    rawMaterialAccountCode = models.CharField(max_length=50, blank=True)
    explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class Channel(models.Model):
    nameChannel = models.CharField(max_length=50, unique=True)
    codeChannel = models.CharField(max_length=50, blank=True)
    explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class EmploymentRequestChannel(models.Model):
    # employmentRequest_Id = models.ForeignKey()
    # channel_Id = models.ForeignKey()
    explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class Job(models.Model):
    # Tbl_Post_Id = models.ForeignKey()
    # Tbl_PlaceType_Id = models.ForeignKey()
    # Tbl_JobGroup_Id = models.ForeignKey()
    code = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    vision = models.CharField(max_length=50, blank=True)
    mBTI = models.CharField(max_length=50, blank=True)
    explanation = models.CharField(max_length=50, blank=True)
    revisionDate = models.CharField(max_length=50, blank=True)
    yearOfExperience = models.IntegerField(max_length=50, blank=True)
    sexuality = models.SmallIntegerField(max_length=50, blank=True)
    fromAge = models.SmallIntegerField(max_length=50, blank=True)
    toAge = models.SmallIntegerField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)
    internship = models.BooleanField(max_length=50, blank=True)
    educationalSubstitution = models.BooleanField(max_length=50, blank=True)


class Person(models.Model):
    # Tbl_PersonType_Id = models.ForeignKey()
    # Tbl_City_IdAsBirthPlace = models.ForeignKey()
    # Tbl_City_IdAsIssuePlace = models.ForeignKey()
    # Tbl_Country_IdAsNationality = models.ForeignKey()
    # Tbl_MarriageStatus_Id = models.ForeignKey()
    # Tbl_MilitaryService_Id = models.ForeignKey()
    # Tbl_Religion_Id = models.ForeignKey()
    # Tbl_Job_Id = models.ForeignKey()
    FileNumber = models.IntegerField(max_length=50, blank=True)
    CardNumber = models.IntegerField(max_length=50, blank=True)
    Code = models.IntegerField(max_length=50, blank=True)
    FirstName = models.CharField(max_length=50, blank=True)
    LastName = models.CharField(max_length=50, blank=True)
    FatherName = models.CharField(max_length=50, blank=True)
    NationalCode = models.CharField(max_length=50, blank=True)
    BirthCertificateNumber = models.CharField(max_length=50, blank=True)
    IssueDate = models.CharField(max_length=50, blank=True)
    BirthDate = models.CharField(max_length=50, blank=True)
    DeathDate = models.CharField(max_length=50, blank=True)
    MarriageDate = models.CharField(max_length=50, blank=True)
    Email = models.CharField(max_length=50, blank=True)
    NFC = models.CharField(max_length=50, blank=True)
    Password = models.CharField(max_length=50, blank=True)
    Explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)
    Sex = models.BooleanField(max_length=50, blank=True)
    GetEmail = models.BooleanField(max_length=50, blank=True)
    GetSMS = models.BooleanField(max_length=50, blank=True)


class Attachment(models.Model):
    # Tbl_Person_Id = models.ForeignKey()
    # Tbl_AttachmentType_Id = models.ForeignKey()
    Data = models.CharField(max_length=50)
    FileName = models.CharField(max_length=50)
    Explanation = models.CharField(max_length=50)
    Status = models.SmallIntegerField(max_length=50)
    isSent = models.BooleanField(max_length=50)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class Phone(models.Model):
    # Tbl_Person_Id = models.ForeignKey()
    # Tbl_PhoneType_Id = models.ForeignKey()
    Number = models.CharField(max_length=50, blank=True)
    Explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class EmploymentRequest(models.Model):
    # TbL_PlaceType_Id = models.ForeignKey()
    # Tbl_Job_Id = models.ForeignKey()
    # Tbl_Person_Id = models.ForeignKey()
    # TbL_Province_Id = models.ForeignKey()
    # Tbl_City_Id = models.ForeignKey()
    RequestDeadline = models.CharField(max_length=50, blank=True)
    AverageSalary = models.IntegerField(max_length=50, blank=True)
    Date = models.CharField(max_length=50, blank=True)
    IssuerComment = models.CharField(max_length=50, blank=True)
    HRComment = models.CharField(max_length=50, blank=True)
    Explanation = models.CharField(max_length=50, blank=True)
    HRStatus = models.SmallIntegerField(max_length=50, blank=True)
    ManagementStatus = models.SmallIntegerField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class EmploymentRequestReason(models.Model):
    # Tbl_EmploymentRequest_Id = models.ForeignKey()
    # Tbl_Reason_Id = models.ForeignKey()
    Explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class PersonEmploymentRequest(models.Model):
    # Tbl_Person_Id = models.ForeignKey()
    # Tbl_EmploymentRequest_Id = models.ForeignKey()
    Explanation = models.CharField(max_length=50, blank=True)
    Date = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class PersonInterView(models.Model):
    # Tbl_Person_Id = models.ForeignKey()
    # Tbl_PersonEmploymentRequest_Id = models.ForeignKey()
    Comment = models.CharField(max_length=50, blank=True)
    Date = models.CharField(max_length=50, blank=True)
    FromTime = models.DateTimeField(auto_now_add=True)
    ToTime = models.DateTimeField(auto_now_add=True)
    Explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)


class Reason(models.Model):
    name = models.CharField(max_length=150)
    Code = models.CharField(max_length=50, blank=True)
    Explanation = models.CharField(max_length=50, blank=True)
    status = models.SmallIntegerField(max_length=50, blank=True)
    isSent = models.BooleanField(max_length=50, blank=True)
    isDeleted = models.BooleanField(max_length=50, blank=True)
