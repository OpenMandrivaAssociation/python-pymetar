%define oname	pymetar
  
Name:		python-%{oname}
Version:	0.14
Release:	%mkrel 1
Summary:	Weather report Python module
Group:		Development/Python
License:	GPLv2+
URL:		http://www.schwarzvogel.de/software-pymetar.shtml
Source0:	http://www.schwarzvogel.de/pkgs/%{oname}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root 
BuildArch:	noarch 
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python 
  
%description 
This library downloads the weather report for a given station ID,
decodes it and provides easy access to all the data found in the
report.
  
%prep
%setup -q -n %{oname}-%{version}
  
%build 
  
%install 
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2
rm -rf %{buildroot}%{_docdir}

%clean 
rm -rf %{buildroot}
  
%files  
%defattr(-,root,root,-) 
%doc README THANKS librarydoc.txt
%{_bindir}/weather.py
%{py_puresitedir}/%{oname}.py*
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info

