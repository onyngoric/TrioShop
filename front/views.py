from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as user_login
from django.contrib.auth.decorators import login_required
from front.forms import AdForm, AdImageForm
from .models import *
from django.db.models import Q

# Create your views here.

def home(request):
        if request.method == 'POST':
            if request.POST.get('search'):
                search = request.POST.get('search')
                ad=Ad.objects.filter(title__icontains=search).prefetch_related('adimages_set').all()
                return render(request, 'view.html', {'ad':ad})
            if request.POST.get('3D1'):
                ad = Ad.objects.filter(category='3D Printing Technology').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('3D2'):
                ad = Ad.objects.filter(category='Robotics').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Air1'):
                ad = Ad.objects.filter(category='Aircrafts & Airplanes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Air2'):
                ad = Ad.objects.filter(category='Aircraft Dealers').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Air3'):
                ad = Ad.objects.filter(category='Flight Schools').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Air4'):
                ad = Ad.objects.filter(category='Parts, Tires & Accessories').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Air5'):
                ad = Ad.objects.filter(category='Rentals, Lease & Financing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto1'):
                ad = Ad.objects.filter(category='ATVs & Snowmobiles').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto2'):
                ad = Ad.objects.filter(category='Bikes, Boats & Watercraft').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto3'):
                ad = Ad.objects.filter(category='Cars & Heavy Trucks').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto4'):
                ad = Ad.objects.filter(category='Damaged & Accident Vehicles').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto5'):
                ad = Ad.objects.filter(category='Automobile Dealers').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto6'):
                ad = Ad.objects.filter(category='Driving Schools').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto7'):
                ad = Ad.objects.filter(category='Parts, Tires & Accessories').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto8'):
                ad = Ad.objects.filter(category='Rentals, Lease & Financing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto9'):
                ad = Ad.objects.filter(category='RoadSide Assistance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Auto10'):
                return redirect('view')
            if request.POST.get('Auto10'):
                return redirect('view')
            if request.POST.get('Bis1'):
                ad = Ad.objects.filter(category='Renting').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Bis2'):
                ad = Ad.objects.filter(category='Opportunities').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Bis3'):
                ad = Ad.objects.filter(category='Cryptocurrencies').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Bis4'):
                ad = Ad.objects.filter(category='Finance & Investments').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Bis5'):
                ad = Ad.objects.filter(category='Franchise/ Trading').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Bis6'):
                ad = Ad.objects.filter(category='Partnership & Joint Ventures').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Bis7'):
                return redirect('view')
            if request.POST.get('Cls1'):
                ad = Ad.objects.filter(category='Art, Music & Dance Classes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls2'):
                ad = Ad.objects.filter(category='Computer - Multimedia Classes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls3'):
                ad = Ad.objects.filter(category='Continuing Education').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls4'):
                ad = Ad.objects.filter(category='Language Classes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls5'):
                ad = Ad.objects.filter(category='Online Bootcamps & Mastermind').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls6'):
                ad = Ad.objects.filter(category='Sports & Wellness Classes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls7'):
                ad = Ad.objects.filter(category='Tutoring - Private Lessons').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Cls8'):
                return redirect('view')
            if request.POST.get('Clot1'):
                ad = Ad.objects.filter(category='Baby Fashions').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Clot2'):
                ad = Ad.objects.filter(category='Men Fashions').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Clot3'):
                ad = Ad.objects.filter(category='Teenage Fashions').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Clot4'):
                ad = Ad.objects.filter(category='Women Fashions').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Clot5'):
                return redirect('view')
            if request.POST.get('Com1'):
                ad = Ad.objects.filter(category='Artists, Musicians & Bands').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com2'):
                ad = Ad.objects.filter(category='Auctions / Groups').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com3'):
                ad = Ad.objects.filter(category='Carpool & Rideshare').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com4'):
                ad = Ad.objects.filter(category='Charity, Donate').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com5'):
                ad = Ad.objects.filter(category='Community Activities').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com6'):
                ad = Ad.objects.filter(category='Elderly Home Assistance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com7'):
                ad = Ad.objects.filter(category='Household Help').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com8'):
                ad = Ad.objects.filter(category='Lost & Found').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com9'):
                ad = Ad.objects.filter(category='Public Announcements').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com10'):
                ad = Ad.objects.filter(category='Recreation').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Com11'):
                return redirect('view')
            if request.POST.get('Con1'):
                ad = Ad.objects.filter(category='Attachments').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con2'):
                ad = Ad.objects.filter(category='Building Supplies').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con3'):
                ad = Ad.objects.filter(category='Construction Equipment').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con4'):
                ad = Ad.objects.filter(category='Damaged & Accident Vehicles').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con5'):
                ad = Ad.objects.filter(category='Farming Equipment').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con6'):
                ad = Ad.objects.filter(category='Rentals, Lease & Financing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con7'):
                ad = Ad.objects.filter(category='RoadSide Assistance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con8'):
                ad = Ad.objects.filter(category='Trailer').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con9'):
                ad = Ad.objects.filter(category='Trucks').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Con10'):
                return redirect('view')
            if request.POST.get('Elec1'):
                ad = Ad.objects.filter(category='Alarms & Security Systems').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Elec2'):
                ad = Ad.objects.filter(category='Cameras, Camcorders & Drones').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Elec3'):
                ad = Ad.objects.filter(category='Computer & Gaming').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Elec4'):
                ad = Ad.objects.filter(category='Media & Streaming Equipment').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Elec5'):
                ad = Ad.objects.filter(category='Projectors, Tablets & TV').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Elec6'):
                return redirect('view')
            if request.POST.get('Frl1'):
                ad = Ad.objects.filter(category='Content Creation').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Frl2'):
                ad = Ad.objects.filter(category='Design & Graphics').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Frl3'):
                ad = Ad.objects.filter(category='Digital Marketing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Frl4'):
                ad = Ad.objects.filter(category='Programming & APP Development').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Frl5'):
                ad = Ad.objects.filter(category='Social Media Manager').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Frl6'):
                ad = Ad.objects.filter(category='Video & Animation').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Frl7'):
                return redirect('view')
            if request.POST.get('Fur1'):
                ad = Ad.objects.filter(category='Beds & Mattresses').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Fur2'):
                ad = Ad.objects.filter(category='Couches & Futons').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Fur3'):
                ad = Ad.objects.filter(category='Dressers & Wardrobes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Fur4'):
                ad = Ad.objects.filter(category='Office Furniture').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Fur5'):
                ad = Ad.objects.filter(category='Sofas, Chairs & Loveseats').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Fur6'):
                ad = Ad.objects.filter(category='Tables, Recliners & Mirrors').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Fur7'):
                return redirect('view')
            if request.POST.get('Ins1'):
                ad = Ad.objects.filter(category='Auto Insurance & Financing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Ins2'):
                ad = Ad.objects.filter(category='Home Insurance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Ins3'):
                ad = Ad.objects.filter(category='Insurance Brokers / Agents').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Ins4'):
                ad = Ad.objects.filter(category='Life Insurance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Ins5'):
                return redirect('view')
            if request.POST.get('Jbs1'):
                ad = Ad.objects.filter(category='Accounting & Finance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs2'):
                ad = Ad.objects.filter(category='Administrative & Clerical').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs3'):
                ad = Ad.objects.filter(category='Advertising, Marketing & PR').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs4'):
                ad = Ad.objects.filter(category='Agriculture & Farming').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs5'):
                ad = Ad.objects.filter(category='Architect & Design').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs6'):
                ad = Ad.objects.filter(category='Arts & Entertainment Jobs').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs7'):
                ad = Ad.objects.filter(category='Babysitter & Nanny').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs8'):
                ad = Ad.objects.filter(category='Bar/Hotel/Guesthouse').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs9'):
                ad = Ad.objects.filter(category='Biotech, Science & Pharmacy').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs10'):
                ad = Ad.objects.filter(category='Civil Services & Policy').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs11'):
                ad = Ad.objects.filter(category='Construction & Trades').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs12'):
                ad = Ad.objects.filter(category='>Customer Service & Call Centre').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs13'):
                ad = Ad.objects.filter(category='Domestic Help').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs14'):
                ad = Ad.objects.filter(category='Driver & Security').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs15'):
                ad = Ad.objects.filter(category='Education / Training & Childcare').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs16'):
                ad = Ad.objects.filter(category='Entry level').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs17'):
                ad = Ad.objects.filter(category='General Labor').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs18'):
                ad = Ad.objects.filter(category='Government & Public Service').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs19'):
                ad = Ad.objects.filter(category='Health Jobs').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs20'):
                ad = Ad.objects.filter(category='Health & Wellness Jobs').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs21'):
                ad = Ad.objects.filter(category='Hospitality, Tourism & Travel').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs22'):
                ad = Ad.objects.filter(category='Human Resource').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs23'):
                ad = Ad.objects.filter(category='Import & Export Jobs').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs24'):
                ad = Ad.objects.filter(category='Installation, Maintenance & Repair').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs25'):
                ad = Ad.objects.filter(category='Insurance').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs26'):
                ad = Ad.objects.filter(category='Internet').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs27'):
                ad = Ad.objects.filter(category='IT & Engineering').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs28'):
                ad = Ad.objects.filter(category='Journalism & Media').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs29'):
                ad = Ad.objects.filter(category='Legal - Paralegal').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs30'):
                ad = Ad.objects.filter(category='Management & Executive').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs31'):
                ad = Ad.objects.filter(category='Manufacturing & Production').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs32'):
                ad = Ad.objects.filter(category='Military').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs33'):
                ad = Ad.objects.filter(category='Real Estate').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs34'):
                ad = Ad.objects.filter(category='Research & Development').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs35'):
                ad = Ad.objects.filter(category='Restaurants').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs36'):
                ad = Ad.objects.filter(category='Retail & Wholesale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs37'):
                ad = Ad.objects.filter(category='Sales').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs38'):
                ad = Ad.objects.filter(category='Shipping & Distribution').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs39'):
                ad = Ad.objects.filter(category='Social Work & Nonprofit').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs40'):
                ad = Ad.objects.filter(category='Teaching').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs41'):
                ad = Ad.objects.filter(category='Transportation & Logistics').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs42'):
                ad = Ad.objects.filter(category='Warehouse/Storage').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs43'):
                ad = Ad.objects.filter(category='Work From Home').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Jbs44'):
                return redirect('view')
            if request.POST.get('Mat1'):
                ad = Ad.objects.filter(category='Brides Wear').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Mat2'):
                ad = Ad.objects.filter(category='Grooms Wear').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Mat3'):
                ad = Ad.objects.filter(category='Services').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Mat4'):
                ad = Ad.objects.filter(category='Wedding Products, Accessories').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Mat5'):
                return redirect('view')
            if request.POST.get('Pts1'):
                ad = Ad.objects.filter(category='Equipment & Accessories').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Pts2'):
                ad = Ad.objects.filter(category='Missing Pets').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Pts3'):
                ad = Ad.objects.filter(category='Pets for sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Pts4'):
                return redirect('view')
            if request.POST.get('Hse1'):
                ad = Ad.objects.filter(category='Agencies / Brokers & Builders').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse2'):
                ad = Ad.objects.filter(category='Apartments For Rent & Lease').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse3'):
                ad = Ad.objects.filter(category='Apartments For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse4'):
                ad = Ad.objects.filter(category='Cottages For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse5'):
                ad = Ad.objects.filter(category='Duplex & Triplex For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse6'):
                ad = Ad.objects.filter(category='Farmland For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse7'):
                ad = Ad.objects.filter(category='Foreclosure Listings').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse8'):
                ad = Ad.objects.filter(category='Homes For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse9'):
                ad = Ad.objects.filter(category='Investment Properties').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse10'):
                ad = Ad.objects.filter(category='Lands & Plots For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse11'):
                ad = Ad.objects.filter(category='Mobile Homes For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse12'):
                ad = Ad.objects.filter(category='Multiplex & Quadruplex For Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse13'):
                ad = Ad.objects.filter(category='New Property Developments').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse14'):
                ad = Ad.objects.filter(category='Open House Listings').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse15'):
                ad = Ad.objects.filter(category='Parking Spot for Rent').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse16'):
                ad = Ad.objects.filter(category='Real Estate Agents').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse17'):
                ad = Ad.objects.filter(category='Residential Property Listing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse18'):
                ad = Ad.objects.filter(category='Rooms for Rent / Sublet').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse19'):
                ad = Ad.objects.filter(category='Shops For Rent / Lease').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse20'):
                ad = Ad.objects.filter(category='Vacation Rentals').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Hse21'):
                return redirect('view')
            if request.POST.get('Srv1'):
                ad = Ad.objects.filter(category='Architects & Interior Designers').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv2'):
                ad = Ad.objects.filter(category='Astrology, Numerology & Vastu').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv3'):
                ad = Ad.objects.filter(category='Child Care').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv4'):
                ad = Ad.objects.filter(category='Cleaning / Maids').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv5'):
                ad = Ad.objects.filter(category='Computer & Consulting').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv6'):
                ad = Ad.objects.filter(category='Courier Service & Cargo').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv7'):
                ad = Ad.objects.filter(category='Electrician / Handyman').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv8'):
                ad = Ad.objects.filter(category='Event Services').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv9'):
                ad = Ad.objects.filter(category='General Contractors').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv10'):
                ad = Ad.objects.filter(category='Gifts, Flower Delivery & Cakes').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv11'):
                ad = Ad.objects.filter(category='Handyman').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv12'):
                ad = Ad.objects.filter(category='Health, Beauty & Fitness').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv13'):
                ad = Ad.objects.filter(category='Home Mortgage & Improvements').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv14'):
                ad = Ad.objects.filter(category='House Keeping / Landscaping').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv15'):
                ad = Ad.objects.filter(category='Language Translation').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv16'):
                ad = Ad.objects.filter(category='Lawyers, Advocates & Legal').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv17'):
                ad = Ad.objects.filter(category='Limousine').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv18'):
                ad = Ad.objects.filter(category='Moving & Storage Services').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv19'):
                ad = Ad.objects.filter(category='Music').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv20'):
                ad = Ad.objects.filter(category='Packers & Movers').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv21'):
                ad = Ad.objects.filter(category='Pest Control').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv22'):
                ad = Ad.objects.filter(category='Photography & Videography').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv23'):
                ad = Ad.objects.filter(category='Plumbing').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv24'):
                ad = Ad.objects.filter(category='Recycling').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv25'):
                ad = Ad.objects.filter(category='Restaurants & Food Joints').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv26'):
                ad = Ad.objects.filter(category='Roofing / Repair').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv27'):
                ad = Ad.objects.filter(category='Scrap & Junk Removal').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv28'):
                ad = Ad.objects.filter(category='Tax').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv29'):
                ad = Ad.objects.filter(category='Web & Graphic Design').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Srv30'):
                return redirect('view')
            if request.POST.get('Sftwr1'):
                ad = Ad.objects.filter(category='Windows').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sftwr2'):
                ad = Ad.objects.filter(category='Mac').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sftwr3'):
                ad = Ad.objects.filter(category='Open Source').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sftwr4'):
                return redirect('view')
            if request.POST.get('Sp1'):
                ad = Ad.objects.filter(category='Equipments').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sp2'):
                ad = Ad.objects.filter(category='Jobs').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sp3'):
                ad = Ad.objects.filter(category='Missions').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sp4'):
                ad = Ad.objects.filter(category='Spacecraft').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sp5'):
                return redirect('view')
            if request.POST.get('Tkt1'):
                ad = Ad.objects.filter(category='Cinema / Theatre / Ballet').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Tkt2'):
                ad = Ad.objects.filter(category='Discounts / Coupons').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Tkt3'):
                ad = Ad.objects.filter(category='Sports / Shows / Tickets').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Tkt4'):
                ad = Ad.objects.filter(category='Other Tickets').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Tkt5'):
                return redirect('view')
            if request.POST.get('Trvl1'):
                ad = Ad.objects.filter(category='Bus & Train Tickets').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Trvl2'):
                ad = Ad.objects.filter(category='Hotels & Resorts').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Trvl3'):
                ad = Ad.objects.filter(category='Taxi & Bus Hire').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Trvl4'):
                ad = Ad.objects.filter(category='Tour Packages').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Trvl5'):
                ad = Ad.objects.filter(category='Travel Agents').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Trvl6'):
                return redirect('view')
            if request.POST.get('Sl1'):
                ad = Ad.objects.filter(category='Clearance & Discount Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sl2'):
                ad = Ad.objects.filter(category='Free For Pickup').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sl3'):
                ad = Ad.objects.filter(category='Garage & Moving Sale').prefetch_related('adimages_set').all()
                return render(request, 'view.html',{'ad':ad})
            if request.POST.get('Sl4'):
                return redirect('view')
        else:
            return render(request, 'index.html')
