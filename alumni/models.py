from django.db import models
import datetime


class Alumnus(models.Model):
    objects = None
    fullname = models.CharField(max_length=255)
    #fullname = models.CharField(max_length=255)
    #lastname = models.CharField(max_length=255)
    #phone = models.IntegerField(null=True , blank=True)
    #    joined_date = models.DateField(null=True)
    #    FRESHMAN = "FR"
    #    SOPHOMORE = "SO"
    #    JUNIOR = "JR"
    #    SENIOR = "SR"
    #    GRADUATE = "GR"
    #    YEAR_IN_SCHOOL_CHOICES = [
    #        (FRESHMAN, "Freshman"),
    #        (SOPHOMORE, "Sophomore"),
    #        (JUNIOR, "Junior"),
    #        (SENIOR, "Senior"),
    #        (GRADUATE, "Graduate"),
    #    ]
    #    year_in_school = models.CharField(
    #        max_length=2,
    #        choices=YEAR_IN_SCHOOL_CHOICES,
    #        default=FRESHMAN,
    #    )

    GENDER_CHOICES = (
        ('ወ', 'ወንድ'),
        ('ሴ', 'ሴት'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    department = models.CharField(max_length=255, default='')
    COURSE_YEARS_CHOICES = (
        ('2', '2 ዓመት'),
        ('3', '3 ዓመት'),
        ('4', '4 ዓመት'),
        ('5', '3 ዓመት'),
    )
    no_of_course_years = models.CharField(max_length=10, choices=COURSE_YEARS_CHOICES, default='4')

    YEAR_CHOICES = [(r, r) for r in range(1959, datetime.date.today().year -7)]

    year_of_graduation = models.IntegerField(('Year Of Graduation'), choices=YEAR_CHOICES, default=datetime.datetime.now().year -8)
    #INSTITUE_CHOICES = (
    #    ('POLY', 'Bahr Dar Polytechnic Institute'),
    #    ('PEDA', 'Bahr Dar Pedagogy'),
    #    ('BDU', 'Bahr Dar University'),
    #)
    #graduated_from = models.CharField(max_length=20, choices=INSTITUE_CHOICES, default='BDU')

    class Meta:
        verbose_name_plural = 'Alumnus'
# Create your models here.
