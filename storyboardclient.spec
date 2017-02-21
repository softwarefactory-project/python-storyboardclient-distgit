%global         commit0 cfdfaf866ca5da63ac734552772e1fe2f87c6543 
%global         shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global         checkout 02212017git%{shortcommit0}

Name:           python-storyboardclient
Version:        0.1
Release:        1%{dist}
Summary:        Python Client library for StoryBoard

License:        ASL 2.0
URL:            https://github.com/openstack-infra/${name}
Source0:        https://github.com/openstack-infra/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

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

%description -n python2-storyboardclient
Python Client library for StoryBoard

%prep
%autosetup -n %{name}-%{commit0}

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
* Tue Feb 21 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-02212017gitcfdfaf8
- Initial packaging
