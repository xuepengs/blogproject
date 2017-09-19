from django import template
from django.db.models.aggregates import Count
from ..models import Post, Category
from blog.models import Tag
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
tag_list = Tag.objects.annotate(num_posts=Count('post')
