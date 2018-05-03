#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mraa
Version  : 1.5.1
Release  : 6
URL      : https://github.com/intel-iot-devkit/mraa/archive/v1.5.1.tar.gz
Source0  : https://github.com/intel-iot-devkit/mraa/archive/v1.5.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 LGPL-2.1 MIT
Requires: mraa-bin
Requires: mraa-lib
Requires: mraa-python
Requires: mraa-data
BuildRequires : cmake
BuildRequires : json-c-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : swig-bin

%description
These headers was automatically generated from a Linux kernel header
of the same name, to make information necessary for userspace to
call into the kernel available to libc.  It contains only constants,
structures, and macros generated from the original header, and thus,
contains no copyrightable information.

%package bin
Summary: bin components for the mraa package.
Group: Binaries
Requires: mraa-data

%description bin
bin components for the mraa package.


%package data
Summary: data components for the mraa package.
Group: Data

%description data
data components for the mraa package.


%package dev
Summary: dev components for the mraa package.
Group: Development
Requires: mraa-lib
Requires: mraa-bin
Requires: mraa-data
Provides: mraa-devel

%description dev
dev components for the mraa package.


%package lib
Summary: lib components for the mraa package.
Group: Libraries
Requires: mraa-data

%description lib
lib components for the mraa package.


%package python
Summary: python components for the mraa package.
Group: Default

%description python
python components for the mraa package.


%prep
%setup -q -n mraa-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525380520
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DBUILDSWIGNODE=OFF -DBUILDTESTS=OFF -DENABLEEXAMPES=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ||: ; popd

%install
export SOURCE_DATE_EPOCH=1525380520
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mraa-gpio
/usr/bin/mraa-i2c

%files data
%defattr(-,root,root,-)
/usr/share/mraa/examples/CMakeLists.txt
/usr/share/mraa/examples/analogin_a0.c
/usr/share/mraa/examples/blink-io.c
/usr/share/mraa/examples/blink_onboard.c
/usr/share/mraa/examples/c++/AioA0.cpp
/usr/share/mraa/examples/c++/Blink-IO.cpp
/usr/share/mraa/examples/c++/CMakeLists.txt
/usr/share/mraa/examples/c++/I2c-compass.cpp
/usr/share/mraa/examples/c++/Iio-dummy.cpp
/usr/share/mraa/examples/c++/Isr-pin6.cpp
/usr/share/mraa/examples/c++/Pwm3-cycle.cpp
/usr/share/mraa/examples/c++/Spi-pot.cpp
/usr/share/mraa/examples/c++/Uart-example.cpp
/usr/share/mraa/examples/c++/UartOW.cpp
/usr/share/mraa/examples/c++/initio.cpp
/usr/share/mraa/examples/cycle-pwm3.c
/usr/share/mraa/examples/firmata_curie_imu.c
/usr/share/mraa/examples/gpio_read6.c
/usr/share/mraa/examples/helloedison.c
/usr/share/mraa/examples/hellomraa.c
/usr/share/mraa/examples/i2c_HMC5883L.c
/usr/share/mraa/examples/i2c_firmata.c
/usr/share/mraa/examples/iio_driver.c
/usr/share/mraa/examples/initio.c
/usr/share/mraa/examples/isr_pin6.c
/usr/share/mraa/examples/java/AioA0.java
/usr/share/mraa/examples/java/BlinkIO.java
/usr/share/mraa/examples/java/BlinkOnboard.java
/usr/share/mraa/examples/java/Bmp85.java
/usr/share/mraa/examples/java/CyclePwm3.java
/usr/share/mraa/examples/java/Example.java
/usr/share/mraa/examples/java/FTDITest.java
/usr/share/mraa/examples/java/GpioMmapped.java
/usr/share/mraa/examples/java/GpioRead6.java
/usr/share/mraa/examples/java/HelloEdison.java
/usr/share/mraa/examples/java/I2cCompass.java
/usr/share/mraa/examples/java/Isr.java
/usr/share/mraa/examples/java/SpiMAX7219.java
/usr/share/mraa/examples/java/SpiMCP4261.java
/usr/share/mraa/examples/java/UartExample.java
/usr/share/mraa/examples/javascript/AioA0.js
/usr/share/mraa/examples/javascript/Blink-IO.js
/usr/share/mraa/examples/javascript/GPIO_DigitalRead.js
/usr/share/mraa/examples/javascript/GPIO_DigitalWrite.js
/usr/share/mraa/examples/javascript/bmp85.js
/usr/share/mraa/examples/javascript/firmata.js
/usr/share/mraa/examples/javascript/gpio-tool.js
/usr/share/mraa/examples/javascript/initio.js
/usr/share/mraa/examples/javascript/isr.js
/usr/share/mraa/examples/javascript/rgblcd.js
/usr/share/mraa/examples/javascript/spi.js
/usr/share/mraa/examples/javascript/uart.js
/usr/share/mraa/examples/mmap-io2.c
/usr/share/mraa/examples/mraa-gpio.c
/usr/share/mraa/examples/mraa-i2c.c
/usr/share/mraa/examples/platform/turbotjson.json
/usr/share/mraa/examples/python/__pycache__/aio.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/blink-io8.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/bmp85.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/cycle-pwm3.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/firmata.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/hello_gpio.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/hello_isr.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/initio.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/rgblcd.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/spi.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/uart_receiver.cpython-36.pyc
/usr/share/mraa/examples/python/__pycache__/uart_sender.cpython-36.pyc
/usr/share/mraa/examples/python/aio.py
/usr/share/mraa/examples/python/blink-io8.py
/usr/share/mraa/examples/python/bmp85.py
/usr/share/mraa/examples/python/cycle-pwm3.py
/usr/share/mraa/examples/python/firmata.py
/usr/share/mraa/examples/python/hello_gpio.py
/usr/share/mraa/examples/python/hello_isr.py
/usr/share/mraa/examples/python/initio.py
/usr/share/mraa/examples/python/rgblcd.py
/usr/share/mraa/examples/python/spi.py
/usr/share/mraa/examples/python/uart_receiver.py
/usr/share/mraa/examples/python/uart_sender.py
/usr/share/mraa/examples/samples.mapping.txt
/usr/share/mraa/examples/spi_max7219.c
/usr/share/mraa/examples/spi_mcp4261.c
/usr/share/mraa/examples/uart.c
/usr/share/mraa/examples/uart_ow.c

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/*.hpp
/usr/include/mraa/aio.h
/usr/include/mraa/aio.hpp
/usr/include/mraa/common.h
/usr/include/mraa/common.hpp
/usr/include/mraa/firmata.h
/usr/include/mraa/gpio.h
/usr/include/mraa/gpio.hpp
/usr/include/mraa/i2c.h
/usr/include/mraa/i2c.hpp
/usr/include/mraa/iio.h
/usr/include/mraa/iio.hpp
/usr/include/mraa/iio_kernel_headers.h
/usr/include/mraa/pwm.h
/usr/include/mraa/pwm.hpp
/usr/include/mraa/spi.h
/usr/include/mraa/spi.hpp
/usr/include/mraa/types.h
/usr/include/mraa/types.hpp
/usr/include/mraa/uart.h
/usr/include/mraa/uart.hpp
/usr/include/mraa/uart_ow.h
/usr/include/mraa/uart_ow.hpp
/usr/lib64/libmraa.so
/usr/lib64/pkgconfig/mraa.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmraa.so.1
/usr/lib64/libmraa.so.1.5.1

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*
