from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate,logout,login as login_aut
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




# Create your views here.


def index(request):
    categorias = Categoria.objects.all()
    obras= Obra.objects.filter(estado=True).order_by("-id_obra")[:3]
    data= {'categorias': categorias, 'obras': obras}
    return render(request, 'index.html', data)

def galeria(request):
    obras= Obra.objects.filter(estado=True)
    categorias = Categoria.objects.all()

    data = {'obras':obras,'categorias': categorias}
    
    return render(request, 'galeria.html', data)

def artistas(request):
    artistas = User.objects.all()
    
    for artista in artistas:
        contadora = artista.obra_set.filter(estado=True).count()
        artista.contadora = contadora
    
    obras = Obra.objects.all()
    foto = Perfiles.objects.all()

    data = {
        'artistas': artistas,
        'obras': obras,
        'foto': foto
    }
    
    return render(request, 'artistas.html', data)

def contacto(request):
    if request.POST:
        nombre= request.POST.get("nombre")
        rut= request.POST.get("rut")
        correo= request.POST.get("correo")
        telefono= request.POST.get("telefono")
        descripcion= request.POST.get("descripcion")
        contacto = Contacto(
             nombre = nombre,
             rut = rut,
             correo = correo,
             telefono= telefono,
             descripcion = descripcion,
            )
        contacto.save()
        return render(request, 'mensaje.html')
    return render(request, 'contacto.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('IND')




def ingreso(request):
    if request.POST:
        nom=request.POST.get("usuario")
        con=request.POST.get("pass1")
        usu= authenticate(request,username=nom,password=con)
        if usu is not None and usu.is_active:
            login_aut(request,usu)
            return render(request,"index.html")
    contexto={'mensaje':'Usuario/Contraseña Incorrecto'}   
    return render(request,"registro2.html",contexto)

   


def mensaje(request):
    return render(request, 'mensaje.html')

def recuperacion(request):
    return render(request, 'olvideContraseña.html')

def descripcion(request, id):
    obra= Obra.objects.get(id_obra=id)
    galeria= Galeria.objects.all()
    listing = Galeria.objects.filter(obra=obra).first()
    if listing:
        obj_galeria = galeria.get(obra=obra)
        data= {'obra':obra,'galeria':obj_galeria}
        return render(request,"descripcion.html", data)
    else:
        data= {'obra':obra}
        return render(request,"descripcion.html", data)

def registro(request):
    contexto={'mensaje':''}
    if request.POST:
        usuario = request.POST.get("usuario")
        nombre = request.POST.get("nombre")
        apellido= request.POST.get("apellido")
        pass1= request.POST.get("pass1")
        usu = User()
        usu.set_password(pass1)
        usu.username=usuario
        usu.last_name=apellido
        usu.first_name=nombre
        try:
            usu.save()
            contexto['mensaje']='grabo el usuario'    
        except:
            contexto['mensaje']='error al grabar'    
    return render(request,"registro2.html",contexto)

def perfil(request):
    mi_nombre= request.user.username
    tec = Tecnica.objects.all()
    cate = Categoria.objects.all()
    usuario= User.objects.get(username=mi_nombre)
    mis_obras= Obra.objects.filter(autor=usuario)
    galeria = Galeria.objects.all()
    contadort= mis_obras.count()
    contadora= mis_obras.filter(estado=True).count()
    contadorr= mis_obras.filter(estado=False).count()
    
    listing = Perfiles.objects.filter(user=usuario).first()
    if listing:   
        foto= Perfiles.objects.get(user=usuario)
        data= {'foto': foto, 'obras': mis_obras, 'user': usuario, 'contadort':contadort, 'contadora':contadora, 
           'contadorr':contadorr, 'tec':tec, 'cate':cate, 'gale':galeria}
        if request.POST:
            print('entro con')
            sw=int(request.POST.get("txtform"))
            print(f"entro {sw}")
            if sw == 1:
                nombre= request.POST.get("txttitulo")
                historia= request.POST.get("txthistoria")
                desc= request.POST.get("txtdescripcion")
                tecnica= request.POST.get("cbotecnica")
                precio= request.POST.get("txtprecio")
                categoria= request.POST.get("cbocategoria")
                foto_obra= request.FILES.get("customFile")
                obj_tecnica = Tecnica.objects.get(nombre=tecnica)
                obj_categoria = Categoria.objects.get(nombre=categoria)
                obra = Obra(
                    nombre = nombre,
                    historia = historia,
                    descripcion = desc,
                    tecnica= obj_tecnica,
                    precio = precio,
                    categoria = obj_categoria,
                    foto = foto_obra,
                    autor= usuario
                )
                obra.save()
                return render(request, 'perfil.html', data)

            if sw == 2:
                id_obra= request.POST.get("txtid")
                ob= Obra.objects.get(id_obra=id_obra)
                angulo1= request.POST.get("txtangulo1")
                angulo2= request.POST.get("txtangulo2")
                angulo3= request.POST.get("txtangulo3")
                foto_1= request.FILES.get("imggaleria1")
                foto_2= request.FILES.get("imggaleria2")
                foto_3= request.FILES.get("imggaleria3")
                galeria = Galeria(
                    angulo_1 = angulo1,
                    angulo_2 = angulo2,
                    angulo_3 = angulo3,
                    obra = ob,
                    foto_1 = foto_1,
                    foto_2 = foto_2,
                    foto_3 = foto_3
                )
                galeria.save()
                return render(request, 'perfil.html', data)
            if sw == 3:
                avatar= request.FILES.get("imgavatar")
                grupo= request.POST.get("txtgrupo")
                descripcion= request.POST.get("txtdespcripcionn")
                perfil = Perfiles(
                    user = usuario,
                    avatar = avatar,
                    grupo = grupo,
                    descripcion= descripcion,
                    
                )
                perfil.save()
                return redirect('PERF')
            if sw == 4:
                id = request.POST.get("txtid")
                nombre= request.POST.get("txttitulo")
                historia= request.POST.get("txthistoria")
                desc= request.POST.get("txtdescripcion")
                tecnica= request.POST.get("cbotecnica")
                precio= request.POST.get("txtprecio")
                categoria= request.POST.get("cbocategoria")
                foto_obra= request.FILES.get("customFile")
                obj_tecnica = Tecnica.objects.get(nombre=tecnica)
                obj_categoria = Categoria.objects.get(nombre=categoria)
                obra = Obra.objects.get(id_obra=id)
                obra.nombre = nombre
                obra.historia = historia
                obra.descripcion = desc
                obra.tecnica= obj_tecnica
                obra.precio = precio
                obra.categoria = obj_categoria
                obra.autor= usuario
                if foto_obra is not None:
                    obra.foto = foto_obra
                obra.save()
                return render(request, 'perfil.html', data)

    else:
        
        data= {'obras': mis_obras, 'user': usuario, 'contadort':contadort, 'contadora':contadora, 
           'contadorr':contadorr, 'tec':tec, 'cate':cate, 'gale':galeria}
        if request.POST:
            print('entro sin')
            sw=int(request.POST.get("txtform"))
            print(f"entro {sw}")
            if sw == 1:
                nombre= request.POST.get("txttitulo")
                historia= request.POST.get("txthistoria")
                desc= request.POST.get("txtdescripcion")
                tecnica= request.POST.get("cbotecnica")
                precio= request.POST.get("txtprecio")
                categoria= request.POST.get("cbocategoria")
                foto_obra= request.FILES.get("customFile")
                obj_tecnica = Tecnica.objects.get(nombre=tecnica)
                obj_categoria = Categoria.objects.get(nombre=categoria)
                obra = Obra(
                    nombre = nombre,
                    historia = historia,
                    descripcion = desc,
                    tecnica= obj_tecnica,
                    precio = precio,
                    categoria = obj_categoria,
                    foto = foto_obra,
                    autor= usuario
                )
                obra.save()
                return render(request, 'perfil.html', data)

            if sw == 2:
                id_obra= request.POST.get("txtid")
                ob= Obra.objects.get(id_obra=id_obra)
                angulo1= request.POST.get("txtangulo1")
                angulo2= request.POST.get("txtangulo2")
                angulo3= request.POST.get("txtangulo3")
                foto_1= request.FILES.get("imggaleria1")
                foto_2= request.FILES.get("imggaleria2")
                foto_3= request.FILES.get("imggaleria3")
                galeria = Galeria(
                    angulo_1 = angulo1,
                    angulo_2 = angulo2,
                    angulo_3 = angulo3,
                    obra = ob,
                    foto_1 = foto_1,
                    foto_2 = foto_2,
                    foto_3 = foto_3
                )
                galeria.save()
                return render(request, 'perfil.html', data)
            if sw == 3:
                avatar= request.FILES.get("imgavatar")
                grupo= request.POST.get("txtgrupo")
                descripcion= request.POST.get("txtdespcripcionn")
                perfil = Perfiles(
                    user = usuario,
                    avatar = avatar,
                    grupo = grupo,
                    descripcion= descripcion,
                    
                )
                perfil.save()
                return redirect('PERF')
            if sw == 4:
                id = request.POST.get("txtid")
                nombre= request.POST.get("txttitulo")
                historia= request.POST.get("txthistoria")
                desc= request.POST.get("txtdescripcion")
                tecnica= request.POST.get("cbotecnica")
                precio= request.POST.get("txtprecio")
                categoria= request.POST.get("cbocategoria")
                foto_obra= request.FILES.get("customFile")
                obj_tecnica = Tecnica.objects.get(nombre=tecnica)
                obj_categoria = Categoria.objects.get(nombre=categoria)
                obra = Obra.objects.get(id_obra=id)
                obra.nombre = nombre
                obra.historia = historia
                obra.descripcion = desc
                obra.tecnica= obj_tecnica
                obra.precio = precio
                obra.categoria = obj_categoria
                obra.autor= usuario
                if foto_obra is not None:
                    obra.foto = foto_obra
                obra.save()
                return render(request, 'perfil.html', data)
        
    return render(request, 'perfil.html', data)
    

        
    
        


def busca(request):
    artistas = User.objects.all()
    obras = Obra.objects.all()
    foto = Perfiles.objects.all()
    cbobusca=request.POST.get("cbobusca")
    contaro =Obra.objects.all().count()
    contara =User.objects.all().count()
    print(cbobusca)
    if request.method == "POST":
        if cbobusca == 'Artistas':
            busqueda = request.POST.get("txtbusca")
            artistas = User.objects.filter(first_name__icontains=busqueda.lower())
            contara = User.objects.filter(first_name__icontains=busqueda.lower()).count
            data = {'obras':obras, 'artistas':artistas ,'foto':foto, 'cantidad':contara}
            return render(request, 'artistas.html', data)
        if cbobusca == 'Obras':
            busqueda = request.POST.get("txtbusca")
            obras =  Obra.objects.filter(nombre__icontains=busqueda.lower())
            contaro = Obra.objects.filter(nombre__icontains=busqueda.lower()).count
            data = {'obras':obras, 'artistas':artistas , 'cantidad':contaro}
            return render(request, 'galeria.html', data)
    return redirect('IND')
    
def filtro_cate(request):
    cate = request.POST.get("cboCategoria")
    categorias = Categoria.objects.all()
    if cate=='Todos':
        obras=Obra.objects.filter(estado=True)
        contar = Obra.objects.all().count()
    else:
        obj_cate = Categoria.objects.get(nombre=cate)
        obras=Obra.objects.filter(categoria=obj_cate)
        contar = Obra.objects.filter(categoria=obj_cate).count()
    data = {'obras':obras , 'categorias':categorias,'cantidad':contar}
    return render(request, 'galeria.html', data)

def filtro_categoria(request,id):
    cate = id
    categorias = Categoria.objects.all()
    if cate=='Todos':
        obras=Obra.objects.filter(estado=True)
        contar = Obra.objects.all().count()
    else:
        obj_cate = Categoria.objects.get(nombre=cate)
        obras=Obra.objects.filter(categoria=obj_cate)
        contar = Obra.objects.filter(categoria=obj_cate).count()
    data = {'obras':obras , 'categorias':categorias,'cantidad':contar}
    return render(request, 'galeria.html', data)

@csrf_exempt
def verificar_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            User.objects.get(username=username)
            return JsonResponse({'available': False})
            
        except User.DoesNotExist:
            return JsonResponse({'available': True})

def carrito(request):
    obras = Obra.objects.all()
    data = {'obras':obras}
    return render(request, 'carrito.html', data)
