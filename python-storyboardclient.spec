%global         commit0 940dd5c41ee8729d5697f232ba7365d67df0ac70
%global         shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global         checkout 20170428git%{shortcommit0}

Name:           python-storyboardclient
Version:        0.1
Release:        4.%{checkout}%{dist}
Summary:        Python Client library for StoryBoard

License:        ASL 2.0
URL:            https://github.com/openstack-infra/${name}
Source0:        https://github.com/openstack-infra/%{name}/archive/%{commit0}.tar.gz

Source1:        fix-distibution-name.patch 

BuildArch:      noarch

Requires:       python-babel
Requires:       python2-oslo-config
Requires:       python2-oslo-i18n
Requires:       python2-oslo-log
Requires:       python2-oslo-serialization
Requires:       python2-oslo-utils
Requires:       python-requests
Requires:       python-six
Requires:       python2-stevedore

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python-pbr
Buildrequires:  python-nose
Buildrequires:  python2-oslotest
Buildrequires:  python2-stevedore
BuildRequires:  python-babel
BuildRequires:  python2-oslo-config
BuildRequires:  python2-oslo-i18n
BuildRequires:  python2-oslo-log
BuildRequires:  python2-oslo-serialization
BuildRequires:  python2-oslo-utils
BuildRequires:  python-requests
BuildRequires:  python-six

%description
Python Client library for StoryBoard

%package -n python2-storyboardclient
Summary:        Python Client library for StoryBoard
Requires:       python-babel
Requires:       python2-oslo-config
Requires:       python2-oslo-i18n
Requires:       python2-oslo-log
Requires:       python2-oslo-serialization
Requires:       python2-oslo-utils
Requires:       python-requests
Requires:       python-six
Requires:       python2-stevedore

Buildrequires:  python2-devel
Buildrequires:  python-setuptools
Buildrequires:  python-pbr
Buildrequires:  python-nose
Buildrequires:  python2-oslotest
Buildrequires:  python2-stevedore
BuildRequires:  python-babel
BuildRequires:  python2-oslo-config
BuildRequires:  python2-oslo-i18n
BuildRequires:  python2-oslo-log
BuildRequires:  python2-oslo-serialization
BuildRequires:  python2-oslo-utils
BuildRequires:  python-requests
BuildRequires:  python-six

%description -n python2-storyboardclient
Python Client library for StoryBoard

%prep
%autosetup -n %{name}-%{commit0}
patch -p0 < %{SOURCE1}

%build
export PBR_VERSION=0.1
%{__python2} setup.py build

%install
export PBR_VERSION=0.1
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
export PBR_VERSION=0.1
nosetests -v

%files -n python2-storyboardclient
%{python2_sitelib}/*

%changelog
* Fri Apr 28 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-4
- Bump to last available version this day

* Tue Mar 07 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 0.1-320170221gitcfdfaf8
- Renamed spec file and fix release number

* Wed Mar 01 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-202212017gitcfdfaf8
- Fix python package distribution name

* Tue Feb 22 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-02212017gitcfdfaf8
- Dependencies fix

* Tue Feb 21 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-02212017gitcfdfaf8
- Initial packaging
