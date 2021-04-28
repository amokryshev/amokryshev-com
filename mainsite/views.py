import json
from django.shortcuts import render, get_object_or_404
from django.utils import translation
from django.views.decorators.cache import cache_page
from amokryshev.settings import CACHE_TIMEOUT
from .models import AboutSection, PortfolioSection, FactsSection, SkillsSection, CvSection, \
    ServicesSection, TestimonialsSection, Article


@cache_page(CACHE_TIMEOUT)
def index(request):

    locale = translation.get_language()

    context = {
        'about':  AboutSection.serialize_for_snippet(required_locale=locale),
        'portfolio': PortfolioSection.serialize_for_snippet(required_locale=locale),
        'facts': FactsSection.serialize_for_snippet(required_locale=locale),
        'skills': json.dumps(SkillsSection.serialize_for_snippet(required_locale=locale)),
        'cv': CvSection.serialize_for_snippet(required_locale=locale),
        'services': ServicesSection.serialize_for_snippet(required_locale=locale),
        'testimonials': TestimonialsSection.serialize_for_snippet(required_locale=locale),
    }

    return render(request, 'index.html', context)


def article(request, article_id):
    req_locale = translation.get_language()
    article_obj = get_object_or_404(Article, locale=req_locale, slug=article_id, is_published='Y')

    context = {
        'breadcrumbs':[
            {
                'text': 'Home',
                'link': '/index.html'
            },
            {
                'text': 'Articles',
                'link': ''
            },
            {
                'text': article_id,
                'link': ''
            },
        ],
        'internal_link': 'articles/',
        'article': article_obj,
    }

    return render(request, 'inner-page.html', context)


def error_400(request, exception):

    context = {
        'error_code': '400 Bad Request',
        'error_text': "Ugh nasty! That was really bad request! :-) Dont do this anymore plz! Be nice and try again another way! :-)"
    }

    return render(request, 'error-page.html', context, status=400)


def error_403(request, exception):

    context = {
        'error_code': '403 Forbidden',
        'error_text': "This is restricted area! You don't allowed to pass here! Ask access from the site owner!"
    }

    return render(request, 'error-page.html', context, status=403)


def error_404(request, exception):

    context = {
        'error_code': '404 Not Found',
        'error_text': "The page you requested doesnt exists on the server. Could you plz choose another one?"
    }

    return render(request, 'error-page.html', context, status=404)


def error_500(request):

    context = {
        'error_code': '500 Internal Server Error',
        'error_text': "Oups! It's not you, it's us! Take our apologise plz, let us fix the problem, would you plz come again a little bit later?"
    }

    return render(request, 'error-page.html', context, status=500)


def error_503(request, exception):

    context = {
        'error_code': '503 Service Temporarily Unavailable',
        'error_text': "Oups! It's not you, it's us! Take our apologise plz, probably the server is overloaded now, would you plz try again a little bit later?"
    }

    return render(request, 'error-page.html', context, status=503)
