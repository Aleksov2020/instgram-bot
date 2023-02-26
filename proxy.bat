cd C:\Program Files\Microvirt\MEmu
memuc -i 1 adb shell input tap 357 1151
TIMEOUT /T 1 /NOBREAK
memuc -i 1 adb shell input tap 225 777
TIMEOUT /T 4 /NOBREAK
memuc -i 1 adb shell input tap 561 227
TIMEOUT /T 3 /NOBREAK
memuc sendkey -i 1 home