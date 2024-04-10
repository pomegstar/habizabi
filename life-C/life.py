import inflect
import sys
from datetime import date
from word2num import word2num

p = inflect.engine()


def main():
    t = input("Date of Birth (YYYY-MM-DD): ")
    i = input("How many years do you want to live (only digit will be accepted): ")
    w = input("How do you want to measure your age? (Seconds/Minutes/Hours/Days): ").strip()
    if (len(w.lower()) >= 3) and (w.lower() in "seconds"):
        s = seconds(t, i)
        print(f"You have passed {s[0]} seconds and only {s[1]} seconds are left in your life.")
    elif (len(w.lower()) >= 3) and (w.lower() in "minutes"):
        s = minutes(t, i)
        print(f"You have passed {s[0]} minutes and only {s[1]} minutes are left in your life.")
    elif (len(w.lower()) >= 3) and (w.lower() in "hours"):
        s = hours(t, i)
        print(f"You have passed {s[0]} hours and only {s[1]} hours are left in your life.")
    elif (len(w.lower()) >= 3) and (w.lower() in "days"):
        s = days(t, i)
        print(f"You have passed {s[0]} days and only {s[1]} days are left in your life.")
    else:
        sys.exit("Invalid input")


def seconds(t, i, to=date.today()):
    try:
        ti = t.split("-")
        if len(ti) < 3:
            raise ValueError
        e = date(int(ti[0]), int(ti[1]), int(ti[2]))
        r = (to - e).total_seconds()
        if r < 0:
            raise ValueError
        words = p.number_to_words(round(r), andword="")
        x = f"'{words.capitalize()}'"
        d = date(int(ti[0])+int(i), int(ti[1]), int(ti[2]))
        k = (d - to).total_seconds()
        if k < 0:
            raise ValueError
        words = p.number_to_words(round(k), andword="")
        y = f"'{words.capitalize()}'"
        return x, y
    except ValueError:
        sys.exit("Invalid input")


def minutes(t, i, to=date.today()):
    h = seconds(t, i, to)
    ho = word2num(h[0])/60
    words = p.number_to_words(round(ho), andword="")
    x = f"'{words.capitalize()}'"
    hou = word2num(h[1])/60
    words = p.number_to_words(round(hou), andword="")
    y = f"'{words.capitalize()}'"
    return x, y


def hours(t, i, to=date.today()):
    h = seconds(t, i, to)
    ho = word2num(h[0])/3600
    words = p.number_to_words(round(ho), andword="")
    x = f"'{words.capitalize()}'"
    hou = word2num(h[1])/3600
    words = p.number_to_words(round(hou), andword="")
    y = f"'{words.capitalize()}'"
    return x, y


def days(t, i, to=date.today()):
    h = seconds(t, i, to)
    ho = word2num(h[0])/86400
    words = p.number_to_words(round(ho), andword="")
    x = f"'{words.capitalize()}'"
    hou = word2num(h[1])/86400
    words = p.number_to_words(round(hou), andword="")
    y = f"'{words.capitalize()}'"
    return x, y


if __name__ == "__main__":
    main()
