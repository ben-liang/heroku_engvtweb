from django import forms
from django.forms.formsets import formset_factory

class AddToCartForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #may want to make this a choices field but it might just
    #be easier to keep as CharField so that choices don't have to be modified
    #as new objects are added
    object_type = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1)

    # NULL_VARIANT = '## N/A ##'
    def __init__(self,*args,**kwargs):
        """
        Add hide_variant kwarg as boolean.
        :param args:
        :param kwargs:
        :return:
        """
        super(AddToCartForm, self).__init__(*args,**kwargs)
        # if kwargs.has_key('initial'):
        #     if kwargs['initial'].has_key('variant'):
        #         variant = kwargs['initial']['variant']
        #         if variant == self.NULL_VARIANT:
        #             self.base_fields['variant'] = forms.CharField(widget=forms.HiddenInput)
        #             self.base_fields['variant'].initial = self.NULL_VARIANT

    def clean(self):
        cleaned_data = super(AddToCartForm, self).clean()
        # if cleaned_data['variant'] == self.NULL_VARIANT:
        #     cleaned_data['variant'] = None
        # #custom validation goes here
        return cleaned_data

class AddToCartWithVariantForm(AddToCartForm):
    variant = forms.CharField(max_length=32, label='Size')

class UpdateQuantityForm(forms.Form):
    #id of item in cart
    item_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=0, label='')

    def clean(self):
        cleaned_data = super(UpdateQuantityForm, self).clean()
        return cleaned_data

CartFormset = formset_factory(UpdateQuantityForm, extra=0)