Summary:	A program which will display a fortune
Summary(pl):	Program wy¶wietlaj±cy losow± fortunkê
Name:		fortune-mod
Version:	1.0
Release:	12
License:	BSD
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune/%{name}-9708.tar.gz
Patch0:		%{name}-offense.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

%package data
Summary:	A program which will display a fortune
Summary(pl):	Program wy¶wietlaj±cy losow± fortunkê
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Requires:	%{name}

%description data
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

This package constain english data files for fortunes.

%description data -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

Ten pakiet zawiera angielskie pliki z danymi dla fortunek.

%prep
%setup -q -n fortune-mod-9708
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags} \\\$(DEFINES)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_sbindir},%{_mandir}/man{1,6},%{_datadir}/games/fortune}

%{__make} FORTDIR=$RPM_BUILD_ROOT%{_prefix}/games \
	COOKIEDIR=$RPM_BUILD_ROOT%{_datadir}/games/fortunes \
	BINDIR=$RPM_BUILD_ROOT%{_sbindir} \
	BINMANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	FORTMANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	install

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1
echo ".so strfile.1" > $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1

gzip -9nf README ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO}.gz
%attr(755,root,root) %{_prefix}/games/fortune
%attr(755,root,root) %{_sbindir}/strfile
%attr(755,root,root) %{_sbindir}/unstr
%{_mandir}/man6/fortune.6*
%{_mandir}/man1/*

%files data
%defattr(644,root,root,755)
%{_datadir}/games/fortunes
