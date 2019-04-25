def tag_schema_validator(tag_input):
    tag_schema = {"items": list, "has_more": bool, "quota_max": int, "quota_remaining": int}
    for key in tag_input:
        if key in tag_schema:
            assert type(tag_input[key]) is tag_schema[key]
        else:
            assert False


def tag_item_schema_validator(tag_input):
    item_tag_schema = {"has_synonyms": bool, "is_moderator_only": bool, "is_required": bool, "count": int,
                       "name": str}
    tag_schema_validator(tag_input=tag_input)
    items = tag_input['items']
    if len(items):
        for item in items:
            for key in item:
                if key in item_tag_schema:
                    assert type(item[key]) is item_tag_schema[key]
                else:
                    assert False


def tag_schema_validator_for_synonyms(tag_input):
    item_tag_synonyms_schema = {"creation_date": int, "applied_count": int, "to_tag": str,
                                "from_tag": str, "last_applied_date": int}
    tag_schema_validator(tag_input=tag_input)
    items = tag_input['items']
    if len(items):
        for item in items:
            for key in item:
                if key in item_tag_synonyms_schema:
                    assert type(item[key]) is item_tag_synonyms_schema[key]
                else:
                    assert False


def validate_response_for_invalid_site(json_data, site_name):

    tag_schema = {"error_id": int, "error_message": str, "error_name": str}

    for key in json_data:
        if key in tag_schema:
            assert type(json_data[key]) == tag_schema[key]
        else:
            assert False

    assert json_data['error_id'] == 400
    assert json_data['error_message'] == "No site found for name `{}`".format(site_name)
    assert json_data['error_name'] == 'bad_parameter'


def check_if_element_is_present_in_response(element, json_data):

    present_item = []
    for item in json_data['items']:
        if item[element] == True:
            present_item.append(item)
    return present_item


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj




