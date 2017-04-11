%{?_javapackages_macros:%_javapackages_macros}
Name:          jatl
Version:       0.2.2
Release:       11%{?dist}
Summary:       Java Anti-Template Language
License:       ASL 2.0
# https://github.com/agentgt
URL:           https://github.com/chris-martin/jatl
Source0:       https://github.com/chris-martin/jatl/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
Requires:      mvn(commons-lang:commons-lang)

BuildArch:     noarch

%description
Is an extremely lightweight efficient Java library to
generate XHTML or XML in a micro DSL builder/fluent style.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Unwanted
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-license-plugin
# Unwanted build source jar
%pom_remove_plugin :maven-source-plugin
# Unwanted build javadoc jar
%pom_remove_plugin :maven-javadoc-plugin
# Unavailable
%pom_remove_plugin com.googlecode.maven-gcu-plugin:maven-gcu-plugin

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYING

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 30 2016 gil cattaneo <puntogil@libero.it> 0.2.2-10
- add missing build requires

* Tue Jun 21 2016 gil cattaneo <puntogil@libero.it> 0.2.2-9
- add missing build requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 17 2015 gil cattaneo <puntogil@libero.it> 0.2.2-6
- fix Url tag and Source0 tag

* Fri Feb 06 2015 gil cattaneo <puntogil@libero.it> 0.2.2-5
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.2.2-3
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 04 2013 gil cattaneo <puntogil@libero.it> 0.2.2-1
- initial rpm
