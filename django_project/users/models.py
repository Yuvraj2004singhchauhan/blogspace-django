from django.db import models
from django.contrib.auth.models import User

DEFAULT_PROFILE_IMAGE = (
    "https://res.cloudinary.com/dejnxcov0/image/upload/"
    "v1770530490/default_peljpp.webp"
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    @property
    def image_url(self):
        if self.image:
            try:
                return self.image.url
            except Exception:
                pass
        return DEFAULT_PROFILE_IMAGE




