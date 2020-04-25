from django.shortcuts import render
from .models import Critere, Champ, PoidsChamps
from .forms import CritereForm, ChampForm, PoidsChampForm
from django.shortcuts import redirect
from user.views import group_required
# Create your views here.

@group_required('Responsables de parcours')
def index(request):
	criteres = Critere.objects.all()
	champs = Champ.objects.all()
	poids_champs = PoidsChamps.objects.all()
	return render(request,'criterion/index.html', {'criteres': criteres,'champs':champs, 'poids_champs':poids_champs})

@group_required('Responsables de parcours')
def critere_new(request):
    if request.method == "POST":
        form = CritereForm(request.POST)
        if form.is_valid():
            critere = form.save()
            return redirect('critere:new2', pk=critere.id)
    else:
        form = CritereForm()
    return render(request, 'criterion/edit.html', {'form': form})

@group_required('Responsables de parcours')
def critere_new2(request,pk):
	if request.method =='POST':
		form = PoidsChampForm(request.POST, id = pk)
		if form.is_valid():
			critere = Critere.objects.get(id=pk)
			for champ in critere.champs.all():
				poids_champ = form.cleaned_data.get(champ.nom)
				objet_poids_champ = PoidsChamps.objects.get(champ = champ, critere = critere)
				objet_poids_champ.poids_champ = poids_champ
				objet_poids_champ.save()
			return redirect('critere:index')
	else:
		form = PoidsChampForm(id=pk)

	return render(request,'criterion/edit2.html' ,{'form':form})


@group_required('Responsables de parcours')
def champ_new(request):
    if request.method == "POST":
        form = ChampForm(request.POST)
        if form.is_valid():
            champ = form.save(commit=False)
            champ.save()
            return redirect('critere:index')
    else:
        form = ChampForm()
    return render(request, 'criterion/edit.html', {'form': form})
