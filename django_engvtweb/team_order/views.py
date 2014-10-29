from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet

qbp_sqs = SearchQuerySet().order_by('category', 'brand').\
    facet('category', size=2000, order='term').facet('brand', size=2000, order='term')

class QBPSearchView(FacetedSearchView):
    pass





