 # Archdown

 TODO:
 - all config files in one json
 - select destination folder
 - write better


 This program is intended to download/mirror an external repo of archlinux
 it let you chose the url, and $arch/os/$repo format too, dbs and arch

 # Usage:
 Just modify the *.conf files acording to where you are going to connect
 
 warning:
 the format of preset.conf is where the $arch/os/$repo thing is chosed
 you must put the part separated, like (arch / db) for $arch/$db
 another example could be (arch /os/ db) for $arch/os/$db

 if you got an url like  (http://mirror.yandex.ru/archlinux/),
 got your preset like (arch /os/ db),
 got the arch like (x86_64)
 and got the dbs like (core extra multilib community)
 the final url that this program will solve for each dbs is:

 http://mirror.yandex.ru/archlinux/x86_64/os/core
 http://mirror.yandex.ru/archlinux/x86_64/os/extra
 http://mirror.yandex.ru/archlinux/x86_64/os/multilib
 http://mirror.yandex.ru/archlinux/x86_64/os/community
 
 to start downloading just type
 $ python __init__.py
 on program directory and it will do the work 
