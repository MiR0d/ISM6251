intro = "Sales and Sales Associate Commission Tracker by Michael Rodriguez"
question = "Enter the name of the sales associate or q to quit: "

def getParam():
    n = input("What is the name of the business for this contract?\n")
    b = float(input("What is the monthly advertising budget (b)?\n"))
    s = float(input("What is the agreed Digital Advertising Setup Fee?\n"))
    return n, b, s


def doCalc(n, b, s):
    fixed_fee = 2500
    f = fixed_fee + 0.15 * b
    tar = s + 12 * f
    c = tar * 0.05
    return f, tar, c


def main():
    print(intro)
    print(question)
    a = input()
    total_f = total_tar = total_c = 0

    while (a.lower() != "q"):
        n, b, s = getParam()
        f, tar, c = doCalc(n, b, s)
        total_f += f
        total_tar += tar
        total_c += c

        print()
        print()
        print()
        print("Given b = $", '{0:.2f}'.format(b), ", s = $", '{0:.2f}'.format(s), " for ", n, ".", sep="")
        print("Your monthly management fee will be $", '{0:.2f}'.format(f), ".", sep="")
        print("The total revenue from this sale will be $", '{0:.2f}'.format(tar), " and the commission earned by ", a,
              " will be $", '{0:.2f}'.format(c), ".", sep="")
        print()
        print(question)
        a = input()

    print("The total monthly management fee is Σ(f) = $", '{0:.2f}'.format(total_f), ".", sep="")
    print("The total annual revenue for all the projects is Σ(TAR) = $", '{0:.2f}'.format(total_tar), ".", sep="")
    print("The total commission to all the sales associates is Σ(c) = $", '{0:.2f}'.format(total_c), ".", sep="")

main()
