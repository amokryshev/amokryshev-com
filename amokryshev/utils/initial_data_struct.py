import re

remove_mspaces = re.compile("\s\s+")

pers_utf_hash_standard = {
    'test_string': 'Lorem ipsum dolor sit amet',
    'hash': 338496524657487844672953225842489206917
}

main_menu = [
    {'is_active': True, 'view': 'index', 'anchor': '#hero', 'icon': 'bx bx-home', 'text': 'Начало'},
    {'is_active': False, 'view': 'index', 'anchor': '#about', 'icon': 'bx bx-user', 'text': 'Обо мне'},
    {'is_active': False, 'view': 'index', 'anchor': '#portfolio', 'icon': 'bx bx-book-content', 'text': 'Блог'},
    {'is_active': False, 'view': 'index', 'anchor': '#services', 'icon': 'bx bx-server', 'text': 'Услуги'},
    {'is_active': False, 'view': 'index', 'anchor': '#facts', 'icon': 'bx bx-file-blank', 'text': 'Резюме'},
]

social_links = [
    {'style_cls': 'vc.ru', 'href': 'https://vc.ru/u/100172-alexander-mokryshev', 'icon': 'bx vc-icon'},
    {'style_cls': 'cnews.ru', 'href': 'https://club.cnews.ru/aleksandr_mokryshev', 'icon': 'bx cnews-icon'},
    {'style_cls': 'habr.ru', 'href': 'https://habr.com/ru/users/amokryshev/', 'icon': 'bx habr-icon'},
    {'style_cls': 'Telegram', 'href': 'https://telegram.im/@Amokryshev', 'icon': 'bx bxl-telegram'},
    {'style_cls': 'linkedin', 'href': 'https://www.linkedin.com/in/alexander-mokryshev-72b03a20/', 'icon': 'bx bxl-linkedin'},
]

skills_section = [
    {"tag": "Software Project Management", "count": "40"},
    {"tag": "Business Analysis", "count": "23"},
    {"tag": "IT Service Management", "count": "37"},
    {"tag": "Pre-sales", "count": "22"},
    {"tag": "Scrum", "count": "12"},
    {"tag": "Requirements Analysis", "count": "27"},
    {"tag": "Integration and ETL", "count": "18"},
    {"tag": "SAP", "count": "35"},
    {"tag": "Oracle Hyperion", "count": "8"},
    {"tag": "XML", "count": "6"},
    {"tag": "DWH and OLAP", "count": "10"},
    {"tag": "sql", "count": "8"},
    {"tag": "Python", "count": "30"},
    {"tag": "JavaScript", "count": "15"},
    {"tag": "html", "count": "8"},
    {"tag": "CSS", "count": "5"},
    {"tag": "Docker", "count": "15"},
    {"tag": "Travis-CI", "count": "15"},
    {"tag": "Google Kubernetes Engine", "count": "15"},
    {"tag": "Google Cloud Storage", "count": "15"},
    {"tag": "Django", "count": "20"},
    {"tag": "r", "count": "3"},
    {"tag": "node.js", "count": "5"},
    {"tag": "webpack", "count": "5"},
    {"tag": "json", "count": "10"},
    {"tag": "PostgreSQL", "count": "5"},
    {"tag": "mongodb", "count": "3"},
    {"tag": "Сontinuous Integration", "count": "10"},
    {"tag": "Сontinuous Deployment", "count": "10"},
    {"tag": "Release Management", "count": "36"},
    {"tag": "git-flow", "count": "15"},
    {"tag": "Quality Assurance", "count": "30"},
    {"tag": "DevOps", "count": "20"},
    {"tag": "C", "count": "3"},
    {"tag": "Excel VBA", "count": "20"},
    {"tag": "Management accounting", "count": "20"},
    {"tag": "Budgeting & IFRS Consolidation", "count": "15"},
    {"tag": "linux", "count": "5"},
    {"tag": "Econometrics", "count": "20"},
    {"tag": "Business math", "count": "11"},
    {"tag": "Celery", "count": "5"},
    {"tag": "Redis", "count": "5"},
    {"tag": "nginx", "count": "3"},
    {"tag": "Jira", "count": "25"},
    {"tag": "Confluence", "count": "6"},
    {"tag": "Jenkins", "count": "3"},
    {"tag": "SAP SD/MM", "count": "15"},
    {"tag": "SAP EWM", "count": "15"},
    {"tag": "SAP PI", "count": "10"},
    {"tag": "SAP BW", "count": "15"},
    {"tag": "UX design", "count": "10"},
    {"tag": "System Analysis", "count": "15"},
    {"tag": "Bootstrap", "count": "10"},
    {"tag": "Statistics", "count": "10"},
]

about_section_ru = {
    'picture': 'profile-img.png',
    'picture_name': 'profile-img.png',
    'picture_path': 'initial_media_uploads/profile-img.png',
    'intro': 'Более 8-ми лет управляю проектами и портфелями проектов, бюджетом до 2-х млн долларов США и численностью команды до 50 консультантов SAP и до 30 web-разработчиков. Имею практический опыт проектирования и реализации комплексных ИТ-систем для крупнейших корпораций РФ от стадии идеи до продуктивной эксплуатации, с соблюдением сроков и бюджета. Успешно применяю как Waterfall, так и Agile подходы, разбираюсь в технологиях и с удовольствием работаю руками сам. Сертифицированный PMP и ITIL.',
    'role': 'Product&nbsp;owner &amp; IT&nbsp;Portfolio&nbsp;manager &amp; SAP&nbsp;Project&nbsp;director',
    'sub_role': 'Project Management Professional (PMP® Number: 1957517) &amp; ITIL ITFO (EXIN 2096110_2008553)',
    'message': 'Открыт к профессиональному сотрудничеству в рамках моей специализации и опыта в разных форматах.',
    'features': [
        [
            {'key': 'Возраст', 'value': '34 года', 'href': ''},
            {'key': 'Опыт работы', 'value': '15 лет', 'href': ''},
            {'key': 'Образование', 'value': 'МГСУ, Инженер АСОИУ, Специалист (Магистр)', 'href': ''},
            {'key': 'Локация', 'value': 'Москва', 'href': ''},
            {'key': 'E-mail', 'value': 'amokr@mail.ru', 'href': ''},
            {'key': 'Телефон', 'value': '+7 (926) 608-52-65', 'href': ''},
        ],
        [
            {'key': 'LinkedIn', 'value': 'Alexander Mokryshev',
             'href': 'https://www.linkedin.com/in/alexander-mokryshev-72b03a20/'},
            {'key': 'HH.ru', 'value': 'Александр Мокрышев',
             'href': 'https://hh.ru/resume/91028332ff018a7d100039ed1f61476344394b'},
            {'key': 'Github.com', 'value': 'amokryshev', 'href': 'https://github.com/amokryshev'},
            {'key': 'Habr.com', 'value': 'amokryshev', 'href': 'https://habr.com/ru/users/amokryshev/'},
            {'key': 'geekjob.ru', 'value': 'amokryshev', 'href': 'https://geekjob.ru/'},
        ],
    ],
}

