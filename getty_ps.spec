Summary:	getty and uugetty
Summary(de.UTF-8):	getty und uugetty
Summary(fr.UTF-8):	getty et uugetty
Summary(pl.UTF-8):	getty i uugetty
Summary(tr.UTF-8):	getty ve uugetty
Name:		getty_ps
Version:	2.0.7j
Release:	16
License:	distributable - Copyright 1989,1990 by Paul Sutcliffe Jr.
Group:		Applications/System
Source0:	ftp://tsx-11.mit.edu/pub/linux/sources/sbin/%{name}-%{version}.tar.gz
# Source0-md5:	56bd3fd2f9a23ffdf96503f664f5c914
Patch0:		%{name}-misc.patch
Patch1:		%{name}-y2k.patch
Patch2:		%{name}-rb.patch
Patch3:		%{name}-hangup.patch
Patch4:		%{name}-mktemp.patch
URL:		ftp://tsx-11.mit.edu/pub/linux/sources/sbin/%{name}-%{version}.lsm
BuildRequires:	ncurses-devel >= 5.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
getty and uugetty are used to accept logins on the console or a
terminal. They can handle answer a modem for dialup connections
(although mgetty is recommended for that purpose).

%description -l de.UTF-8
getty und uugetty werden zum Akzeptieren von Logins auf der Konsole
oder einem Terminal verwendet und können ein Modem für Anwähl-
Verbindungen verwenden (wir empfehlen dafür allerdings mgetty).

%description -l fr.UTF-8
Getty et uugetty sont utilisés pour accepter les connexions sur la
console ou sur un terminal. Ils peuvent aussi prendre en charge un
modem pour une connexion par téléphone (bien que mgetty soit
recommandé pour cet usage.

%description -l pl.UTF-8
Programy getty i uugetty są używane do kontroli logowania na terminalu
lub konsoli. Mogą odpowiedzieć na żądanie modemu podczas połączenia
dialup. (W tym wypadku jednak mgetty jest polecane w miejsce getty_ps)

%description -l tr.UTF-8
getty ve uugetty konsol veya terminalerde sisteme giriş sürecini
başlatmakta kullanılır. Aynı zamanda çevirmeli ağ tipi bağlantılar
için modeme yanıt verme özelliklerine de sahiptirler (ama bunun için
mgetty daha kullanışlıdır).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# clean this ...
%{__make} clean

%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
	LIBS="-lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,usr/share/man/man{1,5},etc}

TOPDIR=$RPM_BUILD_ROOT make install

echo ".so getty.1" > $RPM_BUILD_ROOT%{_mandir}/man1/uugetty.1

install Examples/gettydefs.high-speed $RPM_BUILD_ROOT%{_sysconfdir}/gettydefs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Examples/default/* ANNOUNCE README*
%config(missingok) %verify(not md5 mtime size) %{_sysconfdir}/gettydefs
%attr(755,root,root) /sbin/*
%{_mandir}/man[15]/*
