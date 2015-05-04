from django import template

register = template.Library()

def google_flags(x):
    if x:
    	 x = float(x)
    
    if x is None:
        return "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png"
    elif x <= 0:
        return "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png"
    elif 0 < x < 200.00:
        return "http://maps.google.com/mapfiles/ms/icons/orange-dot.png"
    elif 200.00 <= x < 1000.00:
        return "http://maps.google.com/mapfiles/ms/icons/purple-dot.png"
    elif 1000.00 <= x < 5000.00:
        return "http://maps.google.com/mapfiles/ms/icons/green-dot.png"
    elif 5000.00 <= x < 10000.00:
     	return "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"    
    else:
        return "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"

register.filter('google_flags', google_flags)