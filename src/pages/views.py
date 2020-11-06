from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request, request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    # a key/value pair. the key is a string, but the value can be anything.
    my_context = {
        "title": "this is about me",
        "my_number": 123,
        "this_is_true": True,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello Goodfellas</h1>"
    }

    for item in [1313, 4231, 312]:
        my_context['item1'] = item

    return render(request, "about.html", my_context)
