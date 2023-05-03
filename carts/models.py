from django.db import models
import uuid


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="cart")
