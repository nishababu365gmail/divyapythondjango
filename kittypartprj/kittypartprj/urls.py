"""kittypartprj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from kittypartyapp import views

urlpatterns = [
    path('minnu/',views.multform,name='kk'),
    path('mfd/',views.multformdemanddisplay,name='mfd'),
    path('mfp/',views.multformpartsdisplay,name='mfp'),
    path('backtojobcard/<str:jobcard>',views.multformedit,'backtojobcard'),
    path('chikku/',views.concatenatequeryset,name='nn'),
    path('babu/', include('myapiapp.urls')),
    path('leela/', include('snippetsapp.urls')),
    path('',views.callapifromview,name='callapiview'),
    # path('',views.coursesertrial,name='crview'),
    # path('',views.queryview,name='queryview'),
   # path('',views.grasshopper,name='queryview'),
   # path('',views.manaytomanyexample,name='queryview'),
    
    path('CreateCat',views.CreateCategory,name='createcategory'),
    # path('',views.mycategorywisemenulist,name='mycategorywisemenulist'),
    
    path('listcategory',views.CategoryList,name='catlist'),
    path('editcategory/<str:catid>',views.EditCategory,name='editcategory'),
    #path('',views.kittypartydef,name='kittyparty'),
    # path("select2/", include("django_select2.urls")),
    path('myselect2',views.myselect2,name="myselect2"),
    path('kittypartydef',views.kittypartydef,name='kittyparty'),
    path('editkittyparty/<str:parampartyid>',views.editkittyparty,name='editkittyparty'),
    path('kittypartyinvitee',views.kittypartyinvitee,name='kittypartyinvitee'),
    path('kittypartylist',views.kittypartylist,name='kittypartylist'),
    path('editkittypartyinvitee/<str:partyid>',views.editkittypartyinvitee,name='kittypartyinvitee'),
    path('KittyPartyGame',views.KittyPartyGame,name="kittypartygame"),
    path('AddKittyPartyGame/<str:partyid>',views.AddKittyPartyGame,name="addkittyartygame"),
    path('CreateStudent',views.AddStudentWithForm,name='createstudent'),
    path('AddCourseWithFormset',views.AddCourseWithFormset,name='addcoursewithformset'),
    path('regroupme',views.regroupexample1,name='regroup'),
    #path('queryview',views.queryview,name='queryview'),
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]