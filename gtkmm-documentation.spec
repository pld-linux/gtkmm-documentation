%define		glibmm_ver	2.24.0
%define		gtkmm_ver	2.24.0
Summary:	Documentation and examples for gtkmm - C++ API for GTK+
Summary(pl.UTF-8):	Dokumentacja i przykłady do gtkmm - API C++ dla GTK+
Name:		gtkmm-documentation
Version:	2.24.1
Release:	1
License:	FDL v1.2+ (documentation), GPL v2 (examples)
Group:		Documentation
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtkmm-documentation/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	2fcf511c949e8bfd2ff4c05b6cfc3b3b
URL:		http://www.gtkmm.org/
#BuildRequires:	autoconf >= 2.59
#BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd45-xml
BuildRequires:	glibmm-devel >= %{glibmm_ver}
BuildRequires:	gnome-doc-utils >= 0.9.0
BuildRequires:	gtkmm-devel >= %{gtkmm_ver}
BuildRequires:	libstdc++-devel >= 5:3.3.1
BuildRequires:	mm-common
BuildRequires:	perl-base >= 1:5.6.0
BuildRequires:	pkgconfig
Requires:	gtkmm-apidocs >= %{gtkmm_ver}
Suggests:	glibmm-devel >= %{glibmm_ver}
Suggests:	gtkmm-devel >= %{gtkmm_ver}
# common gnome/help/gtkmm-tutorial namespace
Conflicts:	gtkmm3-documentation
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the documentation and example programs for
gtkmm 2.x - C++ API for GTK+ 2.x.

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację oraz programy przykładowe do
gtkmm 2.x - API C++ dla GTK+ 2.x.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/gtkmm-%{version}
cp -pr examples/{book,others,README} $RPM_BUILD_ROOT%{_examplesdir}/gtkmm-%{version}

%find_lang gtkmm-tutorial --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gtkmm-tutorial.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_docdir}/gtkmm-2.4/tutorial
%{_examplesdir}/gtkmm-%{version}
