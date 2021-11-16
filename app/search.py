from flask import current_app

def add_to_index(index, model):
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, doc_type=index,
                                    id=getattr(model, model.__primary_key__),
                                    body=payload)


def remove_from_index(index, model):
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, doc_type=index,
                                     id=getattr(model, model.__primary_key__))


def query_index(index, query, page, per_page):
    if not current_app.elasticsearch:
        return
    search = current_app.elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*'],
                                        "fuzziness": "3"}},
              'from': (page - 1) * per_page, 'size': per_page})
    ids = [int(hit['_id']) for hit in search['hits']['hits']]

    return ids, search['hits']['total']['value']
