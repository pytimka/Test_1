# -*- coding: utf-8 -*-
 
import subprocess
import os
import time
import sys
import serial
from config import com

def nncltool_exec_2(cmd):
		proc = subprocess.Popen("t.exe \"{} 9600 8n1 2000\" \"{}\"".format(com, cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		proc.stdout.readline()
		out = proc.stdout.readlines()
		tmp_str = ''
		try:
			for cur_out in out:
				tmp_str += str(cur_out.decode("latin-1")).replace('\t','').replace('\r','').replace('\n',' ')
		except UnicodeEncodeError as err:
			print_out('Error decoding string from tool')
			tmp_str = ''
		res = { "mess" : tmp_str.rstrip() }
		gg = tmp_str.rstrip()
		#res["time"] = int(gg.split(' ')[-5])# Разбиение строки по разделителю пробел
		return res
		print(res)	