about_section_en = {
    'picture': 'profile-img.png',
    'picture_name': 'profile-img.png',
    'picture_path': 'initial_media_uploads/profile-img.png',
    'intro': 'For more than 8 years I have been managing projects and project portfolios, with a budget of up to USD 2 million and a team of up to 50 SAP consultants and up to 30 web developers. I have practical experience in the design and implementation of complex IT systems for the largest corporations of the Russian Federation from the idea stage to productive operation, in compliance with deadlines and budget. Successfully apply both Waterfall and Agile approaches, understand technologies and enjoy working with my own hands. PMP and ITIL certified.',
    'role': 'Product&nbsp;owner &amp; IT&nbsp;Portfolio&nbsp;manager &amp; SAP&nbsp;Project&nbsp;director',
    'sub_role': 'Project Management Professional (PMP® Number: 1957517) &amp; ITIL ITFO (EXIN 2096110_2008553)',
    'message': 'Open to professional cooperation within my specialty and experience in various forms.',
    'features': [
        [
            {'key': 'Age', 'value': '34 years', 'href': ''},
            {'key': 'Work experience', 'value': '15 years', 'href': ''},
            {'key': 'Degree', 'value': 'Moscow State University of Civil Engineering (MSUCE), Magister, Software Engineering', 'href': ''},
            {'key': 'Location', 'value': 'Moscow', 'href': ''},
            {'key': 'E-mail', 'value': 'amokr@mail.ru', 'href': ''},
            {'key': 'Cell Phone', 'value': '+7 (926) 608-52-65', 'href': ''},
        ],
        [
            {'key': 'LinkedIn', 'value': 'Alexander Mokryshev',
             'href': 'https://www.linkedin.com/in/alexander-mokryshev-72b03a20/'},
            {'key': 'HH.ru', 'value': 'Alexander Mokryshev',
             'href': 'https://hh.ru/resume/91028332ff018a7d100039ed1f61476344394b'},
            {'key': 'Github.com', 'value': 'amokryshev', 'href': 'https://github.com/amokryshev'},
            {'key': 'Habr.com', 'value': 'amokryshev', 'href': 'https://habr.com/ru/users/amokryshev/'},
        ],
    ],
}


portfolio_section_ru = [
    {
        'picture': 'portfolio/ETL-article.png',
        'picture_name': 'ETL-article.png',
        'picture_path': 'initial_media_uploads/portfolio/ETL-article.png',
        'filter': 'filter-article',
        'links': [
            {
                'tip': 'Текст статьи',
                'href': 'https://habr.com/ru/post/248231/',
                'icon': 'bx bx-link'
            },
        ]
    },
    {
        'picture': 'portfolio/Budgeting-article.png',
        'picture_name': 'Budgeting-article.png',
        'picture_path': 'initial_media_uploads/portfolio/Budgeting-article.png',
        'filter': 'filter-article',
        'links': [
            {
                'tip': 'Текст статьи',
                'href': 'https://habr.com/ru/post/335720/',
                'icon': 'bx bx-link'
            },
        ]
    },
    {
        'picture': 'portfolio/Req-article.png',
        'picture_name': 'Req-article.png',
        'picture_path': 'initial_media_uploads/portfolio/Req-article.png',
        'filter': 'filter-article',
        'links': [
            {
                'tip': 'Текст статьи',
                'href': 'https://habr.com/ru/post/340956/',
                'icon': 'bx bx-link'
            },
        ]
    },
]

portfolio_section_en = [
    {
        'picture': 'portfolio/ETL-article.png',
        'picture_name': 'ETL-article.png',
        'picture_path': 'initial_media_uploads/portfolio/ETL-article.png',
        'filter': 'filter-article',
        'links': [
            {
                'tip': 'The article',
                'href': 'https://habr.com/ru/post/248231/',
                'icon': 'bx bx-link'
            },
        ]
    },
    {
        'picture': 'portfolio/Budgeting-article.png',
        'picture_name': 'Budgeting-article.png',
        'picture_path': 'initial_media_uploads/portfolio/Budgeting-article.png',
        'filter': 'filter-article',
        'links': [
            {
                'tip': 'The article',
                'href': 'https://habr.com/ru/post/335720/',
                'icon': 'bx bx-link'
            },
        ]
    },
    {
        'picture': 'portfolio/Req-article.png',
        'picture_name': 'Req-article.png',
        'picture_path': 'initial_media_uploads/portfolio/Req-article.png',
        'filter': 'filter-article',
        'links': [
            {
                'tip': 'The article',
                'href': 'https://habr.com/ru/post/340956/',
                'icon': 'bx bx-link'
            },
        ]
    },
]

