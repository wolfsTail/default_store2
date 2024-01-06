from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline

from .models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    res = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )
    res = res.annotate(
        headline=SearchHeadline(
            "name",
            query,
            start_sel="<span>",
            stop_sel="</span>",
        )
    )
    res = res.annotate(
        headline=SearchHeadline(
            "description",
            query,
            start_sel="<span>",
            stop_sel="</span>",
        )
    )
    return res