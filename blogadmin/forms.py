from django import forms

from blog.models import Post


class BaseInput(forms.Widget):
    class Meta:
        abstract = True


class BaseModelForm(forms.ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(BaseModelForm, self).__init__(*args, **kwargs)
        self.set_required_fields()

    def set_required_fields(self):
        """ Sets the 'required' attribute to 'true' on necessary form fields """
        for field in self.fields:
            if self.fields[field].required:
                self.fields[field].widget.attrs['required'] = 'true'


class PostForm(BaseModelForm):

    class Meta:
        model = Post
