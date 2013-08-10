%define oname ManPageEditor
%define debug_package	%{nil}
%define distsuffix mrb

Name:			manpageeditor
Version:		0.0.4
Release:		1
Summary:		Manual pages editor
License:		GPLv2
Group:			Books/Howtos
URL:			http://gnomefiles.org/content/show.php/Man+Page+Editor+?content=160219&PHPSESSID=3ccc8aaad076b075e5cfdcd4b533c357
Source0:		http://keithhedger.hostingsiteforfree.com/zips/manpageeditor/%{oname}-0.0.4.tar.gz

BuildRequires:		desktop-file-utils
BuildRequires:		pkgconfig(gtksourceview-2.0)
BuildRequires:      imagemagick


%description
Create,edit man-pages.

%prep
%setup -q -n %{oname}-%{version}


%build
%configure --prefix=/usr --enable-aspell
%make

%install
%makeinstall_std

# menu entry
desktop-file-install %{buildroot}%{_datadir}/applications/%{oname}.desktop \
	--remove-key=Encoding \
	--remove-key=Icon \
	--set-icon=%{oname} \
	--remove-key=Version
	

# icons	
install -d -m755 $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{oname}.png
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{oname}.png
convert ManPageEditor/resources/pixmaps/%{oname}.png -resize 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{oname}.png


%files
%doc ChangeLog 
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}/examples/*
%{_datadir}/%{oname}/help/*
%{_mandir}/man1/manpageeditor.1*
%{_miconsdir}/%{oname}.png
%{_iconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_datadir}/pixmaps/%{oname}.png

