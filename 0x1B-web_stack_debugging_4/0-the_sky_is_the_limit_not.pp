# DeBug #4
exec { 'this will output stuff':
  path      => '/bin',
  command   => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx',
  logoutput => true,
}

exec { 'nging restart':
    path    => '/etc/init.d',
    command => 'nginx restart'
}
