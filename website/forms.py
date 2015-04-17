#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

class FormaContacto(forms.Form):
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre','class': 'form-control required'}), required=False)
    Correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo','class': 'form-control required email'}), required=False)
    Telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono','class': 'form-control required'}))
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Esribe aqui tu mensaje...','class': 'form-control required'}), required=False)
    Captcha = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '2 + 4 ?','class': 'form-control required'}))
