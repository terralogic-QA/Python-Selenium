import os

try:
	file_name = 'sample.txt'
	file_stats = os.stat(file_name)
	print('file size is {} bytes'.format(file_stats.st_size))
except IOError:
	print('No file found: Please provide valid file name/path')
