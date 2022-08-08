from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
daily_challenges = {
    "Monday": "Start learning about the basics of Python.",
    "Tuesday": "Study about Classes and Objects",
    "Wednesday": "Read about if,for and while loops.",
    "Thursday": "Study about Decorators, Iterators and Generators.",
    "Friday": "Study the OOPS concepts in Python.",
    "Saturday": "Revise"
}

def index(request):
    list_items = ""
    days = list(daily_challenges.keys())
    return render(request, "challenges/index.html", {
        "days": days
    })


    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def daily_challenge_by_number(request, day):
    days = list(daily_challenges.keys())

    if day > len(days):
        return HttpResponseNotFound("Invalid month")

    redirect_day = days[day - 1]
    redirect_path = reverse("day-challenge", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)


def daily_challenge(request, day):
    try:
        challenge_text = daily_challenges[day]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "day_name": day.capitalize()
        })
    except:
        raise Http404()