from django.shortcuts import redirect,render
from system.models import slider,banner_area,Main_Category
def BASE(request):
    return render(request, 'base.html')



def HOME(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]
    
    main_category = Main_Category.objects.all().order_by('-id')
    print(main_category)
    context = {
        'sliders':sliders,
        'banners':banners,
        'main_category':main_category,
    }
    return render(request, 'Main/home.html',context)
