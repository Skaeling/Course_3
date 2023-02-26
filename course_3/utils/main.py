import funcs


def main():
    data_url = "https://www.jsonkeeper.com/b/DVZ1"
    data_list = funcs.load_data(data_url)
    op_executed = funcs.data_filter(data_list)
    last_ops = funcs.time_filter(op_executed)
    op_date = funcs.format_date(last_ops)



if __name__ == "__main__":
    main()

