# update_idc
config like a json object.

target:
update IDC(internet data center) program & script.


架构图
Local >>===Internet===<< IDC Server
Local负责将文件打包，并记录更新内容，发给Server[python]
IDC Server负责自动更新[Shell]

类图

class config
	function comment(local_url)

class svn
	function check_out(url, version)
	function login(url, username, password)

class zfile
	function zip(dest_file, src_files)
	funtion unzip(src_file)

class ssh
	function cert(url, username, password)
	function sftp(url, username, password, src_file)


流程图

pro_list = config.comment();

<< input SVN username, password

file_list = svn.check_out(pro_list, username, password);

print file_list << input continue

zfile.zip(zip, file_list);

<< input IDC username, password

sftp(url, username, password, "unzip file");

print success