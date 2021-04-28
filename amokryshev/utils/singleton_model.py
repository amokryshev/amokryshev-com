from django.db import models
from django.contrib import admin


class SingletonModel(models.Model):
    """This is the abstract ancestor for all models
    that should have a strictly single record in the database"""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class SingletonAdm(admin.ModelAdmin):
    """The dummy for django admin interface of SingletonModel"""

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
