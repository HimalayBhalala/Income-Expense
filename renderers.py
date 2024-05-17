from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''

        if 'ErrorDetail' in data:
            response = json.dumps({'errors':data})
        else:
            response = json.dumps({'data':data})

        # import pdb
        # pdb.set_trace()

        return response