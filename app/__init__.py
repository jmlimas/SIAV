from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.models import User as DjangoUser

flag = "false"


if(DjangoGroup.objects.all == 0):
  Admins = DjangoGroup(name='Admins')
  Admins.save()
  
  admins_group = DjangoGroup.objects.get(name="Admins")
  admin = DjangoUser.objects.get(pk=1)
  admins_group.user_set.add(admin)

  Usuarios = DjangoGroup(name='Usuarios')
  Usuarios.save()
  flag = "false"
