from django import template
from django.contrib.auth.models import User
from django.utils.html import format_html

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
