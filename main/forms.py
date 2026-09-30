from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, TextInput, Textarea, URLInput, Select
from django.utils.html import strip_tags

from main.models import Education, Experience


def plain_text(value):
    """Buang tag HTML lalu rapikan spasi di awal/akhir."""
    return strip_tags(value or "").strip()


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Title",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Thumbnail Link",
            "started_at": "Start Date",
            "ended_at": "End Date",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g. Competitive Programming Teacher",
                }
            ),
            "description": Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What did you do in this role?",
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "started_at": DateInput(attrs={"type": "date"}),
            "ended_at": DateInput(attrs={"type": "date"}),
        }

    def clean_title(self):
        title = plain_text(self.cleaned_data["title"])
        if not title:
            raise ValidationError("Title tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return plain_text(self.cleaned_data["description"])


class EducationForm(ModelForm):
    class Meta:
        model = Education

        fields = [
            "institution",
            "program",
            "level",
            "description",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "institution": "Institution Name",
            "program": "Program",
            "level": "Level",
            "description": "Description",
            "thumbnail": "Thumbnail Link",
            "started_at": "Start Date",
            "ended_at": "End Date",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "e.g. University of Indonesia",
                }
            ),
            "program": TextInput(
                attrs={
                    "placeholder": "e.g. Computer Science",
                }
            ),
            "level": Select(),
            "description": Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "What did you focus on or do here?",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://...",
                }
            ),
            "started_at": DateInput(attrs={"type": "date"}),
            "ended_at": DateInput(attrs={"type": "date"}),
        }

    def clean_institution(self):
        institution = plain_text(self.cleaned_data["institution"])
        if not institution:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return institution

    def clean_program(self):
        program = plain_text(self.cleaned_data["program"])
        if self.fields["program"].required and not program:
            raise ValidationError("Program tidak boleh hanya berisi tag HTML.")
        return program

    def clean_description(self):
        return plain_text(self.cleaned_data["description"])