facts_section_ru = {
    'intro': 'Большую часть карьеры я трудился в ИТ-консалтинге, оказывая услуги предприятиям из следующих отраслей бизнеса.',
    'finale': 'Кроме того знаком с бизнес-процессами отраслей: Теплоэнергетика, Электроэнергетика, Сельское хозяйство, Девелопмент, Авиастроение, Промышленное производство, Благотворительность.',
    'items': [
        {'icon': 'icofont-cart', 'years': 3, 'branch': 'Ритеил', 'details': 'Детский&nbsp;Мир; X5&nbsp;Retail'},
        {'icon': 'icofont-at', 'years': 3, 'branch': 'Программное&nbsp;обеспечение и&nbsp;Интернет',
         'details': 'PlatformaT&nbsp;(Агрегатор&nbsp;такси, cтартап&nbsp;в&nbsp;SAPRUN Group); Рамблер.'},
        {'icon': 'icofont-umbrella-alt', 'years': 4, 'branch': 'Страхование',
         'details': 'Страховой&nbsp;Дом&nbsp;ВСК; СК&nbsp;РОСГОССТРАХ; ВТБ&nbsp;Страхование.'},
        {'icon': 'icofont-network-tower', 'years': 4, 'branch': 'Телекоммуникации',
         'details': 'МегаФон; Corbina&nbsp;telecom (Билайн Домашний&nbsp;Интернет); Стартап (фиксированная&nbsp;связь).'},
    ]
}

facts_section_en = {
    'intro': 'For most of my career, I have worked in IT Consulting, providing services to enterprises from the following business sectors.',
    'finale': 'In addition, I am superficially familiar with the business processes: Heat power engineering, Electric power engineering, Agriculture, Development, Aircraft construction, Industrial production, Charity.',
    'items': [
        {'icon': 'icofont-cart', 'years': 3, 'branch': 'Retail', 'details': 'Detsky&nbsp;Mir; X5&nbsp;Retail'},
        {'icon': 'icofont-at', 'years': 3, 'branch': 'Software&nbsp;&amp;&nbsp;Web',
         'details': 'PlatformaT&nbsp;(Analogue of Uber for enterprices&nbsp;Startup in the SAPRUN Group); Rambler.'},
        {'icon': 'icofont-umbrella-alt', 'years': 4, 'branch': 'Insurance',
         'details': 'VSK&nbsp;Insurance&nbsp;House; IS&nbsp;RosGosStrakh; VTB&nbsp;Insurance.'},
        {'icon': 'icofont-network-tower', 'years': 4, 'branch': 'Телекоммуникации',
         'details': 'Megafon; Beeline; Startup (Fiber optic provider).'},
    ]
}

