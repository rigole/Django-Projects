from django.shortcuts import render
from .models import Profile
# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        university = request.POST.get("university", "")
        school = request.POST.get("school", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")

        profile = Profile(name=name, email=email,phone=phone,summary=summary,degree=degree,university=university,school=school,previous_work=previous_work,skills=skills)
        profile.save()
    return render(request, 'pdf/form.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    return render(request,'pdf/resume.html',{'user_profile':user_profile})
