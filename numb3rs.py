def main():
    ip = input('Enter the IP adress: ')
    validate_ip = validate(ip)

    print(validate_ip)


def validate(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    
    return True

if __name__ == '__main__':
    main()

