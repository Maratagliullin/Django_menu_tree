from menuapp.models import MenuItem
from django import template

register = template.Library()

tree_structure = {}


def recursive_menu(main, full):
    for key, item in enumerate(main):
        if item['id'] in full:
            main[key]['children'] = full[item['id']]
            recursive_menu(main[key]['children'], full)


def generate_tree(menu_items):
    for item in menu_items:
        if item.parent is None:
            tree_structure[0] = []
        else:
            tree_structure[item.parent.id] = []

    for item in menu_items:
        if item.parent is None:
            tree_structure[0].append(
                {'id': item.id,
                 'title': item.title,
                 'url': item.url, 'children': []})
        else:
            tree_structure[
                item.parent.id].append({'id': item.id,
                                        'title': item.title,
                                        'url': item.url, 'children': []})
        parent_structure = tree_structure[0]
        recursive_menu(parent_structure, tree_structure)
    return parent_structure


@register.inclusion_tag('menuapp/menu_item.html')
def draw_menu(menu_name, request):
    """Мезаника работы:
    1.Выбираем все записи,которые соответсвуют пунктам одного меню
    за один sql запрос
    2.Сохраняем значения в структуру
    3.Формируем древовидную структуру для последующей отрисовки в шаблоне
    """
    objects = MenuItem.objects.select_related(
        'parent').filter(menu_name=menu_name)
    menu_items = list(objects)
    objects_dict = generate_tree(menu_items)

    return {'menu_items': objects_dict, 'request': request}
