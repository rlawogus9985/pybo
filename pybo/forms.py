from django import forms
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject','content']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control','rows':10}),
        # }
        labels={
            'subject':'제목',
            'content':'내용',
        }
        #{{ form.as_p }}로 자동완성 말고 수작업으로 HTML코드를 작성

class AnswerForm(forms.ModelForm):
    class Meta:
        model= Answer
        fields = ['content']
        lables= {
            'content':'답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }