from django.contrib import messages
from django.shortcuts import render, redirect ,HttpResponse
from .models import Notes, Homework , Todo
from .forms import NotesForm,HomeworkForm,SearchForm ,TodoForm
from youtubesearchpython import VideosSearch
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return render(request,'home.html')


def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST,label_suffix='')
        if form.is_valid():
            notes = Notes.objects.create(user=request.user,title=request.POST.get('title'),
                                         description=request.POST.get('description'))
            notes.save()
            messages.add_message(request,messages.SUCCESS,f'Notes added from {request.user.username}')
            return redirect('notes')
    else:
        form = NotesForm(label_suffix='')
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'notes.html',context)


def delete_notes(request,pk=None):
    obj = Notes.objects.get(id=pk)
    obj.delete()
    return redirect('notes')


def details_notes(request,pk=None):
    obj = Notes.objects.get(id=pk)
    return render(request,'notes_detail.html',{'notes':obj})


def homework(request,pk=None):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            obj = Homework.objects.create(user=request.user,subject=data['subject'],title=data['subject'],
                                          description=data['description'],due=data['due'],is_complete=data[
                    'is_complete'])
            obj.save()
            return redirect('homework')
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    print("======================",homework)
    if len(homework) == 0:
        homework_done = True

    else:
        homework_done = False

    return render(request,'homework.html',{'homeworks':homework,'homework_done':homework_done,'form':form})


def homework_update(request,pk=None):
    homework = Homework.objects.get(id=pk)
    print(homework)
    if homework.is_complete == True:
        homework.is_complete = False
    else:
        homework.is_complete = True
    homework.save()
    return redirect('homework')


def delete_homework(request,pk=None):
    homework = Homework.objects.get(id=pk)
    homework.delete()
    return redirect('homework')


def youtube(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cln = form.cleaned_data
            video_search = VideosSearch(cln['search'],limit=100)
            searchres = video_search.result()
            result_list = []
            for video in searchres['result']:
                result_dict = {
                    'title': video['title'],
                    'description': None,
                    'channel': video['channel']['name'],
                    'duration': video['duration'],
                    'view': video['viewCount']['short'],
                    'published': video['publishedTime'],
                    'thumbnail':video['thumbnails'][0]['url'],
                    'link':video['link']
                }

                desc = ''
                if video['descriptionSnippet']:
                    for j in video['descriptionSnippet']:
                        desc = desc + j['text']
                result_dict['description'] = desc
                result_list.append(result_dict)



            return render(request,'youtube.html',{'form':form,'results':result_list})
            # return redirect('youtube')


    else:
        form = SearchForm()
    return render(request,'youtube.html',{'form':form})


def todo(request):
    obj = Todo.objects.filter(user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            datavar = form.cleaned_data
            savedata = Todo.objects.create(user=request.user,title=datavar['title'],is_finished=datavar[
                'is_finished'])
            savedata.save()
            return redirect('todo')
    else:
        form = TodoForm()
    todo = Todo.objects.filter(user=request.user)
    if len(todo) == 0:
        todos_done = True
    else:
        todos_done = False

    return render(request,'todo.html',{'todo':obj,'form':form,'todos_done':todos_done})


def todo_update(request,pk=None):
    todo = Todo.objects.get(id=pk)
    if todo.is_finished == True:
        todo.is_finished = False
    else:
        todo.is_finished = True
    todo.save()
    return redirect('todo')


def todo_delete(request,pk=None):
    obj = Todo.objects.get(id=pk)
    obj.delete()
    return redirect('todo')


def books(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            pass



    return render(request,'books.html',{'form':form})