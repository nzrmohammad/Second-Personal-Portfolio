from django.shortcuts import render
from django.http import JsonResponse
from .models import Home, About, Service, Skill, Testimonial, Category, Portfolio, Article, ContactUs, Contact, Social_Profile
from .forms import ContactUsForm

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def home(request):
    home = Home.objects.latest('updated')
    about = About.objects.latest('updated')
    services = Service.objects.all()
    skill = Skill.objects.all()
    categories = Category.objects.filter()
    portfolio = Portfolio.objects.all()
    testimonials = Testimonial.objects.all()
    article = Article.objects.all().order_by('-publish')[:3]
    contact = Contact.objects.latest('updated')
    social_profile = Social_Profile.objects.all()
    context = {
        'home':home,
        'about':about,
        'skill':skill,
        'services':services,
        'testimonials':testimonials,
        'categories':categories,
        'portfolios':portfolio,
        'article':article,
        'contact':contact,
        'form':ContactUsForm,
        'social_profile':social_profile,
    }

    if request.method == "POST":
        contactUsform = ContactUs()
        contactUsform.name = request.POST.get('name')
        contactUsform.email = request.POST.get('email')
        contactUsform.subject = request.POST.get('subject')
        contactUsform.message = request.POST.get('message')
        contactUsform.save()
        return JsonResponse({'msg':'Success'})


    return render(request, 'index.html',context)


def detail(request,id):

    portfolio = Portfolio.objects.filter(id=id)

    context = {

        'portfolios':portfolio,

    }

    return render(request, 'project-details-image.html',context)