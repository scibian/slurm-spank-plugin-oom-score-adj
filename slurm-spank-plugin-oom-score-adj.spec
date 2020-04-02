%define __plugin oom-score-adj
%define __lib_dir %{_prefix}/lib

Name: slurm-spank-plugin-%{__plugin}
Version: 3.9.1
Release: 1
Summary: Slurm spank plugin for OOM killer score advisory
Source: %{name}-%{version}.tar.gz

Group: System Environment/Base
License: unknown
Vendor: none
URL: https://github.com/scibian/slurm-spank-plugin-oom-score-adj
Packager: Scibian Project <packaging@scibian.org>

BuildRequires: slurm-devel
Requires: slurm

%description
Slurm spank plugin for OOM killer score advisory
 This plugin adjusts the Out-of-Memory (OOM) score of the tasks
spawned by Slurm.

%prep
%setup -q -n %{name}-%{version}
#echo "include /etc/slurm-llnl/plugstack.conf.d/*.conf" > %{_builddir}/%{name}-%{version}/plugstack.conf

%build
gcc -g -std=gnu99 -Wall -o slurm-spank-%{__plugin}.o -fPIC -c slurm-spank-%{__plugin}.c
gcc -shared -o %{__plugin}.so slurm-spank-%{__plugin}.o

%install
install -d %{buildroot}%{__lib_dir}/slurm
#install -d %{buildroot}%{_sysconfdir}/slurm/plugstack.conf.d
install -m 755 %{__plugin}.so %{buildroot}%{__lib_dir}/slurm/
#install -m 644 plugstack.conf \
#    %{buildroot}%{_sysconfdir}/slurm/plugstack.conf.d/slurm-spank-%{__plugin}.conf

%clean
rm -rf %{buildroot}

%files
#%doc README LICENSE
%defattr(-,root,root,-)
%{__lib_dir}/slurm/%{__plugin}.so
#%config %{_sysconfdir}/slurm/plugstack.conf.d/slurm-spank-%{__plugin}.conf

%changelog
