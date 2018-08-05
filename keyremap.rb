package 'python3-pip' do
  action :install
end

# xsession
template "/home/#{node[:user]}/.xsessionrc" do
  owner node[:user].to_s
  group node[:user].to_s
  source "files/xkeysnail/xsessionrc"
end

# apparmor
template "/etc/apparmor.d/usr.local.bin.xkeysnail" do
  source "files/xkeysnail/apparmor"
end

service "apparmor" do
  action :reload
end

# xkeysnail
execute "install xkeyxnail" do
  not_if "which xkeysnail"
  command "pip3 install xkeysnail"
end

directory "/etc/xkeysnail"
template "/etc/xkeysnail/config.py" do
  source "files/xkeysnail/config.py"
end

template "/etc/systemd/system/xkeysnail.service" do
  source "files/xkeysnail/xkeysnail.service"
end

service "xkeysnail" do
  action [:enable, :restart]
end
