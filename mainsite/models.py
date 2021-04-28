from django.db import models
from django.core.exceptions import ValidationError
from amokryshev.utils import QueryResultIsEmpty, IS_PUBLISHED, CONTENT_LOCALE, \
    localised_classmethod, LocalizedModel, FileFieldDedupByName


class Article(LocalizedModel):
    title = models.CharField('Title', max_length=250)
    tags = models.CharField('Tags', max_length=120, blank=True)
    slug = models.CharField('Slug', max_length=160)
    summary = models.CharField('Summary', max_length=250, blank=True)
    picture = FileFieldDedupByName('Avatar_photo', upload_to='portfolio')
    content = models.TextField('Content')
    related = models.ManyToManyField("self", blank=True)
    is_published = models.CharField('Is published', max_length=1, default='Y', choices=IS_PUBLISHED)
    pub_date = models.DateTimeField('Published', auto_now_add=True)
    author = models.CharField('Author', max_length=160, blank=True)
    author_link = models.CharField('Author link', max_length=250, blank=True)
    source = models.CharField('Source', max_length=160, blank=True)
    source_link = models.CharField('Source link', max_length=250, blank=True)


class TestimonialsSection(LocalizedModel):
    intro = models.TextField('Introduction')

    @classmethod
    @localised_classmethod
    def serialize_for_snippet(cls, required_locale):

        source = cls.objects.filter(locale=required_locale)[0]

        if source is None:
            raise QueryResultIsEmpty('There havent got testimonials data for the required_locale!')

        target = {
            'intro': source.intro,
            'details': []
        }

        for detail in TestimonialsSectionDetail.objects.filter(header=source).order_by('pos'):
            target['details'].append(
                {
                    'text': detail.text,
                    'picture': detail.picture.name,
                    'person': detail.person,
                    'position': detail.position
                }
            )

        if len(target['details']) == 0:
            raise QueryResultIsEmpty('There havent got testimonials details for the required_locale!')

        return target


class TestimonialsSectionDetail(models.Model):
    header = models.ForeignKey(TestimonialsSection, models.SET_NULL, blank=True, null=True)
    pos = models.IntegerField('Position on page')
    text = models.TextField('Description')
    picture = FileFieldDedupByName('Persons photo', upload_to='testimonials')
    person = models.CharField('Person', max_length=200)
    position = models.CharField('Persons position', max_length=100, blank=True)


class ServicesSection(LocalizedModel):
    intro = models.TextField('Introduction')

    @classmethod
    @localised_classmethod
    def serialize_for_snippet(cls, required_locale):

        source = cls.objects.filter(locale=required_locale)[0]

        if source is None:
            raise QueryResultIsEmpty('There havent got services data for the required_locale!')

        target = {
            'intro': source.intro,
            'details': []
        }

        for detail in ServicesSectionDetail.objects.filter(header=source).order_by('pos'):
            target['details'].append(
                {
                    'title': detail.title,
                    'icon': detail.icon,
                    'href': detail.href,
                    'description': detail.description
                }
            )

        if len(target['details']) == 0:
            raise QueryResultIsEmpty('There havent got services details for the required_locale!')

        return target


class ServicesSectionDetail(models.Model):
    header = models.ForeignKey(ServicesSection, models.SET_NULL, blank=True, null=True)
    pos = models.IntegerField('Position on page')
    title = models.CharField('Service title', max_length=200)
    icon = models.CharField("CSS cls icofont", max_length=30)
    href = models.CharField('External link', max_length=200, blank=True)
    description = models.TextField('Description')


