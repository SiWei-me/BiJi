import json
import os

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def stave(request):
    text = request.POST.get('text')
    page_id = request.POST.get('page_id')
    page_intr = request.POST.get('page_intr')
    if page_id is '':
        page_id = 0
    page_id = int(page_id)
    page_name = request.POST.get('page_name')
    with open('./data/info.json', 'r') as f:
        info = f.read()
    info = json.loads(info)
    print(page_id)
    print(type(page_id))
    print(page_name)
    print(type(page_name))
    print(text)
    print(type(text))
    for i in info['data']:
        print(i)
        print(page_id == i['id'])
        if page_id == i['id']:
            print("a")
            with open(f'./data/{page_id}.json', 'w') as f:
                f.write(json.dumps({'text': text}))
                return HttpResponse('Ok')

    info['num'] = info['num'] + 1
    id = int(info['data'][-1]['id']) + 1
    info['data'].append({
        'id': id,
        'name': page_name,
        'summary': page_intr
    })
    with open(f'./data/info.json', 'w') as f:
        f.write(json.dumps(info))
    with open(f'./data/{id}.json', 'w') as f:
        f.write(json.dumps({'text': text}))
    return HttpResponse(json.dumps({'msg': 'Ok', 'page_id': id}))


@csrf_exempt
def delete(request):
    page_id = request.POST.get('page_id')
    page_id = int(page_id)
    with open('./data/info.json', 'r') as f:
        info = f.read()
    info = json.loads(info)
    n = 0
    for i in info['data']:
        print(page_id)
        print(type(page_id))
        print(i['id'])
        print(type(i['id']))
        if page_id == i['id']:
            del info['data'][n]
            break
        n += 1
    info['num'] = info['num'] - 1
    print(info)
    with open(f'./data/info.json', 'w') as f:
        f.write(json.dumps(info))
    os.remove(f'./data/{page_id}.json')
    return HttpResponse('Ok')


@csrf_exempt
def reintr(request):
    page_id = request.POST.get('page_id')
    page_id = int(page_id)
    page_intr = request.POST.get('new_intr')
    with open('./data/info.json', 'r') as f:
        info = f.read()
    info = json.loads(info)
    n = 0
    for i in info['data']:
        if page_id == i['id']:
            break
        n += 1
    info['data'][n]['summary'] = page_intr
    with open(f'./data/info.json', 'w') as f:
        f.write(json.dumps(info))
    return HttpResponse('Ok')


@csrf_exempt
def rename(request):
    page_id = request.POST.get('page_id')
    page_id = int(page_id)
    new_name = request.POST.get('new_name')
    with open('./data/info.json', 'r') as f:
        info = f.read()
    info = json.loads(info)
    n = 0
    for i in info['data']:
        if page_id == i['id']:
            break
        n += 1
    info['data'][n]['name'] = new_name
    with open(f'./data/info.json', 'w') as f:
        f.write(json.dumps(info))
    return HttpResponse('Ok')
