from django.conf import settings
from django.db import models

class Match(models.Model):
    class SkillChoices(models.IntegerChoices): #TODO: BKRP을 반영한 실력 분류 알고리즘 적용 예정 
        Was_player = 2800, "선수 출신"
        Aclass = 2700, "A조"
        Bclass = 2600, "B조"
        Cclass = 2500, "C조"
        Dclass = 2000, "D조"
        Skillful_User = 1500, "기본적인 스트로크 구사 가능자"
        Beginner = 1000, "초보자"

    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'manage_match_set', 
                                on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='badminton/match/%Y/%m/%d')
    address = models.CharField(max_length=50)
    match_day = models.DateTimeField(blank=True)
    match_time = models.IntegerField()
    match_rank = models.IntegerField(default=1500, choices=SkillChoices.choices)
    cost = models.IntegerField()
    player = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='play_match_set')

    # def get_absolute_url(self):
    #     return reverse("badminton:match_detail",kwargs={'pk':self.pk})

    # def is_enter_user(self, user):
        # return self.player.filter(pk=user.pk).exists()
    
    class Meta:
        ordering = ['-match_day']

class Review(models.Model):
    class ScoreChoices(models.IntegerChoices):
        good = 3, "최고에요"
        soso = 2, "보통이에요"
        bad = 1, "아쉬워요"

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    satisfaction = models.IntegerField(choices=ScoreChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']