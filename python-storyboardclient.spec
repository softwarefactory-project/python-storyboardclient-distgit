Name:           python-storyboardclient
Version:        0.2.0
Release:        1%{dist}
Summary:        Python Client library for StoryBoard

License:        ASL 2.0
URL:            https://github.com/openstack-infra/%{name}
Source0:        http://tarballs.openstack.org/python-storyboardclient/python-storyboardclient-%{version}.tar.gz

Source1:        fix-distibution-name.patch

Patch0:         0001-Set-a-by-default-retry.patch

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
%autosetup -n %{name}-%{version} -p1
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
* Thu Nov 22 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 0.2.0-1
- Bump version

* Wed May 10 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-5
- Patch to add reconnection capability

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
