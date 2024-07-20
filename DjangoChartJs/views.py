from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

PERSIAN_MONTH = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']


class IndexView(TemplateView):
    template_name = 'index.html'


class SampleBarDataView(View):
    def get(self, request, *args, **kwargs):
        datasets = [
            {
                "label": 'My First Dataset',
                "data": [65, 59, 80, 81, 56, 55, 40, 56, 55, 40, 59, 80],
            },
            {
                "label": 'My First Dataset',
                "data": [65, 59, 80, 81, 56, 55, 40, 56, 55, 40, 59, 80],
            }
        ]
        return JsonResponse({
            "labels": PERSIAN_MONTH,
            "datasets": datasets
        })


class SampleLineDataView(View):
    def get(self, request, *args, **kwargs):
        datasets = [
            {
                "label": 'My First Dataset',
                "data": [55, 40, 59, 80, 65, 59, 80, 81, 56, 55, 40, 56, ],
            },
            {
                "label": 'My First Dataset',
                "data": [40, 56, 55, 40, 59, 80, 65, 59, 80, 81, 56, 55, ],
            }
        ]
        return JsonResponse({
            "labels": PERSIAN_MONTH,
            "datasets": datasets
        })


class SampleDoughnutDataView(View):
    def get(self, request, *args, **kwargs):
        labels = [
            'America',
            'Asia',
            'Europe',
            'Oceania',
        ]
        datasets = [
            {
                "label": 'Economy Percent',
                "data": [60, 13, 12, 0.5],
            }
        ]
        return JsonResponse({
            "labels": labels,
            "datasets": datasets
        })


class SamplePieDataView(View):
    def get(self, request, *args, **kwargs):
        labels = [
            'America',
            'Asia',
            'Europe',
            'Oceania',
        ]
        datasets = [
            {
                "label": 'Economy Percent',
                "data": [30, 13, 12, 3],
            }
        ]
        return JsonResponse({
            "labels": labels,
            "datasets": datasets
        })


class SampleRadarDataView(View):
    def get(self, request, *args, **kwargs):
        labels = [
            'America',
            'Asia',
            'Europe',
            'Oceania',
            'Mars',
        ]
        datasets = [
            {
                "label": 'Economy Percent',
                "data": [30, 13, 12, 3, 25],
            },
            {
                "label": 'Economy Population ',
                "data": [12, 3, 25,30, 13, ],
            }
        ]
        return JsonResponse({
            "labels": labels,
            "datasets": datasets
        })
