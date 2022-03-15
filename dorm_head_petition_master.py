import datetime
import sys
import argparse

from fpdf import FPDF


def create_petition(is_gender_male, group_num, name_str, room_num):
    male = is_gender_male
    group_num = group_num
    name_str = name_str
    gender_endings = ["у", "му"] if male else ["ке", "ей"]
    room_num = room_num
    months = ["января",
              "февраля",
              "марта",
              "апреля",
              "мая",
              "июня",
              "июля",
              "августа",
              "сентября",
              "октября",
              "ноября",
              "декабря"]

    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    pt_per_cm = pdf.fw_pt / 21
    # print(pt_per_cm)
    pdf.set_margins(3 * pt_per_cm, 2 * pt_per_cm, 1 * pt_per_cm)

    pdf.add_font("Times New Roman", '', './fonts/timesnewromanpsmt.ttf', uni=True)
    pdf.set_font("Times New Roman", size=14)
    pdf.multi_cell(0, 28, txt='''Ректору\nСПбГЭТУ "ЛЭТИ"\nШелудько Виктору Николаевичу''', align="R")
    pdf.ln()
    pdf.multi_cell(0, 28, txt='''Ходатайство''', align="C")
    pdf.ln()
    pdf.multi_cell(0, 28, txt='     '
                              'Прошу оказать материальную поддержку студент%s группы %s '
                              '%s, проживающе%s в общежитии №7 в комнате %s. Долгов по оплате за проживание не '
                              'имеет. Дисциплинарных взысканий также не имеет.'
                              % (gender_endings[0], group_num, name_str, gender_endings[1], room_num),
                   align='J')
    pdf.ln()
    pdf.ln()
    pdf.multi_cell(0, 28, txt='"%d" %s %d г.' % (
        datetime.date.today().day, months[datetime.date.today().month], datetime.date.today().year), align="L")
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.ln()
    pdf.cell(0, 28, txt="Староста общежития №7", ln=0, align="L")
    pdf.cell(-50, 28, txt="Э.Э. Абибулаев", ln=1, align="R")

    pdf.output("%s.pdf" % name_str)


def main(argv):
    parser = argparse.ArgumentParser(description="Creates dormitory headman petition for students.")
    parser.add_argument('full_name', metavar='--name_str', type=str, nargs='?', help="Student name for petition.")
    parser.add_argument('group_num', metavar='--group_num', type=int, nargs='?', help="Student group number.")
    parser.add_argument('room_num', metavar='--room_num', type=int, nargs='?', help="Student room number.")
    parser.add_argument('is_gender_male', metavar='--is_gender_male', type=bool, nargs='?', help="Student gender.")

    if len(argv) > 1:
        args = parser.parse_args()
        create_petition(args.is_gender_male, args.group_num, args.full_name, args.room_num)
    else:
        gender = True if input("Is gender male? (Y/n): ") in ("y","\n") else False
        name_str = input("Enter student full name: ")
        group_num = int(input("Enter student group number: "))
        room_num = int(input("Enter student room number: "))
        create_petition(gender,group_num, name_str, room_num)

if __name__ == "__main__":
    main(sys.argv)
