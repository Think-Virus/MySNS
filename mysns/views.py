#각 url에서 어떤 작업을 할지 정해주는 공간

from django.http import HttpResponse # HttpResponses는 문자열을 보여주는 것
from django.shortcuts import render # html 표출



def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

def first_view(request) :
    return render(request, 'my_test.html')