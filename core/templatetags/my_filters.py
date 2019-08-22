from django import template

register = template.Library()


@register.filter
def minus(first, second):
    return first - second


@register.simple_tag
def get_post_tags(post):
    tags = post.tags.all()
    return ', '.join([f'<a href="#">#{x.name}</a>' for x in tags])


@register.inclusion_tag(filename='nav.html')
def nav(selected='home'):
    return {
        'selected': selected
    }
