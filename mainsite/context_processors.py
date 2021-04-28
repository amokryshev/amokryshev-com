from .models import SocialLink, MainMenuPoint


def load_settings(request):
    """The processor for implements social_links and menu options in the context of every page on the site"""

    return {
        'social_links': SocialLink.objects.all(),
        'main_menu': MainMenuPoint.objects.all(),
    }
