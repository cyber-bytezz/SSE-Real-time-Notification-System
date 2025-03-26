from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project, Task, Comment, Notification

def create_notification(content):
    Notification.objects.create(content=content)

@receiver(post_save, sender=Project)
def project_handler(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    create_notification(f"Project {action}: {instance.name}")

@receiver(post_save, sender=Task)
def task_handler(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    create_notification(f"Task {action}: {instance.title}")

@receiver(post_save, sender=Comment)
def comment_handler(sender, instance, created, **kwargs):
    action = "created" if created else "updated"
    create_notification(f"Comment {action} on Task ID {instance.task.id}")
