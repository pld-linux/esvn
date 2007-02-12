Summary:	eSvn - a cross-platform (Qt-based) GUI frontend for the Subversion revision system
Summary(pl.UTF-8):	eSvn - wieloplatformowy (oparty na Qt) graficzny interfejs użytkownika do Subversion
Name:		esvn
Version:	0.6.11
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://esvn.umputun.com/%{name}-%{version}-1.tar.gz
# Source0-md5:	2ded6a349fc8692631f781bbb475fadc
Patch0:		%{name}-build.patch
URL:		http://esvn.umputun.com/
BuildRequires:	qmake
BuildRequires:	qt-devel >= 3.0.0
BuildRequires:	sed >= 4.0
Requires:	subversion
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eSvn is a cross-platform (Qt-based) GUI frontend for the Subversion
revision system.

%description -l pl.UTF-8
eSvn jest wieloplatformowym (opartym na Qt) graficznym interfejsem
użytkownika dla Subversion.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__sed} -i 's,-lqt ,-lqt-mt ,g' *.vpj
%{__sed} -i 's,Categories.*,Categories=Qt;Development;RevisionControl;,' eSvn.desktop

export QTDIR=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_docdir}/esvn}
install esvn $RPM_BUILD_ROOT%{_bindir}/esvn
install esvn-diff-wrapper $RPM_BUILD_ROOT%{_bindir}/esvn-diff-wrapper
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
