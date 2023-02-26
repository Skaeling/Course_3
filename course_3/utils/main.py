import funcs


def main():
    data_url = "https://www.jsonkeeper.com/b/DVZ1"
    data_list = funcs.load_data(data_url)
    op_executed = funcs.data_filter(data_list)
    last_ops = funcs.time_filter(op_executed)
    op_date = funcs.format_date(last_ops)
    for i in op_date:
        if "from" in i:
            out_acc = []
            out_acc += i['from'].split(" ")
            out_bill = out_acc.pop(-1)
            out_acc = " ".join(out_acc)
            print(f"{i['date']} {i['description']}\n"
                  f"{out_acc} {out_bill[:4]} {out_bill[4:6]}** **** {out_bill[-4:]} -> Счет **{i['to'][-4:]}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
        else:
            print(f"{i['date']} {i['description']}\n-> Счет **{i['to'][-4:]}\n"
                  f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")


if __name__ == "__main__":
    main()

