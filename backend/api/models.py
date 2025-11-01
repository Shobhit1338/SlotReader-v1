"""Models for SlotReader API."""

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from pgvector.django import VectorField


class User(AbstractUser):
    """Custom User model with UUID primary key."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.username or self.email or str(self.id)


class UserPreferences(models.Model):
    """User preferences for persona, goals, and scheduling."""

    PERSONA_CHOICES = [
        ('techie', 'Techie'),
        ('business', 'Business'),
        ('student', 'Student'),
        ('freelancer', 'Freelancer'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='preferences',
    )
    persona = models.CharField(
        max_length=20,
        choices=PERSONA_CHOICES,
        blank=True,
        null=True,
    )
    goal_reads_per_week = models.IntegerField(default=5)
    preferred_time_slot = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_preferences'
        verbose_name = 'User Preferences'
        verbose_name_plural = 'User Preferences'

    def __str__(self) -> str:
        return f'Preferences for {self.user.username}'


class Topic(models.Model):
    """Topics that users want to read about."""

    SOURCE_TYPE_CHOICES = [
        ('url', 'URL'),
        ('keyword', 'Keyword'),
        ('pdf', 'PDF'),
        ('youtube', 'YouTube'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPE_CHOICES,
    )
    source_value = models.CharField(max_length=500)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='topics',
    )
    score = models.FloatField(default=1.0, help_text='Scheduler weighting score')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'topics'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        indexes = [
            models.Index(fields=['user', 'is_active']),
            models.Index(fields=['user', 'score']),
        ]

    def __str__(self) -> str:
        return self.name


class Schedule(models.Model):
    """Weekly reading schedule slots."""

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('skipped', 'Skipped'),
    ]

    DAY_OF_WEEK_CHOICES = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='schedules',
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        related_name='schedules',
        null=True,
        blank=True,
        help_text='Nullable for placeholder slots',
    )
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK_CHOICES)
    time_slot = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )
    week_start_date = models.DateField(
        help_text='Date of Monday for this week',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schedules'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        indexes = [
            models.Index(fields=['user', 'week_start_date']),
            models.Index(fields=['user', 'day_of_week', 'status']),
            models.Index(fields=['user', 'status']),
        ]

    def __str__(self) -> str:
        day_name = dict(self.DAY_OF_WEEK_CHOICES)[self.day_of_week]
        topic_name = self.topic.name if self.topic else 'Placeholder'
        return f'{day_name} {self.time_slot} - {topic_name}'


class Summary(models.Model):
    """Generated summaries for scheduled reading slots."""

    FORMAT_CHOICES = [
        ('recap', 'Recap'),
        ('bullets', 'Bullets'),
    ]

    VERIFICATION_BADGE_CHOICES = [
        ('GREEN', 'Green'),
        ('AMBER', 'Amber'),
        ('RED', 'Red'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    schedule = models.OneToOneField(
        Schedule,
        on_delete=models.CASCADE,
        related_name='summary',
    )
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='summaries',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='summaries',
    )
    format = models.CharField(
        max_length=20,
        choices=FORMAT_CHOICES,
    )
    content = models.TextField()
    citation_spans = models.JSONField(
        default=dict,
        blank=True,
        help_text='Citation metadata and spans',
    )
    verification_badge = models.CharField(
        max_length=10,
        choices=VERIFICATION_BADGE_CHOICES,
        default='AMBER',
    )
    verification_score = models.FloatField(
        default=0.0,
        help_text='Numerical verification score',
    )
    citation_density = models.FloatField(
        default=0.0,
        help_text='Citations per 120 words',
    )
    embedding = VectorField(
        dimensions=1536,
        null=True,
        blank=True,
        help_text='Vector embedding for RAG retrieval',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'summaries'
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['topic', 'created_at']),
        ]

    def __str__(self) -> str:
        return f'Summary for {self.topic.name} - {self.format}'

