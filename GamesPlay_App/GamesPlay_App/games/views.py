from django.shortcuts import render, redirect

from GamesPlay_App.games.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from GamesPlay_App.games.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'core/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = get_profile()

    context = {
        'games': games,
        'profile': profile,
    }

    return render(request, 'core/dashboard.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'profiles/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    games = Game.objects.all()

    games_count = games.count()

    games_rating = 0.0
    if games:
        for game in games:
            games_rating += game.rating

        games_rating = games_rating / games_count

    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': games_rating,
    }

    return render(request, 'profiles/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profiles/delete-profile.html', context)


def game_create(request):
    profile = get_profile()

    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'games/create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'game': game,
    }

    return render(request, 'games/details-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'

    context = {
        'profile': profile,
        'game': game,
        'form': form,
    }

    return render(request, 'games/delete-game.html', context)
