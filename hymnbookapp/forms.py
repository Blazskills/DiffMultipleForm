from calendar import c
from unicodedata import category
from django import forms
from hymnbookapp.models import Approved_Sector, Members, Profession, Profile, Snippet


class ApprovedSector(forms.ModelForm):
    sector_name = forms.CharField()

    class Meta:
        model = Approved_Sector
        fields = ["sector_name"]

        # labels = {
        #     'sector_name': "Approved Sector"
        # }

    def clean(self):
        cleaned_data = super().clean()
        sector_name = cleaned_data["sector_name"]
        #     item = cleaned_data['item']
        #     warehouse = cleaned_data['warehouse']
        #     weight = cleaned_data['weight']
        #     bags = cleaned_data['bags']
        #     direct_to_client = cleaned_data['direct_to_client']
        #     logistic_officer = cleaned_data['logistic_officer']
        #     grade = cleaned_data['grade']

        if sector_name == "" or len(sector_name) <= 8:
            raise forms.ValidationError(
                f"ensure fields is not empty and sector name is too small",
                "sector_name",
            )

    #     if not direct_to_client and logistic_officer:
    #         raise forms.ValidationError(
    #             f"Dispatch must be direct to client if Logistic Officer is selected", 'logistic_officer')

    #     if item.item_type == 'Commodity':
    #         if weight <= 0 or int(weight) <= 0:  # check weight is created in KG
    #             raise forms.ValidationError(
    #                 "Weight must be greater than 0", 'weight')

    #         if not can_debit_client_inventory_account(client, item.product, warehouse, weight):
    #             raise forms.ValidationError(
    #                 f"{client} does not have {weight}KG of {item} in {warehouse.name}", 'item')
    #         if not can_debit_warehouse_inventory_account(warehouse, item, grade, weight, weight, bags):
    #             raise forms.ValidationError(
    #                 {'warehouse': f'Warehouse does not have up to {weight}KG of {grade} {item}'})

    #     elif item.item_type == 'Input':
    #         if bags <= 0 or int(bags) <= 0:
    #             raise forms.ValidationError("Bags must be greater than 0", 'bags')

    #         if not can_debit_client_input_account(client, item.product, warehouse, bags):
    #             raise forms.ValidationError(
    #                 f"{client} does not have {bags}Units of {item} in {warehouse}", 'item')

    #         if not can_debit_warehouse_input_account(warehouse, item, bags):
    #             raise forms.ValidationError(
    #                 {'warehouse': f'Warehouse does not have up to {bags} units of {item}'})

    # def clean_bags(self):
    #     bags = self.data.get('bags')
    #     item = self.cleaned_data.get('item')
    #     if item.item_type == 'Commodity':
    #         bags = bags or 0
    #     elif item.item_type == 'Input':
    #         if not bags:
    #             bags = 0
    #     return int(bags)

    # def clean_weight(self):
    #     weight = self.data.get('weight')
    #     item = self.cleaned_data.get('item')
    #     if item.item_type == 'Input':
    #         weight = weight or 0
    #     elif item.item_type == 'Commodity':
    #         if not weight:
    #             weight = 0
    #     return int(weight)


# <style type="text/css">
# 			input, textarea, select, button {
# 			font-family: "Montserrat-Regular";
# 			color: rgb(0, 0, 0);
# 			font-size: 15px;
# 		}
# 	</style>

# {{form.startup_sector}}


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField(label="E-mail")
    category = forms.ChoiceField(
        choices=[
            ("question", "Question"),
            ("other", "Other"),
        ]
    )
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):
    date = forms.CharField(label="Date of birth", required=True)
    company_name = forms.CharField(
        label="Your company name ",
        max_length=90,
        widget=forms.TextInput(),
        required=True,
    )

    class Meta:
        model = Snippet
        fields = ["name", "date", "company_name", "body"]

    # def clean_company_name(self):
    #         if self.cleaned_data.get('company_name') == '':
    #             company_name = None
    #         else:
    #              company_name = self.cleaned_data.get('company_name') # this returns always None because artist_id is not in cleaned_fields (this seemed to work with previous django versions but not with current SVN version)
    #         if company_name != None:
    #             company_name = Snippet.objects.get(name=company_name)
    #         else:
    #             company_name = None
    #      return company_name


# Inline form format


class ContactForm2(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)


# Approved sector here
class ApprovedSector2(forms.Form):
    sectorname = forms.CharField(max_length=100)

    def clean_sectorname(self):
        sectorname = self.cleaned_data["sectorname"]
        if Approved_Sector.objects.filter(sector_name=sectorname).exists():
            raise forms.ValidationError("Sector name already exists")

        return sectorname


# Profile registration process


class ProfileRegistrationForm(forms.ModelForm):
    startup_name = forms.CharField(
        required=False,
        label="Startup name",
        widget=forms.TextInput(
            attrs={"class": "form-control",}
        ),
    )
    
    # account_type = forms.Select( widget=forms.Select(attrs={'class': 'form-control'}))
    # account_type = forms.Select(required=False, widget=forms.TextInput(attrs={"class": "form-control",}),)

    class Meta:
        model = Profile
        fields = ["name", "startup_name",  "email","startup_sector", "account_type"]

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", }
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control",}
            ),
            "startup_sector": forms.Select(attrs={"class": "form-control"}),
            "account_type": forms.Select(attrs={"class": "form-control"}),
        }

        # def clean_(self):
        #     sectorname = self.cleaned_data["sectorname"]
        # if Approved_Sector.objects.filter(sector_name=sectorname).exists():
        #     raise forms.ValidationError("Sector name already exists")

        # return sectorname

# weight = forms.DecimalField(label="Weight(KG)", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Weight"}))




class MembershipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MembershipForm, self).__init__(*args, **kwargs)
        # self.fields['jobs'].queryset = Profession.objects.all()
# self.fields['item'].queryset = Item.objects.get_for_tenant(self.tenant)
    class Meta:
        model = Members
        fields = [
            'name', 'jobs', 'gender', 'email', 'phone']
        # labels = {
        #     'jobs': 'Job(Profession)',
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your name'}),
            'jobs': forms.Select(attrs={'class': 'form-control mx-select'}),
            'gender': forms.Select(attrs={'class': 'form-control mx-select'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            
        }





