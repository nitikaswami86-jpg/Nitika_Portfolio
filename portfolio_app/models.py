from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('python', 'Python / Django'),
        ('frontend', 'Frontend'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='web')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=80)
    category = models.CharField(max_length=50, default='frontend')
    icon = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
