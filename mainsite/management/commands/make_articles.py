import os
import datetime
from django.core.management.base import BaseCommand
from django.core.files import File
from amokryshev import settings
from mainsite.models import Article


class Command(BaseCommand):
    help = '''
        test command, should be deleted in the future
    '''


    def handle(self, *args, **options):
        l_data = ['ru', 'en', ]
        article = {
            'title': 'Lorem ipsum dolor sit amet',
            'tags': 'Lorem, ipsum, dolor, sit, amet',
            'slug': 'lorem_ipsum',
            'summary': '''<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sed magna venenatis, placerat nibh id, egestas mauris. Donec vel lorem aliquet, lacinia diam sed, condimentum augue. Praesent augue turpis, rhoncus in iaculis ac, </p>''',
            'picture_name': 'art-hero-bg.jpg',
            'picture': 'img/hero-bg.jpg',
            'content': '''<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sed magna venenatis, placerat nibh id, egestas mauris. Donec vel lorem aliquet, lacinia diam sed, condimentum augue. Praesent augue turpis, rhoncus in iaculis ac, rutrum id turpis. Etiam lacus velit, gravida id urna convallis, laoreet vulputate ex. Proin elementum nulla et mi molestie, a lacinia ipsum molestie. Ut a lacus vitae nibh laoreet venenatis non vel leo. Cras ipsum orci, facilisis sit amet nulla quis, gravida tempor felis. Donec in elit volutpat, placerat diam id, placerat nunc.</p>
<p>Maecenas et metus ac dolor porttitor varius. Duis vitae augue porta, finibus libero sit amet, pellentesque odio. Curabitur in lorem eleifend, venenatis nulla vel, viverra quam. Pellentesque iaculis massa mi, a rutrum justo bibendum at. Donec dignissim urna in nibh condimentum aliquet. Cras fermentum consectetur bibendum. Vestibulum vel eros feugiat, pellentesque libero ac, ultricies arcu. Quisque rutrum sodales nulla, varius porttitor purus tempor a. Maecenas vel justo sed ex laoreet ullamcorper. Ut pharetra non nulla sollicitudin mollis. Suspendisse potenti. Aenean dapibus massa quis dui imperdiet tincidunt eu quis felis. Sed ac sodales purus. Maecenas feugiat lacinia eros facilisis gravida. Sed vitae ligula non ligula dapibus pulvinar non nec lectus. Maecenas consequat placerat nisi, eget vehicula purus commodo consectetur.</p>
<p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam vel mi laoreet quam tempor vestibulum non ac nisl. Etiam rutrum leo mauris, in egestas dui ornare eget. Sed eu turpis rhoncus, porttitor metus in, tincidunt felis. Fusce interdum justo enim, lobortis vulputate dui aliquet quis. Curabitur viverra elementum magna, sit amet vestibulum dolor semper quis. Donec tincidunt diam nec leo sagittis viverra. Donec tincidunt consequat ex vitae faucibus. Praesent mollis malesuada sem a accumsan. Quisque rhoncus ultrices hendrerit. Ut quam ipsum, porttitor vel ultricies convallis, pellentesque eget sapien. Aliquam ultrices lectus ligula, non tempor lectus cursus at. Donec eget massa eget ligula facilisis interdum vel id mauris.</p>
<p>Donec et dolor aliquam, tincidunt quam et, eleifend odio. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed tincidunt massa non posuere tincidunt. Suspendisse massa nunc, aliquet feugiat pretium in, maximus at diam. Nullam non mattis lorem. Fusce at tortor vel elit molestie posuere sit amet vel arcu. Maecenas dignissim turpis elit, nec congue enim iaculis at. Suspendisse sed fringilla est. Proin nec suscipit nisi. Vestibulum gravida auctor ligula nec molestie. Curabitur lacinia justo sed velit congue pharetra. Ut sed elit quis turpis ornare maximus. Vestibulum eros velit, viverra in ligula sed, semper sodales est.</p>
<p>Duis sed justo sem. Vivamus dapibus in nisi nec mattis. Vestibulum justo mi, fermentum nec vulputate tristique, convallis at erat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce vitae suscipit quam. In in ante nisi. Pellentesque gravida vitae metus non ultrices. Proin orci ante, scelerisque id bibendum id, auctor et magna. Suspendisse non hendrerit eros, vel faucibus sem. Quisque viverra scelerisque augue nec condimentum.</p>
<p>Pellentesque tristique maximus libero et fringilla. Etiam vel tortor risus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus tempor ac purus non laoreet. Pellentesque dapibus mi tortor, quis tristique nulla condimentum at. Curabitur mollis lacus eu nulla facilisis aliquam. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam porta dolor arcu, ut semper leo auctor ut. Sed varius urna et ligula aliquet fringilla. Etiam cursus dui quis nisi consequat maximus. Nulla ultricies, lorem eget consequat malesuada, nisl quam malesuada est, at auctor odio lectus et nibh. Nulla molestie in neque at vehicula. Donec nec porta massa. Cras eros orci, dapibus et lacus non, faucibus scelerisque turpis.</p>
<p>Nam a est vitae ex aliquet tristique ac a dui. Suspendisse venenatis erat magna, in tristique urna rutrum gravida. Sed sed lectus ut ex placerat viverra at a tellus. Etiam sit amet iaculis velit. Duis a sollicitudin arcu. Aenean in dolor odio. Ut efficitur fringilla erat non vestibulum. Praesent lacus erat, lacinia id odio id, euismod convallis orci. Morbi tempus justo nec est cursus ultrices. Fusce scelerisque urna in volutpat accumsan. Cras pellentesque eu turpis in vehicula. Integer ultricies fringilla nisi, vitae varius lorem placerat quis. Nunc commodo purus sit amet lacus facilisis ultricies. Nulla eu purus interdum purus elementum maximus at quis diam. Cras feugiat neque et pulvinar dapibus.</p>
<p>Quisque lorem tellus, consequat non ex feugiat, ornare accumsan tellus. In in elit lorem. Aliquam nec volutpat leo. Aliquam eu condimentum lacus, non pulvinar massa. Maecenas a laoreet mi. Nullam in tortor vel ante vehicula commodo et eu purus. Etiam ultrices condimentum mi, ac fermentum arcu malesuada nec. Maecenas ipsum diam, imperdiet finibus justo sit amet, ultrices mattis leo. Duis consequat ornare elementum. Vestibulum ullamcorper enim a neque dictum fringilla. Vivamus quis dui nec tortor dictum fermentum et vitae lorem. Etiam iaculis tellus lacinia tortor hendrerit consectetur. Nunc rhoncus mauris nec arcu malesuada congue.</p>
<p>Sed dignissim tristique ullamcorper. Phasellus porta, orci quis pulvinar commodo, tortor quam fermentum nisi, sit amet semper lorem metus et mi. Maecenas tincidunt pretium consectetur. Fusce porttitor felis erat, vel pharetra magna ultricies a. Aliquam suscipit augue a semper lobortis. Aenean vulputate turpis eu dui pretium aliquet. Cras et ligula porta, malesuada elit et, porttitor ante. Praesent faucibus et sem auctor scelerisque. Aenean vestibulum, nunc id tempor fermentum, leo arcu pulvinar neque, a interdum felis quam a metus. Proin facilisis elementum metus, sit amet consectetur sapien luctus non. Nulla efficitur eu sapien sit amet efficitur.</p>
<p>Donec hendrerit, odio vitae congue interdum, quam erat placerat odio, et dictum orci libero eu elit. Praesent aliquam, tortor a pellentesque ornare, lectus lacus mattis lacus, fringilla ultricies lectus lectus maximus erat. Morbi nec arcu condimentum, sodales ipsum in, consequat leo. Pellentesque bibendum libero sit amet mollis placerat. Nulla blandit et odio pulvinar varius. Donec vitae ultricies metus. Sed ac ante dignissim, congue arcu ut, volutpat tortor. Aenean eu sem id nisi interdum fringilla ac eget justo. Nam euismod, mi vel pretium varius, ante dolor fermentum ipsum, ullamcorper fringilla odio lorem nec ipsum. Pellentesque non posuere mauris. Quisque varius ipsum non mi rutrum, nec porta leo porta. Aenean faucibus venenatis magna, sed eleifend nulla molestie ac. Mauris non rutrum est, at auctor odio.</p>''',
            'related': [],
            'pub_date': datetime.datetime(2021, 2, 5, 12, 30, 10),
            'author': 'AMokryshev',
            'author_link': 'https://habr.com/ru/users/amokryshev/',
            'source': 'habr.com',
            'source_link': 'https://habr.com',
        }

        for lang in l_data:
            articles = {}
            for num in range(4):
                pic = File(open(os.path.join(settings.STATICFILES_DIRS[0], article['picture'] ), "rb"))
                art = Article()
                art.locale = lang
                art.title = article['title']
                art.tags = article['tags']
                art.slug = 'temp'
                art.summary = article['summary']
                art.content = article['content']
                art.pub_date = article['pub_date']
                art.author = article['author']
                art.author_link = article['author_link']
                art.source = article['source']
                art.source_link = article['source_link']
                art.picture.save(article['picture_name'], pic, save=True)
                art.slug = '{0}_{1}'.format(article['slug'], art.id)
                for item in articles:
                    art.related.add(item)
                art.save()

                articles.update({art.id: art})
