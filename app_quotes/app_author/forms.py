from django.forms import (
    ModelForm,
    CharField,
    Textarea,
    ImageField,
    TextInput,
    FileInput,
    URLField,
)

from .models import Author


class AuthorForm(ModelForm):
    # fullname = CharField(max_length=255)
    # born_date = CharField(max_length=255)
    # born_location = CharField(max_length=255)
    # description = Textarea()
    # website = URLField()

    class Meta:
        model = Author
        fields = (
            "fullname",
            "born_date",
            "born_location",
            "description",
            "website",
        )
