from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthObj = {
    "january" : "January",
    "february" : "Challenge"
}


def index(request):
    months = list(monthObj.keys())
    return render(request, 'challenges/index.html', {
        "months": months
    })

def monthly_challenge_by_num(request, month):
    print(month)
    months = list(monthObj.keys())
    if month > len(months):
        return HttpResponseNotFound('Error')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month_challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthObj[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        raise Http404()
    