from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, render_to_response,get_object_or_404


class AutoLogout:
  def process_request(self, request):
   
    if not request.user.is_authenticated() :
      #Can't log out if not logged in
      return

    try:
      
      last_touch = datetime.strptime(request.session['last_touch'], '%Y-%m-%d %H:%M:%S.%f')
      if datetime.now() - last_touch > timedelta( 0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        state="SE CERRO SPID POR INACTIVIDAD." 
        auth.logout(request)
        del request.session['last_touch']
        form = DependenciasForm()
        formd = []
        return
    except KeyError:
      pass
     

   
    request.session['last_touch'] = str(datetime.now())
  