def home2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('search'):
                search = request.POST.get('search')
                ad=Ad.objects.filter(title__icontains=search).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html', {'ad':ad,'username':username})
            if request.POST.get('3D1'):
                ad = Ad.objects.filter(category='3D Printing Technology').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('3D2'):
                ad = Ad.objects.filter(category='Robotics').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Air1'):
                ad = Ad.objects.filter(category='Aircrafts & Airplanes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Air2'):
                ad = Ad.objects.filter(category='Aircraft Dealers').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Air3'):
                ad = Ad.objects.filter(category='Flight Schools').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Air4'):
                ad = Ad.objects.filter(category='Parts, Tires & Accessories').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Air5'):
                ad = Ad.objects.filter(category='Rentals, Lease & Financing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto1'):
                ad = Ad.objects.filter(category='ATVs & Snowmobiles').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto2'):
                ad = Ad.objects.filter(category='Bikes, Boats & Watercraft').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto3'):
                ad = Ad.objects.filter(category='Cars & Heavy Trucks').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto4'):
                ad = Ad.objects.filter(category='Damaged & Accident Vehicles').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto5'):
                ad = Ad.objects.filter(category='Automobile Dealers').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto6'):
                ad = Ad.objects.filter(category='Driving Schools').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto7'):
                ad = Ad.objects.filter(category='Parts, Tires & Accessories').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto8'):
                ad = Ad.objects.filter(category='Rentals, Lease & Financing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto9'):
                ad = Ad.objects.filter(category='RoadSide Assistance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Auto10'):
                return redirect('view')
            if request.POST.get('Auto10'):
                return redirect('view')
            if request.POST.get('Bis1'):
                ad = Ad.objects.filter(category='Renting').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Bis2'):
                ad = Ad.objects.filter(category='Opportunities').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Bis3'):
                ad = Ad.objects.filter(category='Cryptocurrencies').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Bis4'):
                ad = Ad.objects.filter(category='Finance & Investments').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Bis5'):
                ad = Ad.objects.filter(category='Franchise/ Trading').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Bis6'):
                ad = Ad.objects.filter(category='Partnership & Joint Ventures').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Bis7'):
                return redirect('view')
            if request.POST.get('Cls1'):
                ad = Ad.objects.filter(category='Art, Music & Dance Classes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls2'):
                ad = Ad.objects.filter(category='Computer - Multimedia Classes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls3'):
                ad = Ad.objects.filter(category='Continuing Education').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls4'):
                ad = Ad.objects.filter(category='Language Classes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls5'):
                ad = Ad.objects.filter(category='Online Bootcamps & Mastermind').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls6'):
                ad = Ad.objects.filter(category='Sports & Wellness Classes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls7'):
                ad = Ad.objects.filter(category='Tutoring - Private Lessons').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Cls8'):
                return redirect('view')
            if request.POST.get('Clot1'):
                ad = Ad.objects.filter(category='Baby Fashions').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Clot2'):
                ad = Ad.objects.filter(category='Men Fashions').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Clot3'):
                ad = Ad.objects.filter(category='Teenage Fashions').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Clot4'):
                ad = Ad.objects.filter(category='Women Fashions').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Clot5'):
                return redirect('view')
            if request.POST.get('Com1'):
                ad = Ad.objects.filter(category='Artists, Musicians & Bands').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com2'):
                ad = Ad.objects.filter(category='Auctions / Groups').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com3'):
                ad = Ad.objects.filter(category='Carpool & Rideshare').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com4'):
                ad = Ad.objects.filter(category='Charity, Donate').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com5'):
                ad = Ad.objects.filter(category='Community Activities').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com6'):
                ad = Ad.objects.filter(category='Elderly Home Assistance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com7'):
                ad = Ad.objects.filter(category='Household Help').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com8'):
                ad = Ad.objects.filter(category='Lost & Found').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com9'):
                ad = Ad.objects.filter(category='Public Announcements').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com10'):
                ad = Ad.objects.filter(category='Recreation').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Com11'):
                return redirect('view')
            if request.POST.get('Con1'):
                ad = Ad.objects.filter(category='Attachments').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con2'):
                ad = Ad.objects.filter(category='Building Supplies').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con3'):
                ad = Ad.objects.filter(category='Construction Equipment').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con4'):
                ad = Ad.objects.filter(category='Damaged & Accident Vehicles').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con5'):
                ad = Ad.objects.filter(category='Farming Equipment').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con6'):
                ad = Ad.objects.filter(category='Rentals, Lease & Financing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con7'):
                ad = Ad.objects.filter(category='RoadSide Assistance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con8'):
                ad = Ad.objects.filter(category='Trailer').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con9'):
                ad = Ad.objects.filter(category='Trucks').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Con10'):
                return redirect('view')
            if request.POST.get('Elec1'):
                ad = Ad.objects.filter(category='Alarms & Security Systems').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Elec2'):
                ad = Ad.objects.filter(category='Cameras, Camcorders & Drones').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Elec3'):
                ad = Ad.objects.filter(category='Computer & Gaming').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Elec4'):
                ad = Ad.objects.filter(category='Media & Streaming Equipment').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Elec5'):
                ad = Ad.objects.filter(category='Projectors, Tablets & TV').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Elec6'):
                return redirect('view')
            if request.POST.get('Frl1'):
                ad = Ad.objects.filter(category='Content Creation').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Frl2'):
                ad = Ad.objects.filter(category='Design & Graphics').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Frl3'):
                ad = Ad.objects.filter(category='Digital Marketing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Frl4'):
                ad = Ad.objects.filter(category='Programming & APP Development').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Frl5'):
                ad = Ad.objects.filter(category='Social Media Manager').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Frl6'):
                ad = Ad.objects.filter(category='Video & Animation').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Frl7'):
                return redirect('view')
            if request.POST.get('Fur1'):
                ad = Ad.objects.filter(category='Beds & Mattresses').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Fur2'):
                ad = Ad.objects.filter(category='Couches & Futons').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Fur3'):
                ad = Ad.objects.filter(category='Dressers & Wardrobes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Fur4'):
                ad = Ad.objects.filter(category='Office Furniture').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Fur5'):
                ad = Ad.objects.filter(category='Sofas, Chairs & Loveseats').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Fur6'):
                ad = Ad.objects.filter(category='Tables, Recliners & Mirrors').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Fur7'):
                return redirect('view')
            if request.POST.get('Ins1'):
                ad = Ad.objects.filter(category='Auto Insurance & Financing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Ins2'):
                ad = Ad.objects.filter(category='Home Insurance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Ins3'):
                ad = Ad.objects.filter(category='Insurance Brokers / Agents').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Ins4'):
                ad = Ad.objects.filter(category='Life Insurance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Ins5'):
                return redirect('view')
            if request.POST.get('Jbs1'):
                ad = Ad.objects.filter(category='Accounting & Finance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs2'):
                ad = Ad.objects.filter(category='Administrative & Clerical').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs3'):
                ad = Ad.objects.filter(category='Advertising, Marketing & PR').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs4'):
                ad = Ad.objects.filter(category='Agriculture & Farming').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs5'):
                ad = Ad.objects.filter(category='Architect & Design').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs6'):
                ad = Ad.objects.filter(category='Arts & Entertainment Jobs').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs7'):
                ad = Ad.objects.filter(category='Babysitter & Nanny').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs8'):
                ad = Ad.objects.filter(category='Bar/Hotel/Guesthouse').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs9'):
                ad = Ad.objects.filter(category='Biotech, Science & Pharmacy').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs10'):
                ad = Ad.objects.filter(category='Civil Services & Policy').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs11'):
                ad = Ad.objects.filter(category='Construction & Trades').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs12'):
                ad = Ad.objects.filter(category='>Customer Service & Call Centre').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs13'):
                ad = Ad.objects.filter(category='Domestic Help').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs14'):
                ad = Ad.objects.filter(category='Driver & Security').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs15'):
                ad = Ad.objects.filter(category='Education / Training & Childcare').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs16'):
                ad = Ad.objects.filter(category='Entry level').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs17'):
                ad = Ad.objects.filter(category='General Labor').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs18'):
                ad = Ad.objects.filter(category='Government & Public Service').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs19'):
                ad = Ad.objects.filter(category='Health Jobs').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs20'):
                ad = Ad.objects.filter(category='Health & Wellness Jobs').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs21'):
                ad = Ad.objects.filter(category='Hospitality, Tourism & Travel').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs22'):
                ad = Ad.objects.filter(category='Human Resource').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs23'):
                ad = Ad.objects.filter(category='Import & Export Jobs').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs24'):
                ad = Ad.objects.filter(category='Installation, Maintenance & Repair').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs25'):
                ad = Ad.objects.filter(category='Insurance').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs26'):
                ad = Ad.objects.filter(category='Internet').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs27'):
                ad = Ad.objects.filter(category='IT & Engineering').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs28'):
                ad = Ad.objects.filter(category='Journalism & Media').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs29'):
                ad = Ad.objects.filter(category='Legal - Paralegal').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs30'):
                ad = Ad.objects.filter(category='Management & Executive').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs31'):
                ad = Ad.objects.filter(category='Manufacturing & Production').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs32'):
                ad = Ad.objects.filter(category='Military').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs33'):
                ad = Ad.objects.filter(category='Real Estate').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs34'):
                ad = Ad.objects.filter(category='Research & Development').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs35'):
                ad = Ad.objects.filter(category='Restaurants').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs36'):
                ad = Ad.objects.filter(category='Retail & Wholesale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs37'):
                ad = Ad.objects.filter(category='Sales').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs38'):
                ad = Ad.objects.filter(category='Shipping & Distribution').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs39'):
                ad = Ad.objects.filter(category='Social Work & Nonprofit').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs40'):
                ad = Ad.objects.filter(category='Teaching').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs41'):
                ad = Ad.objects.filter(category='Transportation & Logistics').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs42'):
                ad = Ad.objects.filter(category='Warehouse/Storage').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs43'):
                ad = Ad.objects.filter(category='Work From Home').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Jbs44'):
                return redirect('view')
            if request.POST.get('Mat1'):
                ad = Ad.objects.filter(category='Brides Wear').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Mat2'):
                ad = Ad.objects.filter(category='Grooms Wear').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Mat3'):
                ad = Ad.objects.filter(category='Services').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Mat4'):
                ad = Ad.objects.filter(category='Wedding Products, Accessories').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Mat5'):
                return redirect('view')
            if request.POST.get('Pts1'):
                ad = Ad.objects.filter(category='Equipment & Accessories').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Pts2'):
                ad = Ad.objects.filter(category='Missing Pets').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Pts3'):
                ad = Ad.objects.filter(category='Pets for sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Pts4'):
                return redirect('view')
            if request.POST.get('Hse1'):
                ad = Ad.objects.filter(category='Agencies / Brokers & Builders').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse2'):
                ad = Ad.objects.filter(category='Apartments For Rent & Lease').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse3'):
                ad = Ad.objects.filter(category='Apartments For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse4'):
                ad = Ad.objects.filter(category='Cottages For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse5'):
                ad = Ad.objects.filter(category='Duplex & Triplex For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse6'):
                ad = Ad.objects.filter(category='Farmland For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse7'):
                ad = Ad.objects.filter(category='Foreclosure Listings').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse8'):
                ad = Ad.objects.filter(category='Homes For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse9'):
                ad = Ad.objects.filter(category='Investment Properties').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse10'):
                ad = Ad.objects.filter(category='Lands & Plots For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse11'):
                ad = Ad.objects.filter(category='Mobile Homes For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse12'):
                ad = Ad.objects.filter(category='Multiplex & Quadruplex For Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse13'):
                ad = Ad.objects.filter(category='New Property Developments').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse14'):
                ad = Ad.objects.filter(category='Open House Listings').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse15'):
                ad = Ad.objects.filter(category='Parking Spot for Rent').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse16'):
                ad = Ad.objects.filter(category='Real Estate Agents').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse17'):
                ad = Ad.objects.filter(category='Residential Property Listing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse18'):
                ad = Ad.objects.filter(category='Rooms for Rent / Sublet').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse19'):
                ad = Ad.objects.filter(category='Shops For Rent / Lease').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse20'):
                ad = Ad.objects.filter(category='Vacation Rentals').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Hse21'):
                return redirect('view')
            if request.POST.get('Srv1'):
                ad = Ad.objects.filter(category='Architects & Interior Designers').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv2'):
                ad = Ad.objects.filter(category='Astrology, Numerology & Vastu').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv3'):
                ad = Ad.objects.filter(category='Child Care').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv4'):
                ad = Ad.objects.filter(category='Cleaning / Maids').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv5'):
                ad = Ad.objects.filter(category='Computer & Consulting').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv6'):
                ad = Ad.objects.filter(category='Courier Service & Cargo').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv7'):
                ad = Ad.objects.filter(category='Electrician / Handyman').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv8'):
                ad = Ad.objects.filter(category='Event Services').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv9'):
                ad = Ad.objects.filter(category='General Contractors').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv10'):
                ad = Ad.objects.filter(category='Gifts, Flower Delivery & Cakes').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv11'):
                ad = Ad.objects.filter(category='Handyman').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv12'):
                ad = Ad.objects.filter(category='Health, Beauty & Fitness').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv13'):
                ad = Ad.objects.filter(category='Home Mortgage & Improvements').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv14'):
                ad = Ad.objects.filter(category='House Keeping / Landscaping').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv15'):
                ad = Ad.objects.filter(category='Language Translation').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv16'):
                ad = Ad.objects.filter(category='Lawyers, Advocates & Legal').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv17'):
                ad = Ad.objects.filter(category='Limousine').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv18'):
                ad = Ad.objects.filter(category='Moving & Storage Services').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv19'):
                ad = Ad.objects.filter(category='Music').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv20'):
                ad = Ad.objects.filter(category='Packers & Movers').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv21'):
                ad = Ad.objects.filter(category='Pest Control').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv22'):
                ad = Ad.objects.filter(category='Photography & Videography').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv23'):
                ad = Ad.objects.filter(category='Plumbing').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv24'):
                ad = Ad.objects.filter(category='Recycling').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv25'):
                ad = Ad.objects.filter(category='Restaurants & Food Joints').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv26'):
                ad = Ad.objects.filter(category='Roofing / Repair').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv27'):
                ad = Ad.objects.filter(category='Scrap & Junk Removal').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv28'):
                ad = Ad.objects.filter(category='Tax').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv29'):
                ad = Ad.objects.filter(category='Web & Graphic Design').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Srv30'):
                return redirect('view')
            if request.POST.get('Sftwr1'):
                ad = Ad.objects.filter(category='Windows').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sftwr2'):
                ad = Ad.objects.filter(category='Mac').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sftwr3'):
                ad = Ad.objects.filter(category='Open Source').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sftwr4'):
                return redirect('view')
            if request.POST.get('Sp1'):
                ad = Ad.objects.filter(category='Equipments').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sp2'):
                ad = Ad.objects.filter(category='Jobs').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sp3'):
                ad = Ad.objects.filter(category='Missions').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sp4'):
                ad = Ad.objects.filter(category='Spacecraft').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sp5'):
                return redirect('view')
            if request.POST.get('Tkt1'):
                ad = Ad.objects.filter(category='Cinema / Theatre / Ballet').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Tkt2'):
                ad = Ad.objects.filter(category='Discounts / Coupons').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Tkt3'):
                ad = Ad.objects.filter(category='Sports / Shows / Tickets').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Tkt4'):
                ad = Ad.objects.filter(category='Other Tickets').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Tkt5'):
                return redirect('view')
            if request.POST.get('Trvl1'):
                ad = Ad.objects.filter(category='Bus & Train Tickets').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Trvl2'):
                ad = Ad.objects.filter(category='Hotels & Resorts').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Trvl3'):
                ad = Ad.objects.filter(category='Taxi & Bus Hire').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Trvl4'):
                ad = Ad.objects.filter(category='Tour Packages').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Trvl5'):
                ad = Ad.objects.filter(category='Travel Agents').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Trvl6'):
                return redirect('view')
            if request.POST.get('Sl1'):
                ad = Ad.objects.filter(category='Clearance & Discount Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sl2'):
                ad = Ad.objects.filter(category='Free For Pickup').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sl3'):
                ad = Ad.objects.filter(category='Garage & Moving Sale').prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            if request.POST.get('Sl4'):
                return redirect('view')
                        
        else:
            username=request.session['trio_User']
            return render(request, 'home2.html',{'username':username})
    else:
        messages.warning(request,"Login Required")
        return redirect('login') 
       
       
