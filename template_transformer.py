#!/usr/bin/python

import sys


if len(sys.argv) != 4:
	print ''
	print 'This script replace pattern: <<EXPRESSION_KEY>> on template file according with the properties.txt mapping.'
	print 'Execute: template_transformer.py properties.txt template.tpl result.ext'
	sys.exit()

def replace_patterns(line, dictionary, pattern):
	new_line = line
	
	for key in dictionary:
		new_pattern = pattern.replace(EXPRESSION_KEY, key)
		new_line = new_line.replace(new_pattern, dictionary[key])
	
	return new_line

EXPRESSION_KEY='EXPRESSION_KEY'
pattern='<<' + EXPRESSION_KEY + '>>'
properties_dictionary={}
output_lines = []

propertiesFileName = sys.argv[1]
templateInputFileName = sys.argv[2]
templateOutputFileName = sys.argv[3]

propertiesFile = open(propertiesFileName, 'r')

for line in propertiesFile:
	line_split = line.strip().split('=')
	if len(line_split) == 2:
		property = line_split[0].strip()
		value = line_split[1].strip()
		properties_dictionary[property] = value


templateInputFile = open(templateInputFileName, 'r')
templateOutputFile = open(templateOutputFileName, 'w')

for line in templateInputFile:
	output_lines.append(replace_patterns(line, properties_dictionary, pattern))
	
templateOutputFile.writelines(output_lines)	
templateOutputFile.close()
templateInputFile.close()

sys.exit()
