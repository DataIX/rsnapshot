Summary: rsync backup snapshot program
Name: rsnapshot
Version: 1.0.3
Release: 1
BuildArch: noarch
Copyright: GPL
Group: Applications/System
Source: http://rsnapshot.scubaninja.com/downloads/rsnapshot-1.0.3.tar.gz
Patch: config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: perl, fileutils

%description
This is a remote backup program that uses rsync to take backup snapshots of filesystems. 
It uses hard links to save space on disk.

%prep

%setup 

%patch

# it's just perl, so no need to compile
%build

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
install -m 755 rsnapshot $RPM_BUILD_ROOT/usr/bin/rsnapshot

install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 rsnapshot.1 $RPM_BUILD_ROOT/usr/share/man/man1/

install -d $RPM_BUILD_ROOT/%{_sysconfdir}
install -m 644 rsnapshot.conf $RPM_BUILD_ROOT/etc/rsnapshot.conf.default
install -m 600 rsnapshot.conf $RPM_BUILD_ROOT/etc/rsnapshot.conf

%post

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}/

%files
%defattr(-,root,root)
%doc GPL README INSTALL TODO
%config %{_sysconfdir}/rsnapshot.conf.default
%config(noreplace) %{_sysconfdir}/rsnapshot.conf
%{_bindir}/rsnapshot
%{_mandir}/man1/rsnapshot.1*

%changelog
* Tue Oct 28 2003 Carl Wilhelm Soderstrom <chrome@real-time.com>
- created spec file