from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
import math
from datetime import date
import time
# from string import strip
from datetime import datetime
from django.template.loader import render_to_string, get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User
import razorpay
from .models import Payment,Packages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



from telusko.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
# Create your views here.

def index(request):

    dests = Packages.objects.all()
    destsWithOffer = Packages.objects.filter(offer=True)
    # print(destsWithOffer)
    testimonials = Contact.objects.filter(subject = "testimonial")
    # print(testimonials)
    # print(testimonials.count())
    return render(request, 'index.html', {'dests': dests, 'testimonials':testimonials, 'testimonialCount':testimonials.count(), 'destsWithOffer': destsWithOffer.count()})


def about(request):
    return render(request, 'about.html')

def Package(request):

    dests = Packages.objects.all()
    return render(request, 'packages.html', {'dests': dests})


def contact(request):
    if request.method == 'POST':
        yourName = request.POST['yourName']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # if request.user.is_authenticated:
        #     con = Contact(yourName=yourName, email=email, subject=subject, message=message)
        #     con.save()
        #     return redirect('contact')
        # else:
        #     return redirect('login')

        c = Contact(yourName=yourName, email=email, subject=subject, message=message)
        c.save()

        return redirect('contact')

    else:
        return render(request, 'contact.html')



def destination_details(request,id):
    dest = Packages.objects.get(id=id)
    # print(dest)
    # print("Price = ", dest.price)
    # print("Loc = ", dest.name)

    request.session['pkg_title'] = dest.pkg_title
    request.session['pkg_price'] = dest.pkg_price
    request.session['pkg_days'] = dest.pkg_days
    request.session['pkg_to'] = dest.pkg_to
    request.session['pkg_from'] = dest.pkg_from
    # request.session['dep_dt'] = datetime.strptime(dest.dep_date, '%Y-%m-%d').date()
    request.session['dep_date'] = dest.dep_date.isoformat()

    # print(request.session['name'])
    # print(request.session['price'])
    # print("Days = ", request.session['day'])

    return render(request,'package_details.html',{'dest':dest})


@login_required(login_url='/accounts/login')
def booking(request, id):
    pkg=Packages.objects.filter(id=id)
    # context={'des':pkg}
    destinationName = request.session['pkg_title']
    destinationPrice = request.session['pkg_price']
    
    # dep=request.session['dep_date']
    # d_date=datetime.fromisoformat(dep)
    # request.session['dep_date']=d_date

    # print(destinationName)
    # print(destinationPrice)

    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        fromCity = request.POST['fromCity']
        toCity = request.POST['toCity']
        depatureDate = request.POST['depatureDate']
        days = request.POST['days']
        noOfRooms = int(request.POST['noOfRooms'])
        noOfAdults = int(request.POST['noOfAdults'])
        noOfChildren = int(request.POST['noOfChildren'])
        email = request.POST['email']
        phoneNo = request.POST['phoneNo']
        # totalAmount = int(request.POST['totalAmount']*noOfAdults)
        totalAmount = int(request.POST['totalAmount'])
        # price=pkg.pkg_price

        request.session['fname'] = firstName
        request.session['lname'] = lastName
        request.session['to_city'] = toCity
        request.session['from_city'] = fromCity
        request.session['depature_date'] = depatureDate
        request.session['days'] = days
        request.session['no_of_rooms'] = noOfRooms
        request.session['no_of_adults'] = noOfAdults
        request.session['no_of_children'] = noOfChildren
        request.session['email'] = email
        request.session['phone_no'] = phoneNo
        request.session['total_amount'] = totalAmount
        # request.session['total_amount'] = noOfAdults*price

        requiredRooms = 1
        if noOfAdults/3 > 1:
            requiredRooms = math.ceil(noOfAdults/3)

        if noOfRooms < requiredRooms:
            noOfRooms = requiredRooms - noOfRooms
            messages.info(request, 'For adding more travellers, Please add' + str(noOfRooms) +' more rooms')
            return redirect('booking', id)

        if noOfRooms > noOfAdults:
            messages.info(request, 'Minimum 1 Adult is required per Room')
            return redirect('booking', id)

        if (noOfAdults + noOfChildren)/4 > 1:
            requiredRooms = math.ceil((noOfAdults + noOfChildren)/4)

        if noOfRooms < requiredRooms:
            noOfRooms = requiredRooms - noOfRooms
            messages.info(request, 'For adding more travellers, Please add'+ str(noOfRooms) + 'more rooms')
            return redirect('booking',id)

        noOfRooms = requiredRooms
        request.session['no_of_rooms'] = noOfRooms
        # print("No of rooms = ", noOfRooms)
        # print("Working")
        # book = Booking(firstName=firstName, lastName=lastName, fromCity=fromCity, toCity=toCity, depatureDate=depatureDate, arrivalDate=arrivalDate, noOfRooms=noOfRooms, noOfAdults=noOfAdults, noOfChildren=noOfChildren, email=email,phoneNo=phoneNo, totalAmount=totalAmount)

        # book.save()
        return redirect('receipt')
    else:
        return render(request, 'booking.html')

