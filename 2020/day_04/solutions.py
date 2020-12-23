def part_1(input_data: str):
    """Return first solution of puzzle."""
    if input_data == "": return ""
    passports = input_data.split("\n\n")
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_total = 0

    for passport in passports:
        marker_valid = False

        passport_str = ' '.join(passport.split('\n'))
        passport_entry_set = set()

        for entry in passport_str.split(' '):
            passport_entry_set.add(entry[0:3])
        
        if required.issubset(passport_entry_set):
            valid_total += 1  
    
            
    return valid_total 



def part_2(input_data: str):
    """Return second solution of puzzle."""
    if input_data == "": return ""

    passports = input_data.split("\n\n")
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    valid_total = 0

    for passport in passports:
        marker_valid = False

        passport_str = ' '.join(passport.split('\n'))
        passport_entry_set = set()

        for entry in passport_str.split(' '):
            entry, value = entry.split(':')
            
            if entry == 'byr':
                if int(value) >= 1920 and int(value) <= 2002:
                    passport_entry_set.add(entry)

            elif entry == 'iyr':
                if int(value) >= 2010 and int(value) <= 2020:
                    passport_entry_set.add(entry)

            elif entry == 'eyr':
                if int(value) >= 2020 and int(value) <= 2030:
                    passport_entry_set.add(entry)

            elif entry == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        passport_entry_set.add(entry)

                elif value[-2:] == 'in':
                    if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        passport_entry_set.add(entry)

            elif entry == 'hcl':
                valid_entry = True
                valid_numbers = [str(i) for i in range(10)]

                if not value[0] == '#':
                    valid_entry = False

                for char in value[1:]:
                    if not((char in valid_numbers) or (char in ['a', 'b', 'c', 'd', 'e', 'f'])):
                        valid_entry = False

                if valid_entry:
                    passport_entry_set.add(entry)

            elif entry == 'ecl':
                if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    passport_entry_set.add(entry)
            
            elif entry =='pid':
                valid_pid = True
                if len(value) == 9:
                    for char in value:
                        if not char.isdigit():
                            valid_pid = False
                    
                    if valid_pid:
                        passport_entry_set.add(entry)

     
        if required.issubset(passport_entry_set):
            valid_total += 1     
            
    return valid_total