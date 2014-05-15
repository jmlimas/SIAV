#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms

class FormaContacto(forms.Form):
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}), required=True)
    Correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Correo'}), required=True)
    Telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Teléfono'}))
    Mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Esribe aqui tu mensaje...'}), required=True)