# Generated from activemodel-3.2.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	activemodel

Summary:	A toolkit for building modeling frameworks (part of Rails)
Name:		rubygem-%{rbname}

Version:	3.2.3
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://www.rubyonrails.org
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	rubygem(activesupport) = %{version}
BuildRequires:	rubygem(builder)
BuildRequires:	rubygem(i18n) => 0.4.2
BuildRequires:	rubygem(mocha)
BuildArch:	noarch

%description
A toolkit for building modeling frameworks like Active Record and Active
Resource. Rich support for attributes, callbacks, validations, observers,
serialization, internationalization, and testing.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/locale
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/locale/*.yml
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/mass_assignment_security
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/mass_assignment_security/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/serializers
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/serializers/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/validations
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/active_model/validations/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Apr 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.2.3-1
+ Revision: 791661
- version update 3.2.3

* Fri Feb 17 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.1-3
+ Revision: 775606
- regenereate spec with gem2rpm5

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 3.2.1-1
+ Revision: 769693
- New release

* Tue Sep 27 2011 Alexander Barakin <abarakin@mandriva.org> 3.1.0-1
+ Revision: 701475
- missing rdoc fix
- imported package rubygem-activemodel

