%define upstream_name    Catalyst-Controller-HTML-FormFu
%define upstream_version 0.09003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Hidden text field which contains a unique token
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Action::RenderView)
BuildRequires:	perl(Catalyst::Component::InstancePerContext)
BuildRequires:	perl(Catalyst::Plugin::ConfigLoader)
BuildRequires:	perl(Catalyst::Plugin::Session)
BuildRequires:	perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires:	perl(Catalyst::Plugin::Session::Store::File)
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Catalyst::View::TT)
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(Config::Any)
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Crypt::DES)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTML::FormFu)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Meta::Attribute::Custom::Trait::Chained)
BuildRequires:	perl(Regexp::Assemble)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::WWW::Mechanize)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

Requires:	perl(Catalyst::Component::InstancePerContext)
Requires:	perl(Regexp::Assemble)

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.30-1mdv2011.0
+ Revision: 674646
- update to new version 0.09003

* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.20-1
+ Revision: 673784
- update to new version 0.09002
- update to new version 0.09000

* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.80.20-3
+ Revision: 658232
- bump req

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.80.20-2
+ Revision: 656886
- rebuild for updated spec-helper

* Tue Nov 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.20-1mdv2011.0
+ Revision: 595442
- update to new version 0.08002

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.10-1mdv2010.1
+ Revision: 477616
- update to 0.06001

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-2mdv2010.1
+ Revision: 471679
- adding missing requires

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 471514
- adding missing buildrequires:
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-Catalyst-Controller-HTML-FormFu


* Sun Nov 29 2009 cpan2dist 0.06000-1mdv
- initial mdv release, generated with cpan2dist
