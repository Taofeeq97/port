from django.shortcuts import render, redirect
from .models import Profile, Skill, Project, Testimony, Message
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.

#
# def index(request):
#     profile = Profile.objects.get(email='otutaofeeqi@gmail.com')
#     first_name = profile.get_first_name().split(' ')[1]
#     hobbies = profile.hobby.split(',')
#     skills = Skill.objects.all()
#     project = Project.objects.all()
#     testimony = Testimony.objects.all()
#
#     if request.method == "POST":
#         data = {
#             'name': request.POST.get('name'),
#             'email': request.POST.get('email'),
#             'subject': request.POST.get('subject'),
#             'message': request.POST.get('message'),
#         }
#         Message.create_message(**data)
#         messages.success(request,'Message sent successfully')
#         return redirect('index')
#
#     context = {
#         'profile': profile,
#         'first_name': first_name,
#         'hobbies': hobbies,
#         'skills': skills,
#         'project': project,
#         'testimony': testimony
#
#     }
#     return render(request, 'portfolio/index.html', context)

class HomePageView(ListView):
    template_name = 'portfolio/index.html'
    queryset = Profile.objects.get()
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = context['profile']
        first_name = profile.get_first_name().split(' ')[1]
        hobbies = profile.hobby.split(',')
        skills = Skill.objects.all()
        project = Project.objects.all()
        testimony = Testimony.objects.all()
        context['first_name'] = first_name
        context['hobbies'] = hobbies
        context['skills'] = skills
        context['project'] = project
        context['testimony'] = testimony
        return context

    # def get(self, request):
    #     profile = Profile.objects.get(email='otutaofeeqi@gmail.com')
    #     first_name = profile.get_first_name().split(' ')[1]
    #     hobbies = profile.hobby.split(',')
    #     skills = Skill.objects.all()
    #     project = Project.objects.all()
    #     testimony = Testimony.objects.all()
    #     context = {
    #         'profile': profile,
    #         'first_name': first_name,
    #         'hobbies': hobbies,
    #         'skills': skills,
    #         'project': project,
    #         'testimony': testimony
    #         }
    #     return render(request, 'portfolio/index.html', context)

    def post(self, request):
        data = {
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'subject': request.POST.get('subject'),
            'message': request.POST.get('message'),
        }
        Message.create_message(**data)
        messages.success(request, 'Message sent successfully, I will respond to your message shortly')
        return redirect('index')
