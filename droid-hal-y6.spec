%define device y6
%define vendor huawei
%define vendor_pretty Huawei
%define device_pretty Y6
%define installable_zip 1

%define straggler_files \
/init.class_main.sh\
/init.qcom.bms.sh\
/init.qcom.early_boot.sh\
/init.qcom.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user inet || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
