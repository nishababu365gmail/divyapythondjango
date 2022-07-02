from django.contrib import admin

from kittypartyapp.models import(kittyparty,invitee,game,student,studentcourse,course,
inviteepartybridge,gamepartybridge,category,menu,menupartybridge,Classes,StudentDivya,Class_Student_Bridge) 
admin.site.register(kittyparty)
admin.site.register(invitee)
admin.site.register(game)
admin.site.register(inviteepartybridge)
admin.site.register(gamepartybridge)
admin.site.register(category)
admin.site.register(menu)
admin.site.register(menupartybridge)
admin.site.register(student)
admin.site.register(studentcourse)
admin.site.register(course)
admin.site.register(StudentDivya)
admin.site.register(Class_Student_Bridge)
admin.site.register(Classes)

