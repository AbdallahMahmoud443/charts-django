from django.http import JsonResponse
from django.shortcuts import render
from chartdemoapp.models import SalesData

# Create your views here.

def Home(request):
    return render(request,'chartdemoapp/home.html')

def Get_Chart_Data(request,chartType):
    if chartType in ['bar','line','pie','doughnut','radar','polarArea']:
        salesData = list(SalesData.objects.values('month','sales'))
        # Build Dict of Data
        chartData={
            'labels':[entry['month'] for entry in salesData],
            'data':[entry['sales'] for entry in salesData]
        }
    elif chartType == 'area':
         salesData = list(SalesData.objects.values('month','sales'))
         chartData={
            'labels':[entry['month'] for entry in salesData],
            'datasets':[{
                'label':'Sales Data',
                'data':[entry['sales'] for entry in salesData],
                'backgroundColor': 'rgba(75,192,192,0.2)',
                'borderColor': 'rgba(75,192,192,1)',
                'borderWidth': 1
            }]
        }
    return JsonResponse(chartData)
        
        