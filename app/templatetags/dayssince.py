from django import template
import datetime

register = template.Library()

def dayssince(value):
    "Returns number of days between today and value."
    today = datetime.date.today()
    diff  = today - value
    if diff.days > 1:
        return '%s dias' % diff.days
    elif diff.days == 1:
        return '1'
    elif diff.days == 0:
        return '0'
    else:
        # Date is in the future; return formatted date.
        return value.strftime("%B %d, %Y")

register.filter('dayssince', dayssince)
