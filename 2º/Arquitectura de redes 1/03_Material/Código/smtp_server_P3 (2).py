# -*- coding: utf-8 -*-

import sys
import smtpd
import asyncore

ALLOWED_EMAIL = "ar1@gpar1.es"

class AR1SMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None,rcpt_options=None):

        print('> Correo recibido de', mailfrom)

        if ALLOWED_EMAIL in rcpttos:
            addr = str(peer[0])
            port = str(peer[1])
            strmail = ""
            for mail in rcpttos:
                strmail+=mail
                strmail+=","

            strdata = data.replace('\n',' ')

            with open("./mails.txt","a") as f:
                f.write(addr+"|"+
                        port+"|"+
                        mailfrom+"|"+
                        strmail+"|"+
                        strdata+"\n"
                        )
        else:
            print('> Enviado a dirección de correo erronea:',rcpttos)

if __name__ == "__main__":
    print('Servidor SMTP iniciado...')
    try:
        server = AR1SMTPServer((sys.argv[1], int(sys.argv[2])), None, decode_data=True)
        asyncore.loop()
    except KeyboardInterrupt:
        print('Servidor SMTP finalizado.')
        exit(0)