class CvSection(LocalizedModel):
    pos = models.IntegerField('Position on page')
    chapter = models.CharField("Chapter", max_length=30)

    @classmethod
    @localised_classmethod
    def serialize_for_snippet(cls, required_locale):

        target = []

        chapters = cls.objects.filter(locale = required_locale)

        if len(chapters) == 0:
            raise QueryResultIsEmpty('There havent got CV chapters data for the required_locale!')

        for chapter in cls.objects.filter(locale = required_locale):

            source = {
                'pos': chapter.pos,
                'chapter': chapter.chapter,
                'items': []
            }

            for item in CvSectionItem.objects.filter(header = chapter):
                source['items'].append({
                    'pos': item.pos,
                    'title': item.title,
                    'period': item.period,
                    'description': item.description,
                    'details': item.get_details()
                })

            if len(source['items']) == 0:
                raise QueryResultIsEmpty('There havent got CV items data for the required_locale!')

            target.append(source)

        return target


class CvSectionItem(models.Model):
    header = models.ForeignKey(CvSection, models.SET_NULL, blank=True, null=True)
    pos = models.IntegerField('Position on page')
    title = models.CharField('Position title', max_length=200)
    period = models.CharField('Time period', max_length=200)
    description = models.CharField('Description', max_length=200)

    def get_details(self):

        target = []

        for detail in CvSectionItemDetail.objects.filter(header = self).order_by('pos'):
            target.append(CvSectionItemDetail.get_subdetails_req(detail))

        return target


