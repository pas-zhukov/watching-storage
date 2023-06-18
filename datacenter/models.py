from django.db import models
from django.utils.timezone import localtime, now


class DictView:
    """
    Класс для отображения атрибутов в виде словаря, необходим для отладки.
    """
    @property
    def dict(self):
        dictionary = self.__dict__
        dictionary.pop("_state")
        dictionary.pop("id")
        return dictionary


class Passcard(models.Model, DictView):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model, DictView):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    @property
    def duration(self):
        if self.leaved_at:
            time_to_count_duration = self.leaved_at
        else:
            time_to_count_duration = localtime(now().replace(microsecond=0),
                                               self.entered_at.tzinfo)
        duration = time_to_count_duration - self.entered_at
        return duration

    def formatted_duration(self) -> str:
        hours = int(self.duration.total_seconds() // 3600)
        minutes = int(self.duration.total_seconds() % 3600 // 60)
        return f"{hours}ч {minutes}мин"

    def is_long(self, minutes: int = 60) -> bool:
        return self.duration.total_seconds() / 60 > minutes
