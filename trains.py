from ns_api.ns_api import NSApi


def main():
    ns_api = NSApi()
    disrupt = ns_api.get_disruptions()
    print(disrupt)


if __name__ == "__main__":
    main()
