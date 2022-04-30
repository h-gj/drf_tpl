from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {
          "code": 1000,
          "message": "success",
          "data": data,
        }

        return super().render(response, accepted_media_type, renderer_context)
