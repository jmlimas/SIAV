from django import template
import datetime

register = template.Library()

def dayssince(value):
    if value is None:
        return '0'
    "Returns number of days between today and value."
    today = datetime.date.today()
    diff  = today - value
    if diff.days > 1:
        return '%s' % diff.days
    elif diff.days == 1:
        return '1'
    elif diff.days == 0:
        return '0'
    else:
        # Date is in the future; return formatted date.
        return value.strftime("%B %d, %Y")

register.filter('dayssince', dayssince)
