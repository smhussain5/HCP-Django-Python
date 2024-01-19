from django.db import models

# Create your models here.


class Physician(models.Model):
    DEGREE_TYPE = {
        "DO": "Doctor of Osteopathic Medicine",
        "MD": "Doctor of Medicine",
    }
    US_STATE = {
        "AL": "Alabama",
        "AK": "Alaska",
        "AZ": "Arizona",
        "AR": "Arkansas",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "HI": "Hawaii",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "IA": "Iowa",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "ME": "Maine",
        "MD": "Maryland",
        "MA": "Massachusetts",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MS": "Mississippi",
        "MO": "Missouri",
        "MT": "Montana",
        "NE": "Nebraska",
        "NV": "Nevada",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NY": "New York",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VT": "Vermont",
        "VA": "Virginia",
        "WA": "Washington",
        "WV": "West Virginia",
        "WI": "Wisconsin",
        "WY": "Wyoming",
    }
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    degree_type = models.CharField(max_length=2, choices=DEGREE_TYPE)
    specialty = models.ForeignKey("Specialty", on_delete=models.CASCADE)
    about_me = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    us_city = models.CharField(max_length=250, verbose_name="US City", null=True, blank=True)
    us_state = models.CharField(max_length=2, choices=US_STATE, verbose_name="US State", default="TX")
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    accepts_medicaid_medicare = models.BooleanField(default=False, verbose_name="Accepts medicaid/medicare")
    taking_new_pts = models.BooleanField(default=False, verbose_name="Taking new patients")

    def __str__(self):
        return f"{self.last_name}, {self.degree_type} ({self.specialty})"


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "specialties"

    def __str__(self):
        return self.name
