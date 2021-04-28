from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SocialLink, MainMenuPoint, AboutSection, AboutSectionFeature, \
    PortfolioSection, PortfolioSectionLink, FactsSection, FactsSectionItem, \
    SkillsSection, CvSection, CvSectionItem, CvSectionItemDetail, ServicesSection, \
    ServicesSectionDetail, TestimonialsSection, TestimonialsSectionDetail, Article


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('summary', 'content',)


class TestimonialsSectionDetailInline(admin.TabularInline):
    model = TestimonialsSectionDetail


@admin.register(TestimonialsSection)
class TestimonialsSectionAdmin(admin.ModelAdmin):
    inlines = [
        TestimonialsSectionDetailInline,
    ]


class ServicesSectionDetailInline(admin.TabularInline):
    model = ServicesSectionDetail


@admin.register(ServicesSection)
class ServicesSectionAdmin(admin.ModelAdmin):
    inlines = [
        ServicesSectionDetailInline,
    ]


class CvSectionItemDetailInline(admin.TabularInline):
    model = CvSectionItemDetail


@admin.register(CvSectionItem)
class CvSectionItemAdmin(admin.ModelAdmin):
    inlines = [
        CvSectionItemDetailInline,
    ]


class FactsSectionItemInline(admin.TabularInline):
    model = FactsSectionItem


@admin.register(FactsSection)
class FactsSectionAdmin(admin.ModelAdmin):
    inlines = [
        FactsSectionItemInline,
    ]


class PortfolioSectionLinkInline(admin.TabularInline):
    model = PortfolioSectionLink


@admin.register(PortfolioSection)
class PortfolioSectionAdmin(admin.ModelAdmin):
    inlines = [
        PortfolioSectionLinkInline,
    ]


class AboutSectionFeatureInline(admin.TabularInline):
    model = AboutSectionFeature


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    inlines = [
        AboutSectionFeatureInline,
    ]


admin.site.register(SocialLink)
admin.site.register(MainMenuPoint)
admin.site.register(SkillsSection)
admin.site.register(CvSection)
