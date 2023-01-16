import sqlalchemy

from dbnb import notebooks, conn

LIMIT_SELECT = 5
OUT_FILE = 'top.html'

query = sqlalchemy.select([notebooks]).order_by(sqlalchemy.desc("rank")).limit(LIMIT_SELECT)
ret = conn.execute(query)

with open(OUT_FILE, 'w') as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="CP-1251">\n<title>Top</title>\n</head>\n')
    f.write('<body>\n')
    f.write('<table border=1>\n')

    f.write('<tr>\n')
    f.write(f'<td>Название</td>\n')
    f.write(f'<td>Дисплей, дюйм</td>\n')
    f.write(f'<td>Частота процессора, ГГц</td>\n')
    f.write(f'<td>ОЗУ, Гб</td>\n')
    f.write(f'<td>SSD, Гб</td>\n')
    f.write(f'<td>Стоимость, руб</td>\n')
    f.write(f'<td>Рейтинг, попугаи</td>\n')
    f.write('</tr>\n')

    for nb in ret.fetchall():
        print(nb)
        f.write('<tr>\n')
        f.write(f'<td><a href="{nb[1]}">{nb[3]}</a></td>\n')
        f.write(f'<td>{nb[4]}</td>\n')
        f.write(f'<td>{nb[5]}</td>\n')
        f.write(f'<td>{nb[6]}</td>\n')
        f.write(f'<td>{nb[7]}</td>\n')
        f.write(f'<td>{nb[8]}</td>\n')
        f.write(f'<td>{nb[9]}</td>\n')
        f.write('</tr>\n')

    f.write('</table>\n')
    f.write('</body>\n')
    f.write('</html>')

conn.close()