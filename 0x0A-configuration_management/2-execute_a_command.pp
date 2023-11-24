# Using Puppet, create a manifest that kills a process named killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  refreshonly => true,
  provider => 'shell'
}
