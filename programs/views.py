from django.shortcuts import render, redirect
from .models import Program


def program_list(request):
    programs = Program.objects.all()
    ctx = {'programs':programs}
    return render(request,'programs/program-list.html', ctx)


def program_create(request):
    title = request.POST.get('title')
    description = request.POST.get('description')


    if title and description :
        Program.objects.create(
            title=title ,
            description=description,
        )
        return redirect('programs:list')

    return render(request, 'programs/program-create.html')



