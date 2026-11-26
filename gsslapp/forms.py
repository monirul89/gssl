from django import forms


class InquiryForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=30)
    service = forms.ChoiceField(
        choices=(
            ("corporate", "Corporate Security"),
            ("industrial", "Industrial Security"),
            ("commercial", "Commercial Security"),
            ("residential", "Residential Security"),
            ("event", "Event & Special Security"),
        )
    )
    message = forms.CharField(max_length=2000)
