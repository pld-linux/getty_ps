Summary:	getty and uugetty
Summary(de):	getty und uugetty
Summary(fr):	getty et uugetty
Summary(pl):	getty i uugetty
Summary(tr):	getty ve uugetty
Name:		getty_ps
Version:	2.0.7j
Release:	6
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Copyright:	Distributable - Copyright 1989,1990 by Paul Sutcliffe Jr.
URL:		ftp://tsx-11.mit.edu/pub/linux/sources/sbin
Source:		%{name}-%{version}.tar.gz
Patch0:		getty_ps-misc.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
getty and uugetty are used to accept logins on the console or
a terminal.  They can handle answer a modem for dialup connections
(although mgetty is recommended for that purpose).

%description -l de
getty und uugetty werden zum Akzeptieren von Logins auf der Konsole
oder einem Terminal verwendet und können ein Modem für Anwähl-
Verbindungen verwenden (wir empfehlen dafür allerdings mgetty).

%description -l fr
Getty et uugetty sont utilisés pour accepter les connexions sur la
console ou sur un terminal. Ils peuvent aussi prendre en charge un
modem pour une connexion par téléphone (bien que mgetty soit
recommandé pour cet usage.

%description -l pl
Programy getty i uugetty s± u¿ywane do kontroli logowania na terminalu lub
konsoli. Mog± odpowiedzieæ na ¿±danie modemu podczas po³±czenia dialup.
(W tym wypadku jednak mgetty jest polecane w miejsce getty_ps)

%description -l tr
getty ve uugetty konsol veya terminalerde sisteme giriþ sürecini baþlatmakta
kullanýlýr. Ayný zamanda çevirmeli að tipi baðlantýlar için modeme yanýt
verme özelliklerine de sahiptirler (ama bunun için mgetty daha kullanýþlýdýr).

%prep
%setup -q
%patch -p1 

%build
# clean this ...
make clean

make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,usr/share/man/man{1,5},etc}

TOPDIR=$RPM_BUILD_ROOT make install

echo ".so getty.1" > $RPM_BUILD_ROOT%{_mandir}/man1/uugetty.1

install Examples/gettydefs.high-speed $RPM_BUILD_ROOT/etc/gettydefs

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,5}/* Examples/default/* \
	    ANNOUNCE README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Examples/default/* ANNOUNCE.gz README*

%config(missingok) %verify(not mtime size md5) /etc/gettydefs

%attr(755,root,root) /sbin/*
%{_mandir}/man[15]/*
