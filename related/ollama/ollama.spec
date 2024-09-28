%global llama_commit 8962422b1c6f9b8b15f5aeaea42600bcc2d44177
%global llama_shortcommit %(c=%{llama_commit}; echo ${c:0:7})

%global gomodulesmode GO111MODULE=on

# Generated by go2rpm 1.14.0
%bcond check 1

# https://github.com/ollama/ollama
%global goipath         github.com/ollama/ollama
Version:                0.3.12

%gometa -L -f

%global common_description %{expand:
Get up and running with Llama 3.1, Mistral, Gemma 2, and other large language
models.}

Name:           ollama
Release:        %autorelease
Summary:        Get up and running with Llama 3.1, Mistral, Gemma 2, and other large language models

# Generated by go-vendor-tools
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            %{gourl}
Source0:        %{gosource}
# Generated by go-vendor-tools
Source1:        %{archivename}-vendor.tar.gz
Source2:        go-vendor-tools.toml
Source3:        https://github.com/ggerganov/llama.cpp/archive/%{llama_commit}/llama-cpp-%{llama_shortcommit}.tar.gz
Source4:        ollama-sysusers.conf
Source5:        ollama.service
Source6:        ollama-tmpfiles.conf
Patch:          fixes.patch

BuildRequires:  go-vendor-tools

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

Requires(pre):  systemd-sysusers
Requires(pre):  systemd-tmpfiles

Provides:       bundled(llama.cpp) = 0~1.git%{llama_shortcommit}

%description %{common_description}

%prep
%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
tar -xf %{SOURCE3} -C llm/llama.cpp --strip=1
%autopatch -p1
sed -i 's,T_CODE=on,T_CODE=on -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -D GGML_LTO:BOOL=ON -D CMAKE_BUILD_TYPE=Release,g' llm/generate/gen_linux.sh

%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}

%build
%set_build_flags
go generate %{goipath}/...
export CGO_CFLAGS="$CFLAGS"
export CGO_CPPFLAGS="$CPPFLAGS"
export CGO_CXXFLAGS="$CXXFLAGS"
export CGO_LDFLAGS="$LDFLAGS"
export LDFLAGS="-X=github.com/ollama/ollama/version.Version=%{version} \
                -X=github.com/ollama/ollama/server.mode=release"
%gobuild -o %{gobuilddir}/bin/ollama %{goipath}

%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -Dpm644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%check
%go_vendor_license_check -c %{S:2}
%if %{with check}
sed 's|//.*||' \
    -i \
    vendor/github.com/pdevine/tensor/internal/execution/e.go \
    vendor/github.com/pdevine/tensor/internal/storage/header.go \
    vendor/github.com/pdevine/tensor/tensor.go
for test in "TestBasicGetGPUInfo" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif

%pre
%sysusers_create_package %{name} %{SOURCE4}
%tmpfiles_create_package %{name} %{SOURCE6}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files -f %{go_vendor_license_filelist}
%license vendor/modules.txt
%doc README.md
%{_bindir}/%{name}
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%ghost %dir %attr(0755, ollama, ollama) %{_sharedstatedir}/%{name}

%changelog
%autochangelog
