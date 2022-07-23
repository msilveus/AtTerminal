import ast
from datetime import datetime
from atelfrpparser import frp
from tabulate import tabulate

class log_files(object):
	"""docstring for log_files"""
	def __init__(self, log_name,rotation_size=5000000):
		super(log_files, self).__init__()
		self.path_serial_log = log_name +".log"
		self.path_info_log = log_name+"_info" +".log"
		self.renew_logs_flag = False
		self.log_rev = 0
		self.serial_log_file = open(self.path_serial_log, 'w+')
		self.serial_info_file = open(self.path_info_log, 'w+')
		#5 mg
		self.rotation_size = rotation_size * 1024 * 1024
	def renew_logs(self):
		self.log_rev += 1
		while self.path_serial_log[-1:].isnumeric():
			#num=num+self.path_serial_log[-1:]
			self.path_serial_log=self.path_serial_log[:-1]
			self.path_info_log=self.path_info_log[:-1]
		else:
			self.path_serial_log = self.path_serial_log+ str(self.log_rev)
			self.path_info_log = self.path_info_log + str(self.log_rev)
			self.serial_log_file = open(self.path_serial_log, 'w+')
			self.serial_info_file = open(self.path_info_log, 'w+')
			return
		self.path_serial_log=self.path_serial_log+ str(self.log_rev)
		self.path_info_log=self.path_info_log + str(self.log_rev)
		self.serial_info_file = open(self.path_info_log, 'w+')
		self.serial_log_file = open(self.path_serial_log, 'w+')
		self.renew_logs_flag = False

def recursive_dict_eval(myDict, itemlist):
	for key,value in myDict.items():
		try:
			if(isinstance(value, dict)):
				itemlist = itemlist + key + "\n"
				itemlist = recursive_dict_eval(dict(value), itemlist)
			else:
				itemlist = itemlist + key + ' : ' + str(value) + '\n'

		except (SyntaxError, ValueError, AssertionError):
			#SyntaxError, ValueError are for the literal_eval exceptions
			pass
	return itemlist


def decodeTLV(dictionary, tagname=None):
	table = list()
	header = list()
	tower_data = list()
	if tagname == None:
		header.append("Name")
		header.append("Value")
	else:
		header.append(tagname)
		header.append("Value")
	table.append(header)
	tags = ""
	for key, value in dictionary.items():
		tag = ""
		try:
			if(isinstance(value, dict)):
				tag = decodeTLV(value, key)
				tags += tag + "\r\n"
#			elif key == "tower_header":
#				for x in range(len(value)):
#					tower_data.append(value[x])
#			elif key == "tower_list":
#				tower_data.append(value)
#				tags += tabulate(tower_data)
			else:
				keyvalue = list()
				keyvalue.append(key)
				keyvalue.append(value)
				table.append(keyvalue)

		except (SyntaxError, ValueError, AssertionError):
			#SyntaxError, ValueError are for the literal_eval exceptions
			pass
	return tabulate(table,headers='firstrow') + "\r\n\r\n" + tags


def formatFRPreport(param):
	dictionary = dict(param)
	itemlist = decodeTLV(dictionary)
	
	return itemlist

def log_line(line, serial_log_file, serial_info_file):
	"""Log one line"""
	serial_log_file.write(line+"\r\n")
	serial_log_file.flush()

	info_line ="[" + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')) +"]" +" - " + line
	serial_info_file.write(info_line+"\r\n")
	if line.startswith("7D"):
		frpreport = frp.frpreport(line)
		report = formatFRPreport(frpreport.get_decoded_dictonary())
		serial_info_file.write(report)
	serial_info_file.flush()
	return True
