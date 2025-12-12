from django.db import models


class StatusChoice(models.IntegerChoices):
    NEGATIVE = 0, "Negative"
    POSITIVE = 1, "Positive"
    NOT_ASSESSED = 98, "Not assessed"
    UNK = 99, "Unknown"


class Response(models.Model):
    status = models.IntegerField(
        choices=StatusChoice, default=StatusChoice.NOT_ASSESSED
    )
