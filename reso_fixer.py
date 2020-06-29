import os
from pathlib import Path
from os import getcwd, chdir

print('Lembre-se de fechar o Spotify antes de executar!\nLembre-se de dar chmod +x reso_fixer.py')

cwd = os.getcwd()
if not cwd.endswith('/.config/spotify'):
	os.chdir(str(Path.home())+'/.config/spotify')

lines = []

with open('prefs', 'r') as file:
	lines = file.readlines()
	c = 0

	for l in lines:
		if(l.startswith('app.window.position.width=')):
			print(l)
			lines[c] = 'app.window.position.width=800\n'
		elif(l.startswith('app.window.position.height=')):
			lines[c] = 'app.window.position.width=600\n'
		c += 1
	file.close()

with open('prefs', 'w') as file:
	file.writelines(lines)
	file.close()
