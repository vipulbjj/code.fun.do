from django.db import models
# Create your models here.

class PdfFile(models.Model):
	file = models.FileField(upload_to='files_pdf/')