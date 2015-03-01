#
# Conditional build:
%bcond_with	offensive	# include offensive fortunes
#
Summary:	A program which will display a fortune
Summary(cs.UTF-8):	Program suenka s vitbou (fortune cookie) s opravami chyb
Summary(da.UTF-8):	fortune-cookie program med mange fejl rettelser
Summary(de.UTF-8):	Glückskeks-Programm mit Bugfixes
Summary(es.UTF-8):	Fortune: frases famosas y refranes
Summary(fi.UTF-8):	Paranneltu fortnue-ohjelma
Summary(fr.UTF-8):	Programme fortune cookie avec correction de bugs
Summary(pl.UTF-8):	Program wyświetlający losową fortunkę
Summary(pt_BR.UTF-8):	Fortune: frases famosas e ditados
Summary(ru.UTF-8):	Программа, печатающая "fortune" (случайно выбранное сообщение)
Summary(uk.UTF-8):	Програма, яка друкує "fortune" (випадково вибране повідомлення)
Name:		fortune-mod
Version:	1.99.1
Release:	5
License:	BSD
Group:		Applications/Games
#Source0:	ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune/%{name}-9708.tar.gz
Source0:	http://www.redellipse.net/code/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	f208805b3b712e32997d7667e0ec52d8
Source1:	%{name}.sh
Source2:	%{name}.csh
Patch0:		%{name}-usage.patch
BuildRequires:	recode-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

%description -l cs.UTF-8
Toto je trvale oblíbený program věstící osud (fortune). Rád zobrazí
náhodnou věštbu, je-li spuštěn. Obvykle je legrace, když se umístí do
souboru .login pro uživatele vašeho systému, aby uviděli něco nového
pokaždé, když se přihlásí.

%description -l da.UTF-8
Dette er det altid populære 'fortune' program. Det vil gladeligt
udskrive en tilfældig besked når det køres. Det er sjovt at have i
.login filen for dine brugere, så de altid ser noget nyt når de logger
ind.

%description -l de.UTF-8
Dies ist das beliebte Glückskeks-Programm. Es druckt eine zufällige
Weisheit. Wenn Sie es in die .login-Datei Ihrer Benutzer schreiben,
erhalten diese bei jedem Anmelden einen neuen Spruch.

%description -l es.UTF-8
Este es el popular programa fortune. Irá satisfactoriamente imprimir
un dictado aleatorio cuando se ejecute. Generalmente, es gracioso
ponerlo en el .login para sus usuarios, para que vean algo nuevo
cuuando entren.

%description -l fi.UTF-8
Tämä on aina suosittu fortune-ohjelma. Se tulostaa satunnaisen
mietelauseen tai vitsin aina ajettaessa. Se yleensä laitetaan
käynnistymään käyttäjien .login-tiedoston kautta, jolloin käyttäjä
näkee aina uuden lauseen kirjautuessaan sisään.

%description -l fr.UTF-8
Le célèbre programme fortune. Il affiche joyeusement un dicton
aléatoire lorsqu'il est lancé. Il est généralement amusant de le
placer dans le .login des utilisateurs d'un système pour qu'ils voient
quelque chose de nouveau à chaque fois qu'ils se loggent.

Cette version supporte l'utilisation de la variable $LANG pour choisir
automatiquemment un sous répertoire adapté à la langue de
l'utilisateur

%description -l it.UTF-8
Questo e' il popolare gioco fortune. Visualizza casualmente delle
frasi sul video. Gli utenti di solito lo aggiungono nel proprio .login
per vedere delle frasi divertenti ogni volta si collegano.

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

%description -l pt_BR.UTF-8
Este é o popular programa fortune. Ele irá alegremente imprimir um
ditado aleatório quando rodar. É geralmente engraçado colocá-lo no
.login para os seus usuários para que eles vejam algo novo toda vez
que entrarem.

%description -l ru.UTF-8
Это всегда популярная программа fortune. Будучи запущенной, она
выводит случайно выбранное из базы сообщение. Обычно ее помещают в
файл .login пользователям системы, в результате чего они всякий раз
при логине видят что-то новое.

%description -l tr.UTF-8
Fortune, her çağrıldığında büyük bir kitaplıktan rasgele seçeceği,
eğlenceli bir metni görüntüleyecektir. Aşırı bilimsel ve yararlı bir
uygulama olmamasına karşın kullanıcıların her sisteme bağlanışında
değişik bir mesajla karşılaşmalarını sağlar.

%description -l uk.UTF-8
Це завжди популярна програма fortune. При запуску вона друкує
випадково вибране з бази повідомлення. Як правило її виклик включають
в файл .login користувачам системи, в результаті чого вони кожного
разу при вході в систему бачать нове повідомлення.

%package data
Summary:	A program which will display a fortune
Summary(pl.UTF-8):	Program wyświetlający losową fortunkę
Group:		Applications/Games
Requires:	%{name}

%description data
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

This package contains English data files for fortune-mod.

%description data -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

Ten pakiet zawiera angielskie pliki z danymi dla fortune-mod.

%package on-login
Summary:	Displays fortune cookie on login
Summary(pl.UTF-8):	Wyświetla fortunkę przy logowaniu
Group:		Applications/Games
Requires:	%{name}

%description on-login
If you want fortune cookie to be displayed each time when you log on
this package is what you need.

%description on-login -l pl.UTF-8
Jeśli chcesz, żeby fortunka była wyświetlana przy każdym logowaniu ten
pakiet jest tym, czego potrzebujesz.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} \\\$(DEFINES)" \
	%{?with_offensive:OFFENSIVE=1}

%{__make} fortune/fortune.man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{1,6},%{_datadir}/games/fortune,/etc/profile.d}

%{__make} install \
	FORTDIR=$RPM_BUILD_ROOT%{_bindir} \
	COOKIEDIR=$RPM_BUILD_ROOT%{_datadir}/games/fortunes \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	BINMANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	FORTMANDIR=$RPM_BUILD_ROOT%{_mandir}/man6 \
	%{?with_offensive:OFFENSIVE=1}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1*

cp -a %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/profile.d
echo '.so strfile.1' > $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/fortune.6*
%{_mandir}/man1/*
%dir %{_datadir}/games/fortunes

%files data
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
%defattr(644,root,root,755)

%files on-login
%defattr(644,root,root,755)
/etc/profile.d/*
