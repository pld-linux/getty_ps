Summary:	getty and uugetty
Summary(de):	getty und uugetty
Summary(fr):	getty et uugetty
Summary(pl):	getty i uugetty
Summary(tr):	getty ve uugetty
Name:		getty_ps
Version:	2.0.7j
Release:	10
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Copyright:	Distributable - Copyright 1989,1990 by Paul Sutcliffe Jr.
URL:		ftp://tsx-11.mit.edu/pub/linux/sources/sbin
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-misc.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
getty and uugetty are used to accept logins on the console or a
terminal. They can handle answer a modem for dialup connections
(although mgetty is recommended for that purpose).

%description -l de
getty und uugetty werden zum Akzeptieren von Logins auf der Konsole
oder einem Terminal verwendet und k�nnen ein Modem f�r Anw�hl-
Verbindungen verwenden (wir empfehlen daf�r allerdings mgetty).

%description -l fr
Getty et uugetty sont utilis�s pour accepter les connexions sur la
console ou sur un terminal. Ils peuvent aussi prendre en charge un
modem pour une connexion par t�l�phone (bien que mgetty soit
recommand� pour cet usage.

%description -l pl
Programy getty i uugetty s� u�ywane do kontroli logowania na terminalu
lub konsoli. Mog� odpowiedzie� na ��danie modemu podczas po��czenia
dialup. (W tym wypadku jednak mgetty jest polecane w miejsce getty_ps)

%description -l tr
getty ve uugetty konsol veya terminalerde sisteme giri� s�recini
ba�latmakta kullan�l�r. Ayn� zamanda �evirmeli a� tipi ba�lant�lar
i�in modeme yan�t verme �zelliklerine de sahiptirler (ama bunun i�in
mgetty daha kullan��l�d�r).

%prep
%setup -q
%patch -p1 

%build
# clean this ...
%{__make} clean

%{__make} OPT="%{rpmcflags}" LIBS="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,usr/share/man/man{1,5},etc}

TOPDIR=$RPM_BUILD_ROOT make install

echo ".so getty.1" > $RPM_BUILD_ROOT%{_mandir}/man1/uugetty.1

install Examples/gettydefs.high-speed $RPM_BUILD_ROOT%{_sysconfdir}/gettydefs

gzip -9nf Examples/default/* ANNOUNCE README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Examples/default/* ANNOUNCE.gz README*

%config(missingok) %verify(not mtime size md5) %{_sysconfdir}/gettydefs

%attr(755,root,root) /sbin/*
%{_mandir}/man[15]/*
