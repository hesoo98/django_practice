from django.db import models
#테이블 새로 만들때 model이랑 admin 둘다 건드려야함
class Bookmark(models.Model):
    title = models.CharField('Title', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

#객체를 문자열로 표현할때 사용, 레코드 하나를 의미함.
    def __str__(self):
        return self.title