def hiw(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'hiw.html', {'username':username})
    else:
        return render(request, 'hiw.html')

def terms(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'terms.html', {'username':username})
    else:
        return render(request, 'terms.html')
    
def privacy(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'privacy.html', {'username':username})
    else:
        return render(request, 'privacy.html')

def cookie(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'cookie.html', {'username':username})
    else:
        return render(request, 'cookie.html')

def disclaimer(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'disclaimer.html', {'username':username})
    else:
        return render(request, 'disclaimer.html')

def faq(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'faq.html', {'username':username})
    else:
        return render(request, 'faq.html')

def ad(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'ad.html', {'username':username})
    else:
        return render(request, 'ad.html')

def view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('more'):
                ad_id=request.POST.get('ad_id')
                ad_categ=request.POST.get('ad_categ')
                ads = Ad.objects.filter(id=ad_id).prefetch_related('adimages_set').all()
                related = Ad.objects.filter(category=ad_categ).prefetch_related('adimages_set').all().exclude(id=ad_id)
                username=request.session['trio_User']
                return render(request, 'detail_view.html',{'username':username,'ads':ads,'related':related})
            elif request.POST.get('chat'):
                ad_id=request.POST.get('ad_id')
                user_id=request.user.username
                ad=Ad.objects.filter(id=ad_id).all()
                chats = AdMessage.objects.filter(adId=ad_id).all()
                username=request.session['trio_User']
                return render(request, 'chats.html', {'username':username, 'chats':chats, 'user_id':user_id, 'ad_id':ad_id, 'ad':ad})
            elif request.POST.get('r1'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Alberta') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r2'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='British Columbia') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r3'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Manitoba') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r4'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='New Brunswick') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r5'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Newfoundland & Labrador') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r6'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='NorthWest Territories') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r7'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Nova Scotia') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r8'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Nuna Vut') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r9'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Ontario') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r10'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Prince Edward Island') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r11'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Quebec') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r12'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Saskatchewan') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('r13'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(location='Tukon Territory') & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p1'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(category=cat).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p2'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__lte=99) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p3'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=100) | Q(price__lte=199) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p4'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=200) | Q(price__lte=299) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p5'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=300) | Q(price__lte=399) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p6'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=400) | Q(price__lte=499) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p7'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=500) | Q(price__lte=999) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p8'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=1000) | Q(price__lte=9999) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
            elif request.POST.get('p9'):
                cat=request.POST.get('ad_categ')
                ad = Ad.objects.filter(Q(price__gte=10000) & Q(category=cat)).prefetch_related('adimages_set').all()
                username=request.session['trio_User']
                return render(request, 'view.html',{'ad':ad,'username':username})
        else:
            username=request.session['trio_User']
            return render(request, 'view.html',{'username':username})
    else:
        return render(request, 'view.html')

