Summary: A program which will display a fortune.
Name: fortune-mod
Version: 1.0
Release: 9
Copyright: BSD
Group: Amusements/Games
Source: ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune-mod-9708.tar.gz
Patch0: fortune-mod-offense.patch
BuildRoot: /var/tmp/fortune-mod-root

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
%patch0 -p1 -b .mike

%build
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{games,sbin,man/man1,man/man6,share/games/fortune}

make	FORTDIR=$RPM_BUILD_ROOT/usr/games \
	COOKIEDIR=$RPM_BUILD_ROOT/usr/share/games/fortunes \
	BINDIR=$RPM_BUILD_ROOT/usr/sbin \
	BINMANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	FORTMANDIR=$RPM_BUILD_ROOT/usr/man/man6 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog TODO
/usr/games/fortune
/usr/sbin/strfile
/usr/sbin/unstr
/usr/share/games/fortunes
/usr/man/man6/fortune.6
/usr/man/man1/strfile.1
/usr/man/man1/unstr.1
