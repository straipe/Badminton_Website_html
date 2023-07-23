from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.shortcuts import resolve_url
from django.template.loader import render_to_string

class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"
    
    class SkillChoices(models.IntegerChoices): #TODO: BKRP을 반영한 실력 분류 알고리즘 적용 예정 
        Was_player = 2800, "선수 출신"
        Aclass = 2700, "A조"
        Bclass = 2600, "B조"
        Cclass = 2500, "C조"
        Dclass = 2000, "D조"
        Skillful_User = 1500, "기본적인 스트로크 구사 가능자"
        Beginner = 1000, "초보자"

    gender = models.CharField(max_length=1, blank=True, choices=GenderChoices.choices)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, 
                                    validators=[RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
                                    help_text="010-XXXX-XXXX 혹은 010XXXXXXXX 모두 가능")
    avatar = models.ImageField(blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="48px * 48px 크기의 png/jpg 파일만 업로드")
    mom = models.IntegerField(default=0)
    
    # Glicko2를 적용하기 위한 컬럼들
    rating = models.IntegerField(default=1500, choices=SkillChoices.choices)
    rd = models.FloatField(default=350.0)
    win_count = models.IntegerField(default=0)
    lose_count = models.IntegerField(default=0)
    draw_count = models.IntegerField(default=0)
    sigma = models.FloatField(default=0.06)


    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def odds(self):
        if (self.win_count+self.lose_count+self.draw_count)==0:
            return 0
        else:
            return self.win_count / (self.win_count+self.lose_count+self.draw_count)
    
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return resolve_url("pydenticon_image",self.username)
    
    def send_welcome_email(self):
        subject = render_to_string("accounts/welcome_email_subject.txt",{
            "user":self,
        })
        content = render_to_string("accounts/welcome_email_content.txt",{
            "user":self,
        })
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject,content, sender_email,[self.email],fail_silently=False)