# @login_required(login_url='/accounts/login')
# def booking(request, pk):
#     pkg=Packages.objects.filter(id=pk)
#     context={'des':pkg}
#     pkg_to=pkg.values('pkg_from')
#     request.session['pkg_to']=pkg_to
#     context={'pkg_to':pkg_to}
    
#     if request.method == 'POST':
#         firstName = request.POST['firstName']
#         lastName = request.POST['lastName']
#         fromCity = request.POST['fromCity']
#         toCity = request.POST['toCity']
#         depatureDate = request.POST['depatureDate']
#         days = request.POST['days']
#         noOfRooms = int(request.POST['noOfRooms'])
#         noOfAdults = int(request.POST['noOfAdults'])
#         noOfChildren = int(request.POST['noOfChildren'])
#         email = request.POST['email']
#         phoneNo = request.POST['phoneNo']
#         totalAmount = int(request.POST['totalAmount']*noOfAdults)
#         price=pkg.pkg_price


#         return redirect('receipt')
#     else:
#         return render(request, 'booking.html',context)


# def search(request):
#     query = request.GET.get('q')
#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')
    
#     # dests = Packages.objects.filter(pkg_title__icontains=query)
    
#     if min_price:
#         dests = Packages.objects.filter(pkg_price__gt=min_price)
#     elif max_price:
#         dests = dests.filter(pkg_price__ls=max_price)
#     elif query:
#         dests = Packages.objects.filter(pkg_title__icontains=query)
    
#     return render(request, 'search.html', {'dests': dests, 'query': query})

def search(request):
    query = request.GET.get('q')
    # min_price = request.GET.get('min_price')
    # max_price = request.GET.get('max_price')
    
    dests = Packages.objects.filter(pkg_title__icontains=query)
    
    # if min_price and max_price:
    #     dests = dests.filter(pkg_price__range=(min_price, max_price))
    
    return render(request, 'search.html', {'dests': dests, 'query': query})

'''
def search(request):
    print(request.GET.urlencode())
    # dests = Destination.objects.all()
    query = request.GET.urlencode()
    # budget = request.GET['budget']
    price = Destination.objects.all()
    # print(price.price)
    # print(query)
    # print("Price = ", budget)
    dests = Destination.objects.filter(name__icontains = query)
    # print(dests)
    # dests = Destination.objects.filter(price__lt = budget)
    # print(dests)

    return render(request, 'search.html', {'dests' : dests, 'query':query})
    # return HttpResponse('This is search')
'''



@login_required(login_url='/accounts/login')
def orderHistory(request):

    bookings = ConfirmBooking.objects.filter(userName = request.user.username,cancel=0)
    destinations = Packages.objects.all()
    context={'bookings':bookings, 'destinations':destinations,'pagename':'my bookings'}

    return render(request, 'dashboard/orderHistory.html',context)
def CancelorderHistory(request):

    bookings = ConfirmBooking.objects.filter(userName = request.user.username,cancel=1)
    destinations = Packages.objects.all()
    context= {'bookings':bookings, 'destinations':destinations,'pagename':'cancelled bookings'}

    return render(request, 'dashboard/orderHistory.html',context)

def delete_destination(request, id):

    if request.method == 'POST':

        message = render_to_string('order_cancel_body.html', {'orderId':id})
        msg = EmailMessage(
            'Dian Tours',
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email]
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()
        reason=request.POST['reason']

        # ConfirmBooking.objects.filter(id=id).delete()
        pkg=ConfirmBooking.objects.get(id=id)
        pkg.cancel=1
        pkg.cancel_reason=request.POST.get('reason')
        pkg.save()


        return redirect('orderHistory')
    
# client = razorpay.Client(auth=(RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY))
# def pmnt(request):
    

#     DATA = {
#     "amount": int(100000),
#     "currency": "INR",
#     }

#     payment_order=client.order.create(dict(data=DATA,payment_capture=1))
#     payment_order_id=payment_order['id']

