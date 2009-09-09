# don't use macros.perl here, it generates only unnecessary dependencies
Summary:	HTML to PostScript converter
Summary(pl.UTF-8):	Konwerter HTML-a do PostScriptu
Name:		html2ps
Version:	1.0b5
Release:	7
License:	GPL
Group:		Applications/Graphics
Source0:	http://user.it.uu.se/~jan/%{name}-%{version}.tar.gz
# Source0-md5:	0998fefa4c8f9a04c88cfac7a83df629
Patch0:		%{name}-conf.patch
Patch1:		%{name}-perl_path.patch
Patch2:		%{name}-open.patch
URL:		http://user.it.uu.se/~jan/html2ps.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Perl script html2ps converts HTML to PostScript. It would have
more capabilities if you have some of these packages installed:
ImageMagick, netpbm-progs, libjpeg-progs, perl-libwww, ghostscript,
tetex, tetex-dvips - see documentation for details.

html2ps can be used as ImageMagick delegate to convert from HTML.

%description -l pl.UTF-8
html2ps jest skryptem w Perlu konwertującym HTML do PostScriptu.
Skrypt ma większe możliwości, jeżeli są zainstalowane pakiety:
ImageMagick, netpbm-rpgs, libjpeg-progs, perl-libwww, ghostscript,
tetex, tetex-dvips - szczegóły w dokumentacji.

html2ps może być używany przez ImageMagick do konwersji z HTML-a.

%package -n xhtml2ps
Summary:	GUI frontend for html2ps, a HTML-to-PostScript converter
Summary(pl.UTF-8):	Interfejs graficzny do html2ps - konwertera HTML-a do PostScriptu
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	tk

%description -n xhtml2ps
xhtml2ps is freely-available GUI frontend for html2ps, a
HTML-to-PostScript converter.

%description -n xhtml2ps -l pl.UTF-8
xhtml2ps jest darmową nakładką z interfejsem graficznym do html2ps -
konwertera z HTML-a do PostScriptu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man{1,5}}

sed \
	-e "s!@CONFDIR@!%{_sysconfdir}!" \
	-e "s!@DOCDIR@!%{_docdir}/%{name}-%{version}!" \
	html2ps > $RPM_BUILD_ROOT%{_bindir}/html2ps

sed \
	-e "s!@CONFDIR@!%{_sysconfdir}!" \
	html2ps.1 > $RPM_BUILD_ROOT%{_mandir}/man1/html2ps.1

install html2psrc.5 $RPM_BUILD_ROOT%{_mandir}/man5
install html2psrc $RPM_BUILD_ROOT%{_sysconfdir}
install contrib/xhtml2ps/xhtml2ps $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README html2ps.html sample
%attr(755,root,root) %{_bindir}/html2ps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man[15]/*

%files -n xhtml2ps
%defattr(644,root,root,755)
%doc contrib/xhtml2ps/README
%attr(755,root,root) %{_bindir}/xhtml2ps
