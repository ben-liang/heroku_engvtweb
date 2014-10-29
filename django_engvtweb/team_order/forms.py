from haystack.forms import FacetedSearchForm

class QbpForm(FacetedSearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
