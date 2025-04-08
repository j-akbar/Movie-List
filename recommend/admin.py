from django.contrib import admin
from .models import Movie, Myrating, MyList

# Register models.
admin.site.register(Movie)
admin.site.register(Myrating)
admin.site.register(MyList)