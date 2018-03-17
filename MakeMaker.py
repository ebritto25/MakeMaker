#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(prog='MakeMaker',description='Create a MakeFile for a C++ program, with compile, test and clean options',formatter_class=argparse.ArgumentDefaultsHelpFormatter)


parser.add_argument('source_file',nargs=1,help='Source file to be compiled')
parser.add_argument('-o','--output',nargs=1,default='exec',type=str,help='Defines the output name.')

args = vars(parser.parse_args())

source = args['source_file'][0]
output = args['output'][0]

if(not source.endswith('.cpp') or not souce.endswith('.c')):
	source += '.cpp'


print('Generating Makefile for "'+source+'" with output name: "'+output+'"')

with open('Makefile','w') as f:
	f.write('all: compile\n')
	f.write('compile:\n')

	f.write("\t@echo 'Compiling'\n")
	f.write("\tg++ "+source+" -o "+output+"\n")

	f.write('test:\n')
	f.write("\t@echo 'Testing'\n")
	f.write("\t./"+output+"\n")
