Summary:	Log file navigator
Name:		lnav
Version:	0.12.4
Release:	1
License:	BSD
Group:		Applications
Source0:	https://github.com/tstack/lnav/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	540fc19e14d28c6ec2494ec5684721c7
URL:		https://lnav.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	curl-devel >= 7.23.0
BuildRequires:	jemalloc-devel
BuildRequires:	libarchive-devel
# c++17
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	ncurses-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	re2c
BuildRequires:	readline-devel
BuildRequires:	sqlite3-devel >= 3.9.0
BuildRequires:	zlib-devel
Requires:	curl-libs >= 7.23.0
Requires:	sqlite3-libs >= 3.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The log file navigator, lnav, is an enhanced log file viewer that
takes advantage of any semantic information that can be gleaned from
the files being viewed, such as timestamps and log levels. Using this
extra semantic information, lnav can do things like interleaving
messages from different files, generate histograms of messages over
time, and providing hotkeys for navigating through the file. It is
hoped that these features will allow the user to quickly and
efficiently zero in on problems.


%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_path_CARGO_CMD= \
	--disable-silent-rules \
	--disable-static \
	--with-jemalloc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS INSTALL NEWS.md README README.md
%attr(755,root,root) %{_bindir}/lnav
%{_mandir}/man1/lnav.1*
