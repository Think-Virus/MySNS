from django.shortcuts import render, redirect
from .models import TweetModel
from .models import TweetComment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView


# Create your views here.

def home(request):  # 사용자 로그인 확인
    user = request.user.is_authenticated  # 로그인된 사용자를 확인하는 기능
    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')


def tweet(request):  # home.html 표출하는 함수
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            all_tweet = TweetModel.objects.all().order_by(
                '-created_at')  # TweetModel.objects.all() : 트윗 모델의 모든 object를 불러오겠다 / order_by('-created_at') 생성된 것의 역순으로 불러오겠다.
            return render(request, 'tweet/home.html',
                          {'tweet': all_tweet})  # 불러온 all_tweet을 tweet/home 화면으로 넘김 // 딕션널리 형식으로 넘겼으므로 이 데이터의 키값은 tweet
        else:
            return redirect('/sign-in')

    if request.method == 'POST':
        user = request.user  # 위와 달리 user까지만 적게되면 지금 접속한 사용자의 모든 정보를 볼 수 있음
        content = request.POST.get('my-content', '')
        tags = request.POST.get('tag','').split(',')

        if content == '':
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'error': '글은 공백일 수 없음', 'tweet': all_tweet})
        else:
            """my_tweet = TweetModel()
            my_tweet.author = user
            my_tweet.content = request.POST.get('my-content', '')
            my_tweet.save()"""
            # 위 내용을 간략화한 코드 ↓
            my_tweet = TweetModel.objects.create(author=user, content=content)
            for tag in tags :
                tag = tag.strip() # 공백 제거
                if tag != '':
                    my_tweet.tags.add(tag)
            my_tweet.save()
            return redirect('/tweet')


@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')


@login_required
def detail_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')
    return render(request, 'tweet/tweet_detail.html', {'tweet': my_tweet, 'comment': tweet_comment})


@login_required
def write_comment(request, id):
    if request.method == 'POST':
        comment = request.POST.get("comment", "")
        current_tweet = TweetModel.objects.get(id=id)

        TC = TweetComment()
        TC.comment = comment
        TC.author = request.user
        TC.tweet = current_tweet
        TC.save()

        return redirect('/tweet/' + str(id))


@login_required
def delete_comment(request, id):
    comment = TweetComment.objects.get(id=id)
    current_tweet = comment.tweet.id
    comment.delete()
    return redirect('/tweet/' + str(current_tweet))

class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
