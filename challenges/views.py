from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

    for day in days:
        capitalized_day = day.capitalize()
        day_path = reverse("day-challenge", args=[day])
        list_items += f"<li><a href=\"{day_path}\">{capitalized_day}</a></li>"


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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
