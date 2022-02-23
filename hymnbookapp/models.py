import uuid
from django.db import models


profile_type = (
    ("Investor", "Investor"),
    ("Startup", "StartUp"),
)

startup_status = (
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
)


# return self.name


class Approved_Sector(models.Model):
    sector_name = models.CharField(max_length=200, unique=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.sector_name


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200, null=True)
    startup_name = models.CharField(max_length=250, unique=True, null=True, blank=True)
    startup_sector = models.ForeignKey(
        Approved_Sector, on_delete=models.SET_NULL, db_index=True, null=True, blank=True
    )
    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=13, choices=profile_type)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name}-------------{self.account_type}"


class Investor(models.Model):
    investor_profile = models.ForeignKey(
        Profile, related_name="investorprofile", on_delete=models.SET_NULL, null=True
    )
    email = models.EmailField()
    address = models.CharField(max_length=200, null=True)
    program_title = models.CharField(max_length=200)  # war against Hunger program
    program_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # user_id = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    # user_id = models.CharField(max_length=200)
    amount_invested = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    amount_left = models.DecimalField(max_digits=30, decimal_places=2, default=0)

    # amount_invested = models.IntegerField()
    targeted_startup_number = models.IntegerField(default=0)
    sectors = models.ManyToManyField(
        Approved_Sector, related_name="sectors", blank=False
    )
    program_start = models.DateTimeField()
    program_ends = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Investor Name: {self.investor_profile.name} Program Title: {self.program_title}"

        # return self.program_title

    @property
    def max_startup_fund_disbursement(self):
        return self.amount_invested / self.targeted_startup_number


class Startup(models.Model):
    startup_profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    investor_programs = models.ForeignKey(
        Investor, on_delete=models.SET_NULL, null=True
    )
    initial_amount_requested = models.DecimalField(
        max_digits=30, decimal_places=2, default=0
    )
    amount_given = models.DecimalField(max_digits=30, decimal_places=2, default=0)
    description_purpose_of_request = models.TextField(null=True, blank=True)
    startup_status = models.CharField(max_length=13, choices=startup_status)
    date_founded = models.DateTimeField()
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Investor Program Title: {self.investor_programs.program_title} Startup Name{self.startup_profile.name}"
        # return self.email






class Snippet(models.Model):
    name = models.CharField(max_length=200)
    body= models.TextField()

    def __str__(self):
        return self.name
    
    
    
level = (
    ("L1", "L1"),
    ("L2", "L2"),
    ("L3", "L3"),
    ("Others", "Others"),


)

class Profession(models.Model):
    job_title = models.CharField(max_length=200)
    salary= models.CharField(max_length=200)
    job_note= models.TextField()
    level = models.CharField(max_length=13, choices=level)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return F"{self.job_title} ---- {self.level}"

        

gender = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class Members(models.Model):
    jobs = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True , blank=True)
    gender = models.CharField(max_length=13, choices=gender, null=True , blank=True)
    email = models.EmailField(null=True , blank=True)
    phone = models.CharField(max_length=50, null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True , blank=True)
    updated = models.DateTimeField(auto_now=True , blank=True)

    
    def __str__(self):
        return F"{self.name} ---- {self.jobs}"
    
    
    class Meta:
        ordering = ["-created"]