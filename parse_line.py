
def parse_line(line):
    entries = []   # will be our final output

    entry_str = ''   # stores the string of the current entry
                     # that we're building up

    inside_quotes = False   # true if we're inside quotes

    quote_symbol = None   # stores the type of quotes we're inside,
                          # i.e. single quotes "'" or
                          # double quotes '"'

    for char in line:
      if inside_quotes == False:
        if char == "\'":
          inside_quotes = True 
          quote_symbol = '\''
        if char == '\"':
          inside_quotes = True 
          quote_symbol = '\"'
      else:
        if char ==  quote_symbol:
          inside_quotes = False
          quote_symbol = None

      if char == ',' and inside_quotes == False:
        entries.append(entry_str)
        entry_str = ''
      else:
        entry_str += char
      
        
        # if we're at a comma that's not inside quotes,
        # store the current entry string. In other words,
        # append entry_str to our list of entries and reset
        # the value of entry_str

        # otherwise, if we're not at a comma or we're at a
        # comma that's inside quotes, then keep building up
        # the entry string (i.e. append char to entry_str)

        # if the char is a single or double quote, and is equal
        # to the quote symbol or there is no quote symbol,
        # then flip the truth value of inside_quotes and
        # change the quote symbol to the current character
    entries.append(entry_str)
    return entries
      


    # append the current entry string to entries and return entries
line_1 = "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S"
assert parse_line(line_1) == ['1', '0', '3', "'Braund, Mr. Owen Harris'", 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']

line_2 = '102,0,3,"Petroff, Mr. Pastcho (""Pentcho"")",male,,0,0,349215,7.8958,,S'
assert parse_line(line_2) == ['102', '0', '3', '"Petroff, Mr. Pastcho (""Pentcho"")"', 'male', '', '0', '0', '349215', '7.8958', '', 'S']

line_3 = '187,1,3,"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)",female,,1,0,370365,15.5,,Q'
assert parse_line(line_3) == ['187', '1', '3', '"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)"', 'female', '', '1', '0', '370365', '15.5', '', 'Q']


