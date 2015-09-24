from __future__ import print_function
import os
import glob
import re


with open('MIPS.txt') as file:
    linhas = file.readlines()




for arquivo in glob.glob('../*.sublime-snippet'):
    print('Removendo:', arquivo)
    os.remove(arquivo)



for linha in linhas:
    pedacos = re.split(r'\s{2,}', linha)



    funcName = pedacos[0]
    CDATA = pedacos[1]
    comentario = pedacos[2].strip()




    content = '''<!-- THIS WAS AUTOMATED GENERATED -->
<snippet>
    <description>'''+comentario+'''</description>
    <content><![CDATA['''+CDATA+''']]></content>
    <tabTrigger>'''+funcName+'''</tabTrigger>
    <scope>source.mips</scope>
</snippet>'''



    fileDest = '../'+funcName+'.sublime-snippet'
    with open(fileDest, 'w') as file:
        file.write(content)