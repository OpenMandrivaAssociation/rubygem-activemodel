%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname activemodel
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

%define testdir %{_tmppath}/%{gemname}-%{version}

Summary:	A toolkit for building modeling frameworks
Name:		rubygem-%{gemname}
Version:	3.1.0
Release:	%mkrel 1
Group:		Development/Ruby
License:	MIT
URL:		http://www.rubyonrails.org
Source0:	http://rubygems.org/gems/%{gemname}-%{version}.gem
#Source1:	% {gemname}-tests.tgz
Requires:	ruby(abi) = 1.8
Requires:	rubygems
Requires:	rubygem(activesupport) = %{version}
Requires:	rubygem(builder) => 2.1.2
Requires:	rubygem(i18n) => 0.4.2
BuildRequires:	rubygems
BuildRequires:	rubygem(activesupport) = %{version}
BuildRequires:	rubygem(builder)
BuildRequires:	rubygem(i18n) => 0.4.2
BuildRequires:	rubygem(mocha)
BuildArch:	noarch
Provides:	rubygem(%{gemname}) = %{version}

%description
Rich support for attributes, callbacks, validations, observers,
serialization, internationalization, and testing. It provides a known
set of interfaces for usage in model classes. It also helps building
custom ORMs for use outside of the Rails framework.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep

%build

%install
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%check
#rm -rf %{testdir}
#mkdir % {testdir}
#tar xzvf % {SOURCE1} -C % {testdir}
#pushd % {testdir}

# load_path is not available, remove its require#.
#sed -i '1,2d' test/cases/helper.rb

#RUBYOPT="rubygems I%{buildroot}%{geminstdir}/lib Itest" testrb test/*/*_test.rb test/*/*/*_test.rb

#popd
#rm -rf %{testdir}

%files
%defattr(-, root, root, -)
%dir %{geminstdir}
%{geminstdir}/lib
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/MIT-LICENSE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(-, root, root, -)
%doc %{geminstdir}/CHANGELOG
%doc %{gemdir}/doc/%{gemname}-%{version}
