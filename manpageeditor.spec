%define oname ManPageEditor
%define debug_package	%{nil}
%define distsuffix mrb

Name:			manpageeditor
Version:		0.0.6
Release:		1
Summary:		Manual pages editor
License:		GPLv3
Group:			Books/Howtos
URL:			http://gnomefiles.org/content/show.php/Man+Page+Editor+?content=160219&PHPSESSID=3ccc8aaad076b075e5cfdcd4b533c357
Source0:		http://keithhedger.hostingsiteforfree.com/zips/manpageeditor/%{oname}-%{version}.tar.gz


BuildRequires:		desktop-file-utils
BuildRequires:		pkgconfig(gtksourceview-2.0)
BuildRequires:      	aspell-devel
BuildRequires:     	imagemagick


%description
Create,edit man-pages.

%prep
%setup -q -n %{oname}-%{version}
cp -r ManPageEditor/resources/docs/gpl-3.0.txt gpl-3.0.txt

%build
%configure --prefix=/usr --enable-aspell
%make

# to be fix properly
perl -pi -e "s|xdg-icon-resource install --context mimetypes --size 128 ManPageEditor/resources/documenticons/maneditdoc.png application-x-maneditdoc||" Makefile
perl -pi -e "s|xdg-mime install ManPageEditor/resources/documenticons/maneditdoc-mime.xml||" Makefile
perl -pi -e "s|update-mime-database /usr/share/mime||" Makefile
perl -pi -e "s|gtk-update-icon-cache --force /usr/share/icons/hicolor||" Makefile



%install
%makeinstall_std 

# menu entry
desktop-file-install ManPageEditor/resources/applications/ManPageEditor.desktop
	

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

