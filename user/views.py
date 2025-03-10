from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse #화면에 글자를 띄울 때, 사용
from django.contrib.auth import get_user_model # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth # 암호된 비밀번호로 로그인하게 하는 것
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user :
            return redirect('/') #redirect('/')는 /를 담당하는 함수는 tweet 앱의 home이라는 함수
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username','') #request.POST : post로 가져온 데이터 / request.POST로 받아온 데이터 중 username 이라는 데이터를 가져오겠다. / 만약 username이 없다면 None으로 가져오겠다.
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2 :
            return render(request, 'user/signup.html',{'error':'패스워드를 확인 해 주세요!'})

        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html',{'error':'사용자 이름과 비밀번호는 필수 값 입니다.'})


            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html',{'error':'이미 가입한 사용자입니다.'})

            else:
                """
                new_user = UserModel()
                new_user.username = username
                new_user.password = password
                new_user.bio = bio
                new_user.save() #위에서 작성한 내용을 DB에 저장
                """
                #위의 내용을 장고에서 제공해주는 기능으로 한번에
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in') # 회원가입이 완료되면 로그인 창으로 이동


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        """
        # 암호화 이전에 직접 구현한 코드    
        me = UserModel.objects.get(username=username)
        if me.password == password:
            request.session['user'] = me.username #session은 사용자 정보를 저장할 수 있다 정도로 생각 / 같은 사람이 요청하는지 확인할 수 있도록 도와주는 것
            return HttpResponse(username)
        else:
            return redirect('/sign-in/')"""

        # 장고의 기능을 활용한 코드
        me = auth.authenticate(request, username=username, password=password)# authenticate는 암호화된 비밀번호와 지금 비밀번호가 일치하는지 확인해주는 기능
        if me is not None:
            auth.login(request, me) # 장고가 이미 선언해놓은 로그인 기능
            return redirect('/')
        else:
            return render(request, 'user/signin.html',{'error':'계정이 일치하지 않습니다.'})


    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user :
            return redirect('/')
        else:
            return render(request, 'user/signin.html')

@login_required #사용자가 로그인 되어야만 접근할 수 있는 함수로 변경
def logout(request) :
    auth.logout(request) #장고에서 제공하는 로그아웃 기능
    return redirect('/')

# user/views.py

@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})

@login_required
def user_follow(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')