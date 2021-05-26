import json

class DataProcessor:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def get_mentees_number(self):
        return len(self.dataframe.index)

    def get_languages(self):
        languages_column = self.__get_column("language")
        return list(set(languages_column))

    def get_average_name_length(self):
        fullname_string = ''.join(self.__get_fullname_list())
        return len(fullname_string) / self.get_mentees_number()

    # This method can be done with a single line : return max(self.__get_fullname_list(), key=len)
    # But I wanted to implement it without using such a highly abstracted method.
    def get_longest_name(self):
        name_count = 0
        longest_name = ""

        for name in self.__get_fullname_formatted_list():
            if len(name) > name_count:
                name_count = len(name)
                longest_name = name

        return longest_name

    def get_shortest_name(self):
        name_count = len(self.__get_fullname_formatted_list()[0])
        shortest_name = ""

        for name in self.__get_fullname_formatted_list():
            if len(name) < name_count:
                name_count = len(name)
                shortest_name = name

        return shortest_name

    def get_json(self):
        report = {"All mentees": self.__get_fullname_formatted_list(),
                  "Number of mentees": self.get_mentees_number(),
                  "Languages": self.get_languages(),
                  "Average name length": self.get_average_name_length(),
                  "Longest name": self.get_longest_name(),
                  "Shortest name": self.get_shortest_name()}

        return json.dumps(report, ensure_ascii=False)

    def __get_column(self, column_name):
        return self.dataframe.loc[:, column_name]

    def __get_fullname_list(self):
        fullname = self.__get_column("first_name") + self.__get_column("last_name")
        return list(fullname)

    def __get_fullname_formatted_list(self):
        fullname = self.__get_column("first_name") + ' ' + self.__get_column("last_name")
        return list(fullname)