#     context={
#         'amount':int(500000),'api_key':RAZORPAY_API_KEY,'order_id':payment_order_id
#     }
#     return render(request,'recipt.html',context)

                       
    
# def cancelpackage(request): 
# # Get the reason for cancellation from the form data
#     reason = request.POST.get('reason')

#     Cancellation.objects.create(
#             user=request.user,
#             reason=reason
#         )

#     # Save the reason for cancellation to the database
   
#     # ... save the reason to the database ...

#     # Return a JSON response to the client
#     return render(request, 'home.html')

@login_required(login_url='/accounts/login')
def receipt(request):
    first_name = request.session.get('fname')
    # print(first_name)
    last_name = request.session.get('lname')
    # print(last_name)
    current_url = request.build_absolute_uri()

    # Append "/success" to the end of the current URL
    callback_url = current_url + "/success"

    tour_amount = int(request.session.get('total_amount')) #Per person
    # print(tour_amount)
    adults = int(request.session.get('no_of_adults'))
    # print(adults)
    rooms = int(request.session.get('no_of_rooms'))
    # print(rooms)
    children = int(request.session.get('no_of_children'))
    # print(adults)
    if rooms > 1:
        totalCost = tour_amount*adults + tour_amount*children/2 + rooms*tour_amount/4
    else:

        totalCost = tour_amount*adults + tour_amount*children/2
    request.session['total_amount'] =(totalCost)
    # request.session['total_amount'] =str(totalCost)

    # print(totalCost)
    # request.session['total_amount'] = tour_amount

    today = date.today()

    t = time.localtime()
    currentTime = time.strftime("%H:%M:%S", t)
    return render(request,'receipt.html',{'callback_url':callback_url,'totalCost':totalCost,'total_paisa':totalCost*100, 'date':today, 'currentTime':currentTime})


def confirm_booking(request):
    if request.method == 'POST':
        fullName = request.POST['fullName']
        fromCity = request.POST['fromCity']
        toCity = request.POST['toCity']
        depatureDate = request.POST['depatureDate']
        arrivalDate = request.POST['days']
        noOfRooms= int(request.POST['noOfRooms'])
        noOfAdults  = int(request.POST['noOfAdults'])
        noOfChildren = int(request.POST['noOfChildren'])
        email = request.POST['email']
        phoneNo = request.POST['phoneNo']
        amountPerPerson = request.POST['amountPerPerson']
        totalAmount = float(request.POST['totalAmount'])
        userName = request.user.username
        pkg_title=request.session['pkg_title']


        books = ConfirmBooking(fullName=fullName, pkg_title=pkg_title, toCity=toCity,
                       depatureDate=depatureDate.strip(), days=arrivalDate, noOfRooms=noOfRooms, noOfAdults=noOfAdults,
                       noOfChildren=noOfChildren, email=email, phoneNo=phoneNo, amountPerPerson=amountPerPerson,
                       totalAmount=totalAmount, userName=userName)
        books.save()

        message = render_to_string('order_placed_body.html', {'fullName':fullName, 'fromCity':fromCity, 'toCity':toCity, 'depatureDate':depatureDate,'arrivalDate':arrivalDate,'noOfRooms':noOfRooms,'noOfAdults':noOfAdults,'noOfChildren':noOfChildren,'email':email,'phoneNo':phoneNo,'amountPerPerson':amountPerPerson, 'totalAmount':totalAmount})
        msg = EmailMessage(
            'Dian Tours',
            message,
            settings.EMAIL_HOST_USER,
            [request.user.email]
        )
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()

        # print("Mail successfully sent")

        # print("User Added")

        return redirect('/')
    else:
        return render(request,'booking.html')
    
def pmnt(request):
    print(settings.RAZORPAY_API_KEY)
    print(settings.RAZORPAY_API_SECRET_KEY)
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET_KEY))
    print(client)
    amount = 1000  # Replace 1000 with the actual amount you want to charge
    order_amount = int(amount * 100)  # Razorpay requires the amount in paise

    data = {
        'amount': order_amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1'
    }

    Payment=Payment(name=name,amount=amount,payment_id=Payment['id'])
    Payment.save()
    try:
        razorpay_order = client.order.create(data=data)
        order_id = razorpay_order['id']
        return render(request, 'recipt.html', {'order_id': order_id, 'amount': amount})
    except razorpay.errors.BadRequestError as e:
        print(e)
        return HttpResponse("An error occurred while creating the Razorpay order.")         

@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        print(a)
    return render(request,"success.html")