cv_section_ru = [
    {
        'pos': 0,
        'chapter': 'Резюме',
        'items': [
            {
                'pos': 0,
                'title': 'Александр Мокрышев',
                'period': '',
                'description': 'Product owner & IT Portfolio manager & SAP Project director',
                'details': [
                    {'text': 'Россия, Москва', 'href': '', 'subdetails': []},
                    {'text': '8 (926) 608-52-65', 'href': '', 'subdetails': []},
                    {'text': 'amokr@mail.ru', 'href': '', 'subdetails': []},
                    {'text': 'Александр Мокрышев@hh.ru',
                     'href': 'https://hh.ru/resume/91028332ff018a7d100039ed1f61476344394b', 'subdetails': []},
                ],
            }
        ],
    },
    {
        'pos': 1,
        'chapter': 'Опыт работы',
        'items': [
            {
                'pos': 0,
                'title': 'Старший руководитель проектов',
                'period': '2018 - 2020',
                'description': 'ПАО Детский Мир',
                'details': [
                    {'text': 'Управление портфелем ИТ-проектов (до 20-ти одновременно).', 'href': '',
                     'subdetails': []},
                    {'text': 'Управление отношениями c бизнес-подразделениями в роли IT бизнес партнера.',
                     'href': '', 'subdetails': []},
                    {'text': 'Организация проектного учета в ДИТ и выполнение роли PMO.', 'href': '',
                     'subdetails': []},
                    {
                        'text': 'Внедрение регрессионного тестирования процесса Интернет-заказа от создания до реализации.',
                        'href': '', 'subdetails': []},
                    {
                        'text': 'Успешный запуск ключевых ИТ-проектов в роли РП и Product Manager:',
                        'href': '',
                        'subdetails': [
                            {
                                'text': 'Обьединение РЦ Интернет-магазина и розничной сети (Крупнейший проект Компании 2018 года (SAP SD, MM, EWM, PI, FI, BW).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Организация программы проектов Маркетплейс, реализация функциональности комиссионной торговли и управления ассортиментом Маркетплейс в SAP (SAP SD, MM, POS DM, EWM, PI, FI, BW).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Перенос функциональности сборки заказов ИМ в розничном магазине на платформу SAP.',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Реализация функциональности курьерской доставки заказов ИМ из розничных магазинов.',
                                'href': '', 'subdetails': []},
                            {'text': 'Открытие РЦ Южного Федерального Округа.', 'href': '', 'subdetails': []},
                            {'text': 'Переезд компании ELC на новый РЦ.', 'href': '', 'subdetails': []},
                            {'text': 'Автоматизация тендерной процедуры по выбору компаний-перевозчиков. (Автоматическая валидация и ранжирование предложений ~50 перевозчиков по ~700 транспортным маршрутам)',
                             'href': '', 'subdetails': []},
                        ]

                    },
                ],

            },
            {
                'pos': 1,
                'title': 'Ведущий менеджер проектов',
                'period': '2016 - 2017',
                'description': 'Rambler&Co',
                'details': [
                    {'text': 'Управление и курирование заказных Интернет-проектов.', 'href': '',
                     'subdetails': []},
                    {'text': 'Организация практики заказной разработки.', 'href': '', 'subdetails': []},
                    {'text': 'Разработка первого заказного проекта Рамблер - Новостной сайт для БФ Рыбаков Фонд.',
                        'href': '', 'subdetails': []},
                ],

            },
            {
                'pos': 2,
                'title': 'Руководитель проектов',
                'period': '2014 - 2016',
                'description': 'SAPRUN',
                'details': [
                    {
                        'text': 'Управление проектами прикладной разработки на Python. (Команда до 30-ти человек, product-менеджер, дизайнеры, разработчики, QA, админы).',
                        'href': '', 'subdetails': []},
                    {'text': 'Управление проектами внедрения SAP.', 'href': '', 'subdetails': []},
                    {'text': 'Проведение пресейлов.', 'href': '', 'subdetails': []},
                    {
                        'text': 'Достижения:',
                        'href': '',
                        'subdetails': [
                            {
                                'text': 'Разработка и вывод в магазины приложений системы распределения заказов для таксопарков (Django + Twisted, приложения iOS и Android, приложение диспетчера Qt).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Организация с нуля направления прикладной разработки в Компании: Выбор технологий, набор команды, создание инфраструктуры (Jira, Bitbucket, Jenkins, etс.).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Организация проекта разработки ПО в соответствии с требованиями SCRUM (Agile), git-flow, развертывание систем Continuous Integration (BitBucket, Jenkins, PyPi), Deployment Automation (Ansible).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Построение процесса product-management и проектирование UX на основании анализа обратной связи от пользователей.',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Реализация проекта по диагностике крупнейшей в мире инсталляции SAP BW Accelerator для X5 Retail.',
                                'href': '', 'subdetails': []},
                            {'text': 'Продажа двух outstaffing контрактов в X5 Retail.', 'href': '',
                             'subdetails': []},
                        ]},
                ],

            },
            {
                'pos': 3,
                'title': 'Руководитель проектов',
                'period': '2012 - 2014',
                'description': 'ГК Систематика (Систематика, ТОПС, Ландата, АНД Проджект, Сайнер, Энсис)',
                'details': [
                    {
                        'text': 'Управление проектами внедрения SAP. (Команды консультантов до 50 человек)',
                        'href': '', 'subdetails': []},
                    {'text': 'Управление проектами внедрения Oracle Hyperion.', 'href': '', 'subdetails': []},
                    {'text': 'Проведение пресейлов.', 'href': '', 'subdetails': []},
                    {
                        'text': 'Достижения:',
                        'href': '',
                        'subdetails': [
                            {
                                'text': 'Внедрение системы финансовой консолидации в Росгосстрах (Hyperion HFM, FDQM, BI).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Проведение миграции используемой бюджетной системы на новое аппаратное окружение в Сибур-Кордиант (Hyperion Planning, Oracle Data Integrator, Oracle DB, Oracle APEX).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Продажа проекта BI, двух контрактов техподдержки и доработок на ~20% от бюджета основного проекта в крупнейшей страховой компании.',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Внедрение системы отчетности для топ-менеджмента компании МОЭК (SAP BW, SAP BO).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Интеграция SAP IS-U, ЛКК и EDI Тензор для обеспечения электронного обмена расчетно-платежными документами за тепловую энергию с клиентами в МОЭК.',
                                'href': '', 'subdetails': []},
                            {'text': 'Разрешение кризиса проекта по внедрению SAP ERP в Русагро.', 'href': '', 'subdetails': []},
                        ]},
                ],

            },
            {
                'pos': 4,
                'title': 'Руководитель проектов',
                'period': '2011 - 2012',
                'description': 'КОРУС Консалтинг',
                'details': [
                    {'text': 'Управление проектами внедрения систем Oracle Hyperion. (Команды консультантов до 6 человек)', 'href': '',
                     'subdetails': []},
                    {'text': 'Проведение пресейлов.', 'href': '', 'subdetails': []},
                    {'text': 'Достижения:', 'href': '', 'subdetails': [
                        {'text': 'Внедрение системы бюджетирования в Ренова Строй Групп(Hyperion Planning, FDQM, BI).', 'href': '', 'subdetails': []},
                        {'text': 'Организация работы по внедрению системы бюджетирования в ОАК (Hyperion Planning).', 'href': '', 'subdetails': []},
                    ]},
                ],

            },
            {
                'pos': 5,
                'title': 'Главный специалист департамента сопровождения ПО',
                'period': '2009 - 2011',
                'description': 'ВСК, САО',
                'details': [
                    {'text': 'Развитие корпоративной методологии управления проектами.', 'href': '', 'subdetails': []},
                    {'text': 'Администрирование портфеля корпоративных проектов.', 'href': '', 'subdetails': []},
                    {'text': 'Организация службы ServiceDesk.', 'href': '', 'subdetails': []},
                ],

            },
            {
                'pos': 6,
                'title': 'Ведущий бизнес-аналитик',
                'period': '2007 - 2009',
                'description': 'Верников и партнеры',
                'details': [
                    {'text': 'Моделирование систем управления по методологии SADT.', 'href': '', 'subdetails': []},
                    {'text': 'Управление проектами описания процессов МегаФон в роли лидера команды.', 'href': '', 'subdetails': []},
                ],

            },
        ],
    },
    {
        'pos': 2,
        'chapter': 'Образование',
        'items': [
            {
                'pos': 0,
                'title': 'Инженер по автоматизации систем обработки информации и управления',
                'period': '2003 - 2008',
                'description': 'Московский Государственный Строительный Университет',
                'details': [],
            },
            {
                'pos': 1,
                'title': 'Эконометрика',
                'period': '2021',
                'description': 'Высшая Школа Экономики, Coursera',
                'details': [],
            },
            {
                'pos': 2,
                'title': 'Project Management Professional',
                'period': '2016',
                'description': 'Project Management Institute, USA',
                'details': [],
            },
            {
                'pos': 3,
                'title': 'ITIL v3 Foundation',
                'period': '2010',
                'description': 'EXIN (Examination Institute for Information Science)',
                'details': [],
            },
        ],
    },
]

