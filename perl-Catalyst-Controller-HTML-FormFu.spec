%define upstream_name    Catalyst-Controller-HTML-FormFu
%define upstream_version 0.09000

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Hidden text field which contains a unique token
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Action::RenderView)
BuildRequires: perl(Catalyst::Component::InstancePerContext)
BuildRequires: perl(Catalyst::Plugin::ConfigLoader)
BuildRequires: perl(Catalyst::Plugin::Session)
BuildRequires: perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires: perl(Catalyst::Plugin::Session::Store::File)
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Catalyst::View::TT)
BuildRequires: perl(Class::C3)
BuildRequires: perl(Config::Any)
BuildRequires: perl(Config::General)
BuildRequires: perl(Crypt::DES)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTML::FormFu)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Moose)
BuildRequires: perl(Regexp::Assemble)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Task::Weaken)
BuildRequires: perl(Template)
BuildRequires: perl(Test::WWW::Mechanize)
BuildRequires: perl(Test::WWW::Mechanize::Catalyst)
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Catalyst::Component::InstancePerContext)
Requires: perl(Regexp::Assemble)

%description
As of version 0.02000, the HTML::FormFu manpage doesn't use the TT template
files by default - it uses in internal rendering engine.

If you don't want to customise the generated markup, you don't need to use
the Catalyst::Helper::HTML::FormFu manpage at all.

If you want to customise the generated markup, you'll need a local copy of
the template files. To create the files in the default 'root/formfu'
directory, run:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
