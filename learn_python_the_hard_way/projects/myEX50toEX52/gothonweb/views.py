# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import Context, loader
from django.shortcuts import render
from django.template import RequestContext
from django.core.urlresolvers import reverse
from gothonweb import map

def index(request):
    #t = loader.get_template('gothonweb/index.html')
    request.session['room'] = map.START
    return HttpResponseRedirect(reverse('gothonweb:gameengine'))

def hello(request):
    if request.method == 'GET':
        return render(request, 'gothonweb/hello_form.html')
    elif request.method == 'POST':
        arg = {'name': 'Mike', 'greet1': 'Yahoo~~'}
        if request.POST.get('sname') and request.POST.get('mygreet'):
            arg['name'] = request.POST.get('sname')
            arg['greet'] = request.POST.get('mygreet')
            greeting = "%s, %s" %(arg['greet'], arg['name'])                        
        else:
            arg['name'] = "Mike"
            arg['greet'] = "Yahoo~~"
            greeting = ""
            
        #greeting = "%s, %s" %(arg['greet'], arg['name'])    
        return render(request, 'gothonweb/index.html', {
                        'greeting': greeting,})
        #return HttpResponseRedirect(reverse('gothonweb:index', args=(arg,)))

def game(request):
    #return render(request, 'gothonweb/hello_form.html')
    if request.method == 'GET':
        if request.session.get('room', False):
            current_room = request.session['room']
            
            if current_room.name == "death":
                return render(request, 'gothonweb/you_died.html')
            else:
                return render(request, 'gothonweb/show_room.html',
                          {'room': request.session['room'],})
        else:
            return HttpResponseRedirect(reverse('gothonweb:hello'))
    
    elif request.method == 'POST':
        if request.session.get('room', False) and \
            request.POST.get('useraction'):
            action = request.POST.get('useraction')
            current_room = request.session['room']
            next_room = current_room.go(action)
            request.session['room'] = next_room
            return HttpResponseRedirect(reverse('gothonweb:gameengine'))
