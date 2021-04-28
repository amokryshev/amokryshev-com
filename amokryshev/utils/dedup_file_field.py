import os
from amokryshev import settings
from django.db.models.fields.files import FieldFile, FileField


class DeduplicatedFieldFile(FieldFile):
    """The implementation of simple deduplication functional while saving the file,
    I couldn't find deduplication feature in Django FileField and didn't want to install
    additional batteries from third party developers, because the functional, required by me,
    too easy, so I wrote a little crutch"""

    def save(self, name, content, save=True):

        if os.path.isfile(os.path.join(settings.MEDIA_ROOT, self.field.upload_to, name)):
            self.name = os.path.join(self.field.upload_to, name)
            setattr(self.instance, self.field.name, self.name)
            self._committed = True

            if save:
                self.instance.save()
        else:
            super().save(name, content)


class FileFieldDedupByName(FileField):
    """The implementation of simple deduplication functional while saving the file,
        I couldn't find deduplication feature in Django FileField and didn't want to install
        additional batteries from third party developers, because the functional, required by me,
        too easy, so I wrote a little crutch"""

    attr_class = DeduplicatedFieldFile
