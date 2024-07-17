import re

class StringPractice(object):
    def parse_string(self):
        input_str = input("input string:\n")
        # match the rule with regular expression
        find_match_string = re. search(r'\d+(?:\.\d+)?',input_str)
        if find_match_string:
            output_string = find_match_string.group()
            if '.' in output_string:
                integer_part, decimal_part = output_string.split('.', 1)
                # if only 1 decimal then supplement zero
                if len(decimal_part) == 1:
                    output_string = f"{output_string[:(output_string.rfind('.') + 2)]}0"
                    print(output_string)
                else:
                # if more than 1 decimal then keep 2 decimal
                    output_string = output_string[:(output_string.rfind('.') + 3)]
                    print(output_string)
            else:
                output_string = f"{output_string}.00"
                print(output_string)
                return output_string
        else:
            # verify if input string not contain numeric
            print('invalid input string')
            return None

if __name__ == '__main__':
    stringPractice = StringPractice()
    stringPractice.parse_string()