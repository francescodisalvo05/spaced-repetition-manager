import json


def get_dict_session(session):
    dict_session = {}
    if not session:
        for k, v in dict.items():
            dict_session[k] = {}

    else:
        # read from the json file
        with open(session) as handle:
            dict_session = json.loads(handle.read())

    return dict_session