cv_section_en = [
    {
        'pos': 0,
        'chapter': 'Resume',
        'items': [
            {
                'pos': 0,
                'title': 'Alexander Mokryshev',
                'period': '',
                'description': 'Product owner & IT Portfolio manager & SAP Project director',
                'details': [
                    {'text': 'Russia, Moscow', 'href': '', 'subdetails': []},
                    {'text': '8 (926) 608-52-65', 'href': '', 'subdetails': []},
                    {'text': 'amokr@mail.ru', 'href': '', 'subdetails': []},
                    {'text': 'Amokryshev.hh.ru',
                     'href': 'https://hh.ru/resume/91028332ff018a7d100039ed1f61476344394b', 'subdetails': []},
                ],
            }
        ],
    },
    {
        'pos': 1,
        'chapter': 'Work Experience',
        'items': [
            {
                'pos': 0,
                'title': 'Senior project manager',
                'period': '2018 - 2020',
                'description': 'OJSC Detskiy Mir',
                'details': [
                    {'text': 'IT Portfolio management (up to 20 at a time).', 'href': '',
                     'subdetails': []},
                    {'text': 'Relationship management with business units as an IT business partner.',
                     'href': '', 'subdetails': []},
                    {'text': 'Developing project management standards in the IT dept and performing the role of PMO.', 'href': '',
                     'subdetails': []},
                    {
                        'text': 'Regression testing implementation in scope of the Internet order process from creation to sale.',
                        'href': '', 'subdetails': []},
                    {
                        'text': 'Successful launch of the key IT projects as a project and product manager:',
                        'href': '',
                        'subdetails': [
                            {
                                'text': "Merge of the online store's and retail supply chains on the one logistics center (The largest project of the Company in 2018)(SAP SD, MM, EWM, PI, FI, BW).",
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Supervising of the Marketplace program at all, and implementation of commission trading, and assortment management of the consignment goods.(SAP SD, MM, POS DM, EWM, PI, FI, BW).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Development functionality of assembling Internet-orders in the retail stores on the SAP platform.',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Developing the functionality of courier delivery from retail stores.',
                                'href': '', 'subdetails': []},
                            {'text': 'Opening of the Southern Federal District Logistics center.', 'href': '', 'subdetails': []},
                            {'text': 'Moving JSC ELC to the new logistics center.', 'href': '', 'subdetails': []},
                            {
                                'text': 'Automation of the tender procedure for the selection of shipping companies. (Automatic validation and ranking the offers from ~ 50 carriers on ~ 700 transport routes once a quarter)',
                                'href': '', 'subdetails': []},
                        ]

                    },
                ],

            },
            {
                'pos': 1,
                'title': 'Senior project manager',
                'period': '2016 - 2017',
                'description': 'Rambler&Co',
                'details': [
                    {'text': 'Management and supervision of custom Internet projects.', 'href': '',
                     'subdetails': []},
                    {'text': 'Organization of custom development practice.', 'href': '', 'subdetails': []},
                    {'text': "Development of the first Rambler's custom project  - News site for the Rybakov Foundation.",
                     'href': '', 'subdetails': []},
                ],

            },
            {
                'pos': 2,
                'title': 'Project manager',
                'period': '2014 - 2016',
                'description': 'SAPRUN',
                'details': [
                    {
                        'text': 'Python development project management. (A team of up to 30 people, product manager, designers, developers, QA, admins).',
                        'href': '', 'subdetails': []},
                    {'text': 'SAP implementation project management.', 'href': '', 'subdetails': []},
                    {'text': 'Pre-sales management.', 'href': '', 'subdetails': []},
                    {
                        'text': 'Achievements:',
                        'href': '',
                        'subdetails': [
                            {
                                'text': 'Development and release to application stores of an order distribution system for taxi fleets (Django + Twisted, iOS, Android, and QT applications).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Developing from scratch of software development practice in the Company: Selection of technologies, hiring teams, infrastructure deployment (Jira, Bitbucket, Jenkins, etc.).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Software development project implementation in accordance with the requirements of SCRUM (Agile), git-flow, deployment of Continuous Integration systems (BitBucket, Jenkins, PyPi), Deployment Automation (Ansible).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Building a product-management process and designing UX based on the analysis of user feedback.',
                                'href': '', 'subdetails': []},
                            {
                                'text': "Implementation of a diagnostic project for the world's largest installation of SAP BW Accelerator for X5 Retail.",
                                'href': '', 'subdetails': []},
                            {'text': 'Sale of two outstaffing contracts at X5 Retail.', 'href': '',
                             'subdetails': []},
                        ]},
                ],

            },
            {
                'pos': 3,
                'title': 'Project manager',
                'period': '2012 - 2014',
                'description': 'Systematica group',
                'details': [
                    {
                        'text': 'SAP implementation project management. (Teams of consultants up to 50 people)',
                        'href': '', 'subdetails': []},
                    {'text': 'Oracle Hyperion implementation project management.', 'href': '', 'subdetails': []},
                    {'text': 'Carrying out pre-sales.', 'href': '', 'subdetails': []},
                    {
                        'text': 'Achievements:',
                        'href': '',
                        'subdetails': [
                            {
                                'text': 'Implementation of a financial consolidation system in Rosgosstrakh, 35 insurance companies from 9 countries (Hyperion HFM, FDQM, BI).',
                                'href': '', 'subdetails': []},
                            {
                                'text': "Migration of the tyre production company's budget system to a new hardware environment in Sibur-Cordiant (Hyperion Planning, Oracle Data Integrator, Oracle DB, Oracle APEX).",
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Sale of the BI project, two technical support contracts and improvements for ~ 20% of the budget of the main project in Rosgosstrakh',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Implementation of the reporting system for top management of MOEK (Moscow Heat Power Company) (SAP BW, SAP BO).',
                                'href': '', 'subdetails': []},
                            {
                                'text': 'Integration of SAP IS-U, personal accounts on the site and EDI Tensor to ensure electronic exchange of payment and settlement documents for heat energy with customers in MOEK.',
                                'href': '', 'subdetails': []},
                            {'text': 'Resolving the crisis of the project for the implementation of SAP ERP in Rusagro.', 'href': '',
                             'subdetails': []},
                        ]},
                ],

            },
            {
                'pos': 4,
                'title': 'Project manager',
                'period': '2011 - 2012',
                'description': 'KORUS Consulting',
                'details': [
                    {
                        'text': 'Project management of Oracle Hyperion systems implementation. (Teams of consultants up to 6 people)',
                        'href': '',
                        'subdetails': []},
                    {'text': 'Carrying out pre-sales.', 'href': '', 'subdetails': []},
                    {'text': 'Achievements:', 'href': '', 'subdetails': [
                        {
                            'text': 'Implementation of a budgeting system in Renova Stroy Group (Large development and construction company) (Hyperion Planning, FDQM, BI).',
                            'href': '', 'subdetails': []},
                        {
                            'text': "Management of 'System design' stage of the budgeting system implementation in the UAC (United Aircraft Company, the holding that's owning Su, MiG, Tupolev and all other aircraft construction companies) (Hyperion Planning).",
                            'href': '', 'subdetails': []},
                    ]},
                ],

            },
            {
                'pos': 5,
                'title': 'Lead engineer of the Software Support Department',
                'period': '2009 - 2011',
                'description': 'VSK Insurance House',
                'details': [
                    {'text': 'Development of a corporate project management methodology.', 'href': '', 'subdetails': []},
                    {'text': 'Portfolio administration of corporate projects.', 'href': '', 'subdetails': []},
                    {'text': 'ServiceDesk service organization.', 'href': '', 'subdetails': []},
                ],

            },
            {
                'pos': 6,
                'title': 'Lead business analyst',
                'period': '2007 - 2009',
                'description': 'Vernikov and partners',
                'details': [
                    {'text': 'Modeling control and management systems using the SADT methodology. (IDEF)', 'href': '', 'subdetails': []},
                    {'text': 'Project management of business-process modeling for MegaFon as a team leader.', 'href': '',
                     'subdetails': []},
                ],

            },
        ],
    },
    {
        'pos': 2,
        'chapter': 'Education',
        'items': [
            {
                'pos': 0,
                'title': 'Engineer for automation of information processing and control systems (Software Engineering)',
                'period': '2003 - 2008',
                'description': 'Moscow State University of Civil Engineering (MSUCE)',
                'details': [],
            },
            {
                'pos': 1,
                'title': 'Econometrics',
                'period': '2021',
                'description': 'Higher School of Economics, Coursera',
                'details': [],
            },
            {
                'pos': 2,
                'title': 'Project Management Professional',
                'period': '2016',
                'description': 'Project Management Institute, USA',
                'details': [],
            },
            {
                'pos': 3,
                'title': 'ITIL v3 Foundation',
                'period': '2010',
                'description': 'EXIN (Examination Institute for Information Science)',
                'details': [],
            },
        ],
    },
]

