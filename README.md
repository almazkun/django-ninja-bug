Bug on alias does not uses the alias when exclude is used

```py
13 objects imported automatically (use -v 2 for details).

Python 3.14.0 (main, Oct  7 2025, 09:34:52) [Clang 17.0.0 (clang-1700.3.19.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
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

instance = Response.objects.create()
ResponseSchemaField.from_orm(instance)
ResponseSchemaExclude.from_orm(instance)
```
```py
ResponseSchemaField(status='Not assessed', id=4)
ResponseSchemaExclude(status=98)
```