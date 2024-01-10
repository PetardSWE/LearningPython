import os
from chardet import detect
import shutil
import glob

path = "H:/ePassi/"
path_source = "H:/ePassi/Employees.csv"
path_out = "//path/out"
path_file_out = "//path/out//Employees.csv"
source_files = glob.glob(path + "/*.csv")  # skapar lista med alla CSV-filer i mappen
target_file = 'Employees.csv'
os.chdir(path)


def check_files_transferred():  # Räknar antalet CSV-filer i Friskvårdsmappen.
    return len(glob.glob(path_out + "/*.csv"))


def get_encoding_type(file):  # läser in vilken codec filen använder
    with open(file, 'rb') as reading_file:
        rawdata = reading_file.read()
    return detect(rawdata)['encoding']


if not source_files:  # Kollar om det finns någon fil, om inte skriv det i output.
    print(f'\nVarning: UTF-8 avbröts', f'Det finns ingen CSV-fil i {path} att konvertera.')
elif len(source_files) == 1:
    if check_files_transferred() == 0:
        for srcfile in source_files:  # kör för varje fil i listan (men det ska ju bara finnas en.)
            from_codec = get_encoding_type(srcfile)
            try:  # byter från tidigare codec till UTF-8 och skapar en ny fil som kallas 'Employees.csv'
                with open(srcfile, 'r', encoding=from_codec) as f, open(target_file, 'w', encoding='utf-8') as e:
                    text = f.read()
                    e.write(text)
                os.remove(srcfile)  # tar bort originalfilen
                shutil.move(path_source, path_file_out)  # flyttar den nya filen till integrationen
                print(f'\nUTF-8 konvertering genomförd.',
                      f'Det finns nu {str(check_files_transferred())} CSV-fil i {path_out}.')
            except UnicodeDecodeError:
                print(f'\nVarning: UTF-8 konvertering misslyckades.', 'UnicodeDecodeError.')
            except UnicodeEncodeError:
                print(f'\nVarning: UTF-8 konvertering misslyckades.', 'UnicodeEncodeError.')
    elif check_files_transferred() != 0:
        print(f'\nVarning: UTF-8 konverteringen avbröts.',
              f'Det finns redan {str(check_files_transferred())} CSV-filer i {path_out}.')
else:
    print(f'\nVarning: UTF-8 konverteringen avbröts. \nDet finns mer än en CSV-fil i {path}.')


