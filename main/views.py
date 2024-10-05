from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tashkilot, Tuman, Xizmatlar, Axoli, Mahalla
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


# View for showing the logged-in user's tashkilot and tumans
@login_required
def tashkilot_view(request):
    tashkilot = get_object_or_404(Tashkilot, user=request.user)
    tumanlar = Tuman.objects.filter(tashkilot=tashkilot)
    tumans = tumanlar.count()
    return render(request, 'tashkilot.html', {'tashkilot': tashkilot, 'tumanlar': tumanlar, 'tumans': tumans})

# View for showing mahallas in a tuman
@login_required
def tuman_view(request, tuman_id):
    tuman = get_object_or_404(Tuman, id=tuman_id)
    mahallalar = Mahalla.objects.filter(tuman=tuman)
    mahallas = mahallalar.count()
    return render(request, 'tuman.html', {'tuman': tuman, 'mahallalar': mahallalar, 'mahallas':mahallas})

# View for showing xizmatlar in a mahalla
@login_required
def mahalla_view(request, mahalla_id):
    mahalla = get_object_or_404(Mahalla, id=mahalla_id)
    xizmatlar = Xizmatlar.objects.filter(mahalla=mahalla)
    return render(request, 'mahalla.html', {'mahalla': mahalla, 'xizmatlar': xizmatlar, 'xizmats':xizmatlar.count()})

# View for showing axoli who have used a xizmat
@login_required
def xizmatlar_view(request, xizmat_id):
    xizmat = get_object_or_404(Xizmatlar, id=xizmat_id)
    axolis = Axoli.objects.filter(xizmat=xizmat)
    return render(request, 'xizmat.html', {'xizmat': xizmat, 'axolis': axolis})

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to tashkilot page after login
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')

@login_required
def axoli_detail_view(request, axoli_id):
    axoli = get_object_or_404(Axoli, id=axoli_id)
    return render(request, 'info.html', {'axoli': axoli})