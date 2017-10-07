from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from member.models import User




class JoinForm(UserCreationForm):
    #여기참조해봐
    # https: // stackoverflow.com / questions / 21779226 / abstractuser - django - full - example
    class Meta:
        model = get_user_model()#뭐 그냥 auth_model 여기 바꾸면 이것도 바뀜
        fields = ('username','password1','password2','email','realname') #UserCreationForm에 없는 realname필드를 정의 할수 있는 이유
        #ㅋ 내가 abstractuser인가 상속받아서 재정의 했지롱 ㅋ
        #이건 추가하는거고 기존 help_texts를 바꾸려면 init 메서드 오버라이딩 해야함
        help_texts = {
            'realname':'풀네임쓰셈'
        }
    # class Meta(UserCreationForm.Meta):
    #     fields = UserCreationForm.Meta.fields + ('email',)
    def __init__(self, *args, **kwargs):
        super(JoinForm,self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = '8자이상 반복패턴x'

    #is_valid() -> clean() ->클린안에서 밸리데이터실행후 통과하면 cleaned_data에 담음
    #그러니까 is_valid() 이게 실행할때 밸리데이터가 실행되는게아니라 그냥 폼에 담는순간 밸리데이터가 실행!!!!!!!!!!
    #is_valid 는 그냥 error이 있나 없나 검사하는거임 폼에 넣는순간 밸리데이터가 실행되며 error 에 에러들이 담김
    #이게 리얼 포인트
    #q.errors 이거는 실행하면 내부적으로 clean 메서드 실행해서 에러 담아주고
    #clean 메서드가 실행되니 cleaned_data 도나온다

    def clean_email(self):
        print('어느시점에 이게 실행이지1')
        email = self.cleaned_data.get('email')
        if email:
            if get_user_model().objects.filter(email = email).exists():
                print('이미존재이메일')
                #화면에보이는 에러임 이건
                raise forms.ValidationError('이미 존재하는 이메일입니다')
        return email

    #raise로 발생시킨 밸리데이션 에러를 form.errors에 담는다 ㅋ
    #그니까 clean_field 메서드는 장고가 이미해주는거와 추가로 더 해주길 원할때
    #이걸쓰는거임 !
    def clean_password1(self):
        print('얘도실행되나')
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.')
        return password1

class JoinvaldationForm(JoinForm):


    def __init__(self, *args, **kwargs):
        super(JoinvaldationForm,self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['email'].required = False
        self.fields['realname'].required = False



