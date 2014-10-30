from django_engvtweb.team_order.models import QbpPart

#map of models to strings used in forms to reference
#each model.  Doing this just to avoid having to do an "eval(str)"
#in order to get the model class.

#Convention will be to just use the model name as a string when
#referencing it.

PRODUCT_MODELS = {
    QbpPart.__name__: QbpPart,
}

