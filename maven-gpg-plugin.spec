%{?_javapackages_macros:%_javapackages_macros}
Name:           maven-gpg-plugin
Version:        1.4
Release:        10.0%{?dist}
Summary:        Maven GPG Plugin


License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-gpg-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         0001-Add-support-for-maven-3.patch

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin

# Uses system gpg binary for actual signing
Requires:      gnupg

Obsoletes: maven2-plugin-gpg <= 0:2.0.8
Provides: maven2-plugin-gpg = 1:%{version}-%{release}

%description
This plugin signs all of the project's attached artifacts with
GnuPG. It adds goals gpg:sign and gpg:sign-and-deploy-file.


%package javadoc

Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

# migrate to maven 3.x 
%patch0 -p1
sed -i 's/${mavenVersion}/3.0.4/' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Tomas Radej <tradej@redhat.com> - 1.4-9
- Added R on gnupg (used for actual singing)

* Tue Jun 25 2013 Tomas Radej <tradej@redhat.com> - 1.4-8
- Removed BR on ant-nodeps (no longer available)

* Tue Feb 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-7
- Use default packaging layout

* Tue Feb 12 2013 Michal Srb <msrb@redhat.com> - 1.4-6
- Build with xmvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Install LICENSE and NOTICE files (#879367)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 6 2011 Alexander Kurtakov <akurtako@redhat.com> 1.4-1
- Update to latest upstream version.

* Mon Jun 13 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.3-1
- Update to latest upstream version

* Fri Mar 25 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-1
- Update to new upstream release.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun  2 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-2
- Fix depmap call
- Add gnupg2 to Requires

* Tue Jun  1 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-1
- Initial package
