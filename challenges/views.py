from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {  # a dictionary that has months and tasks as keys and values
    "january": "drink more water",
    "february": "code for 2 hours daily",
    "march": "practice some cooking",
    "april": "do meditation and write a journal",
    "may": "go vegan this month",
    "june": "workout in the morning",
    "july": "eat junkfood only once this month",
    "august": None,
    "september": "spend time with family",
    "october": "no drinks this month",
    "november": "redecorate places in the house",
    "december": None
}


def index(request):
    response_str = ""
    list_months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months_key": list_months
    })


def number_challenge(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h2>invalid month</h2>")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponse(redirect_path)


def month_challenge(request, month):
    try:
        task = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": task,
            "text2": month
        })

    except:
        raise Http404()
