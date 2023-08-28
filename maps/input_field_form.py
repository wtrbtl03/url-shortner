from django import forms


class InputField(forms.Form):
    input_url = forms.CharField(label="input_url", max_length=256)
