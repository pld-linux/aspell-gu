Summary:	Gujarati dictionary for aspell
Summary(pl):	S³ownik gud¿arati dla aspella
Name:		aspell-gu
Version:	0.02
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/gu/aspell6-gu-%{version}-%{subv}.tar.bz2
# Source0-md5:	42d3eb8a32a020aea56cd3e6ea3de0e1
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gujarati dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik gud¿arati (lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-gu-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
