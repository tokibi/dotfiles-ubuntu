
%w(
  redshift-gtk
  vlc
  rbenv
  ruby-build
  ruby-dev
  binutils
  build-essential
  sysstat
  unrar
  vim
).each do |name|
  package name
end

# Redshift settings
template "/home/#{node[:user]}/.config/redshift.conf" do
  source "files/redshift/redshift.conf"
end

template "/home/#{node[:user]}/.config/autostart/redshift-gtk.desktop" do
  owner node[:user].to_s
  group node[:user].to_s
  source "files/redshift/redshift-gtk.desktop"
end
