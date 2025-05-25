<<<<<<< HEAD
from django.db import models

class UploadedDataset(models.Model):
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
=======
from django.db import models

class UploadedDataset(models.Model):
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
>>>>>>> 330dcfb96b73161d13ab79ae6433b06e887dfd0a
