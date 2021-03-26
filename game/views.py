from django.shortcuts import render
from .forms import AdventureForm, PlayerForm
from .models import Player, Stages


def index(request):
	current_player = None
	context = {}
	context['stage'] = Stages.objects.get(id__exact=2)
	
	if request.method == "POST":
		form = PlayerForm(request.POST)
		if form.is_valid():
			player = form.save()
			player.save()
			context['current_player'] = player.name
			return render(request, 'game/intro.html', context)
	else:
		form = PlayerForm()
	context['form'] = form

	return render(request, 'game/index.html', context)

