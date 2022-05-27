from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Prefetch
from .models import Card
from .forms import CardForm, CardSearch 
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success, error
# Create your views here.

@login_required(login_url='/login/')
def index(request):
  cards = Card.objects.filter(users=request.user).order_by('name')
  form = CardSearch(request.GET)
  card_search = request.GET.get('searched_card')
  if card_search:
    cards = cards.filter(name__icontains=card_search)
  context = {'cards': cards, 'form': form}
  return render(request, 'base.html', context)

@login_required(login_url='/login/')
def addCard(request):
  cards = ''
  form = CardForm(request.POST)
  if form.is_valid():
    cards=Card.objects.filter(name__icontains = form.cleaned_data['card_search'])
    if cards.exists():
      cards[0].users.add(request.user)
      success(request, "Card successfully added to your collection!")
      return redirect('addCard')
    else:
      form = CardForm()
      error(request, "Card does not exist!")
      return redirect('addCard')
  context = {'cards': cards, 'form': form}
  return render(request, 'addCard.html', context)