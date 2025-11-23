from django.db import models
from django.conf import settings
ROLE_CHOICES = {
    ('student','teacher')
}
# Create your models here.
class students(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    student_id = models.PositiveIntegerField(editable = False)
    semester = models.IntegerField(default = 1)
    year = models.IntegerField(default = 1)
    group = models.CharField(max_length = 50)
    role = models.CharField(max_length = 20, choices=ROLE_CHOICES)


    def save(self, *args, **kwargs):
        if not self.student_id and self.user:
            self.student_id = self.user
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.username} ({self.course} - Sem {self.semester})"

    




