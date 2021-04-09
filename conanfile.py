from conans import ConanFile, CMake, tools


class DiscordrpcConan(ConanFile):
    name = "discord-rpc"
    version = "3.4.0"
    license = "MIT"
    author = "Edgar (Edgar@AnotherFoxGuy.com)"
    url = "https://github.com/AnotherFoxGuy/conan-discord-rpc"
    description = "This is a library for interfacing your game with a locally running Discord desktop client. It's known to work on Windows, macOS, and Linux."
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = [
        "source/CMakeLists.txt",
        "source/examples*",
        "source/include*",
        "source/src*"
    ]
    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_EXAMPLES'] = 'OFF'
        cmake.configure(source_folder="source")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
