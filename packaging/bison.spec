Name:           bison
Version:        2.4.1
Release:        1
License:        GPLv2+
Summary:        A GNU general-purpose parser generator
Url:            http://www.gnu.org/software/bison/
Group:          Development/Tools
Source:         ftp://ftp.gnu.org/pub/gnu/bison/bison-%{version}.tar.bz2
BuildRequires:  m4 >= 1.4
Requires:       m4 >= 1.4

%description
Bison is a general purpose parser generator that converts a grammar
description for an LALR(1) context-free grammar into a C program to
parse that grammar. Bison can be used to develop a wide range of
language parsers, from ones used in simple desk calculators to complex
programming languages. Bison is upwardly compatible with Yacc, so any
correctly written Yacc grammar should work with Bison without any
changes. If you know Yacc, you shouldn't have any trouble using
Bison. You do need to be very proficient in C programming to be able
to use Bison. Bison is only needed on systems that are used for
development.

If your system will be used for C development, you should install
Bison.

%package devel
Summary:        -ly library for development using Bison-generated parsers
Group:          Development/Libraries

%description devel
The bison-devel package contains the -ly library sometimes used by
programs using Bison-generated parsers.  If you are developing programs
using Bison, you might want to link with this library.  This library
is not required by all Bison-generated parsers, but may be employed by
simple programs to supply minimal support for the generated parsers.

# -ly is kept static.  It only contains two symbols: main and yyerror,
# and both of these are extremely simple (couple lines of C total).
# It doesn't really pay off to introduce a shared library for that.
#
# Therefore -devel subpackage could have been created as -static, but
# the split was done in Jan 2005, which predates current guidelines.
# Besides there is logic to that: the library is devel in the sense
# that the generated parser could be distributed together with other
# sources, and only bison-devel would be necessary to wrap the build.

%prep
%setup -q

%build
%configure --disable-nls
make

%install
%makeinstall

# Remove unpackaged files.
rm -f %{buildroot}/%{_bindir}/yacc
rm -f %{buildroot}/%{_mandir}/man1/yacc*
rm -rf %{buildroot}/%{_infodir}

# The distribution contains also source files.  These are used by m4
# when the target parser file is generated.
%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README THANKS TODO
%{_mandir}/*/bison*
%{_datadir}/bison
%{_bindir}/bison
%{_datadir}/aclocal/bison*.m4

%files devel
%defattr(-,root,root)
%{_libdir}/liby.a
