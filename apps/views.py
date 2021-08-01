from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail
from website import settings
from django.contrib import messages

# Get all data from database and send to template


def main(request):
    # query to get data
    about = About.objects.all()
    service = Service.objects.all()
    review = Review.objects.all()
    feature = Feature.objects.all()
    package = Package.objects.all()
    blogs = Blog.objects.all()[0:3]
    reviews = Review.objects.all()
    medias = SocialMedia.objects.all()
    company = ComapnyInfo.objects.all()
    teams = Team.objects.all()
    # adding it to dictionary
    data = {'about': about, 'services': service, 'reviews': review,
            'features': feature, 'packages': package, 'blogs': blogs, 'company': company, 'medias': medias, 'teams': teams}
    # sending data to template called index
    return render(request, "apps/index.html", data)


def send_now(subject, name, message, email, receiver_mail, request):
    # calling send_email function of django
    send_mail(
        subject + "- Sunsari Network and Cable",
        "Name:" + name + "\n" + "Message: " + message,
        email,
        (receiver_mail,),
        fail_silently=False,
    )
    messages.success(request, "Email has been sent successfully.")


def send_email(request):

    if request.method == 'POST':
        # getting Post request
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        receiver_mail = settings.receiver_email

        # Checking email sent and sending messages
        if(send_email):
            send_now(subject, name, message, email, receiver_mail, request)
        else:
            messages.error(request, "Email not sent.")

    return redirect('abc')
