Summary:	eSvn - a cross-platform (Qt-based) GUI frontend for the Subversion revision system
Summary(pl):	eSvn - wieloplatformowy (oparty na Qt) graficzny interfejs u¿ytkownika do Subversion
Name:		esvn
Version:	0.6.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://esvn.umputun.com/%{name}-%{version}-1.tar.gz
# Source0-md5:	664de5f7fc4b0b1780f6abd801981a93
URL:		http://esvn.umputun.com/
BuildRequires:	qt-devel >= 3.0.0
Requires:	qt >= 3.0.0
Requires:	subversion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eSvn is a cross-platform (Qt-based) GUI frontend for the Subversion
revision system.

%description -l pl
eSvn jest wieloplatformowym (opartym na Qt) graficznym interfejsem
u¿ytkownika dla Subversion.

%prep
%setup -q -n %{name}

%build
export QTDIR=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_docdir}/esvn
install -m755 esvn $RPM_BUILD_ROOT%{_bindir}/esvn
install -m755 esvn-diff-wrapper $RPM_BUILD_ROOT%{_bindir}/esvn-diff-wrapper
install esvn.png $RPM_BUILD_ROOT%{_pixmapsdir}/esvn.png
install eSvn.desktop $RPM_BUILD_ROOT%{_desktopdir}/eSvn.desktop
cp -f -r html-docs $RPM_BUILD_ROOT%{_docdir}/esvn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog LICENSE README VERSION
%attr(755,root,root) %{_bindir}/esvn
%attr(755,root,root) %{_bindir}/esvn-diff-wrapper
%{_pixmapsdir}/esvn.png
%{_desktopdir}/eSvn.desktop
%{_docdir}/esvn
