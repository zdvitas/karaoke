# -*- coding: utf-8 -*-
# coding: utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
import datetime
from Karaoke import settings
from django.core.paginator import Paginator

from models import Artist
from models import Song
from models import Line
from models import NowPlay
import xlrd


def upload(request):
    context = {"status": "norm"}
    if request.method == "POST":
        rb = xlrd.open_workbook(settings.BASE_DIR + '/Orders/cat.xls', formatting_info=True)
        sheet = rb.sheet_by_index(0)
        base = {}
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            row[0] = int(row[0])
            if sheet.cell(rownum, 1).ctype == 3:
                row[1] = xlrd.xldate_as_tuple(row[1], 0)
                tmp = str(row[1][4])
                if tmp == "0":
                    tmp = "00"
                row[1] = str(row[1][3]) + ":" + tmp
            if sheet.cell(rownum, 1).ctype == 2:
                row[1] = int(row[1])

            b1 = Artist(name=row[2])
            try:
                b1.save()
            except:
                b1 = Artist.objects.filter(name=row[2])[0]

            s = Song(number=row[0], tittle=row[1], minus_quality=row[4], back_vocal=row[3], karaoke_system="test",
                     artist=b1)
            s.save()

        return render(request, 'Orders/upload.html', context)

    return render(request, 'Orders/upload.html', context)


def next_song(request):
    cur = NowPlay.objects.all()[0]
    song_list = get_song_list()
    if len(song_list) > 1:
        cur.table = song_list[1].table
        song_list[0].delete()
    else:
        cur.table = 1
        if len(song_list) == 1:
            song_list[0].delete()
    cur.save()

    return redirect("/admin")


def add_songs(request):
    return redirect("/")


def first(request):
    return redirect("/page1")


def log_out(request):
    logout(request)
    return redirect("/")


def home(request, page):
    if request.user.is_anonymous():
        return redirect("/auth")
    if request.user.is_staff:
        return redirect("/admin")
    context = {}
    table_num = request.user.username

    context["table"] = table_num
    context["songs"] = Song.objects.all()[1:10]
    if request.method == "POST":
        song = request.POST["song"].upper()
        artist = request.POST["artist"].upper()
        obj = Song.objects.all().filter(tittle__contains=song, artist__name__contains=artist)
        context["songs"] = obj

    return render(request, 'Orders/user_page.html', context)


def artists(request):
    context = {}
    obj = Artist.objects.all().order_by("name")
    context["artists"] = obj
    return render(request, 'Orders/artists.html', context)


def artist_list(request, id):
    context = {}
    obj = Song.objects.all().filter(artist__id=id)
    context["songs"] = obj
    return render(request, 'Orders/user_page.html', context)


def add_order(request, id):
    context = {}
    song = Song.objects.get(number=id)
    user = int(request.user.username)
    line = Line(song=song, table=user, date=datetime.datetime.now())
    line.save()
    context["ordered"] = "true"
    # Перекидывать на страницу с очередями
    return redirect("/pull_list")


def auth(request):
    context = {}
    context["users"] = User.objects.all().filter(is_staff=0)
    if request.method == "POST":
        username = request.POST["user"]
        password = request.POST["pass"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'Orders/auth.html', context)


def admin_line(request):
    if not request.user.is_staff:
        return redirect("/")
    context = {}
    tables = {}
    for tab in range(1, 12):
        tables[tab] = Line.objects.all().filter(table=tab).order_by("date")

    context["tables"] = sorted(tables.items())
    cur = NowPlay.objects.all()[0].table
    context["cur"] = cur
    return render(request, 'Orders/admin_line.html', context)


def admin_del(request, id):
    Line.objects.get(id=id).delete()
    return redirect("/admin")


def pull_list(request):
    song = {}
    list = get_song_list()
    song["songs"] = list
    return render(request, 'Orders/line_list.html', song)

def pull_list_dark(request):
    song = {}
    list = get_song_list()
    song["songs"] = list
    return render(request, 'Orders/line_list_dark.html', song)


def get_song_list():
    list = []
    cur = NowPlay.objects.all()[0]
    indexs = [0] * 11
    all_orders_count = len(Line.objects.all())
    while all_orders_count != 0:
        cur.table = cur.table % 12
        try:
            son = Line.objects.all().filter(table=cur.table).order_by("date")[indexs[cur.table]]
            indexs[cur.table] += 1
        except:
            son = None
        if son is not None:
            list.append(son)
            all_orders_count -= 1
        cur.table += 1
    return list