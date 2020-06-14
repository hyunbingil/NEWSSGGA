from django.shortcuts import render, redirect
from cafeapp.models import Cafe
from django.http import Http404
from django.contrib.auth.models import User
from account.models import Profile
from .models import Board
from .forms import BoardForm
# Create your views here.
def cafemain(request, i_id):
    try :
        i = Cafe.objects.get(pk=i_id)
        user = request.user
        p = user.profile

        context = {'i':i, 'p':p}
    except :
        i = Cafe.objects.get(pk=i_id)
        context = {}
    return render(request,'cafe_main.html', context)

def createpost(request, cafe_id):
    try:
        user = request.user
        profile = user.profile

        if request.method == "POST":
            myform = BoardForm(request.POST, request.FILES)
            if myform.is_valid():
                myform.save()
                return redirect('/bulletinboard_page/{}'.format(cafe_id))
        myform = BoardForm()

        all_post = Board.objects.all()
        context = {'take_all_post':all_post, 'profile':profile}
        return render(request, 'createpost.html', context)
    except:
        if request.method == "POST":
            myform = BoardForm(request.POST, request.FILES)
            if myform.is_valid():
                myform.save()
                return redirect('/bulletinboard_page/{}'.format(cafe_id))

        all_post = Board.objects.all()
        context = {'take_all_post':all_post}
        return render(request, 'createpost.html', context)

def deletepost(request, cafe_id, post_id):
    my_post = Board.objects.get(pk=post_id)
    my_post.delete()

    return redirect('/bulletinboard_page/{}'.format(cafe_id))  

def update(request, cafe_id, post_id):
    try:
        user = request.user
        profile = user.profile

        my_post = Board.objects.get(pk=post_id)
        if request.method == "POST":
            update_form = BoardForm(request.POST, instance=my_post)
            if update_form.is_valid()==True:
                update_form.save()

                return redirect('/bulletinboard_page/{}'.format(cafe_id))
            # 검사를 꼭 해주어야 save를 사용할 수 있다.
        # object를 안에다가 넣어준다
        update_form = BoardForm(instance=my_post)

        return render(request, 'update.html', {'update_form': update_form, 'my_post': my_post, 'profile':profile})    
    except:
        my_post = Board.objects.get(pk=post_id)
        if request.method == "POST":
            update_form = BoardForm(request.POST, instance=my_post)
            if update_form.is_valid()==True:
                update_form.save()

                return redirect('/bulletinboard_page/{}'.format(cafe_id))
            # 검사를 꼭 해주어야 save를 사용할 수 있다.
        # object를 안에다가 넣어준다
        update_form = BoardForm(instance=my_post)

        return render(request, 'update.html', {'update_form': update_form, 'my_post': my_post})    

# def board(request):

#     return render(request, 'board.html')    

def post(request, cafe_id, post_id):
    try:
        user = request.user
        profile = user.profile

        my_post = Board.objects.get(pk=post_id)

        cafe = Cafe.objects.get(pk=cafe_id)

        return render(request, 'post.html', {'my_post':my_post, 'cafe':cafe, 'profile':profile})
    except:
        my_post = Board.objects.get(pk=post_id)

        cafe = Cafe.objects.get(pk=cafe_id)

        return render(request, 'post.html', {'my_post':my_post, 'cafe':cafe})


# def iscorrect(request):
#     if pw == Board.password:
        
#     return render()    