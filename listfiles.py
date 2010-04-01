import subprocess
class FileLister():
	def __init__(self, filepath):
		self.path = filepath
		self.ls_output = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE)
		self.file_list = self.ls_output.communicate()[0]
		self.update_list()
	def update_list(self):
		self.output_list = []		
		while self.file_list.find("\n") != -1:
			self.output_list.append(self.file_list[:self.file_list.find("\n")])
			self.file_list = self.file_list[self.file_list.find("\n") + 1:]
		
	def get_icon_name(self, filename):
		self.file_output = subprocess.Popen(['file','-i', '-b', filename], stdout=subprocess.PIPE)
		icon_name = self.file_output.communicate()[0]
		icon_name = icon_name[:icon_name.find(';')]
		icon_name = icon_name.replace("/", "-")		
		return icon_name

	def get_list(self):
		return self.output_list
