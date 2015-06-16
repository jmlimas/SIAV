import django.dispatch

post_viewed = django.dispatch.Signal(providing_args=["a","b","c"])