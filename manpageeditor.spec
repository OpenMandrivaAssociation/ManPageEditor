%define oname ManPageEditor
%define debug_package	%{nil}
#define distsuffix mrb

Name:			manpageeditor
Version:		0.0.15
Release:		1
Summary:		Manual pages editor
License:		GPLv3
Group:			Books/Howtos
URL:			https://keithhedger.hostingsiteforfree.com/
Source0:		http://keithhedger.hostingsiteforfree.com/zips/manpageeditor/%{oname}-%{version}.tar.gz
BuildRequires:		desktop-file-utils
BuildRequires:		pkgconfig(gtksourceview-2.0)
BuildRequires:   	aspell-devel
BuildRequires:     	imagemagick
BuildRequires:     	pkgconfig(gdk-2.0)

%description
Create,edit,import,preview man-pages.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure --prefix=/usr --enable-aspell
%make

%install
# installer is a total mess...
mkdir -p %{buildroot}%{_bindir}
install -m755 ManPageEditor/app/%{name} %{buildroot}%{_bindir}
# man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -m644  ManPageEditor/resources/man/manpageeditor.1 %{buildroot}%{_mandir}/man1
# data files
mkdir -p %{buildroot}%{_datadir}/%{oname}
cp -R ManPageEditor/resources/examples %{buildroot}%{_datadir}/%{oname}/examples
# menu entry fix
mkdir -p %{buildroot}%{_datadir}/applications
cp -R ManPageEditor/resources/applications/%{oname}.desktop %{buildroot}%{_datadir}/applications/%{oname}.desktop
desktop-file-install %{buildroot}%{_datadir}/applications/%{oname}.desktop
# icons	
install -d -m755 %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{oname}.png
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{oname}.png
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 48x48 %{buildroot}%{_liconsdir}/%{oname}.png

rm -fr %{buildroot}%{_datadir}/%{oname}/docs

%files
%doc ChangeLog ManPageEditor/resources/docs/gpl-3.0.txt ManPageEditor/resources/help
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}/examples/*
%{_mandir}/man1/manpageeditor.1*
%{_miconsdir}/%{oname}.png
%{_iconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png