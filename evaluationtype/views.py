from django.shortcuts import render
from .models import EvaluationType, Poids
from .forms import EvaluationTypeForm, PoidsForm
from django.shortcuts import redirect
from user.views import group_required
from django.forms import modelformset_factory
# Create your views here.
@group_required('Responsables de parcours')
def index(request):
	evaluationtypes = EvaluationType.objects.all()
	poids = Poids.objects.all()
	return render(request,'evaluationtype/index.html', {'evaluationtypes': evaluationtypes,'poids' : poids})

@group_required('Responsables de parcours')
def evaluationtype_new(request):
	if request.method == "POST":
		form = EvaluationTypeForm(request.POST)
		if form.is_valid() :
			evaluationtype = form.save()

			return redirect('evaluationtype:new2' , pk=evaluationtype.id)
	else:
		form = EvaluationTypeForm()

	return render(request, 'evaluationtype/edit.html', {'form': form})


@group_required('Responsables de parcours')
def evaluationtype_new2(request,pk):


	if request.method =='POST':
		form = PoidsForm(request.POST, id = pk)

		if form.is_valid():
			evaluationtype = EvaluationType.objects.get(id=pk)
			for critere in evaluationtype.criteres.all():
				poids = form.cleaned_data.get(critere.libelle_critere)
				objet_poids = Poids.objects.get(type_evaluation = evaluationtype, critere = critere)
				objet_poids.poids = poids
				objet_poids.save()

			return redirect('evaluationtype:index')

	else:
		form = PoidsForm(id=pk)

	return render(request,'evaluationtype/edit2.html' ,{'form':form})
