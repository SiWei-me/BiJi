from django.shortcuts import render, HttpResponse
import json
import os


# Create your views here.

def index(request):
    return render(request, 'index.html')


def main(request):
    if not os.path.exists('./data/info.json'):
        with open('./data/info.json', 'w') as f:
            f.write(json.dumps({'num':0,'data':[]}))
    with open('./data/info.json', 'r') as f:
        info = f.read()
    info = json.loads(info)
    info_data = []
    for i in info['data']:
        summary = i['summary']
        if len(i['summary']) < 30:
            summary = i['summary'] + (30 - len(i['summary'])) * '&emsp;'
        info_data.append({'name': i['name'], 'summary': summary, 'url': f'./{str(i["id"]).zfill(6)}'})
    context = {'datas': info_data}
    return render(request, 'main.html', context)


def edit(request, page_id):
    with open('./data/info.json', 'r') as f:
        info = f.read()
    info = json.loads(info)
    page_id = int(page_id)
    n = 0
    for i in info['data']:
        if page_id == i['id']:
            break
        n += 1
    context = {'page_id': page_id,
               'page_name': info['data'][n]['name']}
    open(f'./data/{page_id}.json', 'a+').close()
    with open(f'./data/{page_id}.json', 'r') as f:
        text = f.read()
    print(text)
    if text is not '':
        text = json.loads(text)
        print('Y')
        return render(request, 'edit.html', context={'text': text['text'],
                                                     'page_id': page_id,
                                                     'page_name': info['data'][n]['summary']})
    return render(request, 'edit.html', context)


def edit_add(request):
    return render(request, 'edit.html', context={'page_id': ''})
