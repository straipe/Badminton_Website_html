from datetime import timedelta
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Match, Review
from .forms import MatchForm, ReviewForm

@login_required
def index(request):
    timesince = timezone.now() - timedelta(days=3)
    # print(request.user.rating)
    match_list = Match.objects.all()\
    .filter(
        match_day__gte = timesince
    )\
    .filter(
        Q(match_rank__lte = request.user.rating + 500) &
        Q(match_rank__gte = request.user.rating - 500)
    )
    review_list = Review.objects.all()
    review_form = ReviewForm

    return render(request,'badminton/index.html',{
        'match_list': match_list,
        "review_list": review_list,
        "review_form": review_form,
    })

@login_required
def match_new(request):
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '매치가 등록되었습니다.')
            return redirect('root')
    else:
        form = MatchForm()
    return render(request, "badminton/match_form.html",{
        'form': form,
    })

@login_required
def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'badminton/match_detail.html',{
        'match': match,
    })

@login_required
def review_new(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            if request.headers.get('x-requested-with')=='XMLHttpRequest':
                return render(request,"badminton/_review.html",{
                    "review": review,
                })
            return redirect('root')
    else:
        form = ReviewForm()
    return render(request,"badminton/review_form.html",{
        "form": form,
    })