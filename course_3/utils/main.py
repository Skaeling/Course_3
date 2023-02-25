import funcs


def main():
    data_path = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb" \
                "-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp" \
                "=1677342772554&signature=_C2-rZBAG9ufDhOZg53LDx4-dz-7RXLbUC0CPbGs4IA&downloadName=operations.json"
    data_list = funcs.load_data(data_path)
    print(data_list)
    op_executed = funcs.data_filter(data_list)
    print(op_executed)


if __name__ == "__main__":
    main()