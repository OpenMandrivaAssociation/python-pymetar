%define oname	pymetar
  
Name:		python-%{oname}
Version:	0.19
Release:	1
Summary:	Weather report Python module
Group:		Development/Python
License:	GPLv2+
URL:		http://www.schwarzvogel.de/software-pymetar.shtml
Source0:	http://www.schwarzvogel.de/pkgs/pymetar-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python 
BuildArch:	noarch 
  
%description 
This library downloads the weather report for a given station ID,
decodes it and provides easy access to all the data found in the
report.
  
%prep
%setup -q -n %{oname}-%{version}
  
%build 
  
%install 
python setup.py install --root=%{buildroot} --compile --optimize=2
rm -rf %{buildroot}%{_docdir}

%clean 
  
%files  
%defattr(-,root,root,-) 
%doc README THANKS librarydoc.txt
%{_bindir}/%{oname}
%{py_puresitedir}/*
%{_mandir}/man1/pymetar.1.xz


%changelog
* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2011.0
+ Revision: 603072
- update to new version 0.17

* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.16-1mdv2011.0
+ Revision: 598173
- update file list

  + Sandro Cazzaniga <kharec@mandriva.org>
    - Fix file list
    - update to 0.16

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2010.1
+ Revision: 489358
- new version

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2010.0
+ Revision: 442440
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.14-1mdv2009.1
+ Revision: 319648
- drop some now non-existent docs
- rebuild with python 2.6
- new release 0.14

* Thu Jul 31 2008 Adam Williamson <awilliamson@mandriva.org> 0.13-1mdv2009.0
+ Revision: 258360
- import python-pymetar



