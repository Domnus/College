# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/bentocarlos/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/203.7717.62/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/bentocarlos/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/203.7717.62/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Trabalhos.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Trabalhos.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Trabalhos.dir/flags.make

CMakeFiles/Trabalhos.dir/ex01.c.o: CMakeFiles/Trabalhos.dir/flags.make
CMakeFiles/Trabalhos.dir/ex01.c.o: ../ex01.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Trabalhos.dir/ex01.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Trabalhos.dir/ex01.c.o   -c "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/ex01.c"

CMakeFiles/Trabalhos.dir/ex01.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Trabalhos.dir/ex01.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/ex01.c" > CMakeFiles/Trabalhos.dir/ex01.c.i

CMakeFiles/Trabalhos.dir/ex01.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Trabalhos.dir/ex01.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/ex01.c" -o CMakeFiles/Trabalhos.dir/ex01.c.s

# Object files for target Trabalhos
Trabalhos_OBJECTS = \
"CMakeFiles/Trabalhos.dir/ex01.c.o"

# External object files for target Trabalhos
Trabalhos_EXTERNAL_OBJECTS =

Trabalhos: CMakeFiles/Trabalhos.dir/ex01.c.o
Trabalhos: CMakeFiles/Trabalhos.dir/build.make
Trabalhos: CMakeFiles/Trabalhos.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Trabalhos"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Trabalhos.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Trabalhos.dir/build: Trabalhos

.PHONY : CMakeFiles/Trabalhos.dir/build

CMakeFiles/Trabalhos.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Trabalhos.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Trabalhos.dir/clean

CMakeFiles/Trabalhos.dir/depend:
	cd "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos" "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos" "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug" "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug" "/home/bentocarlos/Documents/Github/College/3º Semestre/Estrutura de Dados e Recuperação de Informação/C/Trabalhos/cmake-build-debug/CMakeFiles/Trabalhos.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Trabalhos.dir/depend

