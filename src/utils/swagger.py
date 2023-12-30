from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.views import get_schema_view
from rest_framework import permissions

swagger_schema_view = get_schema_view(
    openapi.Info(
        title=_("Pay Space APIs"),
        default_version='v1',
       description=render_to_string('swagger/introduction.md'), # it is here to show you my intent and you can replace it with some simple string
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='ghhabib2@gmail.com'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=([permissions.AllowAny,]),
)


class XcodeAutoSchema(SwaggerAutoSchema):
    python_template = None

    def get_operation(self, operation_keys=None):
        assert self.python_template, "All SwaggerAutoSchema class must define python_template filed in it"

        operation = super().get_operation(operation_keys)

        # Using django templates to generate the code
        template_context = {
            "request_url": self.request._request.build_absolute_uri(self.path),
        }



        operation.update({
            'x-codeSamples': [
                {
                    "lang": "Python",
                    "source": render_to_string(self.python_template, template_context)
                },
            ]
        })
        return operation

    @classmethod
    def responses(cls):
        raise NotImplemented("This Class has not implemented yet;")