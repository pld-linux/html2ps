# don't use macros.perl here, it generates only unnecessary dependencies
Summary:	HTML to PostScript converter
Summary(pl):	Konwerter HTML do PostScriptu
Name:		html2ps
Version:	1.0b3
Release:	4
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.tdb.uu.se/~jan/%{name}-%{version}.tar.gz
# Source0-md5:	9386d64649a76e0ad2458393a91d0aab
Patch0:		%{name}-conf.patch
Patch1:		%{name}-perl_path.patch
Patch2:		%{name}-open.patch
URL:		http://www.tdb.uu.se/~jan/html2ps.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xbindir	/usr/X11R6/bin

%description
The Perl script html2ps converts HTML to PostScript. It would have
more capabilities if you have some of these packages installed:
ImageMagick, netpbm-progs, libjpeg-progs, perl-libwww, ghostscript,
tetex, tetex-dvips - see documentation for details.

html2ps can be used as ImageMagick delegate to convert from HTML.

%description -l pl
html2ps jest skryptem w Perlu konwertuj�cym HTML do PostScriptu.
Skrypt ma wi�ksze mo�liwo�ci, je�eli s� zainstalowane pakiety:
ImageMagick, netpbm-rpgs, libjpeg-progs, perl-libwww, ghostscript,
tetex, tetex-dvips - szczeg�y w dokumentacji.

html2ps mo�e by� u�ywany przez ImageMagick do konwersji z HTML.

%package -n xhtml2ps
Summary:	GUI frontend for html2ps, a HTML-to-PostScript converter
Summary(pl):	Interfejs graficzny do html2ps - konwertera HTML do PostScriptu
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}
Requires:	tk

%description -n xhtml2ps
xhtml2ps is freely-available GUI frontend for html2ps, a
HTML-to-PostScript converter.

%description -n xhtml2ps -l pl
xhtml2ps jest darmow� nak�adk� z interfejsem graficznym do html2ps -
konwertera z HTML do PostScriptu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_xbindir},%{_sysconfdir},%{_mandir}/man{1,5}}

sed \
	-e "s!@CONFDIR@!%{_sysconfdir}!" \
	-e "s!@DOCDIR@!%{_docdir}/%{name}-%{version}!" \
	html2ps > $RPM_BUILD_ROOT%{_bindir}/html2ps

sed \
	-e "s!@CONFDIR@!%{_sysconfdir}!" \
	html2ps.1 > $RPM_BUILD_ROOT%{_mandir}/man1/html2ps.1

install html2psrc.5 $RPM_BUILD_ROOT%{_mandir}/man5
install html2psrc $RPM_BUILD_ROOT%{_sysconfdir}
install contrib/xhtml2ps/xhtml2ps $RPM_BUILD_ROOT%{_xbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README html2ps.html sample
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size md5 mtime) %{_sysconfdir}/*
%{_mandir}/man[15]/*

%files -n xhtml2ps
%defattr(644,root,root,755)
%doc contrib/xhtml2ps/README
%attr(755,root,root) %{_xbindir}/*