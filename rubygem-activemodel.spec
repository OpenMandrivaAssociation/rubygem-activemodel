# Generated from activemodel-3.2.1.gem by gem2rpm5 0.6.7 -*- rpm-spec -*-
%define	rbname	activemodel

Summary:	A toolkit for building modeling frameworks (part of Rails)
Name:		rubygem-%{rbname}

Version:	4.1.1
Release:	4
Group:		Development/Ruby
License:	MIT
URL:		https://www.rubyonrails.org
Source0:	http://rubygems.org/downloads/%{rbname}-%{version}.gem
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/active_model
%{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/locale
%{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/locale/*.yml
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/serializers
%{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/serializers/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/validations
%{gem_dir}/gems/%{rbname}-%{version}/lib/active_model/validations/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{rbname}-%{version}
