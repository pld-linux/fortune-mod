Summary:	A program which will display a fortune.
Name:		fortune-mod
Version:	1.0
Release:	10
Copyright:	BSD
Group:		Amusements/Games
Source:		ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune-mod-9708.tar.gz
Patch0:		fortune-mod-offense.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's
your program. Fun-loving system administrators can add fortune to
users' .login files, so that the users get their dose of wisdom 
each time they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%prep
%setup -q -n fortune-mod-9708
%patch0 -p1

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_prefix}/games,%{_sbindir},%{_mandir}/man{1,6},%{_datadir}/games/fortune}

make	FORTDIR=$RPM_BUILD_ROOT%{_prefix}/games \
	COOKIEDIR=$RPM_BUILD_ROOT%{_datadir}/games/fortunes \
	BINDIR=$RPM_BUILD_ROOT%{_sbindir} \
	BINMANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	FORTMANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	install

strip --strip-unneeded $RPM_BUILD_ROOT{%{_sbindir}/*,%{_prefix}/games/fortune} || :

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1
echo ".so strfile.1" > $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1

gzip -9nf README ChangeLog TODO $RPM_BUILD_ROOT%{_mandir}/man{1,6}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO}.gz
%attr(755,root,root) %{_prefix}/games/fortune
%attr(755,root,root) %{_sbindir}/strfile
%attr(755,root,root) %{_sbindir}/unstr
%{_datadir}/games/fortunes
%{_mandir}/man6/fortune.6.gz
%{_mandir}/man1/*
