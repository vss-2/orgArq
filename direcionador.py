from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
# Precisa do pip3 install watchdog

import os
import time
import shutil

cwd = os.getcwd()
arquivos = os.listdir(os.getcwd())

img_switcher {
        ai : True,
        xfc : True,
        svg : True,
        png : True,
        jpg : True,
        bmp : True,
        img : True,
        ico : True,
        drw : True,
        psd : True,
        psp : True,
        xps : True,
        x3d : True,
        dwg : True,
        dwf : True,
        dxf : True,
        tiff : True,
        webp : True,
        blend : True
}

vid_switcher {
        ts: True,
        qt: True,
        rm: True,
        wmv: True,
        mkv: True,
        mts: True,
        flv: True,
        vob: True,
        gif: True,
        gifv: True,
        avi: True,
        mov: True,
        mp4: True,
        m4v: True,
        m4p: True,
        flv: True,
        f4v: True,
        rmvb: True,
        webm: True
}

doc_switcher {
        md: True,
        doc: True,
        odt: True,
        tex: True,
        rtf: True,
        pdf: True,
        sxw: True,
        fb2: True,
        html: True,
        docx: True,
        pages: True,

}

aud_switcher {
        aa: True,
        ra: True,
        wv: True,
        vox: True,
        wav: True,
        wma: True,
        aac: True,
        aax: True,
        mp3: True,
        m4a: True,
        m4b: True,
        m4p: True,
        ogg: True,
        act: True,
        mogg: True,
        opus: True,
        aiff: True,
        alac: True,
        flac: True
}

class fileHandler(FileSystemEventHandler):
        movedor(img_switcher, str(cwd+'/'+arq), '~/Imagens')
        movedor(vid_switcher, str(cwd+'/'+arq), '~/Vídeos')
        movedor(aud_switcher, str(cwd+'/'+arq), '~/Músicas')
        movedor(doc_switcher, str(cwd+'/'+arq), '~/Documentos')
        exit

if '__name__' == '__main__':
	print('Por padrão, vou mover:\n imgs para ~/Imagens,\n videos para ~/Vídeos,\n docs para ~/Documentos, audios para ~/Músicas')
        live = input('Quer a versão rodando em background (s/n)? ')
	img = input('Quer que eu mova imagens (s/n)? ')
	vid = input('Quer que eu mova vídeos (s/n)? ')
	aud = input('Quer que eu mova áudios (s/n)? ')
	doc = input('Quer que eu mova documentos (s/n)? ')
	sufixo = ''
        if(img == 's'):
                movedor(img_switcher, str(cwd+'/'+arq), '~/Imagens')
        if(vid == 's'):
                movedor(vid_switcher, str(cwd+'/'+arq), '~/Vídeos')
        if(aud == 's'):
                movedor(aud_switcher, str(cwd+'/'+arq), '~/Músicas')
        if(doc == 's'):
                movedor(doc_switcher, str(cwd+'/'+arq), '~/Documentos')
        if(live == 's'):
                tempo = int(input('Quanto tempo em segundos observar a pasta?'))
                print('Vou supor que você quer olhar a Downloads, \nsenão for, edite o código (linha 115)')
                pasta_observada = '~/Downloads'
                evento_handler = fileHandler()
                observador = Observer()
                observador.schedule(evento_handler, pasta_observada, recursive=False)
                observador.start()
                try:
                        while True:
                                time.sleep(tempo)
                except KeyboardInterrupt:
                        observador.stop()
                observador.join()
        exit()

def movedor(switcher, src, path):
	for arq in arquivos:
		sufixo = str(arq[-3:])
                sufixo = sufixo.lower()
                if (sufixo in switcher and os.path.isfile(src)):
                        try:
                                shutil.move(str(src), str(path))
                        except OSError as stoper:
                                print('Houve um erro, melhor parar:', stoper)
        return