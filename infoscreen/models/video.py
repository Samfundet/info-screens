from django.db import models
from ..utils.__init__ import parse_url

from root import models as root_models

class Video(root_models.CustomBaseModel):
    name = models.CharField(max_length=140, null=True, blank=True)
    youtube_code = models.CharField(max_length=140, null=False, blank=False)
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.youtube_code = parse_url(self.youtube_code)
        super().save(*args, **kwargs)
