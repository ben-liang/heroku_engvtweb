from django import forms
from django.forms.formsets import formset_factory
from django_engvtweb.team_order.models import TeamOrder

class AddToCartForm(forms.Form):
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #may want to make this a choices field but it might just
    #be easier to keep as CharField so that choices don't have to be modified
    #as new objects are added
    object_type = forms.CharField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=1)

    def clean(self):
        cleaned_data = super(AddToCartForm, self).clean()
        # if cleaned_data['variant'] == self.NULL_VARIANT:
        #     cleaned_data['variant'] = None
        # #custom validation goes here
        return cleaned_data

    @classmethod
    def bind_to_object_list(cls, queryset):
        """
        A little hacky but it works.  Generates a list of forms to be passed to a template with object_type and
        object ID's pre-populated.  Typically used for in-line product list forms, where you don't want to use
        a formset.

        :param queryset: queryset of objects to prepopulate forms
        :return: list of AddToCartForm objects (or subclass)
        """
        return [cls(initial={'object_id': obj.id,
                             'object_type': queryset.model.__name__})
                for obj in queryset]

class AddToCartWithVariantForm(AddToCartForm):
    variant = forms.CharField(max_length=32, label='Size')

class UpdateQuantityForm(forms.Form):
    #id of item in cart
    item_id = forms.IntegerField(widget=forms.HiddenInput)
    quantity = forms.IntegerField(min_value=0, label='')

    def clean(self):
        cleaned_data = super(UpdateQuantityForm, self).clean()
        return cleaned_data

class AssociateToOrderForm(forms.Form):

    team_order = forms.ModelChoiceField(queryset=TeamOrder.objects.all())

CartFormset = formset_factory(UpdateQuantityForm, extra=0)