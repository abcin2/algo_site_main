from django.shortcuts import render

from .models import AlgorithmType

def index(request):
    latest_algo_list = AlgorithmType.objects.all()
    context = {
        'latest_algo_list': latest_algo_list,
    }
    return render(request, 'algorithms/index(test).html', context)
