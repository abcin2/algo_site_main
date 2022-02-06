import time

from tracemalloc import start
from django.shortcuts import redirect, render

from .models import AlgorithmType, DataSet
from .forms import PickYourData

def index(request):
    latest_algo_list = AlgorithmType.objects.all()
    context = {
        'latest_algo_list': latest_algo_list,
    }
    return render(request, 'algorithms/index.html', context)

def bubbleSort(request):
    nums = []
    nums_post = None
    bar_width = 0
    max_bar = 0
    data_form = PickYourData()
    # check for submit button values in order to differentiate between multiple forms
    if request.method == 'POST':
        data_form = PickYourData(request.POST)
        if data_form.is_valid():
            nums_post = data_form.cleaned_data['your_data']
            nums = data_form.cleaned_data['your_data'].split(',')
            bar_width = 10/len(nums)
            max_bar = max(nums)
            print(nums_post)
    elif request.method == 'GET':
        if request.GET.get('visualize'):
            
            def bubble_sort(nums):
                length = len(nums)
    
                for i in range(length - 1):
                    for j in range(0, length - i - 1):
                        print('nums to compare>>>', nums[i], nums[j])
                        if nums[j] > nums[j + 1]:
                            # time.sleep(1)
                            nums[j], nums[j + 1] = nums[j + 1], nums[j]
                            return nums
                            
                return nums
            
            def new_list_to_string(arr):
                new_string = ''
                for i, num in enumerate(arr):
                    if i == len(arr) - 1:
                        new_string += num
                    else:
                    # find end of list and do not add comma
                        new_string += num + ','
                return new_string
            
            nums = bubble_sort(request.GET.get('data').split(','))
            nums_post = new_list_to_string(nums)
            print(nums_post)

            # nums = request.GET.get('data').split(',')
            bar_width = 10/len(nums)
            max_bar = max(nums)
        elif request.GET.get('refresh'):
            redirect('algorithms/bubble_sort')
        
    context = {
        'data_form': data_form,
        'nums': nums,
        'bar_width': bar_width,
        'max_bar': max_bar,
        'nums_post': nums_post,
    }
    
    return render(request, 'algorithms/bubble_sort.html', context)
