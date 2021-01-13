import os
from PIL import Image
from django.db.models.fields.files import ImageField, ImageFieldFile


class ThumbnailImageFieldFile(ImageFieldFile):
    def _add_thumb(self, s):  # 썸네일 이미지 이름 뒤에 thumb 넣어줌. 썸네일 확장자가 jpeg, jpg 아니면 넣어줌.
        parts = s.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return ".".join(parts)

    @property
    def thumb_path(self):   # 썸네일의 경로를 만들어줌.
        return self._add_thumb(self.path)

    @property
    def thumb_url(self):    # 썸네일의 url을 만들어줌.
        return self._add_thumb(self.url)

    def save(self, name, content, save=True):
        super().save(name, content, save)

        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0] - img.size[0]) / 2),
               int((size[1] - img.size[1]) / 2))  # 썸네일과 bg이미지를 합쳐서 정사각형
        background.paste(img, box)                # 모양의 썸넬 이미지를 만듦, 빈공간 흰색
        background.save(self.thumb_path, 'JPEG')  # filename, format, thumb_path 경로에 저장.

    def delete(self, save=True):    # 호출 시 원본 이미지와 썸넬 이미지 삭제
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)


class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs)
