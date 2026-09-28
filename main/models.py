import uuid
from django.contrib.auth.models import User  # Tambahkan baris ini
from django.db import models

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)

    starred_by = models.ManyToManyField(
        User, related_name="starred_experience", blank=True
    )

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    LEVEL_CHOICES = [
        ('grade_school', 'Grade School'),
        ('junior_high_school', 'Junior High School'),
        ('high_school', 'High School'),
        ('undergraduate', 'Undergraduate'),
        ('graduate', 'Graduate'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='undergraduate')
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)

    starred_by = models.ManyToManyField(
        User, related_name="starred_education", blank=True
    )

    def __str__(self):
        return self.institution
        
    @property
    def is_ongoing(self):
        return self.ended_at is None