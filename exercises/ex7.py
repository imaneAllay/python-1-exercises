def calc_total(array, tax):
    total=0
    tax = float(tax.strip('%'))/100
    for i in array:

        total+=float(i)+(float(i)*tax)

    print (total)
    formatted_total = "${:,.2f}".format(total)
    print(formatted_total)
