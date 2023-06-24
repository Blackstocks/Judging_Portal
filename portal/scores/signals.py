from django.db.models.signals import post_save
from django.dispatch import receiver
from customUser.models import Judge, Participant
from .models import Score
from django.db import models
from django.dispatch import Signal

# @receiver(post_save, sender=Judge)
# def create_score_for_judge(sender, instance, created, **kwargs):
#     if created:
#         participants = Participant.objects.all()
#         for participant in participants:
#             Score.objects.get_or_create(participant=participant, judge=instance)

# @receiver(post_save, sender=Participant)
# def create_score_for_participant(sender, instance, created, **kwargs):
#     if created:
#         judges = Judge.objects.all()
#         for judge in judges:
#             Score.objects.get_or_create(participant=instance, judge=judge)

score_created = Signal()

@receiver(post_save, sender=Score)
def update_participant_total_score(sender, instance, **kwargs):
    participant = instance.participant

    # Calculate the average score based on associated scores
    scores = Score.objects.filter(participant=participant)
    total_score = scores.aggregate(total=models.Sum('total'))['total']
    num_judges = scores.count()
    average_score = total_score / num_judges if num_judges > 0 else 0

    participant.total_score = average_score
    participant.save()

@receiver(post_save, sender=Score)
def assign_rank_to_participant(sender, instance, **kwargs):
    participants = Participant.objects.all()
    sorted_participants = sorted(participants, key=lambda p: p.total_score or 0, reverse=True)

    for index, participant in enumerate(sorted_participants):
        participant.rank = index + 1
        participant.save()

@receiver(score_created)
def handle_score_creation(sender, **kwargs):
    judge = kwargs['judge']
    participant = kwargs['participant']
    print("triger")
    Score.objects.get_or_create(judge=judge, participant=participant)