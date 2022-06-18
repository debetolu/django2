from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import generate_avatar
from users.forms import PersonalForm, ProfessionalForm, SubscriptionsForm

User = get_user_model()