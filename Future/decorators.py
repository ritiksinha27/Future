from django.http import HttpResponse
from django.shortcuts import redirect

def unathen_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('stu_portal')
        else:        
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            print('working',allowed_roles)
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('not authorized')
        return wrapper_func
    return decorator