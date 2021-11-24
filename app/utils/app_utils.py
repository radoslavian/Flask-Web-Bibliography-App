'''Various utilities for the application, including
data structures for route (view) functions.
'''


search_fields = [
    {
        'title': 'People names in a responsibility area:',
        'card_header_id': 'responsibility-person-header',
        'collapse_id': 'responsibility-person-collapse',
        'input_id': 'responsibility-person',
        'endpoint': '.get_person_entries',
        'query_parameter': 'responsibility_person_id',
        'filter_id': 'people-names-filter',
        'selected_list_id': 'people-responsibilities-list'
    },
    {
        'title': 'Subject headers of searched documents:',
        'card_header_id': 'subject-headers',
        'collapse_id': 'subject-headers-collapse',
        'input_id': 'keyword-input',
        'endpoint': '.get_keywords',
        'query_parameter': 'keyword_id',
        'filter_id': 'document-keyword-filter',
        'selected_list_id': 'document-keyword-list'
    },
    {
        'title': 'Publication places of searched documents:',
        'card_header_id': 'publication-places-header',
        'collapse_id': 'search-publication-place',
        'input_id': 'publication-place-input',
        'endpoint': '.get_geographic_location',
        'query_parameter': 'publication_place_id',
        'filter_id': 'document-publication-place-dropdown',
        'selected_list_id': 'document-publication-places-list'
    },
    {
        'title': 'Geographic locations as topics:',
        'card_header_id': 'place-topic-header',
        'collapse_id': 'search-place-topic',
        'input_id': 'topic-place-input',
        'endpoint': '.get_geographic_location',
        'query_parameter': 'topic_place_id',
        'filter_id': 'topic-place-dropdown',
        'selected_list_id': 'places-topics-list'
    },
    {
        'title': 'Collective bodies in responsibility area:',
        'card_header_id': 'responsibility-collectivity-header',
        'collapse_id': 'search-responsibility-collectivity',
        'input_id': 'responsibility-collectivity-input',
        'endpoint': '.get_collective_bodies',
        'query_parameter': 'responsibility_collectivity_id',
        'filter_id': 'responsibility-collectivity-dropdown',
        'selected_list_id': 'responsibility-collectivity-list'
    },
    {
        'title': 'Collective bodies as subjects:',
        'card_header_id': 'subject-collectivity-header',
        'collapse_id': 'search-subject-collectivity',
        'input_id': 'subject-collectivity-input',
        'endpoint': '.get_collective_bodies',
        'query_parameter': 'collectivity_topic_id',
        'filter_id': 'subject-collectivity-dropdown',
        'selected_list_id': 'subject-collectivity-list'
    },
    {
        'title': 'Language as a topic:',
        'card_header_id': 'topic-language-header',
        'collapse_id': 'search-topic-language',
        'input_id': 'subject-topic-language-input',
        'endpoint': '.get_language_entries',
        'query_parameter': 'topic_language_id',
        'filter_id': 'topic-language-dropdown',
        'selected_list_id': 'topic-language-list'
    },
    {
        'title': 'Publication languages of searched documents:',
        'card_header_id': 'publication-language-header',
        'collapse_id': 'search-publication-language',
        'input_id': 'publication-language-input',
        'endpoint': '.get_language_entries',
        'query_parameter': 'publication_language_id',
        'filter_id': 'publication-language-dropdown',
        'selected_list_id': 'publication-language-list'
    },
    {
        'title': 'Original languages of searched documents:',
        'card_header_id': 'original-language-header',
        'collapse_id': 'search-original-language',
        'input_id': 'original-language-input',
        'endpoint': '.get_language_entries',
        'query_parameter': 'original_language_id',
        'filter_id': 'document-original-language-filter',
        'selected_list_id': 'document-original-language-list'
    },
    {
        'title': 'Individual (personal) names as topics:',
        'card_header_id': 'person-topic-header',
        'collapse_id': 'search-person-topic',
        'input_id': 'topic-person',
        'endpoint': '.get_person_entries',
        'query_parameter': 'topic_person_id',
        'filter_id': 'people-names-topics-filter',
        'selected_list_id': 'people-topics-list'
    },
]