def details(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        return render(request, 'detail_view.html',{'username':username})    
    else:
        return render(request, 'detail_view.html')
    
def trio_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass')
        user = authenticate(username=username,password=password)
        next_view = request.POST.get('next')
        if user is not None:            
            if next_view == '/post': #check the next url value from the GET method for this view
                user_login(request,user)
                request.session['trio_User'] = user.first_name #store username to a session
                return redirect('active_post')
            else:
                user_login(request,user)
                request.session['trio_User'] = user.first_name #store username to a session                
                return redirect('index')
        else:
            messages.warning(request, "Invalid Username or Password")
            return redirect('login')
    else:        
        return render(request, 'login.html')
    
def signUp(request):
    if request.method == 'POST':       
        name = request.POST.get('name')
        email = request.POST.get('email')
        password =request.POST.get('pass')
        password_2 = request.POST.get('pass2')
        terms = request.POST.get('terms',None)
        exists = User.objects.filter(username=email)
        if terms != "1":
            messages.warning(request, "Please Read and Agree to the Terms")
            return redirect('signUp')
        elif exists:
            messages.warning(request, "User already Exists")
            return redirect('signUp')
        elif password != password_2:
            messages.warning(request, "Passwords Must match.")
            return redirect('signUp')
        else:
            user = User.objects.create_user(username=email,email=email,password=password,first_name=name,is_active=1)
            user.save()
            messages.success(request, "Sign Up Success.")
            return redirect('login')
    else:            
        return render(request, 'signUp.html')
    

@login_required
def post(request):
    if request.user.is_authenticated:
        form = AdForm
        return render(request, 'post.html',{'form':form})
    else:
        messages.warning(request,"Login Required")
        return redirect('login')

def activepost(request):
    form1 = AdForm()
    form2 = AdImageForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form1=AdForm(request.POST)
            form2=AdImageForm(request.POST, request.FILES)
            images=request.FILES.getlist('media')
            if form1.is_valid():                
                f = form1.save(commit=False)
                f.save()
                for i in images:
                    AdImages.objects.create(ad=f,media=i)
                messages.success(request,"Ad posted successfuly")
                return redirect('active_post')
            else:                
                messages.warning(request,"Something Went wrong. Try again")
                return render(request, 'post.html',{'form1':form1,'form2':form2})
        else:
            username=request.session['trio_User']
            email =request.user.email
            return render(request, 'post.html',{'form1':form1,'form2':form2,'username':username, 'email':email})
    else:
        messages.warning(request,"Login Required")
        return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        user_id =request.user.username
        user_ads = Ad.objects.filter(email=user_id).prefetch_related('adimages_set').all()
        ads_count = Ad.objects.filter(email=user_id).count()
        return render(request, 'dashboard.html',{'username':username,'user_ads':user_ads,'count':ads_count})
    else:
        messages.warning(request,"Login Required")
        return redirect('login')

def chat(request):
    if request.user.is_authenticated:
        username=request.session['trio_User']
        if request.method == 'POST':
            adid=request.POST.get('adid')
            userid=request.POST.get('userid')
            name=User.objects.filter(username=userid).values_list('first_name', flat=True)[0]
            message=request.POST.get('message')
            mssg=AdMessage(adId=adid, poster=name, message=message)
            mssg.save()            
            request.session['adid']=adid
            request.session['userid']=userid
            return redirect('chat')
        else:
            userid=request.session['userid']
            adid=request.session['adid']
            ad=Ad.objects.filter(id=adid).all()
            chats = AdMessage.objects.filter(adId=adid).all()
            return render(request, 'chats.html', {'username':username, 'chats':chats, 'user_id':userid, 'ad_id':adid, 'ad':ad})
    else:
        messages.warning(request,"Login Required")
        return redirect('login')

def logout_view(request):
    logout(request)
    messages.success(request,"Successfuly logged out")
    return redirect('login')