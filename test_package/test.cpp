#include <docopt/docopt.h>
#include <string.h>
#include <stdio.h>
#include <map>

static const char USAGE[] =
R"(conan-docopt.cpp test package

Usage:
  test [-h]

Options:
  -h --help              Show help message
)";

int main(int argc, char* argv[])
{
	std::map<std::string, docopt::value> args
		= docopt::docopt(USAGE, { argv + 1, argv + argc }, true, "0.0.0");
	return 0;
}

