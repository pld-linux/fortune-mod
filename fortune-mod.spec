Summary:	A program which will display a fortune
Summary(cs):	Program suenka s vitbou (fortune cookie) s opravami chyb
Summary(da):	fortune-cookie program med mange fejl rettelser
Summary(de):	Glückskeks-Programm mit Bugfixes
Summary(es):	Fortune: frases famosas y refranes
Summary(fi):	Paranneltu fortnue-ohjelma
Summary(fr):	Programme fortune cookie avec correction de bugs.
Summary(pl):	Program wy¶wietlaj±cy losow± fortunkê
Summary(pt_BR):	Fortune: frases famosas e ditados
Summary(ru):	ðÒÏÇÒÁÍÍÁ, ÐÅÞÁÔÁÀÝÁÑ "fortune" (ÓÌÕÞÁÊÎÏ ×ÙÂÒÁÎÎÏÅ ÓÏÏÂÝÅÎÉÅ)
Summary(uk):	ðÒÏÇÒÁÍÁ, ÑËÁ ÄÒÕËÕ¤ "fortune" (×ÉÐÁÄËÏ×Ï ×ÉÂÒÁÎÅ ÐÏ×¦ÄÏÍÌÅÎÎÑ)
Name:		fortune-mod
Version:	1.0
Release:	23
License:	BSD
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/amusements/fortune/%{name}-9708.tar.gz
Patch0:		%{name}-offense.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

%description -l cs
Toto je trvale oblíbený program vìstící osud (fortune). Rád zobrazí
náhodnou vì¹tbu, je-li spu¹tìn. Obvykle je legrace, kdy¾ se umístí do
souboru .login pro u¾ivatele va¹eho systému, aby uvidìli nìco nového
poka¾dé, kdy¾ se pøihlásí.

%description -l da
Dette er det altid populære 'fortune' program. Det vil gladeligt
udskrive en tilfældig besked når det køres. Det er sjovt at have i
.login filen for dine brugere, så de altid ser noget nyt når de logger
ind.

%description -l de
Dies ist das beliebte Glückskeks-Programm. Es druckt eine zufällige
Weisheit. Wenn Sie es in die .login-Datei Ihrer Benutzer schreiben,
erhalten diese bei jedem Anmelden einen neuen Spruch.

%description -l es
Este es el popular programa fortune. Irá satisfactoriamente imprimir
un dictado aleatorio cuando se ejecute. Generalmente, es gracioso
ponerlo en el .login para sus usuarios, para que vean algo nuevo
cuuando entren.

%description -l fi
Tämä on aina suosittu fortune-ohjelma. Se tulostaa satunnaisen
mietelauseen tai vitsin aina ajettaessa. Se yleensä laitetaan
käynnistymään käyttäjien .login-tiedoston kautta, jolloin käyttäjä
näkee aina uuden lauseen kirjautuessaan sisään.

%description -l fr
Le célèbre programme fortune. Il affiche joyeusement un dicton
aléatoire lorsqu'il est lancé. Il est généralement amusant de le
placer dans le .login des utilisateurs d'un système pour qu'ils voient
quelque chose de nouveau à chaque fois qu'ils se loggent.

Cette version supporte l'utilisation de la variable $LANG pour choisir
automatiquemment un sous répertoire adapté à la langue de
l'utilisateur

%description -l it
Questo e' il popolare gioco fortune. Visualizza casualmente delle
frasi sul video. Gli utenti di solito lo aggiungono nel proprio .login
per vedere delle frasi divertenti ogni volta si collegano.

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

%description -l pt_BR
Este é o popular programa fortune. Ele irá alegremente imprimir um
ditado aleatório quando rodar. É geralmente engraçado colocá-lo no
.login para os seus usuários para que eles vejam algo novo toda vez
que entrarem.

%description -l ru
üÔÏ ×ÓÅÇÄÁ ÐÏÐÕÌÑÒÎÁÑ ÐÒÏÇÒÁÍÍÁ fortune. âÕÄÕÞÉ ÚÁÐÕÝÅÎÎÏÊ, ÏÎÁ
×Ù×ÏÄÉÔ ÓÌÕÞÁÊÎÏ ×ÙÂÒÁÎÎÏÅ ÉÚ ÂÁÚÙ ÓÏÏÂÝÅÎÉÅ. ïÂÙÞÎÏ ÅÅ ÐÏÍÅÝÁÀÔ ×
ÆÁÊÌ .login ÐÏÌØÚÏ×ÁÔÅÌÑÍ ÓÉÓÔÅÍÙ, × ÒÅÚÕÌØÔÁÔÅ ÞÅÇÏ ÏÎÉ ×ÓÑËÉÊ ÒÁÚ
ÐÒÉ ÌÏÇÉÎÅ ×ÉÄÑÔ ÞÔÏ-ÔÏ ÎÏ×ÏÅ.

%description -l tr
Fortune, her çaðrýldýðýnda büyük bir kitaplýktan rasgele seçeceði,
eðlenceli bir metni görüntüleyecektir. Aþýrý bilimsel ve yararlý bir
uygulama olmamasýna karþýn kullanýcýlarýn her sisteme baðlanýþýnda
deðiþik bir mesajla karþýlaþmalarýný saðlar.

%description -l uk
ãÅ ÚÁ×ÖÄÉ ÐÏÐÕÌÑÒÎÁ ÐÒÏÇÒÁÍÁ fortune. ðÒÉ ÚÁÐÕÓËÕ ×ÏÎÁ ÄÒÕËÕ¤
×ÉÐÁÄËÏ×Ï ×ÉÂÒÁÎÅ Ú ÂÁÚÉ ÐÏ×¦ÄÏÍÌÅÎÎÑ. ñË ÐÒÁ×ÉÌÏ §§ ×ÉËÌÉË ×ËÌÀÞÁÀÔØ
× ÆÁÊÌ .login ËÏÒÉÓÔÕ×ÁÞÁÍ ÓÉÓÔÅÍÉ, × ÒÅÚÕÌØÔÁÔ¦ ÞÏÇÏ ×ÏÎÉ ËÏÖÎÏÇÏ
ÒÁÚÕ ÐÒÉ ×ÈÏÄ¦ × ÓÉÓÔÅÍÕ ÂÁÞÁÔØ ÎÏ×Å ÐÏ×¦ÄÏÍÌÅÎÎÑ.

%package data
Summary:	A program which will display a fortune
Summary(pl):	Program wy¶wietlaj±cy losow± fortunkê
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
%{__make} fortune/fortune.man

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{1,6},%{_datadir}/games/fortune}

%{__make} install \
	FORTDIR=$RPM_BUILD_ROOT%{_bindir} \
	COOKIEDIR=$RPM_BUILD_ROOT%{_datadir}/games/fortunes \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	BINMANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	FORTMANDIR=$RPM_BUILD_ROOT%{_mandir}/man6

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1
echo ".so strfile.1" > $RPM_BUILD_ROOT%{_mandir}/man1/unstr.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/fortune.6*
%{_mandir}/man1/*

%files data
%defattr(644,root,root,755)
%{_datadir}/games/fortunes
