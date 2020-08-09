from django.db import models
from django.utils import timezone

class QiyaoEvent(models.Model):
    # supported event types:
    # start_feed, end_feed, start_sleep, end_sleep, pee, pass_motion, bottle_feed
    EVENT_TYPE_CHOICES = [
        ('START_FEED', '开始哺乳'),
        ('STOP_FEED', '结束哺乳'),
        ('START_FEED', '开始睡觉'),
        ('END_FEED', '结束睡觉'),
        ('PEE', '小便'),
        ('PASS_MOTION', '大便'),
        ('BOTTLE_FEED', '瓶喂')
    ]
    EVENT_TYPE_DICT = {tup[0]: tup[1] for tup in EVENT_TYPE_CHOICES}

    event_type = models.CharField(max_length=64, choices=EVENT_TYPE_CHOICES) # store available event types string
    time = models.DateTimeField(default=timezone.now)
    int_param = models.IntegerField(null=True, blank=True)
    str_param = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return "{} at {}".format(self.event_type, self.time)

    def get_event_type_display(self):
        return self.EVENT_TYPE_DICT[self.event_type]