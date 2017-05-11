from nxtools import NxConanFile
from conans import CMake, tools


class DocoptCppConan(NxConanFile):
    name = "docopt.cpp"
    version = "0.6.2"
    license = "MIT"
    url = "https://github.com/hoxnox/conan-docopt.cpp"
    license = "https://github.com/docopt/docopt.cpp/blob/master/LICENSE-MIT"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared":[True, False]}
    default_options = "shared=False"
    build_policy = "missing"
    description = "docopt creates beautiful command-line interfaces."

    def do_source(self):
        self.retrieve("c05542245232420d735c7699098b1ea130e3a92bade473b64baf876cdf098a17",
                [
                    "vendor://docopt/docopt.cpp/docopt.cpp-{v}.tar.gz".format(v=self.version),
                    "https://github.com/docopt/docopt.cpp/archive/v{v}.tar.gz".format(v=self.version)
                ],
                "docopt.cpp-{v}.tar.gz".format(v=self.version))

    def do_build(self):
        cmake = CMake(self)
        cmake.build_dir = "{staging_dir}/src".format(staging_dir=self.staging_dir)
        tools.untargz("docopt.cpp-{v}.tar.gz".format(v=self.version), cmake.build_dir)
        cmake_defs = {"CMAKE_INSTALL_PREFIX": self.package_folder, "CMAKE_INSTALL_LIBDIR": "lib"}
        cmake_defs.update(self.cmake_crt_linking_flags())
        cmake.configure(defs = cmake_defs, source_dir="docopt.cpp-{v}".format(v=self.version))
        cmake.build(target="install")

    def do_package_info(self):
        if self.settings.compiler == "Visual Studio":
            self.cpp_info.libs = ["docopt" if self.options.shared else "docopt_s"]
        else:
            self.cpp_info.libs = ["docopt" if self.options.shared else "docopt.a"]
