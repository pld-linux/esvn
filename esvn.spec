Name:		esvn
Summary:	eSvn is a cross-platform (QT-based) GUI frontend for the Subversion revision system.
Summary(pl):	eSvn jest wieloplatformowym (opartym na QT) graficznym interfejsem u¿ytkownika dla Subversion.
Version:	0.6.0
Release:	1
Source0:	http://esvn.umputun.com/%{name}-%{version}-%{release}.tar.gz
# Source0-md5:	664de5f7fc4b0b1780f6abd801981a93
License:	GPL
Group:		X11/Development/Tools
URL:		http://esvn.umputun.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	qt-devel >= 3.0.0
Requires:	qt >= 3.0.0
Requires:	subversion


%description
eSvn is a cross-platform (QT-based) GUI frontend for the Subversion
revision system.

%description -l pl
eSvn jest wieloplatformowym (opartym na QT) graficznym interfejsem
u¿ytkownika dla Subversion.

%prep
rm -rf %{buildroot}

%setup -q -n %{name}

%build
export QTDIR=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/doc/esvn
install -m755 esvn %{buildroot}%{_bindir}/esvn
#install -m644 esvn.pdf %{buildroot}/usr/share/doc/esvn/esvn.pdf
install -m755 esvn-diff-wrapper %{buildroot}%{_bindir}/esvn-diff-wrapper
install esvn.png %{buildroot}%{_datadir}/pixmaps/esvn.png
install eSvn.desktop %{buildroot}%{_datadir}/applications/eSvn.desktop
cp -f -r html-docs %{buildroot}%{_datadir}/doc/esvn

%clean
rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/%{name}-%{version}-%{release}

%post

%preun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/esvn
%attr(755,root,root) %{_bindir}/esvn-diff-wrapper
%{_datadir}/pixmaps/esvn.png
%{_datadir}/applications/eSvn.desktop
#/usr/share/doc/esvn/esvn.pdf
%{_datadir}/doc/esvn/*/*

%doc AUTHORS  COPYING LICENSE  README  VERSION  ChangeLog
