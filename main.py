""" Import required libraries """
import phonenumbers


def extract_phone_number(country_code, phone_number):
    phone_number = phone_number.strip()
    phone_number = phone_number.replace(' ', '')

    try:
        phone_number = phonenumbers.parse(phone_number, country_code.upper())
        phone_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.phonenumberutil.NumberParseException:
        return None
    return phone_number


def main(country_code, phone_number):
    """ Validate a phone number. Format a phone number using E164 format """

    response = {}
    response["valid"] = False
    response["phone_number"] = phone_number

    phone_number = extract_phone_number(country_code, phone_number)

    phone_number = phonenumbers.parse(phone_number)
    if phonenumbers.is_valid_number(phone_number):
        phone_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        response["valid"] = True
        response["phone_number"] = phone_number

    return response
