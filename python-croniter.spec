Name:		python-croniter
Version:	6.0.0
Release:	1
Summary:	Iterate datetime objects with cron-like format
License:	MIT
Group:		Development/Python
URL:		https://github.com/kiorky/croniter
Source0:	https://files.pythonhosted.org/packages/source/c/croniter/croniter-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(python-dateutil)
BuildRequires:	python%{pyver}dist(pytz)
Requires:	python%{pyver}dist(python-dateutil)
Requires:	python%{pyver}dist(pytz)

%description
croniter provides iteration for datetime objects with a cron-like
format. Used by Hermes Agent for scheduled jobs.

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/croniter
%{py_sitedir}/croniter-*.*-info
