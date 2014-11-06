from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from preventivos import views
from preventivos import forms
from preventivos.forms import *
from preventivos.views import *
from django.conf import settings

FORMS = [("nro", PrimerForm),
     ("actores", SegundoForm),    ("autoridades", TerceroForm),     ("confirmation", FinForm),       
    ]

contact_wizard = preventivos.as_view(FORMS)

handler404 = 'preventivos.views.page_not_found'
handler500 = 'preventivos.views.server_error' 

admin.autodiscover()

urlpatterns = patterns('', 
  	(r'^user/$','preventivos.views.new_user'),
   #(r'^permgroups/$','preventivos.views.permisos'),
    (r'^climas/$', 'preventivos.views.climas'),
    (r'^climas/(?P<idcli>[0-9A-Za-z]+)/$','preventivos.views.nclimas'),
    (r'^hogares/$','preventivos.views.hogares'),
    (r'^hogares/(?P<idipv>[0-9A-Za-z]+)/$', 'preventivos.views.nhogares'),
    (r'^lugares/$', 'preventivos.views.lugares'),
    (r'^lugares/(?P<idlugar>[0-9A-Za-z]+)/$', 'preventivos.views.nlugares'),
    (r'^ciudades/$','preventivos.views.ciudades'),
    (r'^addciudades/$','preventivos.views.ciudadesadd'),
    (r'^seleccionar/hechos/tdelito/(?P<idtd>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_delitos'),
    (r'^seleccionar/hechos/delito/(?P<idd>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_modos'),
    (r'^new/first/tdelito/(?P<idtd>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_delitos'),
    (r'^new/first/delito/(?P<idd>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_modos'),
    (r'^actuantes/ure/(?P<ure>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_dependencias'),
    (r'^ure/(?P<ure>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_dependencias'),
    (r'^user/ure/(?P<ure>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_dependencias'),
    (r'^ciudades/(?P<pais>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_provincia'),
    (r'^ciudades/editar/(?P<idciu>[0-9A-Za-z]+)/$', 'preventivos.views.ciudad'),
    (r'^ciudades/dpto/(?P<prvi>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_departa'),
    (r'^paises/$', 'preventivos.views.pais'),
    (r'^newpais/$', 'preventivos.views.npais'),
    (r'^newtipodelito/$', 'preventivos.views.ntipodelito'),
    (r'^provincias/$', 'preventivos.views.provincias'),
    (r'^departamentos/$','preventivos.views.departamentos'),
    (r'^paises/(?P<idlista>[0-9A-Za-z]+)/$', 'preventivos.views.paise'),
    (r'^provincias/(?P<idpcia>[0-9A-Za-z]+)/$', 'preventivos.views.provi'),
    (r'^departamentos/(?P<iddepto>[0-9A-Za-z]+)/$', 'preventivos.views.depto'),
    (r'^unidades/$', 'preventivos.views.unidades'),
    (r'^unidades/(?P<idUnidad>[0-9A-Za-z]+)/$', 'preventivos.views.unidad'),
    (r'^dependencias/$','preventivos.views.dependencias'),
    (r'^dependencias/(?P<idDepe>[0-9A-Za-z]+)/$', 'preventivos.views.dependencia'),
    (r'^peopleenv/$','preventivos.views.personasi'),
    (r'^peopleenv/(?P<idple>[0-9A-Za-z]+)/$', 'preventivos.views.npersonasi'),
    (r'^typedelitos/$', 'preventivos.views.tipodelitos'),
    (r'^typedelitos/(?P<idtipo>[0-9A-Za-z]+)/$', 'preventivos.views.tipodelito'),
     (r'^reportes/(?P<idtd>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_delitos'),
    (r'^delitos/$', 'preventivos.views.delitos'),
    (r'^delitos/(?P<idelito>[0-9A-Za-z]+)/$', 'preventivos.views.delito'),
    (r'^modus/$', 'preventivos.views.modus'),
    (r'^modus/(?P<idmod>[0-9A-Za-z]+)/$', 'preventivos.views.modos'),
    (r'^jobs/$', 'preventivos.views.jobs'),
    (r'^jobs/(?P<idjob>[0-9A-Za-z]+)/$', 'preventivos.views.jobselected'),
    (r'^trademark/$', 'preventivos.views.marcas'),
    (r'^trademark/(?P<idmars>[0-9A-Za-z]+)/$', 'preventivos.views.tradeselec'),
    (r'^typearms/$', 'preventivos.views.tiposarmas'),
    (r'^typearms/(?P<idta>[0-9A-Za-z]+)/$', 'preventivos.views.tiposaselec'),
    (r'^subarms/$', 'preventivos.views.subtiposarms'),
    (r'^subarms/(?P<idsta>[0-9A-Za-z]+)/$', 'preventivos.views.subaselect'),
    (r'^newtypearms/$', 'preventivos.views.ntypesa'),
    (r'^items/$', 'preventivos.views.rubros'),
    (r'^items/(?P<idrub>[0-9A-Za-z]+)/$', 'preventivos.views.itemselec'),
    (r'^category/$', 'preventivos.views.categorias'),
    (r'^category/(?P<idcat>[0-9A-Za-z]+)/$', 'preventivos.views.catselect'),
    (r'^newrubro/$', 'preventivos.views.nrubros'),
    (r'^barrios/$', 'preventivos.views.barrios'),
    (r'^addbarrios/$', 'preventivos.views.addbarrios'),
    (r'^barrios/(?P<idbar>[0-9A-Za-z]+)/$', 'preventivos.views.nbarrios'),
    (r'^helpass/$', 'preventivos.views.helpassword'),
    #(r'^barrios/ids/(?P<idci>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_calles'),
    (r'^address/$', 'preventivos.views.calles'),
    (r'^address/(?P<idadrs>[0-9A-Za-z]+)/$', 'preventivos.views.ncalles'),
    (r'^addcalles/$', 'preventivos.views.addcalles'),
    (r'^authorities/$', 'preventivos.views.autoridades'),
    (r'^authorities/(?P<idaut>[0-9A-Za-z]+)/$', 'preventivos.views.autoridad'),
    (r'^actuantes/$', 'preventivos.views.actuantes'),
    (r'^actuantes/(?P<idact>[0-9A-Za-z]+)/$','preventivos.views.oficiales'),
    #(r'^user/new/$','preventivos.views.new_user'),
   
    (r'^groupusers/$', 'preventivos.views.grupos'),
    (r'^groupfree/$', 'preventivos.views.gruposperm'),
    (r'^newgroup/$', 'preventivos.views.ngrupos'),
    (r'^groupusers/(?P<idgr>[0-9A-Za-z]+)/$', 'preventivos.views.grupusers'),
    (r'^persona/$', 'preventivos.views.personas'),
    (r'^newpersona/$', 'preventivos.views.newperso'),
    (r'^persona/ver/(?P<idper>[0-9A-Za-z]+)/$', 'preventivos.views.persona'),
    (r'^persona/(?P<pais>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_ciudades'),
    url(r'^new/$', contact_wizard, name='contact_wizard'),
    (r'^persona/town/(?P<idcit>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_barrios'),
    (r'^persona/street/(?P<idcit>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_calle'),
    (r'^controller/$', 'preventivos.views.control'),
    (r'^seleccionar/(?P<prev>[0-9A-Za-z]+)/$', 'preventivos.views.selectPrev'),
    url(r'^controller/(?P<user>[0-9A-Za-z]+)/$', 'preventivos.views.reporactivity',name='reporactivity'),
    url(r'^seleccionar/informa/(?P<idhec>[0-9A-Za-z]+)/(?P<idprev>[0-9A-Za-z]+)/$', 'preventivos.views.informe',name='informa'),
    url(r'^user/(?P<iduser>[0-9A-Za-z]+)/$','preventivos.views.usuarios',name="modiuser"),
    url(r'^new/first/(?P<idprev>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_datosfirst',name="newhecho"),
    url(r'^seleccionar/(?P<prev>[0-9A-Za-z]+)/$', 'preventivos.views.selectPrev',name='selectPrev'),
    url(r'^seleccionar/hechos/(?P<idprev>[0-9A-Za-z]+)/$', 'preventivos.views.updatehechos',name='updatehechos'),
    url(r'^seleccionar/hechos/pdfs/(?P<idprev>[0-9A-Za-z]+)/$', 'preventivos.views.pdfs',name='reportes'),
    url(r'^persona/modif@/(?P<idhec>[0-9A-Za-z]+)/(?P<idper>[0-9A-Za-z]+)/$', 'preventivos.views.persinvom',name='persinvoluc'),
    url(r'^persona/(?P<idhec>[0-9A-Za-z]+)/(?P<idper>[0-9A-Za-z]+)/$', 'preventivos.views.persinvo',name='persinvol'),
    url(r'^peoplein/(?P<idper>[0-9A-Za-z]+)/$', 'preventivos.views.verpersin',name='verpersin'),
    url(r'^topdf/$','to_pdf',name= "to_pdf"),
    url(r'^lugar_hecho/(?P<idhecho>[0-9A-Za-z]+)/(?P<idprev>[0-9A-Za-z]+)/$', 'preventivos.views.lugar_hecho',name='lugar_hecho'),
    url(r'^elementos/(?P<idhecho>[0-9A-Za-z]+)/$', 'preventivos.views.elementos',name='elementos'),
    url(r'^elemento/(?P<idhecho>[0-9A-Za-z]+)/(?P<elemento>[0-9A-Za-z]+)/$', 'preventivos.views.elemento',name='elemento'),
    url(r'^getcategory/(?P<rubro>[0-9A-Za-z]+)/$', 'preventivos.views.get_categories',name='get_category'),
    url(r'^mapsanality/$', 'preventivos.views.seemaps',name='seemaps'),
    url(r'^hechos/$', 'preventivos.views.rephechos',name='rephechos'),
    url(r'^automotores/$', 'preventivos.views.repautos',name='repautos'),
    url(r'^homicides/$', 'preventivos.views.killings',name='killings'),
    url(r'^forages/$', 'preventivos.views.repforages',name='repforages'),
    url(r'^ampliacion/(?P<idprev>[0-9A-Za-z]+)/$', 'preventivos.views.ampliacion',name='ampliacion'),
    url(r'^ampliacion/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.ver_ampliacion',name='ver_ampliacion'),
    url(r'^amplielem/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.amplia_ele',name='amplia_ele'),
    url(r'^reporampli/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.reporampli',name='reporampli'),
     url(r'^eleampli/(?P<idhecho>[0-9A-Za-z]+)/(?P<elemento>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.eleampli',name='eleampli'),
     url(r'^amplipers/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.amplia_pers',name='amplia_pers'),
    url(r'^amplipers/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/(?P<idper>[0-9A-Za-z]+)/$', 'preventivos.views.amplia_per',name='amplia_per'),
    url(r'^finalizar/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.finalizar',name='finalizar'),
    url(r'^enviar/(?P<idprev>[0-9A-Za-z]+)/(?P<idamp>[0-9A-Za-z]+)/$', 'preventivos.views.enviar',name='enviar'),
    (r'^modouso/(?P<uso>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_subtiposa'),
    (r'^seedata/$', 'preventivos.views.verprev'),
     (r'^seeampli/$', 'preventivos.views.verampli'),
    (r'^seehechos/$', 'preventivos.views.verhechos'),
    (r'^seedelitos/$', 'preventivos.views.verdelitos'),
    (r'^seedelitos/(?P<idtd>[0-9A-Za-z]+)/$', 'preventivos.views.obtener_delitos'),
    (r'^peoplein/$', 'preventivos.views.verperin'),
    (r'^objectsin/$', 'preventivos.views.verobjin'),
   
    (r'^', 'preventivos.views.page_not_found'),
    (r'^', 'preventivos.views.server_error'),

 
   )
  