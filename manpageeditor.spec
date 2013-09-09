%define oname ManPageEditor
%define debug_package	%{nil}
%define distsuffix mrb

Name:			manpageeditor
Version:		0.0.11
Release:		1
Summary:		Manual pages editor
License:		GPLv3
Group:			Books/Howtos
URL:			http://keithhedger.hostingsiteforfree.com/
Source0:		http://keithhedger.hostingsiteforfree.com/zips/manpageeditor/%{oname}-%{version}.tar.gz


BuildRequires:		desktop-file-utils
BuildRequires:		pkgconfig(gtksourceview-2.0)
BuildRequires:      	aspell-devel
BuildRequires:     	imagemagick


%description
Create,edit,import,preview man-pages.

%prep
%setup -q -n %{oname}-%{version}
cp -r ManPageEditor/resources/docs/gpl-3.0.txt gpl-3.0.txt

%build
%configure --prefix=/usr --enable-aspell
# to be fix properly
perl -pi -e "s|update-mime-database /usr/share/mime||" Makefile
perl -pi -e "s|gtk-update-icon-cache --force /usr/share/icons/hicolor||" Makefile
perl -pi -e "s|xdg-icon-resource install --context mimetypes --size 256 ManPageEditor/resources/documenticons/256/maneditdoc.png application-x-maneditdoc||" Makefile
perl -pi -e "s|xdg-icon-resource install --context mimetypes --size 128 ManPageEditor/resources/documenticons/128/maneditdoc.png application-x-maneditdoc||" Makefile
perl -pi -e "s|xdg-icon-resource install --context mimetypes --size 48 ManPageEditor/resources/documenticons/48/maneditdoc.png application-x-maneditdoc||" Makefile
perl -pi -e "s|xdg-mime install ManPageEditor/resources/documenticons/maneditdoc-mime.xml||" Makefile

%make

%install

%makeinstall_std 

# menu entry fix
desktop-file-install $RPM_BUILD_ROOT%{_datadir}/applications/%{oname}.desktop
# icons	
install -d -m755 $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{oname}.png
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{oname}.png
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{oname}.png

rm -fr $RPM_BUILD_ROOT%{_datadir}/%{oname}/docs

%files
%doc ChangeLog gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}/examples/*
%{_datadir}/%{oname}/help/*
%{_mandir}/man1/manpageeditor.1*
%{_miconsdir}/%{oname}.png
%{_iconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_datadir}/pixmaps/%{oname}.png

