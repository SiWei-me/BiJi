from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def main(request):
    my_data = [
        {'name': 'Data 1', 'summary': 'Summary 1', 'url': './main/1'},
        {'name': 'Data 2', 'summary': 'Summary 2', 'url': './main/2'},
        {'name': 'Data 3', 'summary': 'Summary 3', 'url': './main/3'}
    ]
    context = {'datas': my_data}
    return render(request, 'main.html', context)
