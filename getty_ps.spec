Summary:     getty and uugetty
Summary(de): getty und uugetty
Summary(fr): getty et uugetty
Summary(pl): getty i uugetty
Summary(tr): getty ve uugetty
Name:        getty_ps
Version:     2.0.7j
Release:     5
Group:       Utilities/System
Copyright:   Distributable - Copyright 1989,1990 by Paul Sutcliffe Jr.
Source:      ftp://tsx-11.mit.edu/pub/linux/sources/sbin/%{name}-%{version}.tar.gz
Patch0:      getty_ps-make.patch
Patch1:      getty_ps-jpm.patch
Patch2:      getty_ps-pipe.patch
Patch3:      getty_ps-glibc.patch
Patch4:      getty_ps-signal.patch
Patch5:      getty_ps-ncurses.patch
Buildroot:   /tmp/%{name}-%{version}-%{release}-root

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
%patch0 -p1 -b .make
%patch1 -p1 -b .jpm
%patch2 -p1 -b .pipe
%patch3 -p1 -b .noglibc
%patch4 -p1 -b .signal
%patch5 -p1 -b .ncurses

%build
make clean
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,usr/man/{man1,man5},etc,var/log}

TOPDIR=$RPM_BUILD_ROOT make install

echo ".so getty.1" > $RPM_BUILD_ROOT/usr/man/man1/uugetty.1
install Examples/gettydefs.high-speed $RPM_BUILD_ROOT/etc/gettydefs
touch $RPM_BUILD_ROOT/var/log/getty.log

gzip -9nf $RPM_BUILD_ROOT/usr/man/man{1,5}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc Examples ANNOUNCE README.linux README.2.0.7j README.hi-speed
%config(missingok) %verify(not mtime size md5) /etc/gettydefs
%attr(755, root, root) /sbin/*
%attr(644, root,  man) /usr/man/man[15]/*
%attr(600, root,  man) %ghost /var/log/getty.log

%changelog
* Sat Dec 19 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.7j-5]
- changed permission on /var/log/getty.log to 600,
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment,
- added getty_ps-ncurses.patch for compiling getty_ps against ncurses,
- added using $RPM_OPT_FLAGS during compile.

* Tue Oct 06 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- adde pl translation,
- major modifications of the spec file. 

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- rebuilt to include doco.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Mar 26 1997 Erik Troan <ewt@redhat.com>
- Ported to glibc (I don't know where the last glibc package came from)
- Rebuilt because it was last built against some broken SPARC headers. 
