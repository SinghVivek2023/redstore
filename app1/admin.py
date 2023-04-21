from django.contrib import admin
from django.db import models
from app1.models import Contact
from app1.models import User
from app1.models import Usera


# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Usera)
