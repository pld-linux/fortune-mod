Summary:	A program which will display a fortune
Summary(cs):	Program suenka s vitbou (fortune cookie) s opravami chyb
Summary(da):	fortune-cookie program med mange fejl rettelser
Summary(de):	Gl�ckskeks-Programm mit Bugfixes
Summary(es):	Fortune: frases famosas y refranes
Summary(fi):	Paranneltu fortnue-ohjelma
Summary(fr):	Programme fortune cookie avec correction de bugs.
Summary(pl):	Program wy�wietlaj�cy losow� fortunk�
Summary(pt_BR):	Fortune: frases famosas e ditados
Summary(ru):	���������, ���������� "fortune" (�������� ��������� ���������)
Summary(uk):	��������, ��� ����դ "fortune" (��������� ������� ��צ��������)
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
Toto je trvale obl�ben� program v�st�c� osud (fortune). R�d zobraz�
n�hodnou v�tbu, je-li spu�t�n. Obvykle je legrace, kdy� se um�st� do
souboru .login pro u�ivatele va�eho syst�mu, aby uvid�li n�co nov�ho
poka�d�, kdy� se p�ihl�s�.

%description -l da
Dette er det altid popul�re 'fortune' program. Det vil gladeligt
udskrive en tilf�ldig besked n�r det k�res. Det er sjovt at have i
.login filen for dine brugere, s� de altid ser noget nyt n�r de logger
ind.

%description -l de
Dies ist das beliebte Gl�ckskeks-Programm. Es druckt eine zuf�llige
Weisheit. Wenn Sie es in die .login-Datei Ihrer Benutzer schreiben,
erhalten diese bei jedem Anmelden einen neuen Spruch.

%description -l es
Este es el popular programa fortune. Ir� satisfactoriamente imprimir
un dictado aleatorio cuando se ejecute. Generalmente, es gracioso
ponerlo en el .login para sus usuarios, para que vean algo nuevo
cuuando entren.

%description -l fi
T�m� on aina suosittu fortune-ohjelma. Se tulostaa satunnaisen
mietelauseen tai vitsin aina ajettaessa. Se yleens� laitetaan
k�ynnistym��n k�ytt�jien .login-tiedoston kautta, jolloin k�ytt�j�
n�kee aina uuden lauseen kirjautuessaan sis��n.

%description -l fr
Le c�l�bre programme fortune. Il affiche joyeusement un dicton
al�atoire lorsqu'il est lanc�. Il est g�n�ralement amusant de le
placer dans le .login des utilisateurs d'un syst�me pour qu'ils voient
quelque chose de nouveau � chaque fois qu'ils se loggent.

Cette version supporte l'utilisation de la variable $LANG pour choisir
automatiquemment un sous r�pertoire adapt� � la langue de
l'utilisateur

%description -l it
Questo e' il popolare gioco fortune. Visualizza casualmente delle
frasi sul video. Gli utenti di solito lo aggiungono nel proprio .login
per vedere delle frasi divertenti ogni volta si collegano.

%description -l pl
Fortune-mod zawiera wci�� popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochot� na odrobin� m�dro�ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog� doda� fortune do plik�w .login u�ytkownik�w tak,
by ka�dy otrzyma� swoj� dawk� m�dro�ci przy logowaniu.

%description -l pt_BR
Este � o popular programa fortune. Ele ir� alegremente imprimir um
ditado aleat�rio quando rodar. � geralmente engra�ado coloc�-lo no
.login para os seus usu�rios para que eles vejam algo novo toda vez
que entrarem.

%description -l ru
��� ������ ���������� ��������� fortune. ������ ����������, ���
������� �������� ��������� �� ���� ���������. ������ �� �������� �
���� .login ������������� �������, � ���������� ���� ��� ������ ���
��� ������ ����� ���-�� �����.

%description -l tr
Fortune, her �a�r�ld���nda b�y�k bir kitapl�ktan rasgele se�ece�i,
e�lenceli bir metni g�r�nt�leyecektir. A��r� bilimsel ve yararl� bir
uygulama olmamas�na kar��n kullan�c�lar�n her sisteme ba�lan���nda
de�i�ik bir mesajla kar��la�malar�n� sa�lar.

%description -l uk
�� ������ ��������� �������� fortune. ��� ������� ���� ����դ
��������� ������� � ���� ��צ��������. �� ������� �� ������ ���������
� ���� .login ������������ �������, � ��������Ԧ ���� ���� �������
���� ��� ���Ħ � ������� ������ ���� ��צ��������.

%package data
Summary:	A program which will display a fortune
Summary(pl):	Program wy�wietlaj�cy losow� fortunk�
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
Fortune-mod zawiera wci�� popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochot� na odrobin� m�dro�ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog� doda� fortune do plik�w .login u�ytkownik�w tak,
by ka�dy otrzyma� swoj� dawk� m�dro�ci przy logowaniu.

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