services_section_ru = {
    'intro':    remove_mspaces.sub(" ", '''
                <p>Оказываю услуги управления проектами и продуктами в формате фриланс.</p>
                <p>В случае заинтересованности обращайтесь через средства связи, указанные на этом сайте.</p>
                '''),

    'details': [
        {
            'title': 'Организация команд разработки, проектов и процессов производства ПО',
            'description': remove_mspaces.sub(" ", '''Организация процессов управления проектом и производства программного
                           обеспечения, от сбора требований, до тестирования и управления релизами, 
                           подобр команды, оценка состояние дел, организация и распутывание сложных
                           ситуаций. Проведение пресейлов от вашего лица, организация торгов или участие в торгах,
                           в том числе имею опыт подготовки успешных предложений по ФЗ 223.'''),
            'href': '',
            'icon': 'icofont-unique-idea'
        },
        {
            'title': 'Бизнес-анализ и проектирование систем',
            'description': remove_mspaces.sub(" ", '''Проведение бизнес-анализа вашей идеи, организация и проведение сбора 
                           требований и проектирование функциональности cистемы, проведение проверки гипотез, подготовка 
                           бизнес-плана, расчет и презентация необходимой математики: 
                           Статистической значимости выводов, финансовой модели и бюджета проекта.'''),
            'href': '',
            'icon': 'icofont-chart-bar-graph'
        },
        {
            'title': 'Написание технической документации',
            'description': remove_mspaces.sub(" ", '''Структурирование и оформлкние вашей идеи в виде 
                           технического задания, концептуального проекта или SRS, достижение договоренностей и 
                           согласование ожиданий стейкхолдеров проекта, имею богатый опыт согласования 
                           ожиданий и формирования консистентных требований в проектах с несколькими 
                           десятками стейкхолдеров уровня CEO-1 и CEO-2.'''),
            'href': '',
            'icon': 'icofont-ebook'
        },
        {
            'title': 'Управление проектом',
            'description': remove_mspaces.sub(" ", '''Управление проектами в качестве руководителя полного цикла: От формулирования 
                           задачи и подбора сотрудников, до ежедневного операционного управления командой'''),
            'href': '',
            'icon': 'icofont-tasks'
        },
    ]
}

services_section_en = {
    'intro': remove_mspaces.sub(" ", '''
                   <p>Provide project and product management services in freelance format.</p>
                   <p>In case of interest, you can reach me through the contacts published on this site.</p>
                   '''),

    'details': [
        {
            'title': 'Organization of development teams, projects and software production processes',
            'description': remove_mspaces.sub(" ", '''Help to organize the processes of project management 
                              and software production, from requirements, to testing and release management, 
                              will help to select a team, assess the state of affairs, organize or unravel 
                              a difficult situation. Will conduct a presale for you, organize or participate 
                              a tender with you.'''),
            'href': '',
            'icon': 'icofont-unique-idea'
        },
        {
            'title': 'Business analysis and systems design',
            'description': remove_mspaces.sub(" ", '''Will conduct a business analysis of your idea, collect requirements 
                              and design the functionality of the system, test hypotheses.
                              Will prepare a business plan, calculate and present the necessary mathematics: 
                              Count of statistical significance of conclusions, financial model and project budget.'''),
            'href': '',
            'icon': 'icofont-chart-bar-graph'
        },
        {
            'title': 'Writing technical documentation',
            'description': remove_mspaces.sub(" ", '''Will help to structure and formalize your idea in the 
                              form of a technical assignment, conceptual project or SRS. Will help to create 
                              rapport and align expectations of the project stakeholders, I have extensive 
                              experience in agreeing expectations and forming consistent requirements in 
                              projects with several dozen CEO-1 and CEO-2 stakeholders.'''),
            'href': '',
            'icon': 'icofont-ebook'
        },
        {
            'title': 'Project management',
            'description': remove_mspaces.sub(" ", '''Could manage your project as a full cycle leader: 
                                From task formulation and staff selection, to daily operational team management'''),
            'href': '',
            'icon': 'icofont-tasks'
        },
    ]
}

