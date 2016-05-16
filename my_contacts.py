'''The script that helped me to replace all my contacts from Nokia.
It prints all contacts in conveniant way. 

'''


import os
import re


path = r'C:\Users\Stanislav\Desktop\Нотатки\contacts'


def main():
    for idx, vcf in enumerate(os.listdir(path)):
        fimename = os.path.join(path, vcf)
        with open(fimename, 'r') as f:
            name = ''.join(vcf.split('.')[:-1])
            try:
                sh = re.search('\(\d+\)', name).group()
            except:
                pass
            print(idx, '\n' + name.replace(sh, ''))
            for line in f:
                if line.split(';')[0] == 'TEL':
                    tel = line.split(":")[-1]
                    if tel[:3] == '+38':
                        tel = tel[3:]
                    print(
                        '+38', tel[:-8], tel[-8:-5], tel[-5:-3], tel[-3:], end=''
                    )
            print()


if __name__ == '__main__':
    main()

