import jsonschema


def tag_schema_validator(tag_input):
    # TODO: the doc of the api does not say so but if there is an NULL value then this structure will change.
    schema = {"items": {"type": "array", "items": {"type": "object",
                                                   "properties":
                                                       {"has_synonyms": {"type": "boolean"},
                                                        "is_moderator_only": {"type": "boolean"},
                                                        "is_required": {"type": "boolean"},
                                                        "count": {"type": "number"},
                                                        "name": {"type": "string"}}}},
              "has_more": {"type": "boolean"},
              "quota_max": {"type": "number"},
              "quota_remaining": {"type": "number"}}

    jsonschema.validate(instance=tag_input, schema=schema)


def tag_schema_validator_for_synonyms(tag_input):
    # TODO: the doc of the api does not say so but if there is an NULL value then this structure will change.
    schema = {"items": {"type": "array", "items": {"type": "object",
                                                   "properties":
                                                       {"creation_date": {"type": "number"},
                                                        "applied_count": {"type": "number"},
                                                        "to_tag": {"type": "string"},
                                                        "from_tag": {"type": "string"},
                                                        }}},
              "has_more": {"type": "boolean"},
              "quota_max": {"type": "number"},
              "quota_remaining": {"type": "number"}}

    jsonschema.validate(instance=tag_input, schema=schema)


def validate_response_for_invalid_site(json_data, site_name):

    schema = {"error_id": {"type": "number"},
              "error_message": {"type": "string"},
              "error_name": {"type": "string"}
             }

    jsonschema.validate(instance=json_data, schema=schema)

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





