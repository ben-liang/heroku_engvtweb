from haystack.forms import FacetedSearchForm
from django.forms import ModelChoiceField, Form, EmailField, HiddenInput
from django_engvtweb.team_order.models import TeamOrder

class QbpForm(FacetedSearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

class TeamOrderForm(Form):

    team_order = ModelChoiceField(queryset=TeamOrder.objects.all())

class EmailOrderForm(Form):

    team_order = ModelChoiceField(widget=HiddenInput, queryset=TeamOrder.objects.all())
    email = EmailField()