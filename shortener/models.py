from django.db import models


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.CharField(max_length=15, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("URL")
        verbose_name_plural = ("URLS")
    
    def __str__(self):
        return f"{self.url_hash}"
