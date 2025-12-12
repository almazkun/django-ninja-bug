from ninja import NinjaAPI
from ninja.orm import ModelSchema
from pydantic import Field

from core.models import Response


class ResponseSchemaField(ModelSchema):
    status: str = Field(alias="get_status_display")

    class Meta:
        model = Response
        fields = ["id"]


class ResponseSchemaExclude(ModelSchema):
    status: str = Field(alias="get_status_display")

    class Meta:
        model = Response
        exclude = ["id"]


api = NinjaAPI()


@api.get("/responses/fields/", response=list[ResponseSchemaField])
def responses_fields(request):
    return Response.objects.all()


@api.get("/responses/exclude/", response=list[ResponseSchemaExclude])
def responses_exclude(request):
    return Response.objects.all()
