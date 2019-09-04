from django.db import models
from datetime import datetime  
import pytz

# this will create indivudal todo items in the builtin database
# Step 1: we then run "python manage.py makemigration" to tell the database about the new todoItem class\
# Step 2: to execute this run "python manage.py migrate" now you can user this model
# Step 3: "python manage.py shell"
# Step 4: from todo.moels import TodoItem
# Step 5: a = TodoItem(content = ' xxxxxxxxx ')
# Step 6: a.save()
class TodoItem(models.Model):
    content = models.TextField()
    dateCreated = models.DateTimeField(default=datetime.now(pytz.utc))


# Create your models here.
