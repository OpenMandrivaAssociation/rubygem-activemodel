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
