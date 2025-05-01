from django.contrib import admin
from .models import Todo  # Import your model

# Register the Todo model to appear in the Admin interface
admin.site.register(Todo)