class CvSectionItemDetail(models.Model):
    header = models.ForeignKey(CvSectionItem, models.SET_NULL, blank=True, null=True)
    parent = models.ForeignKey('self', models.SET_NULL, blank=True, null=True)
    pos = models.IntegerField('Position on page')
    text = models.CharField('The item name', max_length=250)
    href = models.CharField('External link', max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.header is not None and self.parent is not None:
            raise ValidationError('CvSectionItemDetail object should contain only ' +
                                  'one of two parameters: header or parent!')
        super().save(self, *args, **kwargs)

    @classmethod
    def get_subdetails_req(cls, detail):
        target = {
            'text': detail.text,
            'href': detail.href,
            'subdetails':[]
        }

        for subdetail in cls.objects.filter(parent = detail).order_by('pos'):
            target['subdetails'].append(cls.get_subdetails_req(subdetail))

        return target


class SkillsSection(models.Model):
    tag = models.CharField("Skill tag", max_length=50)
    count = models.IntegerField('Count of votes')

    @classmethod
    def serialize_for_snippet(cls, required_locale):
        #TODO: Shall be localised in the future
        target = []

        for item in cls.objects.all():
            target.append(
                {'tag': item.tag, 'count': item.count}
            )

        if len(target) == 0:
            raise QueryResultIsEmpty('There havent got Skills data for the required_locale!')

        return target


class FactsSection(LocalizedModel):
    intro = models.TextField('Introduction')
    finale = models.TextField('Inference')

    @classmethod
    @localised_classmethod
    def serialize_for_snippet(cls, required_locale):
        source = cls.objects.filter(locale=required_locale)[0]

        if source is None:
            raise QueryResultIsEmpty('There havent got Facts data for the required_locale!')

        target = {
            'intro': source.intro,
            'finale': source.finale,
            'items': []
        }

        for item in FactsSectionItem.objects.filter(header=source):
            target['items'].append(
                {
                    'icon': item.icon,
                    'years': item.years,
                    'branch': item.branch,
                    'details': item.details
                }
            )

        if len(target['items']) == 0:
            raise QueryResultIsEmpty('There havent got Facts details data for the required_locale!')

        return target


class FactsSectionItem(models.Model):
    header = models.ForeignKey(FactsSection, models.SET_NULL, blank=True, null=True)
    pos = models.IntegerField('Position on page')
    icon = models.CharField("CSS cls icofont", max_length=30)
    years = models.IntegerField('Years count')
    branch = models.CharField('Sector', max_length=50)
    details = models.CharField('Extra info', max_length=200)


class PortfolioSection(LocalizedModel):
    LIST_OF_CHAPTERS = (
        ('filter-app', 'Application'),
        ('filter-article', 'Article'),
        ('filter-other', 'Other'),
    )
    picture = FileFieldDedupByName('Avatar_photo', upload_to='portfolio')
    filter = models.CharField('Chapter', max_length=14, default='filter-article',
                                   choices=LIST_OF_CHAPTERS)
    is_published = models.CharField('Is published', max_length=1, default='Y',
                                   choices=IS_PUBLISHED)
    pub_date = models.DateTimeField('Published', auto_now_add=True)

    @classmethod
    @localised_classmethod
    def serialize_for_snippet(cls, required_locale):
        target = []

        for item in cls.objects.filter(locale = required_locale, is_published='Y').order_by('pub_date'):

            source = {
                'filter': item.filter,
                'picture': item.picture.name,
                'links': []
            }

            for link in PortfolioSectionLink.objects.filter(header = item):
                source['links'].append(
                    {'tip': link.tip, 'href': link.href, 'icon': link.icon}
                )

            if len(source['links']) == 0:
                raise QueryResultIsEmpty('There havent got Portfolio links data for the required_locale!')

            target.append(source)

        if len(target) == 0:
            raise QueryResultIsEmpty('There havent got Portfolio data for the required_locale!')



        return target


class PortfolioSectionLink(models.Model):
    header = models.ForeignKey(PortfolioSection, models.SET_NULL, blank=True, null=True)
    tip = models.CharField('On hover text tip', max_length=50)
    icon = models.CharField("CSS cls icofont", max_length=30)
    view = models.CharField("Name of the view", max_length=50, blank=True)
    anchor = models.CharField("Anchor on the page", max_length=50, blank=True)
    href = models.CharField('External link', max_length=200, blank=True)


class AboutSection(LocalizedModel):
    picture = FileFieldDedupByName('Main photo')
    intro = models.TextField('Introduction')
    role = models.CharField('Roles & Positions', max_length=200)
    sub_role = models.CharField('Roles explanation', max_length=200)
    message = models.TextField('Inference')

    @classmethod
    @localised_classmethod
    def serialize_for_snippet(cls, required_locale):
        source = cls.objects.filter(locale=required_locale)[0]

        if source is None:
            raise QueryResultIsEmpty('There havent got About data for the required_locale!')

        target = {
            'picture': source.picture.name,
            'intro': source.intro,
            'role': source.role,
            'sub_role': source.sub_role,
            'message': source.message,
            'features': [[],[]]
        }

        mapping = {'F': 0, 'S': 1}

        for feature in AboutSectionFeature.objects.filter(header = source):
            target['features'][mapping[feature.list_num]].append(
                {'key': feature.key, 'value': feature.value, 'href': feature.href}
            )

        if len(target['features'][0]) == 0 or len(target['features'][1]) == 0:
            raise QueryResultIsEmpty('There havent got About features data for the required_locale!')

        return target


class AboutSectionFeature(models.Model):
    LIST_OF_FEATURES = (
        ('F', 'First'),
        ('S', 'Second'),
    )
    list_num = models.CharField('Number of list', max_length=1, choices=LIST_OF_FEATURES)
    key = models.CharField('Name of the point', max_length=20)
    value = models.CharField('Text of the point', max_length=200)
    href = models.CharField('Link of the point', max_length=200, blank=True)
    header = models.ForeignKey(AboutSection, models.SET_NULL, blank=True, null=True)


class SocialLink(models.Model):
    style = models.CharField("CSS cls of the link",max_length=30)
    href = models.CharField("the Link", max_length=200)
    icon = models.CharField("CSS cls icofont", max_length=30)

    def __str__(self):
        return 'style: {0} , href: {1}, icon: {2}\n'.format(self.style, self.href, self.icon)


class MainMenuPoint(models.Model):
    pos = models.IntegerField('Position on page')
    is_active = models.BooleanField(default=False)
    view = models.CharField("Name of the view", max_length=50)
    anchor = models.CharField("Anchor on the page", max_length=50)
    icon = models.CharField("CSS cls icofont", max_length=30)
    text = models.CharField("The item name", max_length=50)

    def __str__(self):
        return 'pos: {0} , is_active: {1}, view: {2}, ' \
               'anchor: {3}, icon: {4}, text: {5}\n' \
            .format(self.pos, self.is_active, self.view, self.anchor, self.icon, self.text)