testimonials_section_ru = {
    'intro': remove_mspaces.sub(" ", '''
             <p>Ниже только рекомендации, опубликованные на линкедин, по запросу готов предоставить 
             более полный список рекомендателей и способы связи с ними для проверки.</p>
             '''),
    'details': [
        {
            'text': 'We have been working together with Alexander for the past 3 years. Alexander is a very engaged, extremely motivated and forward thinking person. He successfully managed and launched several business critical logistics and e-commerce projects that will ensure stable business growth, increasing performance and profitability.',
            'picture':'testimonials/Garegin.jpeg',
            'picture_name':'Garegin.jpeg',
            'picture_path': 'initial_media_uploads/testimonials/Garegin.jpeg',
            'person': 'Garegin Margaryan',
            'position': 'Chief technology officer OJSC Detskiy Mir'
        },
        {
            'text': 'За время работы в Александра в ДМ реализовали несколько очень крупных проектов, базирующихся на SAP: перенос склада интернет магазина с изменением технологии на волнолом, маркетплейс и пр. Александр глубоко погружается в процесс, "ведет" проект не только со стороны ИТ, но и понимает и "держит в уме" бизнес составляющую проекта. Хорошо "трекает" большие проекты, состоящие из нескольких команд и связанные с несколькими бизнес заказчиками. В общем, от совместной работы остались хорошие впечатление, Александр, удачи.',
            'picture': 'testimonials/Pavel.jpeg',
            'picture_name': 'Pavel.jpeg',
            'picture_path': 'initial_media_uploads/testimonials/Pavel.jpeg',
            'person': 'Pavel Pischikov',
            'position': 'Head of eCommerce OJSC Detskiy Mir'
        },
    ]
}

testimonials_section_en = {
    'intro': remove_mspaces.sub(" ", '''
                <p>Below are only the recommendations published on Linkedin, upon request, I am ready to provide a 
                more complete list of referees and how to contact them for verification.</p>
                '''),
    'details': [
        {
            'text': 'We have been working together with Alexander for the past 3 years. Alexander is a very engaged, extremely motivated and forward thinking person. He successfully managed and launched several business critical logistics and e-commerce projects that will ensure stable business growth, increasing performance and profitability.',
            'picture': 'testimonials/Garegin.jpeg',
            'picture_name': 'Garegin.jpeg',
            'picture_path': 'initial_media_uploads/testimonials/Garegin.jpeg',
            'person': 'Garegin Margaryan',
            'position': 'Chief technology officer OJSC Detskiy Mir'
        },
        {
            'text': 'За время работы в Александра в ДМ реализовали несколько очень крупных проектов, базирующихся на SAP: перенос склада интернет магазина с изменением технологии на волнолом, маркетплейс и пр. Александр глубоко погружается в процесс, "ведет" проект не только со стороны ИТ, но и понимает и "держит в уме" бизнес составляющую проекта. Хорошо "трекает" большие проекты, состоящие из нескольких команд и связанные с несколькими бизнес заказчиками. В общем, от совместной работы остались хорошие впечатление, Александр, удачи.',
            'picture': 'testimonials/Pavel.jpeg',
            'picture_name': 'Pavel.jpeg',
            'picture_path': 'initial_media_uploads/testimonials/Pavel.jpeg',
            'person': 'Pavel Pischikov',
            'position': 'Head of eCommerce OJSC Detskiy Mir'
        },
    ]
}




