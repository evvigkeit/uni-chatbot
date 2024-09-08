import sqlite3


def base_start():
    global base, cur
    base = sqlite3.connect('data.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS links(group_name TEXT PRIMARY KEY, link_brv TEXT, link_lit TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS teachers_management(teacher_name TEXT PRIMARY KEY, email TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS teachers_it(teacher_name TEXT PRIMARY KEY, email TEXT)')
    # base.execute('INSERT INTO teachers_info VALUES (?, ?)', ('1', '1'))
    base.commit()  # to save changes
    # return base.execute('SELECT * FROM links').fetchall()


def base_links_answer():
    base_link = cur.execute('SELECT * FROM links').fetchall()
    return base_link


def base_teachers_management_answer():
    base_teachers_management = cur.execute('SELECT * FROM teachers_management').fetchall()
    return base_teachers_management


def base_teachers_it_answer():
    base_teachers_it = cur.execute('SELECT * FROM teachers_it').fetchall()
    return base_teachers_it
