import requests


def main():
    result = requests.get("https://www.axur.com.br/")
    print("OK6, status={}".format(result.status_code))


if __name__ == "__main__":
    main()
