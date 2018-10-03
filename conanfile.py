from conans import ConanFile, tools


class Issue3529Conan(ConanFile):
    name = "issue3529"
    version = "0.0.1"
    description = "see: https://github.com/conan-io/conan/issues/3529"
    settings = "os", "compiler", "build_type", "arch"

    no_copy_source = False

    def source(self):
        tools.get("https://github.com/Adnn/issue_conan-3529/releases/download/0.0.1/qtxml.tar.bz2")
