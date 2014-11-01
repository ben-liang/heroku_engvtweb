from django import forms
from django.forms.formsets import formset_factory


class AddToCartForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #may want to make this a choices field but it might just
    #be easier to keep as CharField so that choices don't have to be modified
    #as new objects are added
    object_type = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1)

    def clean(self):
        cleaned_data = super(AddToCartForm, self).clean()
        #custom validation goes here
        return cleaned_data

class UpdateQuantityForm(forms.Form):
    #id of item in cart
    item_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=0, label='')

    def clean(self):
        cleaned_data = super(UpdateQuantityForm, self).clean()
        #custom validation goes here
        return cleaned_data

CartFormset = formset_factory(UpdateQuantityForm, extra=0)