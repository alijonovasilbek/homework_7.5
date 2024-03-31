from django.contrib import messages
from django.shortcuts import  get_object_or_404
from  .models import Prize
from .forms import PrizeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def base(request):
    return render(request,'bootstrap.html')



def prize_detail(request,pk):
    prize=Prize.objects.get(pk=pk)
    return render(request,'prize_info.html',context={'prize':prize})




def prize(request):
    if 'name' not in request.GET:
       prize=Prize.objects.all()

       return render(request,["prize.html","physics.html"],{"prize":prize})
    else:
        prize=Prize.objects.filter(name__contains=request.GET['name'])
        return render(request, "prize.html", {"prize": prize})


@login_required
def add_prize(request):
    if request.method=='POST':
        form=PrizeForm(request.POST,request.FILES)
        form.save()
        return redirect('prizes')

    form=PrizeForm()
    return render(request,'add_prize.html',{'form':form})



@login_required
def prize_edit(request, pk):
    this_prize = get_object_or_404(Prize, id=pk)
    if request.method == 'POST':
        form = PrizeForm(request.POST, request.FILES, instance=this_prize)
        if form.is_valid():
            form.save()
            return redirect('prize_info', pk=this_prize.pk)
    else:
        form = PrizeForm(instance=this_prize)
    return render(request, 'edit_prize.html', {'form': form})



@login_required
def prize_delete(request, pk):
    this_prize = get_object_or_404(Prize, id=pk)


    if request.user.email_confirmed:
        if  request.method == 'POST':
            this_prize.delete()
            return redirect('prizes')
        else:
            form=PrizeForm(instance=this_prize)
            return render(request,'delete_prize.html',{'form':form})

    else:
     messages.error(request, "Iltimos, avval elektron pochtangizni tasdiqlang.")
     return redirect('confirm_email')  # Elektron pochta tasdiqlash sahifasiga yo'naltiriladi

def physics(requst):
    prize=Prize.objects.all()
    return render(requst,'physics.html',{"prize":prize})


def literature(requst):
    prize=Prize.objects.all()
    return render(requst,'literature.html',{"prize":prize})


def chemistry(requst):
    prize=Prize.objects.all()
    return render(requst,'chemistry.html',{"prize":prize})
