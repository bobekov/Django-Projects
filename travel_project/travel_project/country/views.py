from django.shortcuts import render, redirect, get_object_or_404
from travel_project.country.forms import AddCountry, DeleteCountry
from travel_project.country.models import Country


def details_country(request):
    countries = Country.objects.all()

    context = {
        'countries': countries
    }
    return render(request, 'country/details-country.html', context)


def add_new_country(request):
    if request.method == "POST":
        form = AddCountry(request.POST)

        if form.is_valid():
            country = form.save(commit=False)
            country.user = request.user
            country.save()
            return redirect("details-country")
    else:
        form = AddCountry()

    context = {
        "form": form
    }

    return render(request, 'country/add-country.html', context)


def edit_country(request, pk):
    country = get_object_or_404(Country, pk=pk)

    form = AddCountry(instance=country)

    if request.method == 'POST':
        form = AddCountry(request.POST, instance=country)
        if form.is_valid():
            country = form.save(commit=False)
            country.user = request.user
            country.save()
            return redirect('details-country')

    context = {
        'form': form,
        'country': country,
    }
    return render(request, 'country/edit-country.html', context)


def delete_country(request, pk):
    country = get_object_or_404(Country, pk=pk)

    if request.method == 'POST':
        confirmation = request.POST.get('confirmation')

        if confirmation == 'Yes':
            country.delete()
            return redirect('details-country')
        else:
            return redirect('details-country')

    return render(request, 'country/delete-country.html', {'country': country})