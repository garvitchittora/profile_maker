from django.shortcuts import render
from core.models import profile 



def main(request):
    return render(request, "index.html")

def display(request):
    if request.method == "POST":
        print(request.POST, request.FILES) 
        name = request.POST['name']
        img = request.FILES.get('image')
        cover_img=request.FILES.get('cover_image')
        discription=request.POST['discription']
        education=request.POST['education']
        experience=request.POST['experience']
        skills=request.POST['skills']
        linkedin_url=request.POST['linkedin_url']

        obj = profile.objects.create( 
                             name = name,  
                             img = img ,
                             cover_img=cover_img,
                             discription=discription,
                             education=education,
                             experience=experience,
                             skills=skills,
                             linkedin_url=linkedin_url  
                             ) 
        obj.save() 
        
    make=profile.objects.last()
    return render(request, "index1.html",{'make':make})

