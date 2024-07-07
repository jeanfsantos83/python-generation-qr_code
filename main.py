# pip install qrcode #

import qrcode

def gerar_qr_code(texto, nome_arquivo):
    """Gera um QR Code com o texto informado e salva em um arquivo"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

def main():
    texto = input("Digite o texto para gerar o QR Code: ")
    nome_arquivo = input("Digite o nome do arquivo para salvar o QR Code (ex: qr_code.png): ")
    gerar_qr_code(texto, nome_arquivo)
    print("QR Code gerado com sucesso!")

if __name__ == "__main__":
    main()
