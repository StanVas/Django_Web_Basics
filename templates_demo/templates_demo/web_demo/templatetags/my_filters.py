from django.template import Library


register = Library()


@register.filter(name='odd')
def get_odd(nums):
    """" My custom filter """
    """ Use any python/Django tools """
    """ ex: get Object from DB """
    return [x for x in nums if x % 2 == 1]


@register.filter(name='app_style_date')
def app_date(date):
    return date.strftime('%Y/%m/%d')