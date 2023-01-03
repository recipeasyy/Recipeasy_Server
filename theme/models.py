from django.db import models

# Create your models here.

class ThemeType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}: {self.description[:10]}..."


class Theme(models.Model):
    theme_type = models.ForeignKey(ThemeType, on_delete=models.SET_NULL, null=True, related_name='themes')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    recipe_count = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    tips = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.theme_type}] {self.title}, {self.description[:10]}..."
