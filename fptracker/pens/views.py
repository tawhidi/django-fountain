from django.shortcuts import render,redirect
from pens.models import Pen,PenForm


def index(request):
    all_pen = Pen.objects.all()
    context = {
        'pen_list': all_pen,
        'page_title': "Fountain pen website",
    }
    template_name = "index.html"
    return render(request,template_name,context)

def edit_pen(request,pen_id=None):
    if request.method=="POST":
        if pen_id is not None:
            pen = Pen.objects.get(id=pen_id)
            form = PenForm(request.POST,instance=pen)
        else:
            form = PenForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect("pens:index")

    else:
        if pen_id is not None:
            pen = Pen.objects.get(id=pen_id)
            form = PenForm(instance=pen)
        else:

            form = PenForm()
    context = {
        'form':form,
        'pen_id':pen_id
    }
    template_name = "edit_pen.html"
    return render(request,template_name,context)
    
def delete_pen(request,pen_id):
    pen = Pen.objects.get(id=pen_id)
    pen.delete()

    return redirect("pens:index")