[
    {'pos': 0,
     'chapter': 'Резюме',
     'items': [
         {
             'pos': 0,
             'title': 'Александр Мокрышев',
             'period': '',
             'description': 'Product owner & IT Portfolio manager & SAP Project director',
             'details': [
                 {
                     'text': 'Россия, Москва',
                     'href': '', 'subdetails': []
                 },
                 {
                     'text': '8 (926) 608-52-65',
                     'href': '', 'subdetails': []
                 },
                 {
                     'text': 'amokr@mail.ru',
                     'href': '', 'subdetails': []
                 },
                 {
                     'text': 'Александр Мокрышев@hh.ru',
                     'href': 'https://hh.ru/resume/91028332ff018a7d100039ed1f61476344394b',
                     'subdetails': []
                 }
             ]
         }
     ]
     },
    {
        'pos': 1,
        'chapter':
            'Опыт работы',
        'items': [
            {'pos': 0,
             'title': 'Старший руководитель проектов',
             'period': '2018 - 2020',
             'description': 'ПАО Детский Мир',
             'details': [
                 {'text': 'Управление портфелем ИТ-проектов (до 20-ти одновременно).', 'href': '', 'subdetails': []},
                 {'text': 'Управление отношениями c бизнес-подразделениями в роли IT бизнес партнера.', 'href': '', 'subdetails': []},
                 {'text': 'Организация проектного учета в ДИТ и выполнение роли PMO.', 'href': '', 'subdetails': []},
                 {'text': 'Внедрение регрессионного тестирования процесса Интернет-заказа от создания до реализации.', 'href': '', 'subdetails': []},
                 {
                     'text': 'Успешный запуск ключевых ИТ-проектов в роли РП и Product Manager:',
                     'href': '',
                     'subdetails': [
                         {
                             'text': 'Обьединение РЦ Интернет-магазина и розничной сети (Крупнейший проект Компании 2018 года (SAP SD, MM, EWM, PI, FI, BW).',
                             'href': '', 'subdetails': []
                         },
                         {
                             'text': 'Организация программы проектов Маркетплейс, реализация функциональности комиссионной торговли и управления ассортиментом Маркетплейс в SAP (SAP SD, MM, POS DM, EWM, PI, FI, BW).', 'href': '', 'subdetails': []
                         },
                         {
                             'text': 'Перенос функциональности сборки заказов ИМ в розничном магазине на платформу SAP.', 'href': '', 'subdetails': []
                         },
                         {
                             'text': 'Реализация функциональности курьерской доставки заказов ИМ из розничных магазинов.', 'href': '', 'subdetails': []
                         },
                         {
                             'text': 'Открытие РЦ Южного Федерального Округа.', 'href': '', 'subdetails': []
                         },
                         {
                             'text': 'Переезд компании ELC на новый РЦ.', 'href': '', 'subdetails': []
                         },
                         {
                             'text': 'Автоматизация тендерной процедуры по выбору компаний-перевозчиков. (Автоматическая валидация и ранжирование предложений ~50 перевозчиков по ~700 транспортным маршрутам)', 'href': '', 'subdetails': []
                         }
                     ]
                 }
             ]
             },
            {
                'pos': 1,
                'title': 'Ведущий менеджер проектов',
                'period': '2016 - 2017',
                'description': 'Rambler&Co',
                'details': [
                    {'text': 'Управление и курирование заказных Интернет-проектов.', 'href': '', 'subdetails': []},
                    {'text': 'Организация практики заказной разработки.', 'href': '', 'subdetails': []},
                    {'text': 'Разработка первого заказного проекта Рамблер - Новостной сайт для БФ Рыбаков Фонд.', 'href': '', 'subdetails': []}
                ]
            },
            {
                'pos': 2,
                'title': 'Руководитель проектов',
                'period': '2014 - 2016',
                'description': 'SAPRUN',
                'details': [
                    {'text': 'Управление проектами прикладной разработки на Python. (Команда до 30-ти человек, product-менеджер, дизайнеры, разработчики, QA, админы).', 'href': '', 'subdetails': []},
                    {'text': 'Управление проектами внедрения SAP.', 'href': '', 'subdetails': []}, {'text': 'Проведение пресейлов.', 'href': '', 'subdetails': []},
                    {'text': 'Достижения:', 'href': '', 'subdetails': [
                        {'text': 'Разработка и вывод в магазины приложений системы распределения заказов для таксопарков (Django + Twisted, приложения iOS и Android, приложение диспетчера Qt).', 'href': '', 'subdetails': []},
                        {'text': 'Организация с нуля направления прикладной разработки в Компании: Выбор технологий, набор команды, создание инфраструктуры (Jira, Bitbucket, Jenkins, etс.).', 'href': '', 'subdetails': []},
                        {'text': 'Организация проекта разработки ПО в соответствии с требованиями SCRUM (Agile), git-flow, развертывание систем Continuous Integration (BitBucket, Jenkins, PyPi), Deployment Automation (Ansible).', 'href': '', 'subdetails': []},
                        {'text': 'Построение процесса product-management и проектирование UX на основании анализа обратной связи от пользователей.', 'href': '', 'subdetails': []},
                        {'text': 'Реализация проекта по диагностике крупнейшей в мире инсталляции SAP BW Accelerator для X5 Retail.', 'href': '', 'subdetails': []},
                        {'text': 'Продажа двух outstaffing контрактов в X5 Retail.', 'href': '', 'subdetails': []}
                    ]
                     }
                ]
            },
            {
                'pos': 3,
                'title': 'Руководитель проектов',
                'period': '2012 - 2014',
                'description': 'ГК Систематика (Систематика, ТОПС, Ландата, АНД Проджект, Сайнер, Энсис)',
                'details': [
                    {'text': 'Управление проектами внедрения SAP. (Команды консультантов до 50 человек)', 'href': '', 'subdetails': []},
                    {'text': 'Управление проектами внедрения Oracle Hyperion.', 'href': '', 'subdetails': []},
                    {'text': 'Проведение пресейлов.', 'href': '', 'subdetails': []},
                    {'text': 'Достижения:', 'href': '', 'subdetails': [
                        {'text': 'Внедрение системы финансовой консолидации в Росгосстрах (Hyperion HFM, FDQM, BI).', 'href': '', 'subdetails': []},
                        {'text': 'Проведение миграции используемой бюджетной системы на новое аппаратное окружение в Сибур-Кордиант (Hyperion Planning, Oracle Data Integrator, Oracle DB, Oracle APEX).', 'href': '', 'subdetails': []},
                        {'text': 'Продажа проекта BI, двух контрактов техподдержки и доработок на ~20% от бюджета основного проекта в крупнейшей страховой компании.', 'href': '', 'subdetails': []},
                        {'text': 'Внедрение системы отчетности для топ-менеджмента компании МОЭК (SAP BW, SAP BO).', 'href': '', 'subdetails': []},
                        {'text': 'Интеграция SAP IS-U, ЛКК и EDI Тензор для обеспечения электронного обмена расчетно-платежными документами за тепловую энергию с клиентами в МОЭК.', 'href': '', 'subdetails': []},
                        {'text': 'Разрешение кризиса проекта по внедрению SAP ERP в Русагро.', 'href': '', 'subdetails': []}
                    ]
                     }
                ]
            },
            {
                'pos': 4,
                'title': 'Руководитель проектов',
                'period': '2011 - 2012',
                'description': 'КОРУС Консалтинг',
                'details': [
                    {'text': 'Управление проектами внедрения систем Oracle Hyperion. (Команды консультантов до 6 человек)', 'href': '', 'subdetails': []},
                    {'text': 'Проведение пресейлов.', 'href': '', 'subdetails': []},
                    {'text': 'Достижения:', 'href': '', 'subdetails': [
                        {'text': 'Внедрение системы бюджетирования в Ренова Строй Групп(Hyperion Planning, FDQM, BI).', 'href': '', 'subdetails': []},
                        {'text': 'Организация работы по внедрению системы бюджетирования в ОАК (Hyperion Planning).', 'href': '', 'subdetails': []}
                    ]
                     }
                ]
            },
            {
                'pos': 5,
                'title': 'Главный специалист департамента сопровождения ПО',
                'period': '2009 - 2011',
                'description': 'ВСК, САО',
                'details': [
                    {'text': 'Развитие корпоративной методологии управления проектами.', 'href': '', 'subdetails': []},
                    {'text': 'Администрирование портфеля корпоративных проектов.', 'href': '', 'subdetails': []},
                    {'text': 'Организация службы ServiceDesk.', 'href': '', 'subdetails': []}]},
            {'pos': 6, 'title': 'Ведущий бизнес-аналитик', 'period': '2007 - 2009', 'description': 'Верников и партнеры', 'details': [{'text': 'Моделирование систем управления по методологии SADT.', 'href': '', 'subdetails': []}, {'text': 'Управление проектами описания процессов МегаФон в роли лидера команды.', 'href': '', 'subdetails': []}]}]}, {'pos': 2, 'chapter': 'Образование', 'items': [{'pos': 0, 'title': 'Инженер по автоматизации систем обработки информации и управления', 'period': '2003 - 2008', 'description': 'Московский Государственный Строительный Университет', 'details': []}, {'pos': 1, 'title': 'Эконометрика', 'period': '2021', 'description': 'Высшая Школа Экономики, Coursera', 'details': []}, {'pos': 2, 'title': 'Project Management Professional', 'period': '2016', 'description': 'Project Management Institute, USA', 'details': []}, {'pos': 3, 'title': 'ITIL v3 Foundation', 'period': '2010', 'description': 'EXIN (Examination Institute for Information Science)', 'details': []}]}]
