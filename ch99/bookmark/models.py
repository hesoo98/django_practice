from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):  # 테이블 새로 만들때 model, admin 둘다 건드려야함
    title = models.CharField('Title', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # 글쓴이, 외래키로 유저참조, null=True 인 이유는 기존에 작성된게 글쓴이 구현 전에 생성해서.

    # 객체를 문자열로 표현할때 사용, 레코드 하나를 의미함. 안쓰면 어드민에..이름안뜸.
    def __str__(self):
        return self.title
