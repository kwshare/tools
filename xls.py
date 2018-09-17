# coding: utf-8
# WebTerminal2 - xls.py
# 2018/9/13 



from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment, Fill
from openpyxl import Workbook, load_workbook
import itertools
import string
import re
from copy import copy


def style_range(ws, cell_range, border=Border(), fill=None, font=None, alignment=None):
    """
    Apply styles to a range of cells as if they were a single cell.

    :param ws:  Excel worksheet instance
    :param range: An excel range to style (e.g. A1:F20)
    :param border: An openpyxl Border
    :param fill: An openpyxl PatternFill or GradientFill
    :param font: An openpyxl Font object
    """

    top = Border(top=border.top)
    left = Border(left=border.left)
    right = Border(right=border.right)
    bottom = Border(bottom=border.bottom)

    first_cell = ws[cell_range.split(":")[0]]
    if alignment:
        ws.merge_cells(cell_range)
        first_cell.alignment = alignment

    rows = ws[cell_range]
    if font:
        first_cell.font = font

    for cell in rows[0]:
        cell.border = cell.border + top
    for cell in rows[-1]:
        cell.border = cell.border + bottom

    for row in rows:
        l = row[0]
        r = row[-1]
        l.border = l.border + left
        r.border = r.border + right
        if fill:
            for c in row:
                c.fill = fill


read = load_workbook('test.xlsx')
ws = read.active
write_wb = Workbook()
write_ws = write_wb.active
al = Alignment(horizontal="center", vertical="center")
thin = Side(border_style="thin", color="000000")
# double = Side(border_style="double", color="ff0000")
border = Border(top=thin, left=thin, right=thin, bottom=thin)

table = list(itertools.chain(string.ascii_uppercase,
                             (''.join(pair) for pair in itertools.product(string.ascii_uppercase, repeat=2))))
MOVE = 2


def twenty_six(char):
    # 能够把坐标移动MOVE个单位
    index = table.index(char)
    return table[index + MOVE]


def get_alpha(s):
    result = ''.join(re.split(r'[^A-Z]', s))
    return result


def get_int(s):
    return re.findall("\d+", s)[0]


def move_right(col):
    # A1:C2
    # 左半部分 右半部分
    left = col.split(':')[0]
    right = col.split(':')[1]

    left_alpha = get_alpha(left)
    left_int = get_int(left)
    right_alpha = get_alpha(right)
    right_int = get_int(right)

    return "%s%s:%s%s" % (twenty_six(left_alpha), left_int, twenty_six(right_alpha), right_int)


#
# for merge in ws.merged_cells.ranges:
#     style_range(write_ws, move_right(merge.coord), border=border, alignment=al)
#     # style_range(write_ws, merge.coord, border=border, alignment=al)

for i in ws.rows:

    for v in i:
        # print v.value, v.coordinate
        coord = '%s%s' % (twenty_six(get_alpha(v.coordinate)), get_int(v.coordinate))
        # fill border and everything
        write_ws[coord].fill = copy(v.fill)
        write_ws[coord].font = copy(v.font)
        write_ws[coord].border = copy(v.border)
        if v.value:
            write_ws[coord] = v.value
        elif isinstance(v.value, long):
            write_ws[coord] = v.value

# applying styles
for merge in ws.merged_cells.ranges:
    style_range(write_ws, move_right(merge.coord), border=border, alignment=al)

write_wb.save("styled.xlsx")
