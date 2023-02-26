import funcs


def main():
    data_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb" \
               "-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp" \
               "=1677490556581&signature=tpg4Nb1QcvIzL-mlMkhnpOo2UjszMNZqM6ewS_OEIQw&downloadName=operations.json"
    data_list = funcs.load_data(data_url)
    op_executed = funcs.data_filter(data_list)
    last_ops = funcs.time_filter(op_executed)
    print(*last_ops, sep="\n")


if __name__ == "__main__":
    main()

