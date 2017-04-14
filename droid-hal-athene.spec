%define device athene
%define vendor motorola
%define vendor_pretty MOTO
%define device_pretty MOTO G4 Plus
%define installable_zip 1
%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.laser.sh\
/init.mmi.touch.sh\
/init.oem.hw.sh\
/init.qcom.bt.sh\
/init.qcom.ril.sh\
%{nil}
%include rpm/dhd/droid-hal-device.inc
