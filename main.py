import qrcode

def get_qrcode(url='https://www.google.com/', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code {name}.png was created!'

def main():
    print(get_qrcode(url='https://github.com/farafon666', name='github'))
    print(get_qrcode(url='https://pythonworld.ru/', name='python_tutorial'))

if __name__ == '__main__':
    main()