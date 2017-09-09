import os
from staticjinja import make_site


USER = "Иван Иваныч"
COMMENT_TEXT = 'Отличная площадка для поиска поставщиков! Есть конкуренция.Продавцы здорово депенгуют. Я постоянный пользователь данного сервиса. Спасибо за труд!'
ORDER_TEXT = '60шт. ПК от 72-15  до ПК 21-15 можно без сахара. Каргат, с доставкой до порога.'
VIEWS_VALUE = '20 просмотров'


index_content = {
    'user': USER,
    'comments': 4,
    'authors': ['Владислав Пельш, г. Улан-Удэ',
                'Анна Симонян, г. Звенигород',
                'Тина Тинделаки, г. Черепаново',
                'Алексей Диникин, г. Новосибирск',
                ],
    'comment_text': COMMENT_TEXT,
    'orders': 4,
    'time': 'вчера, в 12:50',
    'orders_info': ORDER_TEXT,
    'orders_person_name': ['Кяама Няпока, г. Турдук',
                'Саяна Сушенская, г. Ногузадерищенск',
                'Инокентий Правильный, г. Каркарум',
                'Саркисян Конте, г. пл. Марс',
                ],
    'value_views': VIEWS_VALUE,
}

organisation_content = {
    'user': USER,
    'specification': 'ЖБИ',
    'company_name': 'ООО Строй-Сервис-Монтаж',
    'company_location': 'Новосибирск',
    'company_production': 'ЖБИ, бетон',
    'company_address': 'Под часами, на том же месте',
    'company_phone_number': '00-00-00',
    'specialties':  ['Плиты', 'Перекрытия', 'Доставляем быстро'],
}

catalog_content = {
    'user': USER,
    'specification': 'ЖБИ',
    'tables': 6,
    'company_name': 'ООО Строй-Сервис-Монтаж',
    'company_location': 'Новосибирск',
    'company_production': 'ЖБИ, бетон',
    'company_address': 'Под часами, на том же месте',
    'company_phone_number': '00-00-00',
}


def check_dir_site(site):
    if not os.path.exists(site):
        os.mkdir(site)


if __name__== "__main__":
    name_folder_site = 'site'
    check_dir_site(name_folder_site)
    site = make_site(outpath='site',
                     contexts=[
                         ('index.html', index_content),
                         ('orders_page.html', index_content),
                         ('dir_organizations.html', catalog_content),
                         ('current_dir_organization.html', catalog_content),
                         ('organization_page.html', organisation_content)
                     ])
    site.render()