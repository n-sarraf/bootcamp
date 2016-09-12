
def longest_common_substring(str1, str2):

    """To evaluate the longest common substring between two given strings."""


    if len(str1) <= len(str2):
        shortstr=str1
        longstr=str2
    else:
        longstr=str1
        shortstr=str2

    short_str = shortstr

    # for i, _ in enumerate(shortstr):
    #     while shortstr not in longstr:
    #         shortstr = shortstr[:-1]
    #     else:
    #         shortstr1 = shortstr



    ident_string = ""
    for i, _ in enumerate(shortstr):
         if short_str in longstr:
             shortstr2 = short_str
             if len(shortstr2) > len(ident_string):
                 ident_string = shortstr2

         else:
             short_str = short_str[i:-1]

    ident_string_2 = ""
    for i, _ in enumerate(shortstr):
         if short_str in longstr:
             shortstr2 = short_str
             if len(shortstr2) > len(ident_string):
                 ident_string_2 = shortstr2

         else:
             short_str = short_str[1:i]



    if len(shortstr1) >= len(shortstr2):
         return "The longest common string is " + shortstr1
    else:
         return "The longest common string is " + shortstr2
