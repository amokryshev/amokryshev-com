import os
import json
import copy
from unittest import skip
from django.core.files import File
from django.test import TestCase
from amokryshev import settings
from amokryshev.utils import AnimatedPageTestScenario, localised_classmethod, main_menu, social_links, skills_section,\
    about_section_ru, about_section_en, portfolio_section_ru, portfolio_section_en, facts_section_ru, facts_section_en, \
    cv_section_ru, cv_section_en, services_section_ru, services_section_en, testimonials_section_ru, \
    testimonials_section_en, pers_utf_hash_standard, FunctionalAnimatedPageTest, pers_utf_hash
from amokryshev.utils.dedup_file_field import DeduplicatedFieldFile
from .models import AboutSection,  PortfolioSection, FactsSection, CvSection, ServicesSection, TestimonialsSection

fixture_name = 'initial-data.json'


class DeduplicatedFieldFileTest(TestCase):
    fixtures = [fixture_name]

    def test_deduplicated_field_file(self):

        self.assertTrue(isinstance(AboutSection.objects.get(id=1).picture, DeduplicatedFieldFile))


        pic = File(open(os.path.join(settings.STATICFILES_DIRS[0], about_section_ru['picture_path']), "rb"))

        test_model_one = AboutSection(locale = 'en')
        test_model_one.picture.save(about_section_ru['picture_name'], pic)

        test_model_two = AboutSection(locale='en')
        test_model_two.picture.save(about_section_ru['picture_name'], pic)

        self.assertEqual(test_model_one.picture.path, test_model_two.picture.path)


class LocalizedModelTest(TestCase):
    fixtures = [fixture_name]

    def test_localised_classmethod(self):

        @localised_classmethod
        def test_localized_func(cls, required_locale):
            return True

        self.assertTrue(test_localized_func(self.__class__, 'en'))
        self.assertTrue(test_localized_func(self.__class__, 'ru'))
        self.assertRaises(ValueError, test_localized_func, cls=self.__class__, required_locale='de')

    def test_localized_model(self):
        self.assertTrue(hasattr(AboutSection.objects.get(id=1), 'locale'))


class SingletonModelTest(TestCase):
    """TODO: Should be implemented if SingletonModel would be used"""
    pass


class CustomModelsSerializersTest(TestCase):
    fixtures = [fixture_name]

    def pic_path_ellim(self, data):

        path_flag = False
        name_flag = False

        for element in data:

            if element == 'picture_path':
                path_flag = True
            if element == 'picture_name':
                name_flag = True

            if isinstance(element, dict) or isinstance(element, list):
                elem = element
            else:
                elem = data[element]

            if isinstance(elem, dict) or isinstance(elem, list):
                self.pic_path_ellim(elem)

        if path_flag:
            data.pop('picture_path')

        if name_flag:
            data.pop('picture_name')

        return data

    def test_about_section_serializer(self):
        self.assertEqual(AboutSection.serialize_for_snippet('en'),
                         self.pic_path_ellim(copy.deepcopy(about_section_en)))
        self.assertEqual(AboutSection.serialize_for_snippet('ru'),
                         self.pic_path_ellim(copy.deepcopy(about_section_ru)))

    def test_portfolio_section_serializer(self):
        self.assertEqual(PortfolioSection.serialize_for_snippet('en'),
                         self.pic_path_ellim(copy.deepcopy(portfolio_section_en)))
        self.assertEqual(PortfolioSection.serialize_for_snippet('ru'),
                         self.pic_path_ellim(copy.deepcopy(portfolio_section_ru)))

    def test_facts_section_serializer(self):
        self.assertEqual(FactsSection.serialize_for_snippet('en'), facts_section_en)
        self.assertEqual(FactsSection.serialize_for_snippet('ru'), facts_section_ru)

    def test_cv_section_serializer(self):
        self.assertEqual(CvSection.serialize_for_snippet('en'), cv_section_en)
        self.assertEqual(CvSection.serialize_for_snippet('ru'), cv_section_ru)

    def test_services_section_serializer(self):
        self.assertEqual(ServicesSection.serialize_for_snippet('en'), services_section_en)
        self.assertEqual(ServicesSection.serialize_for_snippet('ru'), services_section_ru)

    def test_testimonials_section_serializer(self):
        self.assertEqual(TestimonialsSection.serialize_for_snippet('en'),
                         self.pic_path_ellim(copy.deepcopy(testimonials_section_en)))
        self.assertEqual(TestimonialsSection.serialize_for_snippet('ru'),
                         self.pic_path_ellim(copy.deepcopy(testimonials_section_ru)))


class TestForAnimatedPagesToolTest(TestCase):
    def test_pers_utf_hash(self):
        self.assertEqual(pers_utf_hash(pers_utf_hash_standard['test_string']), pers_utf_hash_standard['hash'])

@skip("Too heavy for run with main test suite")
class IndexPageTest(FunctionalAnimatedPageTest):
    fixtures = [fixture_name]
    references = ['/en/', '/ru/', ]
    page_parts = json.loads(open('mainsite/fixtures/index_page_snapshot.json').read())
    snapshots_density = 0.5
    snapshots_count = 120

    test_index_page = AnimatedPageTestScenario()

@skip("Too heavy for run with main test suite")
class ArticlePageTest(FunctionalAnimatedPageTest):
    fixtures = [fixture_name]
    references = ['/en/articles/lorem_ipsum_8/', '/ru/articles/lorem_ipsum_4/', ]
    page_parts = json.loads(open('mainsite/fixtures/article_page_snapshot.json').read())
    snapshots_density = 0.5
    snapshots_count = 120

    test_index_page = AnimatedPageTestScenario()
