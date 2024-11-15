from django import forms

from travel_project.country.models import Country


class AddCountry(forms.ModelForm):
    class Meta:
        model = Country
        exclude = ('user', )

        widgets = {
            "description": forms.Textarea(attrs={
                "placeholder": "Make a description of the country."
            }),
            "population": forms.TextInput(attrs={
                "placeholder": "Population in millions."
            }),
        }


class DeleteCountry(AddCountry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
