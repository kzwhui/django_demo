import json
from django.shortcuts import render
from django.http import HttpResponse
from hello_app.models import TStudentInfo

# Create your views here.
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def test_db(request):
    ret_root = {'name' : '', 'score' : 0}

    if not request.GET:
        return render(request, 'db_test.html', ret_root)

    id = request.GET['id']
    rows = TStudentInfo.objects.filter(c_id=id)
    if not rows:
        return render(request, 'db_test.html', ret_root)

    ret_root['name'] = rows[0].c_name
    ret_root['score'] = rows[0].c_score
    return render(request, 'db_test.html', ret_root)

def test_json(request):
    ret_root = {'name' : '', 'score' : 0}

    if not request.GET:
        return HttpResponse(json.dumps(ret_root))

    id = request.GET['id']
    rows = TStudentInfo.objects.filter(c_id=id)
    if not rows:
        return HttpResponse(json.dumps(ret_root))

    ret_root['name'] = rows[0].c_name
    ret_root['score'] = rows[0].c_score
    return HttpResponse(json.dumps(ret_root))