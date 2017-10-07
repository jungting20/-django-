from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login as auth_login ,logout
# Create your views here.
from member.forms import JoinForm, JoinvaldationForm


def joinmember(request):
    if request.method == "POST":
        #딕셔너리로 들어온다 ㅋ
        print('리퀘스트.포스트',request.POST.keys())
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return HttpResponse(form.error_messages)
    else:
        form = JoinForm()
        print(form)
        return render(request,'joinform.html',context={
        'form':form
    }
    )


def login(request):
    if request.method == "POST":

            user = authenticate(username = request.POST.get('username'),
                                password = request.POST.get('password'),)
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    request.session['realname'] = user.realname
                    if request.GET.get('next'):
                        return redirect(request.GET.get('next'))
                    return redirect('boardlist')
            else:
                return HttpResponse("아이디 비번 확인좀")
    else:

        form = AuthenticationForm()
        return render(request,'login.html',context={
            'form':form,
            'next':request.GET.get('next')
        })

def logout(request):
    try:

        logout(request)
        del request.session['realname']
        return redirect('login')
    except:
        return HttpResponse('<script>alert("Some error occured.");history.back();</script>')

def joinmemberajax(request):
    htmlname = request.POST.get('htmlname')
    datadict = {}
    datadict[htmlname] = request.POST.get('data')
    datadict['csrfmiddlewaretoken'] = request.POST.get('csrfmiddlewaretoken')
    #join 밸리데이션폼 이걸 잘써야한다
    print('밸리데이션?')
    form = JoinvaldationForm(datadict)
    errordata = {
        'error_message':form.errors.get(htmlname)
    }
    print('에러메세지',form.errors.get(htmlname))
    return JsonResponse(errordata)

    #필요없지만 코딩해볼만함
    # if error_key == 'username':
    #     data['alreadyex'] = User.objects.\
    #     filter(username__iexact=request.POST.get('username')).exists()



