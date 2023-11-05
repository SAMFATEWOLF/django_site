from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Actors
        fields = ['title', 'slug', 'sex', 'birth', 'death', 'bio', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'bio': forms.Textarea(attrs={'cols': 60, 'rows': 10}),

        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превыщает 200 символов')

        return title

    def clean_sex(self):
        sex = self.cleaned_data['sex']
        allowed = ['Мужской', 'Женский', 'мужской', 'женский']
        flag = None
        for option in allowed:
            if sex == option:
                flag = True
                return sex.title()
            else:
                flag = False
        if not flag:
            raise ValidationError('Пол должен быть указан, как "Мужской" или "Женский"')

