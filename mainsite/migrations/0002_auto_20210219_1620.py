# Generated by Django 3.1.5 on 2021-02-19 13:20
import os
from django.core.files import File
from django.db import migrations
from django.contrib.auth.models import User
from amokryshev import settings
from amokryshev.utils import main_menu, social_links, skills_section, about_section_ru, about_section_en, \
    portfolio_section_ru, portfolio_section_en, facts_section_ru, facts_section_en, cv_section_ru, cv_section_en,\
    services_section_ru, services_section_en, testimonials_section_ru, testimonials_section_en
from mainsite.models import SocialLink, MainMenuPoint, AboutSection, AboutSectionFeature, \
    PortfolioSection, PortfolioSectionLink, FactsSection, FactsSectionItem, \
    SkillsSection, CvSection, CvSectionItem, CvSectionItemDetail, ServicesSection, \
    ServicesSectionDetail, TestimonialsSection, TestimonialsSectionDetail


def data_initial(apps, schema_editor):

    ### Initial data for main  menu ###
    for num, item in enumerate(main_menu):
        MainMenuPoint(pos=num, is_active=item['is_active'], view=item['view'], anchor=item['anchor'],
                      icon=item['icon'], text=item['text']).save()


    ### Initial data for social links block ###
    for item in social_links:
        SocialLink(style=item['style_cls'], href=item['href'], icon=item['icon']).save()

    ### Initial data for skills ###
    for item in skills_section:
        SkillsSection(tag=item['tag'], count=item['count']).save()


    l_data = {
        'ru': {
            'about_section': about_section_ru,
            'portfolio_section': portfolio_section_ru,
            'facts_section': facts_section_ru,
            'cv_section': cv_section_ru,
            'services_section': services_section_ru,
            'testimonials_section': testimonials_section_ru,
        },
        'en': {
            'about_section': about_section_en,
            'portfolio_section': portfolio_section_en,
            'facts_section': facts_section_en,
            'cv_section': cv_section_en,
            'services_section': services_section_en,
            'testimonials_section': testimonials_section_en,
        },
    }

    superuser = User.objects.create_superuser(
        username=settings.env('DJ_AN'),
        email=settings.env('DJ_AE'),
        password=settings.env('DJ_AP')
    )
    superuser.save()

    for lang in l_data:

        ### About section initial data ###
        pic = File(open(os.path.join(settings.STATICFILES_DIRS[0], l_data[lang]['about_section']['picture_path']), "rb"))
        header = AboutSection()
        header.locale = lang
        header.picture.save(l_data[lang]['about_section']['picture_name'], pic)
        header.intro = l_data[lang]['about_section']['intro']
        header.role = l_data[lang]['about_section']['role']
        header.sub_role = l_data[lang]['about_section']['sub_role']
        header.message = l_data[lang]['about_section']['message']
        header.save()

        for item in l_data[lang]['about_section']['features'][0]:
            AboutSectionFeature(header=header, list_num='F', key=item['key'], value=item['value'],
                                href=item['href']).save()

        for item in l_data[lang]['about_section']['features'][1]:
            AboutSectionFeature(header=header, list_num='S', key=item['key'], value=item['value'],
                                href=item['href']).save()


        ### Portfolio section initial data ###
        for article in l_data[lang]['portfolio_section']:
            pic = File(open(os.path.join(settings.STATICFILES_DIRS[0],
                                         article['picture_path']), "rb"))

            header = PortfolioSection()
            header.locale = lang
            header.picture.save(article['picture_name'], pic, save=True)
            header.filter = article['filter']
            header.save()

            for link in article['links']:
                PortfolioSectionLink(header=header, tip=link['tip'],
                                     href=link['href'], icon=link['icon']).save()


        ### Facts section initial data ###
        header = FactsSection()
        header.locale = lang
        header.intro = l_data[lang]['facts_section']['intro']
        header.finale = l_data[lang]['facts_section']['finale']
        header.save()

        for num, fact in enumerate(l_data[lang]['facts_section']['items']):
            FactsSectionItem(header=header, pos=num, icon=fact['icon'], years=fact['years'],
                             branch=fact['branch'], details = fact['details']).save()


        ### CV section initial data ###
        for chap_num, section in enumerate(l_data[lang]['cv_section']):
            header_of_items = CvSection(locale=lang, pos=chap_num, chapter=section['chapter'])
            header_of_items.save()

            for item_num, item in enumerate(section['items']):
                header_of_details = CvSectionItem(header=header_of_items, pos=item_num,
                                                  title=item['title'], period=item['period'],
                                                  description=item['description'])
                header_of_details.save()

                for det_num, detail in enumerate(item['details']):
                    parent_of_details = CvSectionItemDetail(header=header_of_details, pos=det_num,
                                                            text=detail['text'], href=detail['href'])
                    parent_of_details.save()

                    for sub_num, subdetail in enumerate(detail['subdetails']):
                        CvSectionItemDetail(parent=parent_of_details, pos=sub_num, text=subdetail['text'],
                                            href=subdetail['href']).save()

        ### Services section initial data ###
        header = ServicesSection(locale=lang, intro=l_data[lang]['services_section']['intro'])
        header.save()

        for pos, service in enumerate(l_data[lang]['services_section']['details']):
            ServicesSectionDetail(header=header, pos=pos, title=service['title'], href=service['href'],
                                  icon=service['icon'],
                                  description=service['description']).save()


        ### Testimonials section initial data ###
        header = TestimonialsSection(locale = lang,
                                     intro = l_data[lang]['testimonials_section']['intro'])
        header.save()

        for num, detail in enumerate(l_data[lang]['testimonials_section']['details']):
            pic = File(open(os.path.join(settings.STATICFILES_DIRS[0],
                                         detail['picture_path']), "rb"))

            testimonial = TestimonialsSectionDetail()
            testimonial.pos = num
            testimonial.picture.save(detail['picture_name'], pic, save=True)
            testimonial.header = header
            testimonial.text = detail['text']
            testimonial.person = detail['person']
            testimonial.position = detail['position']
            testimonial.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(data_initial),
    ]
