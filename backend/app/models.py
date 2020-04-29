import uuid
from django.db import models
# db/schema.rb

class Items(models.Model):
	# id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	content = models.TextField()
	content_type = models.CharField(max_length=200)
	enc_item_key = models.TextField()
	auth_hash = models.CharField(max_length=200)
	user_uuid = models.CharField(max_length=200)
	deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	last_user_agent = models.TextField()
