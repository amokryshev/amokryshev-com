import os
from django import template
from amokryshev import settings

register = template.Library()


@register.filter()
def split_tags(tags):
    """The tag for splits article tags from string divided by comma to list."""
    return str.split(tags, ',')


@register.simple_tag
def years_verbose(years):
    """The tag for right wordform's substitution depends on count of years.
    Takes values between (0, 100)."""

    flag = True
    residual = years

    while flag:
        flag = False
        if residual == 1:
            answer = 'год'
        elif residual in range(2, 5):
            answer = 'года'
        elif residual in range(5, 21):
            answer = 'лет'
        else:
            flag = True
            residual %= 10

    return answer


@register.simple_tag
def cv_tiered_list(list):
    """The tag is hiding recursive loop for generation tiered list of CV options,
    it makes template code more readable."""

    answer = ""
    for item in list:
        point = item['text']
        if item['href']:
            point = '<a href="{0}">{1}<span class="bx bx-link"/></a>'.format(item['href'], point)
        if len(item['subdetails']) > 0:
            point += cv_tiered_list(item['subdetails'])
        answer += "<li>{}</li>".format(point)
    if answer:
        answer = '<ul>{}</ul>'.format(answer)
    return answer


@register.simple_tag
def picture(image):
    """The tag is hiding location of image storage, it prevent hard coding of '/img/' suffix and makes code DRY"""

    return os.path.join(settings.STATIC_URL, 'img', image)


@register.simple_tag
def media(image):
    """The tag is hiding location of image storage, it prevent hard coding of '/img/' suffix and makes code DRY"""

    return os.path.join(settings.MEDIA_URL, image)
