from rest_framework.renderers import BaseRenderer, JSONRenderer
from rest_framework.utils import json


class ApiRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(data)
        response_dict = {
            'status': 12,
            'result': {},
            'addition': {},
            'description': {},
        }
        if data.get('data'):
            response_dict['data'] = data.get('data')
        if data.get('status'):
            response_dict['status'] = data.get('status')
        if data.get('message'):
            response_dict['message'] = data.get('message')
        data = response_dict
        return super(ApiRenderer, self).render(data, accepted_media_type, renderer_context)
