from django import forms
import changuito

class AddToCartForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #may want to make this a choices field but it might just
    #be easier to keep as CharField so that choices don't have to be modified
    #as new objects are added
    object_type = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField()

    def clean(self):
        cleaned_data = super(AddToCartForm, self).clean()
        return cleaned_data

class RemoveFromCartForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #may want to make this a choices field but it might just
    #be easier to keep as CharField so that choices don't have to be modified
    #as new objects are added
    object_type = forms.CharField(widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super(RemoveFromCartForm, self).clean()
        return cleaned_data
