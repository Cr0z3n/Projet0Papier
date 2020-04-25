from django.shortcuts import render
from django.shortcuts import redirect
from planning.models import Event
from .forms import PostForm
from .models import *
from planning.models import Event
from user.views import group_required

@group_required('Eleves')
def index(request):

	events = Event.objects.filter(eleves__username=request.user)
	#on vient rechercher le nom de l'utilisateur connecté et on récupere toutes les events qui lui sont liées

	return render(request,'evaluation/index.html', {'events': events})



# Create your views here.


@group_required('Responsables de parcours','Evaluateurs')
def evaluation_new(request, event_id=None):


	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = PostForm(request.POST, id=event_id)  # Nous reprenons les données
		if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire


			event = Event.objects.get(pk=event_id)
			for evaluationtype in event.type_evaluation.all():
				for critere in evaluationtype.criteres.all():
					note = form.cleaned_data.get(critere.libelle_critere)
					instance = Note(libelle_critere=critere.libelle_critere,valeur=note)
					instance.save()
					event.notes.add(instance)
					event.evaluateurs.remove(request.user)

			form = PostForm(id = event_id)

			return redirect('planning:calendar') # Redirect after POST
	else: # Si ce n'est pas du POST, c'est probablement une requête GET
        # Nous créons un formulaire pré-rempli
		form = PostForm(id = event_id)
	return render(request, 'evaluation/evaluate.html', locals())
