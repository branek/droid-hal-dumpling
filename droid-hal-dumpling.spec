# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define droid_target_aarch64 1

%define device dumpling
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty 5T

%define installable_zip 1

%define straggler_files \
/bugreports\
/d\
/nonplat_file_contexts\
/nonplat_hwservice_contexts\
/nonplat_property_contexts\
/nonplat_seapp_contexts\
/nonplat_service_contexts\
/plat_file_contexts\
/plat_hwservice_contexts\
/plat_property_contexts\
/plat_seapp_contexts\
/plat_service_contexts\
/sdcard\
/vendor\
/vndservice_contexts\
%{nil}

%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

