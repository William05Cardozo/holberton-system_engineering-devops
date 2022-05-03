# this command change a file

exec { 'Changefile':
command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
path    => '/bin',
}
