# Fix 500 error caused by mispelt file name in /var/www/html/wp-settings.php

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
