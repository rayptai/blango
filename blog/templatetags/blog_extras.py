from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html

from blog.models import Post

register = template.Library()

@register.filter
def author_details(author: User, current_user: User=None) -> str:
  if not isinstance(author, User):
    return ''

  if author.username == current_user.username:
    return format_html('<strong>me</strong>')

  if len(author.first_name) > 0 and len(author.last_name) > 0:
    name = f'{author.first_name} {author.last_name}'
  else:
    name = author.username

  if len(author.email) > 0:
    output = format_html('<a href="mailto:{}">{}</a>', author.email, name)  
  else:
    output = format_html('{}', name)

  return output

@register.simple_tag
def row(extra_classes=''):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return format_html("</div>")

@register.simple_tag
def col(extra_classes=''):
  return format_html('<div class="col {}">', extra_classes)

@register.simple_tag
def endcol():
  return format_html("</div>")

@register.inclusion_tag('blog/post-list.html')
def recent_posts(post: Post):
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {
    'title': 'Recent Posts',
    'posts': posts
  }
