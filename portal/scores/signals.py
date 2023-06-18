from django.db.models.signals import post_save
from django.dispatch import receiver
from customUser.models import Judge, Participant
from .models import Score

@receiver(post_save, sender=Judge)
def create_score_for_judge(sender, instance, created, **kwargs):
    if created:
        participants = Participant.objects.all()
        for participant in participants:
            Score.objects.get_or_create(participant=participant, judge=instance)

@receiver(post_save, sender=Participant)
def create_score_for_participant(sender, instance, created, **kwargs):
    if created:
        judges = Judge.objects.all()
        for judge in judges:
            Score.objects.get_or_create(participant=instance, judge=judge)
