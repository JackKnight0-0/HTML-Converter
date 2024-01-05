from django import forms


class HTMLConverterForm(forms.Form):
    tab = forms.ChoiceField(choices=[(1, '<pr> & <br>'), (2, '<pr>'), (3, '<br>')],
                            widget=forms.Select(attrs={'class': 'form-select'}))
    br = forms.ChoiceField(choices=[('<br>', '<br>'), ('<br />', '<br />')],
                           widget=forms.Select(attrs={'class': 'form-select'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'resize: none;'}))
    html = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'resize: none; readonly'}),
                           required=False)
