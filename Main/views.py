from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


def main(request):
    my_data = [
        {'name': 'Data 1', 'summary': 'Summary 1', 'url': './000001'},
        {'name': 'Data 2', 'summary': 'Summary 2', 'url': './000002'},
        {'name': 'Data 3', 'summary': 'Summary 3', 'url': './000003'}
    ]
    context = {'datas': my_data}
    return render(request, 'main.html', context)


def edit(request, page_id):
    context = {'page_id': page_id}
    return render(request, 'edit.html', context)


def edit_add(request):
    return render(request, 'edit.html', context={'page_id': ''})
